"""Normalize TikTok Shop guides into Markdown + JSON metadata."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

DEFAULT_INPUT_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "tiktok"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[4] / "data" / "processed" / "tiktok" / "guides"

_slug_regex = re.compile(r"[^a-z0-9\-]")


def slugify(name: str) -> str:
    name = name.strip().lower().replace(" ", "-")
    name = _slug_regex.sub("-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-") or "guide"


@dataclass
class GuideRecord:
    slug: str
    title: str
    category: str
    document_id: str | None
    doc_type: int | None
    original_url: str
    markdown_path: str
    json_path: str
    raw_file: str


def normalize_guide(path: Path, input_dir: Path, output_dir: Path) -> GuideRecord | None:
    """
    Convert a single TikTok Shop guide JSON into Markdown + metadata.
    Skips API docs/spec files.
    """
    if path.name.endswith(".spec.json"):
        return None

    rel = path.relative_to(input_dir)
    data = json.loads(path.read_text(encoding="utf-8"))

    # Skip API documents
    if data.get("is_api_doc") is True or data.get("doc_type") == 1:
        return None

    title = data.get("title") or path.stem
    content = (data.get("content") or "").strip()
    category = rel.parent.as_posix() if rel.parent.as_posix() != "." else "general"
    document_id = data.get("document_id") or None
    doc_type = data.get("doc_type")
    slug = slugify(title)

    out_dir = output_dir / rel.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / f"{slug}.md"
    json_path = out_dir / f"{slug}.json"

    original_url = f"https://partner.tiktokshop.com/docv2/page/{document_id}" if document_id else ""

    md_path.write_text(content, encoding="utf-8")

    record = {
        "title": title,
        "category": category,
        "doc_type": doc_type,
        "document_id": document_id,
        "original_url": original_url,
        "raw_file": str(path),
        "markdown_file": str(md_path),
        "content_length": len(content),
        "update_time": data.get("update_time"),
        "view_count": data.get("view_count"),
        "keywords": data.get("keywords", []),
    }
    json_path.write_text(json.dumps(record, indent=2), encoding="utf-8")

    return GuideRecord(
        slug=slug,
        title=title,
        category=category,
        document_id=document_id,
        doc_type=doc_type,
        original_url=original_url,
        markdown_path=str(md_path),
        json_path=str(json_path),
        raw_file=str(path),
    )


def build_guides(input_dir: Path, output_dir: Path) -> List[GuideRecord]:
    records: List[GuideRecord] = []
    for path in sorted(input_dir.rglob("*.json")):
        rec = normalize_guide(path, input_dir, output_dir)
        if rec:
            records.append(rec)

    index = [asdict(r) for r in records]
    (output_dir / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    return records


def main(input_dir: Optional[str] = None, output_dir: Optional[str] = None) -> None:
    in_dir = Path(input_dir).expanduser().resolve() if input_dir else DEFAULT_INPUT_DIR
    out_dir = Path(output_dir).expanduser().resolve() if output_dir else DEFAULT_OUTPUT_DIR

    if not in_dir.exists():
        raise SystemExit(f"Input directory not found: {in_dir}")

    out_dir.mkdir(parents=True, exist_ok=True)
    records = build_guides(in_dir, out_dir)
    print(f"✅ Processed {len(records)} TikTok guides into {out_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build TikTok Shop guides into Markdown + metadata.")
    parser.add_argument("--input-dir", type=str, default=None, help="Raw guides directory (JSON files).")
    parser.add_argument("--output-dir", type=str, default=None, help="Destination for processed guides.")
    args = parser.parse_args()
    main(input_dir=args.input_dir, output_dir=args.output_dir)
