# E-commerce API Documentation

This project contains a set of Python scripts to scrape API documentation from major e-commerce platforms—Lazada, Shopee, and TikTok Shop. It then processes the scraped data into a clean, standardized, and well-structured JSON format, creating a valuable resource for developers and API integrators.

The primary goal is to transform messy, inconsistent web documentation into a consistent and machine-readable format.

## Project Structure

```
.
├── output/
│   ├── scraped/
│   │   ├── lazada.json
│   │   ├── shopee.json
│   │   └── tiktok_shop.json
│   └── structured/
│       ├── lazada/
│       ├── shopee/
│       └── tiktok/
├── scrape_lazada.py
├── scrape_shopee.py
├── scrape_tiktok_shop.py
└── build_structured_docs.py
```

- **`scrape_[platform].py`**: These scripts use Playwright to browse and scrape the raw API documentation from each platform's developer portal. They are configurable via the command line.
- **`build_structured_docs.py`**: This script reads the raw JSON files from `output/scraped/`, cleans and standardizes the data, and organizes it into a clear, module-based structure in `output/structured/`. It is also configurable.
- **`output/scraped/`**: Contains the raw, unprocessed JSON output directly from the scraper scripts.
- **`output/structured/`**: Contains the final, clean, and structured API documentation. The data is organized by platform and module, making it easy to navigate and use.

## How to Use

### Prerequisites

You must have Python and Node.js installed. This project uses [Playwright](https://playwright.dev/python/) for web scraping, which requires a browser installation.

### 1. Install Dependencies

First, install the necessary Python packages.

```bash
pip install playwright
python -m playwright install
```

### 2. Run the Scrapers

Execute the scraper scripts to gather the raw documentation. You can run them without arguments to use the default settings, or you can customize the behavior.

#### Default Usage
```bash
# Scrape Lazada documentation
python scrape_lazada.py

# Scrape Shopee documentation
python scrape_shopee.py

# Scrape TikTok Shop documentation
python scrape_tiktok_shop.py
```
These commands will use the default settings: 8 workers and will save the output to `output/scraped/[platform].json`.

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