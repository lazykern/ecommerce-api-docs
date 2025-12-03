import argparse
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import requests

# Configuration
DEFAULT_BASE_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "shopee"
MAX_WORKERS = 10

# Headers provided in prompt
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://open.shopee.com/',
}

# Shared Params
SPC_CDS = 'e03c60db-915e-4b0b-a39c-451815aec0ac'
SPC_CDS_VER = '2'


def resolve_base_dir(output_dir: Optional[str]) -> Path:
    """Return base output dir, defaulting to repo-level data/raw/shopee."""
    if output_dir:
        return Path(output_dir).expanduser().resolve()
    return DEFAULT_BASE_DIR

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def sanitize_name(name):
    """
    Converts 'Getting Started' -> 'getting-started'
    Keeps dots for API names like 'v2.product.get_item'
    """
    if not name:
        return "unknown"
    # Lowercase
    name = name.lower()
    # Replace spaces with hyphens
    name = name.replace(' ', '-')
    # Remove characters that aren't alphanumerics, underscores, hyphens, or dots
    name = re.sub(r'[^a-z0-9_\-\.]', '', name)
    # Remove repeated hyphens
    name = re.sub(r'-+', '-', name)
    return name.strip('-')

def save_json(data, filepath):
    """Helper to save json data to a specific path."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Failed to save {filepath}: {e}")
        return False

# ------------------------------------------------------------------
# PART 1: Developer Guides (Articles)
# ------------------------------------------------------------------

def fetch_guide_list():
    url = "https://open.shopee.com/opservice/api/v1/developer_guide/list"
    params = {
        'SPC_CDS': SPC_CDS,
        'SPC_CDS_VER': SPC_CDS_VER,
        'language_code': 'en'
    }
    
    try:
        print("Fetching Guide List...")
        resp = requests.get(url, params=params, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Error fetching list: {e}")
        return None

def fetch_document_detail(document_id):
    url = "https://open.shopee.com/opservice/api/v1/developer_guide/detail"
    params = {
        'SPC_CDS': SPC_CDS,
        'SPC_CDS_VER': SPC_CDS_VER,
        'document_id': document_id,
        'language_code': 'en'
    }
    
    current_headers = HEADERS.copy()
    current_headers['Referer'] = f'https://open.shopee.com/developer-guide/{document_id}'

    try:
        resp = requests.get(url, params=params, headers=current_headers)
        if resp.status_code == 200:
            return resp.json()
        return None
    except Exception as e:
        print(f"   ❌ Error Guide ID {document_id}: {e}")
        return None

def process_guide_structure(items, current_path, executor, future_map):
    """
    Recursively creates directories and submits file fetch tasks.
    current_path: The directory path where these items belong.
    """
    # Ensure current directory exists
    os.makedirs(current_path, exist_ok=True)

    for item in items:
        item_type = item.get('item_type')
        item_id = item.get('item_id')
        item_name = item.get('item_name', 'untitled')
        
        safe_name = sanitize_name(item_name)

        if item_type == 1:
            # Category -> Create Subdirectory
            new_path = os.path.join(current_path, safe_name)
            if 'children' in item:
                process_guide_structure(
                    item['children'], new_path, executor, future_map
                )

        elif item_type == 2:
            # Document -> Submit Task for File
            file_path = os.path.join(current_path, f"{safe_name}.json")
            future = executor.submit(fetch_document_detail, item_id)
            # Store metadata so we know where to save result
            future_map[future] = {
                'type': 'guide',
                'path': file_path,
                'name': item_name
            }

# ------------------------------------------------------------------
# PART 2: API Specifications (Endpoints)
# ------------------------------------------------------------------

def fetch_api_module_list():
    url = "https://open.shopee.com/opservice/api/v1/doc/module/"
    params = {
        'version': '2',
        'SPC_CDS': SPC_CDS,
        'SPC_CDS_VER': SPC_CDS_VER
    }

    try:
        print("Fetching API Module List...")
        resp = requests.get(url, params=params, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Error fetching API module list: {e}")
        return None

def fetch_api_detail(api_name):
    url = "https://open.shopee.com/opservice/api/v1/doc/api/"
    params = {
        'SPC_CDS': SPC_CDS,
        'SPC_CDS_VER': SPC_CDS_VER,
        'version': '2',
        'api_name': api_name
    }

    try:
        resp = requests.get(url, params=params, headers=HEADERS)
        if resp.status_code == 200:
            return resp.json()
        return None
    except Exception as e:
        print(f"   ❌ Error API {api_name}: {e}")
        return None

def process_api_structure(modules, executor, future_map, apis_dir):
    """
    Iterates API modules and submits fetch tasks.
    Saves to 'apis/{module_name}/' directory.
    """
    # Ensure base API directory exists
    os.makedirs(apis_dir, exist_ok=True)

    for module in modules:
        # Get module name (e.g. "Product", "Order")
        module_name = module.get('module_name', 'misc')
        safe_module_dir = sanitize_name(module_name)
        
        # Create module-specific path: shopee/apis/product/
        module_path = os.path.join(apis_dir, safe_module_dir)
        os.makedirs(module_path, exist_ok=True)

        for item in module.get('items', []):
            item_name = item.get('name') # e.g., v2.product.get_item
            item_type = item.get('type')
            
            # Filter for actual API endpoints
            if item_type == 1 or ('.' in item_name and 'v2' in item_name):
                # Use item_name directly for filename
                safe_filename = sanitize_name(item_name) + ".json"
                file_path = os.path.join(module_path, safe_filename)
                
                future = executor.submit(fetch_api_detail, item_name)
                future_map[future] = {
                    'type': 'api',
                    'path': file_path,
                    'name': item_name
                }

# ------------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------------

def main(workers: int = MAX_WORKERS, output_dir: Optional[str] = None) -> None:
    base_dir = resolve_base_dir(output_dir)
    guides_dir = base_dir / "guides"
    apis_dir = base_dir / "apis"
    base_dir.mkdir(parents=True, exist_ok=True)

    # Setup mapping of Future -> Metadata
    future_to_meta = {} 

    print(f"Starting Scraper with {workers} workers...")
    print(f"Output Base Directory: {base_dir}")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        
        # 1. Guides Structure
        list_data = fetch_guide_list()
        if list_data and 'developer_guide_list' in list_data:
            print(f"Processing Guide Structure...")
            process_guide_structure(
                list_data['developer_guide_list'], 
                guides_dir, 
                executor, 
                future_to_meta
            )

        # 2. API Structure
        api_list_data = fetch_api_module_list()
        if api_list_data and 'modules' in api_list_data:
            print(f"Processing API Structure...")
            process_api_structure(
                api_list_data['modules'], 
                executor, 
                future_to_meta,
                apis_dir
            )

        # 3. Process Results
        total = len(future_to_meta)
        print(f"\nProcessing {total} queued downloads...")
        
        count = 0
        success_count = 0
        
        for future in as_completed(future_to_meta):
            meta = future_to_meta[future]
            save_path = meta['path']
            
            try:
                result = future.result()
                if result:
                    # Save individual file
                    if save_json(result, save_path):
                        print(f"   [Saved] {os.path.basename(save_path)}")
                        success_count += 1
                else:
                    print(f"   [Failed] {meta['name']}")
            except Exception as exc:
                print(f"   [Error] {meta['name']}: {exc}")
            
            count += 1

    print(f"\n✅ Done! Saved {success_count}/{total} files to '{base_dir}/'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Shopee API docs (guides + endpoints).")
    parser.add_argument("--workers", type=int, default=MAX_WORKERS, help="Number of worker threads.")
    parser.add_argument("--output-dir", type=str, default=None, help="Base directory for raw output.")
    args = parser.parse_args()
    main(workers=args.workers, output_dir=args.output_dir)
