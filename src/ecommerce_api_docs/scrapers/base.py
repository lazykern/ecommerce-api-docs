from abc import ABC, abstractmethod
from typing import Optional
import httpx
from bs4 import BeautifulSoup
from ..models import APIDocumentation


class BaseScraper(ABC):
    """Base class for all API documentation scrapers."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(
            timeout=30.0,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
    
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a web page."""
        try:
            response = self.client.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    @abstractmethod
    def scrape(self) -> APIDocumentation:
        """Main scraping method to be implemented by subclasses."""
        pass
    
    def close(self):
        """Clean up resources."""
        self.client.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close() 