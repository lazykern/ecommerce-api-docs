"""Build an OpenAPI spec from scraped Shopee endpoint JSON files."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple
from urllib.parse import urlsplit

# data/raw/shopee/apis/**/*.json by default
DEFAULT_APIS_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "shopee" / "apis"
DEFAULT_OUTPUT_FILE = Path(__file__).resolve().parents[4] / "data" / "processed" / "shopee" / "openapi.json"

TypeSchema = Dict[str, Any]
Parameter = Dict[str, Any]


def safe_json_loads(value: Any, fallback: Any) -> Any:
    """JSON-decode a value that might already be structured or empty."""
    if value is None:
        return fallback
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except Exception:
        return fallback


def ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def clean_text(text: str | None) -> str:
    if not text:
        return ""
    # Keep HTML tags but normalize whitespace so OpenAPI description stays readable.
    normalized = html.unescape(text).replace("\xa0", " ").strip()
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def normalize_method(method: Any) -> str:
    try:
        method_val = int(method)
    except Exception:
        method_val = None
    return "get" if method_val == 2 else "post"


def type_and_format(raw: str) -> Tuple[str, str | None]:
    raw_lower = (raw or "").strip().lower()
    mapping = {
        "int": ("integer", "int"),
        "int32": ("integer", "int32"),
        "int64": ("integer", "int64"),
        "timestamp": ("integer", "timestamp"),
        "float": ("number", "float"),
        "double": ("number", "double"),
        "boolean": ("boolean", None),
        "object": ("object", None),
        "string": ("string", None),
        "file": ("string", "binary"),
        "array": ("array", None),
    }
    return mapping.get(raw_lower, ("string", None))


def is_required(flag: Any) -> bool:
    if isinstance(flag, bool):
        return flag
    if flag is None:
        return False
    return str(flag).strip().lower() in {"true", "yes", "1", "required"}


def base_schema(raw_type: str) -> TypeSchema:
    json_type, fmt = type_and_format(raw_type)
    schema: TypeSchema = {"type": json_type}
    if fmt:
        schema["format"] = fmt
    return schema


def param_schema(param: Parameter) -> TypeSchema:
    raw_type = (param.get("type") or "").strip()
    children = ensure_list(param.get("children"))
    is_array = raw_type.endswith("[]") or raw_type.lower() == "array"
    base_type = raw_type[:-2] if raw_type.endswith("[]") else raw_type

    schema = base_schema(base_type)
    if schema["type"] == "object" and children:
        child_schema = build_schema_from_params(children)
        if child_schema.get("properties"):
            schema["properties"] = child_schema["properties"]
        if child_schema.get("required"):
            schema["required"] = child_schema["required"]

    if is_array:
        items_schema = schema
        if schema.get("type") == "object" and not schema.get("properties") and children:
            items_schema = build_schema_from_params(children)
        schema = {"type": "array", "items": items_schema}

    description = clean_text(param.get("description"))
    if description:
        schema["description"] = description

    sample = param.get("sample")
    if sample not in (None, ""):
        schema["example"] = sample

    return schema


def build_schema_from_params(params: Iterable[Parameter]) -> TypeSchema:
    properties: Dict[str, Any] = {}
    required_fields: List[str] = []

    for param in params or []:
        name = param.get("name")
        if not name:
            continue
        schema = param_schema(param)
        properties[name] = schema
        if is_required(param.get("required")):
            required_fields.append(name)

    schema: TypeSchema = {"type": "object"}
    if properties:
        schema["properties"] = properties
    if required_fields:
        schema["required"] = sorted(set(required_fields))
    return schema


def build_query_parameters(params: Iterable[Parameter]) -> List[Dict[str, Any]]:
    query_params: List[Dict[str, Any]] = []
    for param in params or []:
        name = param.get("name")
        if not name:
            continue
        schema = param_schema(param)
        description = schema.pop("description", clean_text(param.get("description")))
        example = schema.pop("example", None)

        entry: Dict[str, Any] = {
            "name": name,
            "in": "query",
            "required": is_required(param.get("required")),
            "schema": schema,
        }
        if description:
            entry["description"] = description
        if example is not None:
            entry["example"] = example
        query_params.append(entry)
    return query_params


def build_examples(samples: List[Dict[str, Any]]) -> Dict[str, Any]:
    examples: Dict[str, Any] = {}
    for idx, sample in enumerate(samples):
        if not isinstance(sample, dict):
            continue
        label = sample.get("type") or f"example_{idx + 1}"
        key = re.sub(r"\W+", "_", label.lower()) or f"example_{idx + 1}"
        value = sample.get("value")
        if isinstance(value, str):
            parsed = safe_json_loads(value, value)
        else:
            parsed = value
        examples[key] = {"summary": label, "value": parsed}
    return examples


def build_request_body(request_params: List[Parameter], samples: List[Dict[str, Any]]) -> Dict[str, Any]:
    schema = build_schema_from_params(request_params)
    content: Dict[str, Any] = {"application/json": {"schema": schema}}
    request_examples = build_examples(samples)
    if request_examples:
        content["application/json"]["examples"] = request_examples
    return {
        "required": any(is_required(p.get("required")) for p in request_params),
        "content": content,
    }


def dedupe_errors(error_list: Iterable[Dict[str, Any]]) -> List[Dict[str, str]]:
    seen = set()
    cleaned = []
    for err in error_list or []:
        if not isinstance(err, dict):
            continue
        code = err.get("name") or err.get("code") or ""
        message = clean_text(err.get("description") or err.get("message"))
        key = (code, message)
        if key in seen:
            continue
        seen.add(key)
        cleaned.append({"code": code, "message": message})
    return cleaned


def build_responses(
    response_params: List[Parameter],
    response_samples: List[Dict[str, Any]],
    error_codes: List[Dict[str, str]],
    error_examples: List[Dict[str, Any]],
) -> Dict[str, Any]:
    responses: Dict[str, Any] = {}

    schema = build_schema_from_params(response_params)
    content: Dict[str, Any] = {"application/json": {"schema": schema}}
    examples = build_examples(response_samples)
    if examples:
        content["application/json"]["examples"] = examples
    responses["200"] = {"description": "Successful operation", "content": content}

    if error_codes or error_examples:
        error_schema = {
            "type": "object",
            "properties": {
                "error": {"type": "string"},
                "message": {"type": "string"},
            },
        }
        error_content: Dict[str, Any] = {"application/json": {"schema": error_schema}}
        error_example_payload = build_examples(error_examples)
        if error_example_payload:
            error_content["application/json"]["examples"] = error_example_payload

        error_lines = "; ".join(f"{err['code']}: {err['message']}" for err in error_codes if err.get("code"))
        responses["400"] = {
            "description": error_lines or "Error response",
            "content": error_content,
        }

    return responses


def extract_server(url: str | None) -> str | None:
    if not url:
        return None
    parsed = urlsplit(url)
    if parsed.scheme and parsed.netloc:
        return f"{parsed.scheme}://{parsed.netloc}"
    return None


def build_operation(data: Dict[str, Any], source_path: Path) -> Dict[str, Any]:
    param_blob = safe_json_loads(data.get("params"), {})
    request_params = ensure_list(param_blob.get("request_params"))
    response_params = ensure_list(param_blob.get("response_params"))

    common_params = ensure_list(safe_json_loads(data.get("common_params"), []))
    request_samples = ensure_list(safe_json_loads(data.get("request_sample"), []))
    response_samples = ensure_list(safe_json_loads(data.get("response_sample"), []))
    error_examples = ensure_list(safe_json_loads(data.get("error_example"), []))
    error_codes = dedupe_errors(data.get("error_list") or [])

    description = clean_text(data.get("define"))
    module_name = data.get("module_name") or source_path.parent.name

    operation: Dict[str, Any] = {
        "tags": [module_name.title()],
        "summary": data.get("api_name") or data.get("path") or str(source_path.stem),
        "description": description,
        "operationId": data.get("api_name") or str(source_path.stem),
        "parameters": [],
        "responses": {},
    }

    # Common query params are always appended to the URL.
    operation["parameters"].extend(build_query_parameters(common_params))

    method = normalize_method(data.get("method"))
    if method == "get":
        operation["parameters"].extend(build_query_parameters(request_params))
    else:
        if request_params:
            operation["requestBody"] = build_request_body(request_params, request_samples)

    operation["responses"] = build_responses(response_params, response_samples, error_codes, error_examples)

    # Keep extra context for downstream tooling.
    if error_codes:
        operation["x-error-codes"] = error_codes
    if data.get("api_permission"):
        operation["x-api-permissions"] = data.get("api_permission")
    operation["x-source-file"] = str(source_path)

    return operation


def build_openapi(apis_dir: Path) -> Dict[str, Any]:
    paths: Dict[str, Any] = {}
    tags: set[str] = set()
    servers: set[str] = set()
    warnings: List[str] = []

    for file_path in sorted(apis_dir.rglob("*.json")):
        try:
            with file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            warnings.append(f"Failed to load {file_path}: {exc}")
            continue

        path = data.get("path")
        if not path:
            warnings.append(f"Missing path for {file_path}")
            continue

        method = normalize_method(data.get("method"))
        operation = build_operation(data, file_path)
        tags.update(operation.get("tags", []))

        server_values = [extract_server(data.get("url")), extract_server(data.get("test_url"))]
        servers.update([s for s in server_values if s])

        paths.setdefault(path, {})[method] = operation

    openapi_spec: Dict[str, Any] = {
        "openapi": "3.1.0",
        "info": {
            "title": "Shopee Open Platform API",
            "version": "v2",
            "description": "Auto-generated OpenAPI specification from Shopee developer docs.",
        },
        "servers": [{"url": url, "description": ("Test Server" if "test" in url else "Live Server")} for url in sorted(servers)],
        "tags": [{"name": tag} for tag in sorted(tags)],
        "paths": paths,
        "x-generator": {"source": str(apis_dir), "warnings": warnings},
    }
    return openapi_spec


def main(apis_dir: str | None = None, output_file: str | None = None) -> None:
    apis_path = Path(apis_dir).expanduser().resolve() if apis_dir else DEFAULT_APIS_DIR
    out_path = Path(output_file).expanduser().resolve() if output_file else DEFAULT_OUTPUT_FILE

    if not apis_path.exists():
        raise SystemExit(f"Input directory not found: {apis_path}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    spec = build_openapi(apis_path)
    out_path.write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    endpoints_count = sum(len(ops) for ops in spec["paths"].values())
    print(f"✅ Built OpenAPI for {endpoints_count} endpoints -> {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Shopee OpenAPI spec from scraped JSON.")
    parser.add_argument("--apis-dir", type=str, default=None, help="Directory containing scraped Shopee APIs.")
    parser.add_argument("--output-file", type=str, default=None, help="Where to write the OpenAPI JSON.")
    args = parser.parse_args()
    main(apis_dir=args.apis_dir, output_file=args.output_file)
