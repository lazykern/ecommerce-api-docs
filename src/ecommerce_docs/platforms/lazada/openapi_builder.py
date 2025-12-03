"""Build an OpenAPI spec from scraped Lazada API JSON files."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple
from urllib.parse import urlsplit

# data/raw/lazada/apis/**/*.json by default
DEFAULT_APIS_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "lazada" / "apis"
DEFAULT_OUTPUT_FILE = Path(__file__).resolve().parents[4] / "data" / "processed" / "lazada" / "openapi.json"

TypeSchema = Dict[str, Any]
Param = Dict[str, Any]


def safe_json_loads(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except Exception:
        return value


_SECRET_PATTERNS = [
    re.compile(r"(OSSAccessKeyId=)([^&]+)", re.IGNORECASE),
    re.compile(r"(AccessKeyId=)([^&]+)", re.IGNORECASE),
    re.compile(r"(LTAI[A-Za-z0-9]{10,})"),
]


def redact_secrets(value: Any) -> Any:
    """Scrub access keys and tokens from example payloads/strings."""
    if isinstance(value, dict):
        return {k: redact_secrets(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact_secrets(v) for v in value]
    if isinstance(value, str):
        redacted = value
        for pat in _SECRET_PATTERNS:
            redacted = pat.sub(lambda m: f"{m.group(1)}<redacted>" if m.lastindex and m.lastindex >= 2 else "<redacted>", redacted)
        return redacted
    return value


def ensure_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def clean_text(text: str | None) -> str:
    if not text:
        return ""
    normalized = html.unescape(text).replace("\xa0", " ").strip()
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


def normalize_methods(raw: str | None) -> List[str]:
    if not raw:
        return ["post"]
    methods = []
    for part in re.split(r"[\/\s]+", raw.strip(), flags=re.IGNORECASE):
        if not part:
            continue
        low = part.lower()
        if low in {"get", "post", "put", "delete"}:
            methods.append(low)
        elif low == "hsf":
            methods.append("post")
    return methods or ["post"]


def type_and_format(raw: str) -> Tuple[str, str | None]:
    raw_lower = (raw or "").strip().lower()
    mapping = {
        "string": ("string", None),
        "string[]": ("array", None),
        "number": ("number", None),
        "number[]": ("array", None),
        "integer": ("integer", None),
        "boolean": ("boolean", None),
        "object": ("object", None),
        "object[]": ("array", None),
        "payload": ("string", None),
        "byte[]": ("string", "byte"),
    }
    return mapping.get(raw_lower, ("string", None))


def base_schema(raw_type: str) -> TypeSchema:
    json_type, fmt = type_and_format(raw_type)
    schema: TypeSchema = {"type": json_type}
    if fmt:
        schema["format"] = fmt
    return schema


def is_required(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() in {"true", "yes", "1", "required"}


def param_schema(param: Param) -> TypeSchema:
    raw_type = param.get("type") or ""
    is_array = raw_type.endswith("[]")
    base_type = raw_type[:-2] if is_array else raw_type

    schema = base_schema(base_type)
    children = ensure_list(param.get("children"))

    if schema["type"] == "object" and children:
        child_schema = build_schema_from_params(children)
        schema.update({k: v for k, v in child_schema.items() if k in {"properties", "required"}})

    if is_array:
        items_schema = schema
        if schema.get("type") == "object" and children and not schema.get("properties"):
            items_schema = build_schema_from_params(children)
        schema = {"type": "array", "items": items_schema}

    description = clean_text(param.get("desc"))
    if description:
        schema["description"] = description

    demo = param.get("demo")
    if demo not in (None, ""):
        schema["example"] = safe_json_loads(demo)

    return schema


def build_schema_from_params(params: Iterable[Param]) -> TypeSchema:
    properties: Dict[str, Any] = {}
    required_fields: List[str] = []

    for param in params or []:
        name = param.get("name")
        if not name:
            continue
        properties[name] = param_schema(param)
        if is_required(param.get("required")):
            required_fields.append(name)

    schema: TypeSchema = {"type": "object"}
    if properties:
        schema["properties"] = properties
    if required_fields:
        schema["required"] = sorted(set(required_fields))
    return schema


def build_query_parameters(params: Iterable[Param]) -> List[Dict[str, Any]]:
    query_params: List[Dict[str, Any]] = []
    for param in params or []:
        name = param.get("name")
        if not name:
            continue
        schema = param_schema(param)
        description = schema.pop("description", clean_text(param.get("desc")))
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


def build_request_body(params: Iterable[Param]) -> Dict[str, Any] | None:
    params_list = list(params or [])
    if not params_list:
        return None

    # Heuristic: if there is a single Payload param, treat it as raw string.
    if len(params_list) == 1 and (params_list[0].get("type") or "").lower() == "payload":
        schema = param_schema(params_list[0])
    else:
        schema = build_schema_from_params(params_list)

    return {
        "required": any(is_required(p.get("required")) for p in params_list),
        "content": {"application/json": {"schema": schema}},
    }


def build_examples(request_codes: List[Dict[str, Any]], response_code: Any) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    req_examples: Dict[str, Any] = {}
    for idx, sample in enumerate(request_codes or []):
        lang = sample.get("lang") or f"example_{idx+1}"
        key = re.sub(r"\\W+", "_", lang.lower()) or f"example_{idx+1}"
        code = sample.get("code")
        if code:
            req_examples[key] = {"summary": lang, "value": redact_secrets(code)}

    resp_examples: Dict[str, Any] = {}
    parsed = redact_secrets(safe_json_loads(response_code))
    if parsed not in (None, ""):
        resp_examples["example"] = {"summary": "Response example", "value": parsed}
    return req_examples, resp_examples


def build_responses(output_params: Iterable[Param], response_examples: Dict[str, Any], error_codes: List[Dict[str, Any]]) -> Dict[str, Any]:
    schema = build_schema_from_params(output_params)
    responses: Dict[str, Any] = {
        "200": {
            "description": "Successful operation",
            "content": {
                "application/json": {
                    "schema": schema,
                    **({"examples": response_examples} if response_examples else {}),
                }
            },
        }
    }

    if error_codes:
        error_schema = {
            "type": "object",
            "properties": {
                "code": {"type": "string"},
                "message": {"type": "string"},
            },
        }
        responses["400"] = {
            "description": "; ".join(f"{err.get('code')}: {clean_text(err.get('solution'))}" for err in error_codes if err.get("code")),
            "content": {"application/json": {"schema": error_schema}},
        }
    return responses


def extract_servers(endpoint_params: Iterable[Param]) -> List[str]:
    servers: List[str] = []
    for ep in endpoint_params or []:
        desc = ep.get("desc")
        if not desc:
            continue
        parsed = urlsplit(desc)
        if parsed.scheme and parsed.netloc:
            url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            if url not in servers:
                servers.append(url)
    return servers


def build_operation(api: Dict[str, Any], source_path: Path) -> Dict[str, Any]:
    common_params = ensure_list(api.get("commonParameters", {}).get("data"))
    req_params = ensure_list(api.get("parameters", {}).get("data"))
    output_params = ensure_list(api.get("outputParameters", {}).get("data"))
    examples_data = ensure_list(api.get("examples", {}).get("data"))
    example_block = examples_data[0] if examples_data else {}

    req_examples, resp_examples = build_examples(
        ensure_list(example_block.get("requestCodes")),
        example_block.get("responseCode"),
    )

    error_codes = ensure_list(api.get("errorCodes", {}).get("data"))

    operation: Dict[str, Any] = {
        "tags": [source_path.parent.name],
        "summary": api.get("title") or api.get("path"),
        "description": clean_text(api.get("desc")),
        "operationId": api.get("title") or api.get("path") or source_path.stem,
        "parameters": build_query_parameters(common_params),
        "responses": build_responses(output_params, resp_examples, error_codes),
        "x-error-codes": [
            {
                "code": err.get("code"),
                "description": clean_text(err.get("codeDesc")),
                "solution": clean_text(err.get("solution")),
            }
            for err in error_codes
            if isinstance(err, dict)
        ],
        "x-source-file": str(source_path),
    }

    request_body = build_request_body(req_params)
    if request_body:
        operation["requestBody"] = request_body
    if req_examples:
        operation.setdefault("x-code-samples", req_examples)

    return operation


def build_openapi(apis_dir: Path) -> Dict[str, Any]:
    paths: Dict[str, Any] = {}
    tags: set[str] = set()
    servers: set[str] = set()
    warnings: List[str] = []

    for file_path in sorted(apis_dir.rglob("*.json")):
        try:
            with file_path.open("r", encoding="utf-8") as f:
                doc = json.load(f)
        except Exception as exc:
            warnings.append(f"Failed to load {file_path}: {exc}")
            continue

        api_list = ensure_list(doc.get("data", {}).get("apiList"))
        if not api_list:
            warnings.append(f"No apiList in {file_path}")
            continue

        for api in api_list:
            path = api.get("path")
            if not path:
                warnings.append(f"Missing path for {file_path}")
                continue

            methods = normalize_methods(api.get("method"))
            operation = build_operation(api, file_path)
            tags.update(operation.get("tags", []))
            servers.update(extract_servers(api.get("endpointParams", {}).get("data")))

            for method in methods:
                paths.setdefault(path, {})[method] = operation

    openapi_spec: Dict[str, Any] = {
        "openapi": "3.1.0",
        "info": {
            "title": "Lazada Open Platform API",
            "version": "v1",
            "description": "Auto-generated OpenAPI specification from Lazada developer docs.",
        },
        "servers": [{"url": url, "description": "Lazada region"} for url in sorted(servers)],
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
    endpoints_count = sum(len(v) for v in spec["paths"].values())
    print(f"✅ Built OpenAPI for {endpoints_count} endpoints -> {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Lazada OpenAPI spec from scraped JSON.")
    parser.add_argument("--apis-dir", type=str, default=None, help="Directory containing scraped Lazada APIs.")
    parser.add_argument("--output-file", type=str, default=None, help="Where to write the OpenAPI JSON.")
    args = parser.parse_args()
    main(apis_dir=args.apis_dir, output_file=args.output_file)
