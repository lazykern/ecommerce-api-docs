import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import json
import re
import time
import argparse
import os

CONCURRENT_WORKERS = 8

async def scrape_table(page, table_locator):
    """
    Scrapes a table, including nested rows, into a structured list of dictionaries.
    """
    table_data = []
    try:
        if not await table_locator.count() or not await table_locator.is_visible():
            return []
        
        expand_all_button = table_locator.locator("th button.style-module__table-td-svg-button--RtzNm")
        if await expand_all_button.count() > 0:
            try:
                await expand_all_button.click(timeout=1000)
                await page.wait_for_timeout(300)
            except PlaywrightTimeoutError:
                pass # Ignore if button is not clickable
        
        headers = [re.sub(r'\s+', '_', h.strip()).lower().replace('or_not', '') for h in await table_locator.locator('thead th .zone-container').all_inner_texts()]
        rows_locator = table_locator.locator('tbody tr')
        if await rows_locator.count() == 0:
            return []

        root_items = []
        parent_stack = []

        for i in range(await rows_locator.count()):
            row = rows_locator.nth(i)
            if not await row.is_visible():
                continue

            first_cell_wrapper = row.locator('td:first-child .style-module__table-body-td-cell--DxNGr').first
            if await first_cell_wrapper.count() == 0:
                continue
            
            style_attr = await first_cell_wrapper.get_attribute('style') or ''
            padding_match = re.search(r'padding-left:\s*(\d+)', style_attr)
            level = int(padding_match.group(1)) // 12 if padding_match else 0
            
            cells = await row.locator('td').all()
            row_data = {}
            for j, header in enumerate(headers):
                if j < len(cells):
                    cell_content = await cells[j].locator('.zone-container').first.inner_text()
                    row_data[header] = (' '.join(cell_content.split())).strip()

            if not row_data or not row_data.get(headers[0]):
                continue
            
            current_node = row_data

            while parent_stack and parent_stack[-1][0] >= level:
                parent_stack.pop()
            
            if not parent_stack:
                root_items.append(current_node)
            else:
                _, parent_node = parent_stack[-1]
                if 'children' not in parent_node:
                    parent_node['children'] = []
                parent_node['children'].append(current_node)
            
            parent_stack.append((level, current_node))

        table_data = root_items
    except Exception as e:
        print(f"     - Error scraping table: {e}")
        
    return table_data

async def scrape_prose_page(page, category):
    """
    Scrapes a general explanatory, article, or category page.
    """
    documentation = {"page_type": "Prose", "category": category}
    try:
        title_loc_article = page.locator('h1.style-module__document-title--ueDM1')
        title_loc_category = page.locator('div.heading-h1 span[id]').first

        if await title_loc_article.is_visible(timeout=5000):
            documentation['title'] = await title_loc_article.inner_text()
        elif await title_loc_category.is_visible(timeout=5000):
            documentation['title'] = await title_loc_category.inner_text()
        else:
            documentation['title'] = "Untitled Article"

        content_loc_markdown = page.locator('.style-module__markdown-container--Z_9Rl')
        content_loc_rich_text = page.locator('.doc-rich-text')

        if await content_loc_markdown.count() > 0:
             documentation['content'] = await content_loc_markdown.inner_text()
        elif await content_loc_rich_text.count() > 0:
             documentation['content'] = await content_loc_rich_text.inner_text()
        else:
            documentation['content'] = "No main content found."
        
    except Exception as e:
        print(f"     - Could not scrape prose page: {e}")
        return None
    return documentation


