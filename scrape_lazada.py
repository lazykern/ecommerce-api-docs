import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import json
import re
import time
import argparse
import os

# Number of parallel workers to run
# This will be set by the command-line argument.
CONCURRENT_WORKERS = 8

async def scrape_table(page, table_locator):
    """
    Scrapes a table, including nested rows, into a structured list of dictionaries,
    using the modern Locator API.
    """
    table_data = []
    try:
        # Check if the table itself exists
        if not await table_locator.count():
            return []

        headers = [re.sub(r'\s+', '_', h.strip()).lower().replace('or_not', '') for h in await table_locator.locator('thead th').all_inner_texts()]
        
        rows_locator = table_locator.locator('tbody tr')
        if await rows_locator.count() == 0:
            # Handle cases where the table exists but is empty (e.g., just says "No Data")
            return []

        root_items = []
        parent_stack = []  # Stack to hold (level, node) tuples

        # Iterate through rows using an index to avoid stale element issues
        for i in range(await rows_locator.count()):
            row = rows_locator.nth(i)
            # Skip hidden rows which are part of collapsed sections
            row_class = await row.get_attribute('class') or ''
            if 'hidden' in row_class:
                continue
            
            first_cell_wrapper = row.locator('td:first-child .next-table-cell-wrapper')
            if await first_cell_wrapper.count() == 0:
                continue

            style_attr = await first_cell_wrapper.get_attribute('style') or ''
            padding_match = re.search(r'padding-left:\s*(\d+)', style_attr)
            level = int(padding_match.group(1)) // 12 if padding_match else 0
            
            cells = await row.locator('td').all()
            row_data = {}
            for i, header in enumerate(headers):
                if i < len(cells):
                    cell = cells[i]
                    link_locator = cell.locator('a')
                    if await link_locator.count() > 0 and await link_locator.get_attribute('href'):
                         link_text = (await link_locator.inner_text()).strip()
                         link_href = (await link_locator.get_attribute('href')).strip()
                         cell_content = f"{link_text} ({link_href})"
                    else:
                         cell_content = (' '.join((await cell.inner_text()).split())).strip()
                    row_data[header] = cell_content
            
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
        print(f"    - Error scraping table: {e}")

    return table_data

async def scrape_endpoint_details(page, path):
    """
    Scrapes the detailed documentation for a single API endpoint page.
    This version handles nested tables and checks for error or loading pages.
    """
    documentation = {}
    pending_tasks = []
    try:
        # FIX: Create tasks for each condition we're waiting for.
        task_api_detail = asyncio.create_task(page.wait_for_selector(".api-detail", timeout=20000))
        task_loading = asyncio.create_task(page.wait_for_selector(".lzd-roller-loading", timeout=20000))
        task_not_found = asyncio.create_task(page.wait_for_selector("text='Oops, Page not found'", timeout=20000))
        
        all_tasks = [task_api_detail, task_loading, task_not_found]
        done, pending_tasks = await asyncio.wait(all_tasks, return_when=asyncio.FIRST_COMPLETED)

        # After waiting, check which condition was met.
        if not await page.locator('.api-detail').is_visible():
            print(f"    - Content not loaded for endpoint: {path}. Skipping.")
            return {}

        api_detail_block = page.locator('.api-detail')
        
        documentation['endpoint_name'] = await api_detail_block.locator('.api-name').inner_text()
        
        api_tags = api_detail_block.locator('.api-tags')
        documentation['method'] = await api_tags.locator('.next-tag').first.inner_text()
        documentation['path'] = await api_tags.locator('.copy-text-item').first.inner_text()
        
        desc_text = await api_detail_block.locator('.api-desc').inner_text()
        documentation['description'] = ' '.join(desc_text.replace('Description:', '').strip().split())

        documentation['service_endpoints'] = await scrape_table(page, api_detail_block.locator("h2:has-text('Service Endpoints') + .next-table"))
        documentation['common_parameters'] = await scrape_table(page, api_detail_block.locator("h2:has-text('Common Parameters') + .next-table"))
        documentation['parameters'] = await scrape_table(page, api_detail_block.locator("h2:has-text('Parameters') + .next-table"))
        documentation['response_parameters'] = await scrape_table(page, api_detail_block.locator("h2:has-text('Response Parameters') + .next-table"))
        documentation['error_codes'] = await scrape_table(page, api_detail_block.locator("h2:has-text('Error Code') + .next-table"))

        async def scrape_code_examples():
            examples = {}
            code_area = api_detail_block.locator('.code-area')
            if await code_area.is_visible():
                tabs = await code_area.locator('.next-tabs-tab').all()
                for tab in tabs:
                    lang_name = (await tab.inner_text()).strip().lower()
                    await tab.click()
                    await asyncio.sleep(0.1) 
                    
                    active_pane = code_area.locator('.next-tabs-tabpane.active')
                    if await active_pane.locator('code.hljs').is_visible():
                        code_content = await active_pane.locator('code.hljs').inner_text()
                        examples[lang_name] = code_content.strip()
            return examples

        documentation['request_example'] = await scrape_code_examples()
        if await page.locator(".ui-response-code code.hljs").count() > 0:
            documentation['response_example'] = { "json": await page.locator(".ui-response-code code.hljs").inner_text() }
        else:
            documentation['response_example'] = {}
        
    except PlaywrightTimeoutError:
         print(f"    - Timeout waiting for content on endpoint: {path}. Skipping.")
    except Exception as e:
        print(f"    - Could not scrape full details for endpoint: {path}. Error: {e}")
    
    finally:
        # Cancel any tasks that didn't complete to prevent them running in the background.
        for task in pending_tasks:
            task.cancel()
        
    return documentation

