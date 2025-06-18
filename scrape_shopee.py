import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import json
import re
import time
import argparse
import os

# Number of parallel workers to run
CONCURRENT_WORKERS = 8

async def scrape_endpoint_documentation(page, endpoint_name):
    """
    Scrapes the documentation for a single API endpoint efficiently.
    """
    documentation = {}
    try:
        # The main loop now handles waiting for navigation.
        # This initial wait can be removed to speed things up.
        
        # Locate the main container for the endpoint details
        detail_container = page.locator('.api-reference-detail-container')

        documentation['request_method'] = await detail_container.locator('.request-method').inner_text()
        documentation['request_url'] = await detail_container.locator('.request-url').inner_text()
        documentation['description'] = await detail_container.locator('.api-reference-description').inner_text()

        # Helper function to scrape tables into a list of dictionaries
        async def scrape_table(selector):
            """
            Scrapes a table and returns a list of dictionaries,
            using the table headers as keys.
            """
            table_data = []
            table = await page.query_selector(selector)
            if table:
                header_elements = await table.query_selector_all('thead th')
                headers = [re.sub(r'\s+', '_', (await h.inner_text()).strip()).lower() for h in header_elements]
                
                rows = await table.query_selector_all('tbody > tr')
                for row in rows:
                    cells = await row.query_selector_all('td')
                    row_data = {}
                    for i, cell in enumerate(cells):
                        if i < len(headers):
                            cell_text = (' '.join((await cell.inner_text()).split())).strip()
                            row_data[headers[i]] = cell_text
                    if row_data:
                        table_data.append(row_data)
            return table_data

        documentation['common_parameters'] = await scrape_table('.common-parameters-box .basic-table')
        documentation['request_parameters'] = await scrape_table('.request-parameters-box .basic-table')
        documentation['response_parameters'] = await scrape_table('.response-parameters-box .basic-table')
        documentation['error_codes'] = await scrape_table('.error-codes-box .basic-table')

        async def scrape_code_example(selector):
            """
            Optimized to scrape code examples from tabbed sections
            by waiting for content instead of using fixed delays.
            """
            example_data = {}
            container = await page.query_selector(selector)
            if container:
                tabs = await container.query_selector_all('.tab-label-container')
                for tab in tabs:
                    label = (await tab.inner_text()).strip()
                    await tab.click()
                    
                    key = label.lower().replace(' ', '_')
                    example_container_selector = f'.example-container[name="{label}"]'
                    
                    # Efficiently wait for the specific tab content to be visible
                    try:
                        await page.wait_for_selector(example_container_selector, state='visible', timeout=1000)
                        example_container = await container.query_selector(example_container_selector)
                        if example_container:
                            code_text = await example_container.inner_text()
                            example_data[key] = code_text.strip()
                    except Exception:
                        # Handle cases where a tab might not have content or is slow to load
                        example_data[key] = "N/A"

            return example_data

        documentation['request_example'] = await scrape_code_example('.request-example-box')
        documentation['response_example'] = await scrape_code_example('.response-example-box')
        documentation['error_example'] = await scrape_code_example('.error-example-box')

    except Exception as e:
        print(f"    - Could not scrape full details for {endpoint_name}: {e}")

    return documentation

async def worker(browser, endpoint_names, worker_id):
    """
    A worker that scrapes a subset of endpoint documentation pages.
    """
    print(f"[Worker {worker_id}] Starting to scrape {len(endpoint_names)} endpoints.")
    context = await browser.new_context()
    page = await context.new_page()
    worker_docs = {}

    try:
        # Each worker navigates to the base URL once
        await page.goto("https://open.shopee.com/documents/v2/v2.product.get_category?module=89&type=1", wait_until='networkidle')

        for i, endpoint_name in enumerate(endpoint_names):
            print(f"[Worker {worker_id}] Scraping: {endpoint_name} ({i+1}/{len(endpoint_names)})")
            try:
                endpoint_link_locator = page.locator(f".api-reference-item[data-ts-content_name='{endpoint_name}']")
                await endpoint_link_locator.click()
                await page.wait_for_load_state('networkidle', timeout=30000)
                
                documentation = await scrape_endpoint_documentation(page, endpoint_name)
                worker_docs[endpoint_name] = documentation
            except PlaywrightTimeoutError:
                print(f"  [Worker {worker_id}] Timeout processing endpoint {endpoint_name}. Skipping.")
                continue
            except Exception as e:
                print(f"  [Worker {worker_id}] Failed to process endpoint {endpoint_name}: {e}")
                # Optional: Add a retry mechanism here
                continue
    except Exception as e:
        print(f"[Worker {worker_id}] Failed to navigate to base URL: {e}")
    finally:
        await context.close()
        print(f"[Worker {worker_id}] Finished.")
    
    return worker_docs

async def main(args):
    """Main function to orchestrate the Shopee API documentation scraping."""
    start_time = time.time()
    all_documentation = {}
    BASE_API_REF_URL = "https://open.shopee.com/documents/v2/v2.product.get_category?module=89&type=1"
    
    global CONCURRENT_WORKERS
    CONCURRENT_WORKERS = args.workers

    print("Starting Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            print(f"Navigating to {BASE_API_REF_URL} to collect endpoint list...")
            await page.goto(BASE_API_REF_URL, wait_until='networkidle')
            print("Page loaded successfully.")

            category_containers = await page.query_selector_all('.category-item-container')
            print(f"Found {len(category_containers)} API categories.")

            endpoint_names = []
            for container in category_containers:
                # This logic to expand categories seems to be based on the class,
                # which might not be the most robust. Let's try to click if not expanded.
                is_expanded = await container.query_selector('.category-folded-icon--expand') is not None
                if not is_expanded:
                    category_name_box = await container.query_selector('.category-item-name-box')
                    if category_name_box:
                        await category_name_box.click()
                        # It might be good to wait for a moment for the content to load
                        await page.wait_for_timeout(200)

                links = await container.query_selector_all('.api-reference-item')
                for link in links:
                    name = await link.get_attribute('data-ts-content_name')
                    if name:
                        endpoint_names.append(name)

            await page.close()
            print(f"Found a total of {len(endpoint_names)} endpoints to scrape.")

            if endpoint_names:
                chunk_size = (len(endpoint_names) + CONCURRENT_WORKERS - 1) // CONCURRENT_WORKERS
                tasks = []
                for i in range(CONCURRENT_WORKERS):
                    start_index = i * chunk_size
                    end_index = start_index + chunk_size
                    endpoint_chunk = endpoint_names[start_index:end_index]
                    if endpoint_chunk:
                        tasks.append(worker(browser, endpoint_chunk, i + 1))
                
                # Gather results from all workers
                results = await asyncio.gather(*tasks)
                for result_dict in results:
                    all_documentation.update(result_dict)

        except Exception as e:
            print(f"A critical error occurred during setup: {e}")
        
        finally:
            output_file = args.output_file
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            print(f"\nSaving {len(all_documentation)} scraped API docs to '{output_file}'...")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(all_documentation, f, indent=2, ensure_ascii=False)
            
            print(f"Successfully saved data to '{output_file}'.")
            await browser.close()
            end_time = time.time()
            print(f"Scraping complete in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Shopee API documentation.")
    parser.add_argument(
        '--output-file',
        type=str,
        default='output/scraped/shopee.json',
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



