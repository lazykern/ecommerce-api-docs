"""Normalize Lazada developer guides into Markdown + JSON metadata."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List, Optional

import html2text
from bs4 import BeautifulSoup


DEFAULT_INPUT_DIR = Path(__file__).resolve().parents[4] / "data" / "raw" / "lazada" / "guides"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[4] / "data" / "processed" / "lazada" / "guides"


_slug_regex = re.compile(r"[^a-z0-9\-]")


def slugify(name: str) -> str:
    name = name.strip().lower().replace(" ", "-")
    name = _slug_regex.sub("-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-") or "guide"


def _table_to_markdown(table_html: str) -> str:
    soup = BeautifulSoup(table_html, "html.parser")
    rows: list[list[str]] = []

    for tr in soup.find_all("tr"):
        cells = tr.find_all(["th", "td"])
        if not cells:
            continue

        row: list[str] = []
        for cell in cells:
            text = " ".join(cell.stripped_strings)
            text = re.sub(r"\s+", " ", text).strip()
            colspan = int(cell.get("colspan", 1) or 1)
            for i in range(max(colspan, 1)):
                row.append(text if i == 0 else "")

        rows.append(row)

    if not rows:
        return ""

    max_cols = max(len(r) for r in rows)
    padded_rows = [r + [""] * (max_cols - len(r)) for r in rows]

    header = padded_rows[0]
    separator = "|".join(["---"] * max_cols)
    body = padded_rows[1:]

    lines = [
        " | ".join(header),
        separator,
        *(" | ".join(r) for r in body),
    ]
    return "\n".join(lines)


def html_to_markdown(html: str) -> str:
    soup = BeautifulSoup(html or "", "html.parser")
    table_placeholders: dict[str, str] = {}

    for idx, table in enumerate(soup.find_all("table")):
        placeholder = f"__TABLE_PLACEHOLDER_{idx}__"
        table_placeholders[placeholder] = _table_to_markdown(str(table))
        table.replace_with(soup.new_string(placeholder))

    parser = html2text.HTML2Text()
    parser.body_width = 0  # do not wrap
    parser.ignore_links = False
    parser.ignore_images = False
    parser.ignore_emphasis = False
    parser.protect_links = True
    markdown = parser.handle(str(soup)).strip()

    for placeholder, table_md in table_placeholders.items():
        replacement = f"\n\n{table_md}\n\n" if table_md else "\n\n"
        markdown = markdown.replace(placeholder, replacement)

    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()


@dataclass
class GuideRecord:
    slug: str
    title: str
    category: str
    language: str
    document_id: int | None
    original_url: str
    markdown_path: str
    json_path: str


def _pick_content(data: dict) -> tuple[str, str]:
    """Return (language, html_content). Prefers English if present."""
    if data.get("enContent"):
        return "en", data.get("enContent", "")
    if data.get("cnContent"):
        return "cn", data.get("cnContent", "")
    return "unknown", data.get("content", "") or ""


def normalize_guide(path: Path, input_dir: Path, output_dir: Path) -> GuideRecord | None:
    rel = path.relative_to(input_dir)
    data = json.loads(path.read_text(encoding="utf-8"))
    doc = data.get("data") or {}

    title = doc.get("enTitle") or doc.get("cnTitle") or path.stem
    category = rel.parts[0] if len(rel.parts) > 1 else "general"
    language, html_content = _pick_content(doc)
    document_id = doc.get("id")
    slug = slugify(title)

    out_dir = output_dir / rel.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / f"{slug}.md"
    json_path = out_dir / f"{slug}.json"

    original_url = ""
    if document_id:
        node_id = doc.get("parentId")
        if node_id:
            original_url = f"https://open.lazada.com/doc/doc?docId={document_id}&nodeId={node_id}"
        else:
            original_url = f"https://open.lazada.com/doc/doc?docId={document_id}"

    markdown = html_to_markdown(html_content)
    md_path.write_text(markdown, encoding="utf-8")

    record = {
        "title": title,
        "category": category,
        "language": language,
        "document_id": document_id,
        "original_url": original_url,
        "raw_file": str(path),
        "markdown_file": str(md_path),
        "html_length": len(html_content),
        "last_modified": doc.get("lastModified"),
        "views": doc.get("views"),
        "tags": doc.get("enTags") or doc.get("cnTags") or [],
        "author": doc.get("author"),
    }
    json_path.write_text(json.dumps(record, indent=2), encoding="utf-8")

    return GuideRecord(
        slug=slug,
        title=title,
        category=category,
        language=language,
        document_id=document_id,
        original_url=original_url,
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
    print(f"✅ Processed {len(records)} Lazada guides into {out_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Lazada dev guides into Markdown + metadata.")
    parser.add_argument("--input-dir", type=str, default=None, help="Raw guides directory (JSON files).")
    parser.add_argument("--output-dir", type=str, default=None, help="Destination for processed guides.")
    args = parser.parse_args()
    main(input_dir=args.input_dir, output_dir=args.output_dir)
