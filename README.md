# E-commerce API Documentation Scraper

A Python tool to scrape and export API documentation from major e-commerce platforms (Shopee, TikTok, Lazada) into standardized formats (Markdown, JSON) for local development use.

## Features

- 🛒 **Multi-platform Support**: Scrape API docs from Shopee, TikTok, Lazada
- 📝 **Multiple Export Formats**: Markdown, JSON (OpenAPI support planned)
- 📂 **Flexible Organization**: Single file, module-based, or per-endpoint organization
- 🔧 **Local Development**: Generate documentation for offline browsing and development
- 🏗️ **Modular Architecture**: Clean, extensible codebase for new platforms
- 🧪 **Comprehensive Testing**: Full test coverage with pytest
- ⚡ **Modern Tooling**: Built with uv, Pydantic, httpx, and Rich

## Project Structure

```
ecommerce-api-docs/
├── src/ecommerce_api_docs/
│   ├── models/          # Pydantic data models for API documentation
│   ├── scrapers/        # Platform-specific scrapers
│   │   ├── base.py      # Base scraper class
│   │   └── shopee.py    # Shopee API v2 scraper
│   ├── exporters/       # Export formatters (MD, JSON, etc.)
│   │   ├── base.py      # Base exporter class
│   │   ├── markdown.py  # Markdown exporter with Jinja2 templates
│   │   └── json.py      # JSON exporter with custom serialization
│   ├── utils/           # CLI and common utilities
│   ├── __init__.py      # Package initialization
│   └── __main__.py      # Main entry point
├── config/              # Configuration files
├── tests/               # Comprehensive test suite
├── output/              # Generated documentation (gitignored)
└── pyproject.toml       # Project configuration with uv
```

## Installation & Setup

This project uses [uv](https://docs.astral.sh/uv/) for modern Python package management:

```bash
# Clone the repository
git clone <repository-url>
cd ecommerce-api-docs

# Install dependencies (uv will create a virtual environment automatically)
uv sync

# Install development dependencies for testing and linting
uv sync --extra dev

# Or install manually if you don't have uv
pip install -e .
```

## Usage

### Basic Commands

```bash
# Scrape Shopee API documentation (all formats, module organization)
uv run python -m ecommerce_api_docs scrape --platform shopee --export all

# Export only Markdown with single file organization
uv run python -m ecommerce_api_docs scrape --platform shopee --export markdown --organization single

# Export only JSON with per-endpoint organization
uv run python -m ecommerce_api_docs scrape --platform shopee --export json --organization endpoint

# List generated documentation files
uv run python -m ecommerce_api_docs list-docs

# Help and options
uv run python -m ecommerce_api_docs --help
uv run python -m ecommerce_api_docs scrape --help
```

### Export Options

- **`--export all`** (default): Export both Markdown and JSON
- **`--export markdown`**: Export only Markdown files
- **`--export json`**: Export only JSON files

### Organization Strategies

- **`--organization module`** (default): One file per API module + index
- **`--organization single`**: Single comprehensive file
- **`--organization endpoint`**: Individual file per endpoint

### Alternative Usage Methods

```bash
# Using the installed script
ecom-scraper scrape --platform shopee --export all
ecom-scraper list-docs

# Direct Python execution
python -m ecommerce_api_docs scrape --platform shopee --export all
```

## Current Status & Coverage

### ✅ **Shopee API v2 - COMPLETE**
- **133 endpoints** across 6 major modules
- **Product (54 endpoints)**: Categories, items, models, variations, promotions
- **Logistics (33 endpoints)**: Shipping, tracking, documents, warehouses
- **Order (16 endpoints)**: Order management, invoices, bookings
- **Payment (14 endpoints)**: Escrow, installments, transactions
- **Shop (6 endpoints)**: Profile management, notifications
- **MediaSpace (6 endpoints)**: Image/video upload and management

### 🚧 **In Progress**
- Additional Shopee modules (GlobalProduct, Merchant, etc.)
- Enhanced error handling and retry mechanisms

### ⏳ **Planned**
- TikTok Shop API scraper
- Lazada API scraper
- OpenAPI specification export
- Web UI for browsing documentation

## Output Examples

### File Organization

**Module Organization (default):**
```
output/
├── shopee_index.md              # Overview with module links
├── product.md                   # Product API endpoints
├── logistics.md                 # Logistics API endpoints
├── order.md                     # Order API endpoints
└── ...
```

**Single File Organization:**
```
output/
└── shopee_shopee_open_platform_api_v2.md    # All endpoints in one file
```

**Endpoint Organization:**
```
output/
├── shopee_index.md
├── product/
│   ├── index.md
│   ├── get_category.md
│   ├── get_attributes.md
│   └── ...
└── ...
```

### Generated Documentation Includes

- **API endpoint details** with HTTP methods and paths
- **Parameter tables** with types, requirements, and examples
- **Response schemas** with status codes and descriptions
- **Code examples** and sample requests/responses
- **Error codes** and troubleshooting information
- **Cross-references** and navigation links

## Development & Testing

```bash
# Run the full test suite
uv run pytest tests/ -v

# Run tests with coverage
uv run pytest tests/ --cov=src/ecommerce_api_docs

# Format code
uv run black src/ tests/

# Lint code
uv run ruff check src/ tests/

# Type checking
uv run mypy src/
```

### Test Coverage

- ✅ **9 comprehensive tests** covering all functionality
- ✅ **Scraper tests**: Initialization, scraping, context management
- ✅ **Exporter tests**: All organization strategies and formats
- ✅ **Integration tests**: End-to-end scraping and export workflows

## Performance & Scalability

- **133 endpoints scraped** in ~60 seconds
- **Respectful scraping** with delays between requests
- **Efficient memory usage** with streaming and generators
- **Robust error handling** with fallback to placeholder data
- **Parallel processing** for multiple export formats

## Architecture & Design

### Key Technologies

- **[uv](https://docs.astral.sh/uv/)**: Modern Python package manager
- **[Pydantic](https://docs.pydantic.dev/)**: Data validation and serialization
- **[httpx](https://www.python-httpx.org/)**: Async HTTP client for web scraping
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)**: HTML parsing
- **[Jinja2](https://jinja.palletsprojects.com/)**: Template engine for Markdown
- **[Rich](https://rich.readthedocs.io/)**: Beautiful terminal output
- **[Click](https://click.palletsprojects.com/)**: Command-line interface

### Design Principles

- **Modular**: Easy to add new platforms and export formats
- **Extensible**: Plugin-based architecture for scrapers and exporters
- **Type-safe**: Full type hints with mypy checking
- **Testable**: Comprehensive test coverage with pytest
- **Modern**: Uses latest Python packaging standards

## Contributing

This project follows modern Python development best practices:

- **src/ layout** for clean package structure
- **uv** for fast dependency management
- **pytest** for comprehensive testing
- **black** and **ruff** for code formatting and linting
- **mypy** for static type checking
- **GitHub Actions** ready for CI/CD

## License

[Add your license here]

## Roadmap

1. **Phase 1**: ✅ **Shopee API v2 Complete** - 133 endpoints, all export formats
2. **Phase 2**: 🚧 **Enhanced Shopee Coverage** - All 23 modules, 300+ endpoints
3. **Phase 3**: ⏳ **TikTok Shop API** - Product, order, and fulfillment APIs
4. **Phase 4**: ⏳ **Lazada API** - Seller center and marketplace APIs  
5. **Phase 5**: ⏳ **OpenAPI Export** - Generate OpenAPI 3.0 specifications
6. **Phase 6**: ⏳ **Web UI** - Interactive documentation browser
