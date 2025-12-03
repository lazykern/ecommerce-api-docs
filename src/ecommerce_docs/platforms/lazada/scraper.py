import argparse
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional, Dict, Any

import requests

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
DEFAULT_BASE_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "lazada"
MAX_WORKERS = 10

# Endpoints
URL_DOC_TREE = "https://open.lazada.com/handler/share/doc/getCategories.json"
URL_DOC_DETAIL = "https://open.lazada.com/handler/share/doc/getDocDetail.json.json"
URL_API_TREE = "https://isvconsole.lazada.com/handler/share/apidoc/getApiCategoryMixed.json"
URL_API_DETAIL = "https://isvconsole.lazada.com/handler/share/apidoc/getApi.json"

# Headers (Mimicking Browser to avoid blocks)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://open.lazada.com/',
}

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def resolve_base_dir(output_dir: Optional[str]) -> Path:
    """Return base output dir."""
    if output_dir:
        return Path(output_dir).expanduser().resolve()
    return DEFAULT_BASE_DIR

def sanitize_name(name: str) -> str:
    """
    Sanitizes string for file system usage.
    Example: "Product API V2.0" -> "product-api-v2.0"
    """
    if not name:
        return "unknown"
    name = name.lower()
    name = name.replace(' ', '-')
    # Keep alphanumeric, underscores, hyphens, and dots
    name = re.sub(r'[^a-z0-9_\-\.]', '', name)
    # Remove repeated hyphens
    name = re.sub(r'-+', '-', name)
    return name.strip('-')

def save_json(data: Any, filepath: Path) -> bool:
    """Helper to save json data to a specific path."""
    try:
        # Ensure directory exists before saving
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Failed to save {filepath}: {e}")
        return False

# ------------------------------------------------------------------
# PART 1: Developer Guides (Tree Structure)
# ------------------------------------------------------------------

def fetch_doc_tree():
    """Fetches the sidebar navigation tree for Guides."""
    params = {
        'oeid': 'LZD_DOC',
        'lang': 'en_US',
        'typeId': '6'
    }
    try:
        print("Fetching Guide Structure...")
        resp = requests.get(URL_DOC_TREE, params=params, headers=HEADERS)
        resp.raise_for_status()
        data = resp.json()
        if 'data' in data and 'children' in data['data']:
            return data['data']['children']
        return []
    except Exception as e:
        print(f"Error fetching guide categories: {e}")
        return []

def fetch_doc_detail(doc_id: int, node_id: int):
    """Fetches specific content of a document guide."""
    params = {
        'oeid': 'LZD_DOC',
        'lang': 'en_US',
        'docId': doc_id,
        'nodeId': node_id
    }
    try:
        resp = requests.get(URL_DOC_DETAIL, params=params, headers=HEADERS)
        if resp.status_code == 200:
            return resp.json()
        return None
    except Exception as e:
        print(f"   ❌ Error Doc {doc_id}: {e}")
        return None

def process_doc_structure(node: Dict, current_path: Path, executor, future_map):
    """
    Recursively walks the Guide JSON tree.
    1. Creates directory for current node.
    2. Queues downloads for documents.
    3. Recurses into sub-nodes.
    """
    node_title = node.get('enTitle', 'untitled')
    node_id = node.get('id')
    
    # Create Directory
    safe_dir_name = sanitize_name(node_title)
    node_dir = current_path / safe_dir_name
    
    docs = node.get('currentDocList', [])
    children = node.get('children', [])

    if docs or children:
        os.makedirs(node_dir, exist_ok=True)

    # Process Documents
    if docs:
        for doc in docs:
            doc_title = doc.get('enTitle', 'untitled')
            doc_id = doc.get('id')
            safe_filename = f"{sanitize_name(doc_title)}.json"
            file_path = node_dir / safe_filename
            
            future = executor.submit(fetch_doc_detail, doc_id, node_id)
            future_map[future] = {
                'type': 'guide',
                'path': file_path,
                'name': doc_title,
                'id': doc_id
            }

    # Process Children
    if children:
        for child in children:
            process_doc_structure(child, node_dir, executor, future_map)

