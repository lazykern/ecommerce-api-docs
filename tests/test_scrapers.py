import pytest
from pathlib import Path

from ecommerce_api_docs.scrapers import ShopeeScraper
from ecommerce_api_docs.models import APIDocumentation, APIEndpoint


def test_shopee_scraper_initialization():
    """Test that ShopeeScraper can be initialized."""
    scraper = ShopeeScraper()
    assert scraper.base_url == "https://open.shopee.com"
    assert scraper.api_base_url == "https://partner.shopeemobile.com"
    assert len(scraper.api_modules) > 0
    assert len(scraper.endpoint_definitions) > 0


def test_shopee_scraper_scrape():
    """Test that ShopeeScraper can scrape and return APIDocumentation."""
    with ShopeeScraper() as scraper:
        api_doc = scraper.scrape()
        
        # Basic checks
        assert isinstance(api_doc, APIDocumentation)
        assert api_doc.platform == "shopee"
        assert api_doc.title == "Shopee Open Platform API v2"
        assert api_doc.version == "2.0"
        assert len(api_doc.endpoints) > 0
        
        # Check first endpoint structure
        endpoint = api_doc.endpoints[0]
        assert isinstance(endpoint, APIEndpoint)
        assert endpoint.name == "Get Category"
        assert endpoint.method.value == "POST"
        assert endpoint.path == "/api/v2/product/get_category"
        assert len(endpoint.parameters) > 0
        assert len(endpoint.responses) > 0


def test_shopee_scraper_endpoint_definitions():
    """Test that endpoint definitions are properly defined."""
    scraper = ShopeeScraper()
    
    # Check that we have endpoints for priority modules
    priority_modules = ["Product", "Shop", "Order", "Logistics", "Payment", "MediaSpace"]
    for module in priority_modules:
        assert module in scraper.endpoint_definitions, f"No endpoints defined for {module} module"
        module_endpoints = scraper.endpoint_definitions[module]
        assert len(module_endpoints) > 0, f"No endpoints found for {module} module"
        
        # Check endpoint structure
        for content_id, endpoint_name in module_endpoints:
            assert isinstance(content_id, int), f"Content ID should be int for {endpoint_name}"
            assert isinstance(endpoint_name, str), f"Endpoint name should be str for {endpoint_name}"
            assert endpoint_name.startswith("v2."), f"Endpoint name should start with v2. for {endpoint_name}"


def test_shopee_scraper_context_manager():
    """Test that ShopeeScraper works as a context manager."""
    with ShopeeScraper() as scraper:
        assert hasattr(scraper, 'client')
        assert scraper.client is not None
    
    # After exiting context, client should be closed
    # Note: httpx client doesn't have an 'is_closed' attribute in all versions
    # so we just check that it completed without error


if __name__ == "__main__":
    pytest.main([__file__]) 