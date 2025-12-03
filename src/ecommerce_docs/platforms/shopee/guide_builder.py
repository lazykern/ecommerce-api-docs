"""Normalize Shopee developer guides into Markdown + JSON metadata."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Optional

import html2text


DEFAULT_INPUT_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "shopee" / "guides"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[4] / "data" / "processed" / "shopee" / "guides"


_slug_regex = re.compile(r"[^a-z0-9\-]")


def slugify(name: str) -> str:
    name = name.strip().lower().replace(" ", "-")
    name = _slug_regex.sub("-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-") or "guide"


def html_to_markdown(html: str) -> str:
    parser = html2text.HTML2Text()
    parser.body_width = 0  # do not wrap
    parser.ignore_links = False
    parser.ignore_images = False
    parser.ignore_emphasis = False
    parser.protect_links = True
    return parser.handle(html or "").strip()


@dataclass
class GuideRecord:
    slug: str
    title: str
    category: str
    language: str
    document_id: int
    original_url: str
    release_time: Optional[int]
    update_time: Optional[int]
    markdown_path: str
    json_path: str


def normalize_guide(path: Path, input_dir: Path, output_dir: Path) -> GuideRecord | None:
    rel = path.relative_to(input_dir)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    title = data.get("title") or path.stem
    category = data.get("category_name") or ""
    language = data.get("language_code") or "en"
    document_id = data.get("document_id") or 0
    html_content = data.get("content") or ""

    # Build markdown + metadata
    markdown = html_to_markdown(html_content)
    slug = slugify(title)

    out_dir = output_dir / rel.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / f"{slug}.md"
    json_path = out_dir / f"{slug}.json"

    original_url = f"https://open.shopee.com/developer-guide/{document_id}" if document_id else ""

    md_path.write_text(markdown, encoding="utf-8")

    record = {
        "title": title,
        "category": category,
        "language": language,
        "document_id": document_id,
        "release_time": data.get("release_time"),
        "update_time": data.get("update_time"),
        "status": data.get("status"),
        "original_url": original_url,
        "raw_file": str(path),
        "markdown_file": str(md_path),
        "html_length": len(html_content),
    }
    json_path.write_text(json.dumps(record, indent=2), encoding="utf-8")

    return GuideRecord(
        slug=slug,
        title=title,
        category=category,
        language=language,
        document_id=document_id,
        original_url=original_url,
        release_time=data.get("release_time"),
        update_time=data.get("update_time"),
        markdown_path=str(md_path),
        json_path=str(json_path),
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
    print(f"✅ Processed {len(records)} guides into {out_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Shopee dev guides into Markdown + metadata.")
    parser.add_argument("--input-dir", type=str, default=None, help="Raw guides directory (JSON files).")
    parser.add_argument("--output-dir", type=str, default=None, help="Destination for processed guides.")
    args = parser.parse_args()
    main(input_dir=args.input_dir, output_dir=args.output_dir)