async def worker(browser, endpoint_paths, worker_id):
    """A worker that scrapes a subset of endpoint documentation pages."""
    print(f"[Worker {worker_id}] Starting to scrape {len(endpoint_paths)} endpoints.")
    context = await browser.new_context()
    page = await context.new_page()
    worker_docs = {}

    for i, path in enumerate(endpoint_paths):
        url = f"https://open.lazada.com/apps/doc/api?path={path}"
        print(f"[Worker {worker_id}] Scraping ({i+1}/{len(endpoint_paths)}): {url}")
        try:
            await page.goto(url, wait_until='domcontentloaded', timeout=90000)
            documentation = await scrape_endpoint_details(page, path)
            if documentation:
                worker_docs[path] = documentation
        except PlaywrightTimeoutError:
            print(f"  [Worker {worker_id}] Page navigation timed out for {path}. Skipping.")
        except Exception as e:
            print(f"  [Worker {worker_id}] FAILED to process {path}: {e}")
            continue
    
    await context.close()
    print(f"[Worker {worker_id}] Finished.")
    return worker_docs

async def main(args):
    """Main function to orchestrate the Lazada API documentation scraping."""
    start_time = time.time()
    all_documentation = {}
    BASE_URL = "https://open.lazada.com/apps/doc/api"

    # Use the number of workers from the arguments
    global CONCURRENT_WORKERS
    CONCURRENT_WORKERS = args.workers

    print("Starting Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            print(f"Navigating to {BASE_URL} to collect endpoint list...")
            await page.goto(BASE_URL, wait_until='domcontentloaded', timeout=60000)
            print("Page loaded successfully.")

            await page.wait_for_selector('.next-menu', timeout=30000)
            print("API navigation menu found.")
            
            category_headers = await page.locator('.next-menu-sub-menu-wrapper > .next-menu-item').all()
            for header in category_headers:
                try:
                    await header.click(timeout=2000)
                    await asyncio.sleep(0.2)
                except Exception:
                    pass
            
            print("Expanded all categories.")
            
            endpoint_links = await page.locator('li[data-spm^="d/"] a').all()
            endpoint_paths = []
            for link in endpoint_links:
                href = await link.get_attribute('href')
                if href and 'path=' in href:
                    path = href.split('path=')[-1]
                    if path not in endpoint_paths:
                        endpoint_paths.append(path)
            
            await page.close()
            print(f"Found {len(endpoint_paths)} unique endpoints to scrape.")
            
            if endpoint_paths:
                chunk_size = (len(endpoint_paths) + CONCURRENT_WORKERS - 1) // CONCURRENT_WORKERS
                tasks = []
                for i in range(CONCURRENT_WORKERS):
                    start_index = i * chunk_size
                    end_index = start_index + chunk_size
                    endpoint_chunk = endpoint_paths[start_index:end_index]
                    if endpoint_chunk:
                        tasks.append(worker(browser, endpoint_chunk, i + 1))
                
                results = await asyncio.gather(*tasks)
                for result_dict in results:
                    all_documentation.update(result_dict)

        except Exception as e:
            print(f"A critical error occurred during setup: {e}")
        
        finally:
            output_file = args.output_file
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            print(f"\nSaving {len(all_documentation)} scraped API docs to '{output_file}'...")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(all_documentation, f, indent=2, ensure_ascii=False)
            
            print(f"Successfully saved data to '{output_file}'.")
            await browser.close()
            end_time = time.time()
            print(f"Scraping complete in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Lazada API documentation.")
    parser.add_argument(
        '--output-file',
        type=str,
        default='output/scraped/lazada.json',
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