# ------------------------------------------------------------------
# PART 2: API References (Console Structure)
# ------------------------------------------------------------------

def fetch_api_tree():
    """Fetches the list of API categories and endpoints."""
    try:
        print("Fetching API Structure...")
        resp = requests.get(URL_API_TREE, headers=HEADERS)
        resp.raise_for_status()
        data = resp.json()
        if 'data' in data and isinstance(data['data'], list):
            return data['data']
        return []
    except Exception as e:
        print(f"Error fetching API list: {e}")
        return []

def fetch_api_detail(api_path: str):
    """Fetches technical details for a specific API endpoint."""
    params = {'path': api_path}
    try:
        resp = requests.get(URL_API_DETAIL, params=params, headers=HEADERS)
        if resp.status_code == 200:
            return resp.json()
        return None
    except Exception as e:
        print(f"   ❌ Error API {api_path}: {e}")
        return None

def process_api_structure(categories: list, base_dir: Path, executor, future_map):
    """
    Iterates API categories and queues endpoint downloads.
    """
    for category in categories:
        cat_name = category.get('name', 'misc')
        safe_cat_name = sanitize_name(cat_name)
        cat_dir = base_dir / safe_cat_name
        
        api_list = category.get('apiList', [])
        if api_list:
            os.makedirs(cat_dir, exist_ok=True)
            
            for api in api_list:
                api_title = api.get('title')
                api_path = api.get('path')
                
                if not api_path: 
                    continue

                safe_filename = f"{sanitize_name(api_title)}.json"
                file_path = cat_dir / safe_filename
                
                future = executor.submit(fetch_api_detail, api_path)
                future_map[future] = {
                    'type': 'api',
                    'path': file_path,
                    'name': api_title,
                    'id': api_path
                }

# ------------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------------

def main(workers: int = MAX_WORKERS, output_dir: Optional[str] = None) -> None:
    base_dir = resolve_base_dir(output_dir)
    guides_dir = base_dir / "guides"
    apis_dir = base_dir / "apis"
    base_dir.mkdir(parents=True, exist_ok=True)

    future_to_meta = {} 

    print(f"Starting Lazada Scraper with {workers} workers...")
    print(f"Output Directory: {base_dir}")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        
        # 1. Process Developer Guides (Recursive Tree)
        doc_tree = fetch_doc_tree()
        if doc_tree:
            for root_node in doc_tree:
                process_doc_structure(root_node, guides_dir, executor, future_to_meta)

        # 2. Process API References (Flat Categories)
        api_tree = fetch_api_tree()
        if api_tree:
            process_api_structure(api_tree, apis_dir, executor, future_to_meta)

        # 3. Process Downloads
        total = len(future_to_meta)
        print(f"\nProcessing {total} queued downloads...")
        
        success_count = 0
        
        for future in as_completed(future_to_meta):
            meta = future_to_meta[future]
            save_path = meta['path']
            
            try:
                result = future.result()
                if result and result.get('success', False):
                    if save_json(result, save_path):
                        print(f"   [Saved] {save_path.name}")
                        success_count += 1
                else:
                    msg = result.get('errorMessage') if result else "Empty Response"
                    print(f"   [Failed] {meta['type'].upper()}: {meta['name']} - {msg}")
            except Exception as exc:
                print(f"   [Error] {meta['name']}: {exc}")

    print(f"\n✅ Done! Saved {success_count}/{total} files to '{base_dir}/'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Lazada Open Platform (Guides + API Refs).")
    parser.add_argument("--workers", type=int, default=MAX_WORKERS, help="Number of worker threads.")
    parser.add_argument("--output-dir", type=str, default=None, help="Base directory for raw output.")
    args = parser.parse_args()
    
    main(workers=args.workers, output_dir=args.output_dir)