"""Configuration settings for the ecommerce API scraper."""

from typing import Dict, List
from pathlib import Path

# Base directories
PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
CACHE_DIR = PROJECT_ROOT / ".cache"

# Scraping settings
SCRAPER_SETTINGS = {
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "timeout": 30,
    "retry_attempts": 3,
    "delay_between_requests": 1.0,  # seconds
}

# Platform-specific settings
PLATFORM_SETTINGS = {
    "shopee": {
        "base_url": "https://open.shopee.com",
        "api_base_url": "https://partner.shopeemobile.com",
        "docs_url": "https://open.shopee.com/documents",
        "rate_limit": "1000 requests per hour",
    },
    "tiktok": {
        "base_url": "https://developers.tiktok.com",
        "api_base_url": "https://open-api.tiktok.com",
        "docs_url": "https://developers.tiktok.com/doc",
        "rate_limit": "500 requests per hour",
    },
    "lazada": {
        "base_url": "https://open.lazada.com",
        "api_base_url": "https://api.lazada.com",
        "docs_url": "https://open.lazada.com/doc",
        "rate_limit": "1000 requests per hour",
    },
}

# Export settings
EXPORT_SETTINGS = {
    "create_index": True,
    "pretty_json": True,
    "include_metadata": True,
    "markdown_theme": "default",
}

# Logging configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file_enabled": True,
    "file_path": PROJECT_ROOT / "logs" / "scraper.log",
} 