import json
import os
import re
from urllib.parse import unquote

OUTPUT_DIR = "docs"


def clean_key(key):
    """Removes invisible characters from dictionary keys."""
    return re.sub(r'[\u200b\uff0c]', '', key).strip()


def clean_value(value):
    """Removes invisible characters from string values."""
    if isinstance(value, str):
        return re.sub(r'[\u200b\uff0c]', '', value).strip()
    return value


def clean_recursively(obj):
    """Recursively removes invisible characters from all keys and string values in a nested structure."""
    if isinstance(obj, dict):
        return {clean_key(k): clean_recursively(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_recursively(elem) for elem in obj]
    return clean_value(obj)


def ensure_dir(file_path):
    """Ensures the directory for a given file path exists."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_json(data, file_path):
    """Saves a dictionary to a JSON file."""
    ensure_dir(file_path)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_module_and_name_from_path(path):
    """Extracts a module and resource name from a URL path."""
    parts = [part for part in path.split('/') if part and not part.isdigit()]
    if not parts:
        return 'general', 'default'
    
    module_parts = []
    # Collect parts that are likely module names (not version-like)
    for part in parts:
        if not re.match(r'^(v\d+|\d{6,})$', part):
            module_parts.append(part)
        else:
            break # Stop when a version-like part is found
    
    if len(module_parts) > 1:
        return module_parts[0], '_'.join(module_parts[1:])
    elif len(module_parts) == 1:
        return module_parts[0], module_parts[0]
    
    return 'general', '_'.join(parts)


def process_lazada_docs():
    platform = "lazada"
    input_file = "lazada_api_documentation.json"
    print(f"Processing {input_file}...")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Could not read or parse {input_file}: {e}")
        return

    for path_encoded, endpoint_data_raw in data.items():
        endpoint_data = clean_recursively(endpoint_data_raw)
        path = unquote(endpoint_data.get('path', ''))
        module, name_from_path = get_module_and_name_from_path(path)
        
        endpoint_name = endpoint_data.get('endpoint_name') or name_from_path
        safe_endpoint_name = re.sub(r'[^\w\-.]', '_', endpoint_name)

        methods = [m.strip() for m in endpoint_data.get('method', '').split('/') if m.strip()]

        parameters = {
            "path": [], "query": [], "header": [], "body": [],
            "common": [{
                "name": p.get("name"), "type": p.get("type"),
                "required": "yes" in p.get("required_", "").lower(),
                "description": p.get("description")
            } for p in endpoint_data.get("common_parameters", [])]
        }
        
        request_params = endpoint_data.get("parameters", [])
        common_param_names = {p['name'] for p in parameters['common']}
        parameters["query"] = [{
            "name": p.get("name"), "type": p.get("type"),
            "required": "yes" in p.get("required_", "").lower(),
            "description": p.get("description")
        } for p in request_params if p.get('name') not in common_param_names]
        
        structured_data = {
            "platform": platform, "module": module, "endpoint_name": endpoint_name,
            "version": None,
            "summary": endpoint_data.get('description', '').split('.')[0],
            "description": endpoint_data.get('description'),
            "path": path, "http_method": methods, "parameters": parameters,
            "request_examples": [{"language": lang, "code": code} for lang, code in endpoint_data.get("request_example", {}).items()],
            "response": {
                "schema": endpoint_data.get("response_parameters", []),
                "examples": [{"language": lang, "code": code} for lang, code in endpoint_data.get("response_example", {}).items()]
            },
            "error_codes": [{ "code": e.get("error_code"), "message": e.get("error_message"), "description": e.get("solution") } for e in endpoint_data.get("error_codes", [])],
            "platform_specific": { "service_endpoints": endpoint_data.get("service_endpoints", []) }
        }
        
        output_path = os.path.join(OUTPUT_DIR, platform, module, f"{safe_endpoint_name}.json")
        save_json(structured_data, output_path)
    
    print(f"Finished processing for {platform}.")


def process_shopee_docs():
    platform = "shopee"
    input_file = "shopee_api_documentation.json"
    print(f"Processing {input_file}...")

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Could not read or parse {input_file}: {e}")
        return

    for key, endpoint_data_raw in data.items():
        endpoint_data = clean_recursively(endpoint_data_raw)
        parts = key.split('.')
        version, module, endpoint_name = (parts[0], parts[1], '_'.join(parts[2:])) if len(parts) > 2 else (None, 'general', key)
        
        safe_endpoint_name = re.sub(r'[^\w\-.]', '_', endpoint_name)

        parameters = {
            "path": [], "query": [], "header": [], "body": [], "common": []
        }
        parameters["query"] = [{
            "name": p.get("name"), "type": p.get("type"),
            "required": "true" in p.get("required", "").lower(),
            "description": p.get("description"), "sample": p.get("sample"),
        } for p in endpoint_data.get("request_parameters", [])]
        
        structured_data = {
            "platform": platform, "module": module, "endpoint_name": endpoint_name,
            "version": version,
            "summary": endpoint_data.get('description', '').split('.')[0],
            "description": endpoint_data.get('description'),
            "path": endpoint_data.get('request_url'),
            "http_method": [endpoint_data.get('request_method')], "parameters": parameters,
            "request_examples": [{"language": lang, "code": code} for lang, code in endpoint_data.get("request_example", {}).items() if code != "N/A"],
            "response": {
                "schema": endpoint_data.get("response_parameters", []),
                "examples": [{"language": lang, "code": code} for lang, code in endpoint_data.get("response_example", {}).items() if code != "N/A"]
            },
            "error_codes": [{ "code": e.get("error"), "message": e.get("error_description") } for e in endpoint_data.get("error_codes", [])],
            "platform_specific": { "service_endpoints": endpoint_data.get("common_parameters", []) }
        }
        
        output_path = os.path.join(OUTPUT_DIR, platform, module, f"{safe_endpoint_name}.json")
        save_json(structured_data, output_path)

    print(f"Finished processing for {platform}.")


def process_tiktok_docs():
    platform = "tiktok_shop"
    input_file = "tiktok_shop_api_documentation.json"
    print(f"Processing {input_file}...")

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Could not read or parse {input_file}: {e}")
        return

    for url, page_data_raw in data.items():
        page_data = clean_recursively(page_data_raw)
        
        page_type = page_data.get('page_type')
        module_raw = page_data.get('category', 'general')
        module = re.sub(r'\s+', '_', module_raw.lower())

        if page_type == 'API' and page_data.get('path'):
            path = page_data.get('path', '')
            version_match = re.search(r'/(\d{6,})/', path)
            version = version_match.group(1) if version_match else None
            
            _, name_from_path = get_module_and_name_from_path(path)
            endpoint_name = page_data.get('endpoint_name') or name_from_path
            safe_endpoint_name = re.sub(r'[^\w\-.]', '_', endpoint_name)
            
            parameters = {
                "path": [], "query": [], "header": [], "body": [], "common": []
            }
            parameters['header'] = page_data.get('header', [])
            parameters['query'] = page_data.get('query', [])
            parameters['body'] = page_data.get('body', [])

            structured_data = {
                "platform": platform, "module": module, "endpoint_name": endpoint_name,
                "version": version,
                "summary": page_data.get('description', '').split('.')[0],
                "description": page_data.get('description'),
                "path": path,
                "http_method": [page_data.get('method', '')],
                "parameters": parameters,
                "request_examples": [{"language": lang, "code": code} for lang, code in page_data.get("request_example", {}).items()],
                "response": {
                    "schema": page_data.get("parameters", []),
                    "examples": [{"language": lang, "code": code} for lang, code in page_data.get("response_example", {}).items()]
                },
                "error_codes": page_data.get("error_code", []),
                "platform_specific": {"original_url": url}
            }
            
            output_path = os.path.join(OUTPUT_DIR, platform, module, f"{safe_endpoint_name}.json")
            save_json(structured_data, output_path)

        elif page_type == 'Prose':
            title = page_data.get('title', 'Untitled Article')
            content = page_data.get('content', 'No content found.')
            safe_title = re.sub(r'[^\w\-.]', '_', title) if title else "untitled"

            structured_data = {
                "platform": platform,
                "page_type": "article",
                "module": module,
                "title": title,
                "content": content,
                "platform_specific": {"original_url": url}
            }

            output_path = os.path.join(OUTPUT_DIR, platform, module, f"{safe_title}.json")
            save_json(structured_data, output_path)

    print(f"Finished processing for {platform}.")


def main():
    """Main function to orchestrate the documentation processing."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    processors = {
        "Lazada": process_lazada_docs,
        "Shopee": process_shopee_docs,
        "TikTok Shop": process_tiktok_docs,
    }

    for name, processor_func in processors.items():
        try:
            processor_func()
        except Exception as e:
            print(f"An error occurred processing {name}: {e}")

    print(f"\nProcessing complete. Structured documentation is in '{OUTPUT_DIR}'.")
    print(f"You can explore the generated files to see the new structure.")

if __name__ == "__main__":
    main() 