# E-commerce API Documentation

This project contains a set of Python scripts to scrape API documentation from major e-commerce platforms—Lazada, Shopee, and TikTok Shop. It then processes the scraped data into a clean, standardized, and well-structured JSON format, creating a valuable resource for developers and API integrators.

The primary goal is to transform messy, inconsistent web documentation into a consistent and machine-readable format.

## Project Structure

```
.
├── src/ecommerce_docs/           # package code (scrapers, builders, CLI)
│   └── platforms/{shopee,lazada}/  # platform scrapers + generators
├── data/
│   ├── raw/shopee/               # scraped JSON (guides + apis)
│   ├── processed/shopee/         # generated artifacts (e.g., openapi.json)
│   └── legacy/                   # archived outputs/old trees
└── scripts/                      # optional thin shims (future)
```

- **`src/ecommerce_docs/platforms/[platform]`**: Platform-specific scrapers and generators.
- **`data/raw/`**: Raw, unprocessed JSON directly from scraper scripts.
- **`data/processed/`**: Generated artifacts (OpenAPI specs, future dev guides).
- **`shopee/*.py`**: Legacy entrypoints that forward to the package code; prefer the CLI.

## How to Use

### Prerequisites

You must have Python and Node.js installed. This project uses [Playwright](https://playwright.dev/python/) for web scraping, which requires a browser installation.

### 1. Install Dependencies

With [`uv`](https://github.com/astral-sh/uv) (recommended):

```bash
uv sync
python -m playwright install
```

Without `uv`:

```bash
pip install playwright
python -m playwright install
```

### 2. Run the Scrapers

You can use the CLI entrypoint (new) or the original scripts (existing).

#### Using the CLI (uv)
```bash
uv run ecomdocs shopee scrape
# add --workers N or --output-dir PATH if needed

uv run ecomdocs lazada scrape
# add --workers N or --output-dir PATH if needed

uv run ecomdocs tiktok scrape
# add --workers N or --output-dir PATH if needed
# writes doc + spec JSON into data/raw/tiktok/ by default

uv run ecomdocs lazada build-guides
# add --input-dir PATH or --output-dir PATH to override

uv run ecomdocs shopee build-guides
# add --input-dir PATH or --output-dir PATH to override

uv run ecomdocs tiktok build-guides
# add --input-dir PATH or --output-dir PATH to override
```

#### Using the original scripts

Execute the scraper scripts to gather the raw documentation. You can run them without arguments to use the default settings, or you can customize the behavior.

- Shopee legacy: `python shopee/scrape_shopee.py` (delegates to the new package code; prefer the CLI)

#### Default Usage
```bash
# Scrape Lazada documentation
python scrape_lazada.py

# Scrape Shopee documentation
python scrape_shopee.py

# Scrape TikTok Shop documentation
python scrape_tiktok_shop.py
```
These legacy scripts default to 8 workers and write to `output/scraped/[platform].json`; the `ecomdocs` CLI writes to `data/raw/<platform>/` unless you pass `--output-dir`.

#### Custom Usage
You can specify the number of workers and the output file path.
```bash
# Example: Scrape Lazada with 4 workers and a custom output file
python scrape_lazada.py --workers 4 --output-file custom/lazada_raw.json
```

### 3. Build the Structured Documentation

After scraping, run the build script to process the raw data.

#### Default Usage
```bash
python build_structured_docs.py
```
This will read from `output/scraped/` and write the structured documentation to `output/structured/`.

#### Custom Usage
You can specify the input and output directories.
```bash
# Example: Build docs from a custom source to a custom destination
python build_structured_docs.py --input-dir custom/ --output-dir release/docs
```

## Output Data Model

The final JSON files in `output/structured/` follow a consistent data model, making them easy to parse and integrate into other systems.

### API Endpoint Model

```json
{
  "platform": "tiktok",
  "module": "product",
  "endpoint_name": "products_search",
  "version": "202405",
  "summary": "This API is used to get a list of products that meet certain criteria.",
  "description": "This API is used to get a list of products that meet certain criteria. Version\n202405\n  \nAPI Testing Tool",
  "path": "/product/202405/products/search",
  "http_method": ["POST"],
  "parameters": {
    "path": [],
    "query": [],
    "header": [],
    "body": []
  },
  "request_examples": [],
  "response": {
    "schema": [],
    "examples": []
  },
  "error_codes": [],
  "platform_specific": {
    "original_url": "https://partner.tiktokshop.com/docv2/page/663c9d79a37c1a02e6e3f469"
  }
}
```

### Article Model

For platforms with prose documentation (like TikTok Shop), articles are also saved in a structured format.

```json
{
  "platform": "tiktok",
  "page_type": "article",
  "module": "products",
  "title": "Products API overview",
  "content": "...",
  "platform_specific": {
    "original_url": "https://partner.tiktokshop.com/docv2/page/650a6e74b143de02c01b1793"
  }
}
```

## Legacy locations

- `data/legacy/output/` and `data/legacy/output_old/`: archived outputs from the previous layout.
- `data/legacy/shopee_old/`: historical Shopee scripts/assets kept for reference.