async def scrape_endpoint_details(page, category):
    """
    Scrapes the detailed documentation for a single API endpoint page.
    """
    documentation = {"page_type": "API", "category": category}
    try:
        main_content = page.locator('.api-doc-module__scroll-intersection-center--DqFgY')
        
        title_locator = main_content.locator('div.heading-h1 span[id]').first
        documentation['endpoint_name'] = (await title_locator.inner_text()).strip()
        
        url_container = main_content.locator('.url-display-container').first
        documentation['method'] = (await url_container.locator('.url-display-tag-wrapper').inner_text()).strip()
        documentation['path'] = (await url_container.locator('.url-display-url-wrapper').inner_text()).strip()

        all_lines_loc = main_content.locator('div[data-type="Text"] > .zone-container > .ace-line')
        all_lines_count = await all_lines_loc.count()
        desc_lines = []
        collecting = False
        for i in range(all_lines_count):
            line_loc = all_lines_loc.nth(i)
            line_text = await line_loc.inner_text()
            if not collecting and documentation['endpoint_name'] in line_text:
                collecting = True
                continue
            if collecting:
                if await line_loc.locator('.url-display-container').count() > 0:
                    break
                cleaned_line = line_text.strip()
                if cleaned_line:
                    desc_lines.append(cleaned_line)
        documentation['description'] = ' '.join(desc_lines)

        collapsible_sections = await main_content.locator('.doc-collapse-item').all()
        for section in collapsible_sections:
            header_loc = section.locator('.arco-collapse-item-header')
            if await header_loc.count() and "arco-collapse-item-active" not in (await section.get_attribute('class') or ''):
                 await header_loc.click()
                 await page.wait_for_timeout(250)

            header_text_raw = await section.locator('.arco-collapse-item-header-title').inner_text()
            header_text = re.sub(r'\s+', '_', header_text_raw.strip()).lower()
            table_locator = section.locator('.style-module__table-container--IzbfJ')
            if await table_locator.count() > 0 and await table_locator.is_visible():
                documentation[header_text] = await scrape_table(page, table_locator)
        
        example_sections = await main_content.locator('.style-module__json-viewer-container--aINvi').all()
        for section in example_sections:
            parent_header_loc = section.locator('xpath=./ancestor::div[contains(@class, "doc-collapse-item")]//div[contains(@class, "arco-collapse-item-header-title")]')
            if await parent_header_loc.count() > 0:
                parent_header = await parent_header_loc.first.inner_text()
                example_type = 'request_example' if 'request' in parent_header.lower() else 'response_example'
                current_examples = {}
                lang_tabs = await section.locator('.style-module__language-name--EMXNh').all()
                for tab in lang_tabs:
                    lang = (await tab.inner_text()).lower().strip()
                    if not lang: continue
                    await tab.click()
                    await page.wait_for_timeout(250)
                    code_lines = await section.locator('.monaco-editor .view-line').all_inner_texts()
                    current_examples[lang] = '\n'.join(code_lines)
                documentation[example_type] = current_examples
    except Exception as e:
        print(f"     - Could not scrape API endpoint page: {e}")
        return None
        
    return documentation

async def worker(browser, pages_to_scrape, worker_id):
    """A worker that scrapes a subset of pages, accepting tuples of (url, category)."""
    print(f"[Worker {worker_id}] Starting to scrape {len(pages_to_scrape)} pages.")
    context = await browser.new_context()
    page = await context.new_page()
    worker_docs = {}

    for i, (url, category) in enumerate(pages_to_scrape):
        print(f"[Worker {worker_id}] Scraping ({i+1}/{len(pages_to_scrape)}): {url}")
        try:
            await page.goto(url, wait_until='networkidle', timeout=60000)
            if i == 0:
                try:
                    await page.locator("button:has-text('Allow all')").click(timeout=5000)
                    print(f"  [Worker {worker_id}] Accepted cookie banner.")
                except PlaywrightTimeoutError:
                    print(f"  [Worker {worker_id}] Cookie banner not found, continuing.")
            
            await page.locator('div[id="doc_scroll_container"]').wait_for(timeout=30000)

            documentation = None
            if await page.locator('.url-display-container').count() > 0:
                print(f"   -> Detected API Page for category '{category}'.")
                documentation = await scrape_endpoint_details(page, category)
            else:
                print(f"   -> Detected Prose Page for category '{category}'.")
                documentation = await scrape_prose_page(page, category)

            if documentation:
                worker_docs[url] = documentation
        except PlaywrightTimeoutError:
            print(f"  [Worker {worker_id}] Page navigation or content timed out for {url}. Skipping.")
        except Exception as e:
            print(f"  [Worker {worker_id}] FAILED to process {url}: {e}")
            continue
    
    await context.close()
    print(f"[Worker {worker_id}] Finished.")
    return worker_docs

