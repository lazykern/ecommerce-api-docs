# E-commerce API Documentation Scraper

A Python project to scrape and extract API documentation from major e-commerce platforms (Shopee, TikTok, Lazada) and export them in standardized formats for local development use.

## Features

- 🛒 **Multi-platform Support**: Scrape API docs from Shopee, TikTok, Lazada
- 📝 **Multiple Export Formats**: Markdown, JSON (OpenAPI support planned)
- 🔧 **Local Development**: Feed scraped data to APIs for local documentation viewing
- 🏗️ **Modular Architecture**: Easy to extend for new platforms

## Project Structure

```
ecommerce-api-docs/
├── src/ecommerce_api_docs/
│   ├── models/          # Data models for API documentation
│   ├── scrapers/        # Platform-specific scrapers
│   ├── exporters/       # Export formatters (MD, JSON, etc.)
│   ├── utils/           # Common utilities and CLI
│   ├── __init__.py      # Package initialization
│   └── __main__.py      # Main entry point
├── config/              # Configuration files
├── output/              # Generated documentation
├── tests/               # Test files
└── pyproject.toml       # Project configuration
```

## Installation & Setup

This project uses [uv](https://docs.astral.sh/uv/) for modern Python package management:

```bash
# Clone the repository
git clone <repository-url>
cd ecommerce-api-docs

# Install dependencies (uv will create a virtual environment automatically)
uv sync

# Or install manually if you don't have uv
pip install -e .
```

## Usage

### With uv (Recommended)

```bash
# Scrape Shopee API documentation (Markdown + JSON)
uv run python -m ecommerce_api_docs scrape --platform shopee --export both

# Scrape and export only Markdown
uv run python -m ecommerce_api_docs scrape --platform shopee --export markdown

# Scrape and export only JSON
uv run python -m ecommerce_api_docs scrape --platform shopee --export json

# List generated documentation files
uv run python -m ecommerce_api_docs list-docs

# Help
uv run python -m ecommerce_api_docs --help
```

### Using the installed script

```bash
# After installation, you can also use the ecom-scraper command
ecom-scraper scrape --platform shopee --export both
ecom-scraper list-docs
```

### Direct Python execution

```bash
# If you have the package installed in your environment
python -m ecommerce_api_docs scrape --platform shopee --export both
```

## Current Status

- ✅ Project structure setup
- ✅ Shopee API v2 scraper (sample endpoint)
- ✅ Markdown export
- ✅ JSON export
- ✅ CLI interface with uv support
- 🚧 Full Shopee API scraping (in progress)
- ⏳ TikTok scraper (planned)
- ⏳ Lazada scraper (planned)

## Output Formats

### Markdown
- Human-readable documentation
- Perfect for local development wikis
- Easy to browse and search
- Includes parameter tables, examples, and error codes

### JSON
- Machine-readable format
- Can be fed to API documentation tools
- Structured data for further processing
- Compatible with documentation generators

## Example Output

After running the scraper, you'll get files like:
```
output/
├── shopee_shopee_open_platform_api.md    # Human-readable docs
└── shopee_shopee_open_platform_api.json  # Machine-readable data
```

The Markdown includes:
- API endpoint details
- Parameter tables with types and descriptions
- Response examples
- Error codes
- Authentication requirements
- Rate limiting information

## Development

```bash
# Run tests
uv run pytest

# Format code
uv run black .

# Lint code
uv run ruff check .

# Type checking
uv run mypy .
```

## Roadmap

1. **Phase 1**: ✅ Shopee API v2 foundation + MD/JSON export
2. **Phase 2**: 🚧 Complete Shopee API scraping
3. **Phase 3**: ⏳ TikTok Shop API scraper
4. **Phase 4**: ⏳ Lazada API scraper  
5. **Phase 5**: ⏳ OpenAPI specification export
6. **Phase 6**: ⏳ Web UI for browsing documentation

## Contributing

This project follows modern Python packaging standards:
- Uses `src/` layout for the package
- Entry points defined in `pyproject.toml`
- Compatible with `uv` for dependency management
- Modular architecture for easy extension
