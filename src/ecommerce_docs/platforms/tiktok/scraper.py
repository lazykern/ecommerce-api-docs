import argparse
import json
import os
import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional, List, Dict, Any

import requests

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
DEFAULT_BASE_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "tiktok"
MAX_WORKERS = 10

# API Endpoints
URL_DOC_TREE = "https://partner.tiktokshop.com/api/v1/document/tree"
URL_DOC_DETAIL = "https://partner.tiktokshop.com/api/v1/document/detail"
URL_API_META = "https://partner.tiktokshop.com/api/v1/document/api_meta"

# Static Parameters
COMMON_PARAMS = {
    'workspace_id': '3',
    'aid': '359713',
    'locale': 'en-US'
}

# Headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://partner.tiktokshop.com/',
}

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def resolve_base_dir(output_dir: Optional[str]) -> Path:
    if output_dir:
        return Path(output_dir).expanduser().resolve()
    return DEFAULT_BASE_DIR

def sanitize_name(name: str) -> str:
    """Sanitizes string for file system usage."""
    if not name:
        return "untitled"
    name = name.lower()
    name = name.replace(' ', '-').replace('/', '-')
    name = re.sub(r'[^a-z0-9_\-\.]', '', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')

def save_json(data: Any, filepath: Path) -> bool:
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Failed to save {filepath}: {e}")
        return False

# ------------------------------------------------------------------
# API Interaction
# ------------------------------------------------------------------

def fetch_document_tree() -> List[Dict]:
    """Fetches the entire navigation tree."""
    try:
        print("Fetching Documentation Tree...")
        resp = requests.get(URL_DOC_TREE, params=COMMON_PARAMS, headers=HEADERS)
        resp.raise_for_status()
        data = resp.json()
        if data.get('code') == 0 and 'data' in data:
            return data['data'].get('document_tree', [])
        return []
    except Exception as e:
        print(f"Error fetching tree: {e}")
        return []

def fetch_doc_content(doc_path_id: str):
    """
    Fetches the textual content (Markdown/HTML).
    Used for Guides (doc_type 2) and API Overviews (doc_type 10/1).
    """
    params = COMMON_PARAMS.copy()
    params['document_id'] = doc_path_id
    try:
        resp = requests.get(URL_DOC_DETAIL, params=params, headers=HEADERS)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('code') == 0:
                return data.get('data')
        return None
    except Exception as e:
        print(f"   ❌ Error Content {doc_path_id}: {e}")
        return None

def fetch_api_spec(src_doc_id: str):
    """
    Fetches the structured API specification (Parameters, Schema).
    Used for API Endpoints (doc_type 1).
    """
    params = COMMON_PARAMS.copy()
    params['src_document_id'] = src_doc_id
    try:
        resp = requests.get(URL_API_META, params=params, headers=HEADERS)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('code') == 0:
                return data.get('data')
        return None
    except Exception as e:
        print(f"   ❌ Error Spec {src_doc_id}: {e}")
        return None

# ------------------------------------------------------------------
# Processing Logic
# ------------------------------------------------------------------

def build_hierarchy(flat_list: List[Dict]) -> Dict[str, List[Dict]]:
    tree_map = defaultdict(list)
    for item in flat_list:
        pid = item.get('parent_id', 'ROOT')
        if not pid: pid = 'ROOT'
        tree_map[pid].append(item)
    return tree_map

def process_node_recursive(
    parent_id: str, 
    tree_map: Dict[str, List[Dict]], 
    current_path: Path, 
    executor: ThreadPoolExecutor, 
    future_map: Dict
):
    children = tree_map.get(parent_id, [])
    
    for node in children:
        doc_name = node.get('name', 'untitled')
        doc_id = node.get('document_id')
        doc_path_slug = node.get('document_path')  # e.g., 'get-product-202309'
        doc_type = node.get('doc_type')            # 1=API, 2=Article, 10=Overview?
        is_dir = node.get('is_dir')                # 1=Folder
        
        safe_name = sanitize_name(doc_name)
        
        # If it's a folder, create directory and recurse
        if is_dir == 1:
            new_dir = current_path / safe_name
            os.makedirs(new_dir, exist_ok=True)
            process_node_recursive(doc_id, tree_map, new_dir, executor, future_map)
            # Some folders might also have content (like an overview page attached to the category)
            # If document_path is present on a folder, fetch it as an index/overview
            if doc_path_slug:
                file_path = new_dir / "overview.json"
                future = executor.submit(fetch_doc_content, doc_path_slug)
                future_map[future] = {'path': file_path, 'name': f"{doc_name} (Overview)"}
        
        else:
            # It is a leaf node (Document or API)
            # Use doc_path_slug if available, else fallback to doc_id (though API usually requires path)
            identifier = doc_path_slug if doc_path_slug else doc_id

            if doc_type == 1:
                # === API Endpoint ===
                # 1. Fetch Documentation (Text)
                doc_file_path = current_path / f"{safe_name}.doc.json"
                future_doc = executor.submit(fetch_doc_content, identifier)
                future_map[future_doc] = {'path': doc_file_path, 'name': f"{doc_name} [Doc]"}

                # 2. Fetch Specification (Meta/Schema)
                spec_file_path = current_path / f"{safe_name}.spec.json"
                future_spec = executor.submit(fetch_api_spec, identifier)
                future_map[future_spec] = {'path': spec_file_path, 'name': f"{doc_name} [Spec]"}
            
            else:
                # === Standard Article / Guide ===
                file_path = current_path / f"{safe_name}.json"
                future = executor.submit(fetch_doc_content, identifier)
                future_map[future] = {'path': file_path, 'name': doc_name}

# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main(workers: int = MAX_WORKERS, output_dir: Optional[str] = None) -> None:
    base_dir = resolve_base_dir(output_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    future_to_meta = {} 

    print(f"Starting TikTok Shop Scraper (V2) with {workers} workers...")
    print(f"Output Directory: {base_dir}")

    # 1. Fetch Tree
    flat_tree = fetch_document_tree()
    if not flat_tree:
        print("No documents found.")
        return

    # 2. Build Hierarchy
    tree_map = build_hierarchy(flat_tree)

    # 3. Process
    with ThreadPoolExecutor(max_workers=workers) as executor:
        print("Building directory structure and queuing downloads...")
        process_node_recursive('ROOT', tree_map, base_dir, executor, future_to_meta)

        # 4. Save Results
        total = len(future_to_meta)
        print(f"\nProcessing {total} queued downloads...")
        
        success_count = 0
        for future in as_completed(future_to_meta):
            meta = future_to_meta[future]
            save_path = meta['path']
            
            try:
                result = future.result()
                if result:
                    if save_json(result, save_path):
                        print(f"   [Saved] {save_path.name}")
                        success_count += 1
                else:
                    # Some nodes might be empty or restricted, just log it
                    print(f"   [Skipped] {meta['name']} (No content)")
            except Exception as exc:
                print(f"   [Error] {meta['name']}: {exc}")

    print(f"\n✅ Done! Saved {success_count}/{total} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape TikTok Shop Partner API Docs (Docs + Specs).")
    parser.add_argument("--workers", type=int, default=MAX_WORKERS, help="Number of worker threads.")
    parser.add_argument("--output-dir", type=str, default=None, help="Base directory for raw output.")
    args = parser.parse_args()
    
    main(workers=args.workers, output_dir=args.output_dir)