async def main(args):
    """Main function to orchestrate the TikTok Shop API documentation scraping."""
    start_time = time.time()
    all_documentation = {}
    BASE_URL = "https://partner.tiktokshop.com/docv2/page/666012dd609d4402cc3be995?external_id=666012dd609d4402cc3be995#"

    global CONCURRENT_WORKERS
    CONCURRENT_WORKERS = args.workers

    print("Starting Playwright for TikTok Shop...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            print(f"Navigating to {BASE_URL} to collect page list...")
            await page.goto(BASE_URL, wait_until='load', timeout=60000)
            print("Page loaded successfully.")
            
            try:
                await page.locator("button:has-text('Allow all')").click(timeout=5000)
                print("Accepted cookie banner.")
            except PlaywrightTimeoutError:
                print("Cookie banner not found on initial page, continuing.")

            sidebar_container = page.locator('.api-doc-module__scroll-intersection-left--oyT74')
            if "left-hidden" in (await sidebar_container.get_attribute("class") or ""):
                print("Sidebar is collapsed, expanding...")
                await sidebar_container.locator('.api-doc-module__icon--JQF1g').click()
                await page.wait_for_function("!document.querySelector('.api-doc-module__scroll-intersection-left-hidden--Wjwyt')")
                print("Sidebar expanded.")

            print("Expanding all categories...")
            # Locate all category headers first.
            category_headers = await page.locator('a.style-module__side-menu-dir--IbLLG').all()
            for header in category_headers:
                try:
                    # Check if the category is already expanded by looking for a specific attribute or class.
                    # This might need adjustment based on the actual DOM state for expanded items.
                    is_expanded = await header.locator('svg.arco-icon-down').count() > 0
                    if not is_expanded:
                        await header.click(timeout=2000, force=True)
                        await asyncio.sleep(0.3)
                except Exception as e:
                    print(f"Could not click category header: {e}")
            print("Expanded all categories.")
            
            all_menu_items = await page.locator('div.style-module__side-menu--ZASKi div[role="menuitem"]').all()
            pages_to_scrape = []
            scraped_urls = set()
            current_category = "Uncategorized"

            for item in all_menu_items:
                # Find the parent category group for the item.
                # The structure seems to be that items are nested inside divs that have a category header.
                # This is complex and might require a different approach if the DOM isn't consistent.
                # A simpler way is to iterate and track the last seen category header.
                
                # Check if the item itself is a category header.
                is_category_header = await item.locator('a.style-module__side-menu-dir--IbLLG').count() > 0
                if is_category_header:
                     header_element = item.locator('a.style-module__side-menu-dir--IbLLG')
                     current_category = await header_element.locator('.style-module__side-menu-span--OT1zx').inner_text()
                
                # Process the link inside the menu item.
                link_element = item.locator('a').first
                href = await link_element.get_attribute('href')

                if href and 'docv2/page/' in href:
                    full_url = f"https://partner.tiktokshop.com{href}"
                    if full_url not in scraped_urls:
                        pages_to_scrape.append((full_url, current_category.strip()))
                        scraped_urls.add(full_url)

            await page.close()
            print(f"Found {len(pages_to_scrape)} unique pages to scrape (including articles).")
            
            if pages_to_scrape:
                chunk_size = (len(pages_to_scrape) + CONCURRENT_WORKERS - 1) // CONCURRENT_WORKERS
                tasks = []
                for i in range(CONCURRENT_WORKERS):
                    start_index = i * chunk_size
                    end_index = start_index + chunk_size
                    page_chunk = pages_to_scrape[start_index:end_index]
                    if page_chunk:
                        tasks.append(worker(browser, page_chunk, i + 1))
                
                results = await asyncio.gather(*tasks)
                for result_dict in results:
                    all_documentation.update(result_dict)

        except Exception as e:
            print(f"A critical error occurred during setup: {e}")
        
        finally:
            output_file = args.output_file
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            print(f"\nSaving {len(all_documentation)} scraped pages to '{output_file}'...")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(all_documentation, f, indent=2, ensure_ascii=False)
            
            print(f"Successfully saved data to '{output_file}'.")
            await browser.close()
            end_time = time.time()
            print(f"Scraping complete in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape TikTok Shop API documentation.")
    parser.add_argument(
        '--output-file',
        type=str,
        default='output/scraped/tiktok_shop.json',
        help='The path to the output JSON file.'
    )
    parser.add_argument(
        '--workers',
        type=int,
        default=8,
        help='The number of concurrent workers to use for scraping.'
    )
    args = parser.parse_args()
    
    try:
        asyncio.run(main(args))
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")