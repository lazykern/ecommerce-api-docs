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

Use the CLI entrypoint (preferred):
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
