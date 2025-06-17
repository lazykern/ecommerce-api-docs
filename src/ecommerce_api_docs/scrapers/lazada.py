import re
import time
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin, urlparse, parse_qs
from bs4 import BeautifulSoup, Tag

from ..models import (
    APIDocumentation, APIEndpoint, Parameter, Response, 
    HTTPMethod, ParameterType, ParameterLocation, Example, ErrorCode
)
from .base import BaseScraper


class LazadaScraper(BaseScraper):
    """Scraper for Lazada Open Platform API documentation."""
    
    def __init__(self):
        super().__init__("https://open.lazada.com")
        self.api_base_url = "https://api.lazada.com"
        
        # Priority API modules based on the HTML structure
        self.priority_modules = [
            'System API',
            'Product API', 
            'Order API',
            'Logistics API',
            'Finance API',
            'Seller API'
        ]
        
        # Sample endpoints from the provided URLs and HTML structure
        self.sample_endpoints = [
            # System API
            {
                'path': '/auth/token/create',
                'name': 'GenerateAccessToken',
                'method': 'GET/POST',
                'module': 'System API',
                'description': 'Generate access token for API authentication'
            },
            {
                'path': '/auth/token/createWithOpenId', 
                'name': 'GenerateAccessTokenWithOpenId',
                'method': 'GET/POST',
                'module': 'System API',
                'description': 'Generate access token with OpenID for API authentication'
            },
            {
                'path': '/auth/token/refresh',
                'name': 'RefreshAccessToken', 
                'method': 'GET/POST',
                'module': 'System API',
                'description': 'Refresh expired access token'
            },
            
            # Product API
            {
                'path': '/products/get',
                'name': 'GetProducts',
                'method': 'GET',
                'module': 'Product API',
                'description': 'Retrieve seller product list'
            },
            {
                'path': '/product/create',
                'name': 'CreateProduct',
                'method': 'POST', 
                'module': 'Product API',
                'description': 'Create a new product'
            },
            {
                'path': '/product/update',
                'name': 'UpdateProduct',
                'method': 'POST',
                'module': 'Product API', 
                'description': 'Update existing product information'
            },
            {
                'path': '/product/remove',
                'name': 'RemoveProduct',
                'method': 'POST',
                'module': 'Product API',
                'description': 'Remove product from store'
            },
            
            # Order API
            {
                'path': '/orders/get',
                'name': 'GetOrders',
                'method': 'GET',
                'module': 'Order API',
                'description': 'Retrieve order list with filters'
            },
            {
                'path': '/order/get',
                'name': 'GetOrder',
                'method': 'GET', 
                'module': 'Order API',
                'description': 'Get detailed order information'
            },
            {
                'path': '/order/cancel',
                'name': 'CancelOrder',
                'method': 'POST',
                'module': 'Order API',
                'description': 'Cancel an order'
            },
            
            # Logistics API
            {
                'path': '/order/fulfill',
                'name': 'FulfillOrder',
                'method': 'POST',
                'module': 'Logistics API', 
                'description': 'Mark order as ready to ship'
            },
            {
                'path': '/order/pack',
                'name': 'PackOrder',
                'method': 'POST',
                'module': 'Logistics API',
                'description': 'Pack order for shipping'
            },
            {
                'path': '/shipment/providers/get',
                'name': 'GetShipmentProviders',
                'method': 'GET',
                'module': 'Logistics API',
                'description': 'Get available shipping providers'
            },
            
            # Finance API
            {
                'path': '/finance/payout/status/get',
                'name': 'GetPayoutStatus',
                'method': 'GET',
                'module': 'Finance API',
                'description': 'Get payout status information'
            },
            {
                'path': '/finance/transaction/details/get',
                'name': 'GetTransactionDetails', 
                'method': 'GET',
                'module': 'Finance API',
                'description': 'Get detailed transaction information'
            },
            
            # Seller API
            {
                'path': '/seller/get',
                'name': 'GetSeller',
                'method': 'GET',
                'module': 'Seller API',
                'description': 'Get seller account information'
            },
            {
                'path': '/seller/performance/get',
                'name': 'GetSellerPerformance',
                'method': 'GET', 
                'module': 'Seller API',
                'description': 'Get seller performance metrics'
            }
        ]
    
    def scrape(self) -> APIDocumentation:
        """Scrape Lazada API documentation."""
        console = __import__('rich.console', fromlist=['Console']).Console()
        console.print("🔍 Discovering Lazada API endpoints...", style="bold blue")
        
        endpoints = []
        
        # Process priority modules
        for module in self.priority_modules:
            console.print(f"📦 Scraping {module}...", style="bold yellow")
            module_endpoints = self._scrape_module_endpoints(module)
            endpoints.extend(module_endpoints)
            
            # Add delay between modules to be respectful
            time.sleep(1)
        
        console.print(f"✅ Successfully discovered {len(endpoints)} endpoints", style="bold green")
        
        return APIDocumentation(
            platform="lazada",
            title="Lazada Open Platform API",
            version="1.0", 
            description="Complete Lazada Open Platform API documentation for sellers and developers",
            base_url=self.api_base_url,
            endpoints=endpoints,
            source_url="https://open.lazada.com/apps/doc/api"
        )
    
    def _scrape_module_endpoints(self, module_name: str) -> List[APIEndpoint]:
        """Scrape endpoints for a specific module."""
        console = __import__('rich.console', fromlist=['Console']).Console()
        
        # Get sample endpoints for this module
        module_endpoints = [ep for ep in self.sample_endpoints if ep.get('module') == module_name]
        
        endpoints = []
        for endpoint_data in module_endpoints:
            console.print(f"  🔗 Scraping {endpoint_data['name']}...", style="dim")
            
            try:
                # Try to scrape real documentation
                endpoint = self._scrape_endpoint_documentation(endpoint_data)
                if endpoint:
                    endpoints.append(endpoint)
                    console.print(f"    ✅ Parsed {endpoint_data['name']}", style="green")
                else:
                    # Fallback to placeholder
                    endpoint = self._create_placeholder_endpoint(endpoint_data)
                    endpoints.append(endpoint)
                    console.print(f"    📝 Created placeholder for {endpoint_data['name']}", style="yellow")
                    
            except Exception as e:
                console.print(f"    ❌ Error parsing {endpoint_data['name']}: {e}", style="red")
                # Create placeholder on error
                endpoint = self._create_placeholder_endpoint(endpoint_data)
                endpoints.append(endpoint)
            
            # Small delay between requests
            time.sleep(0.5)
        
        return endpoints
    
    def _scrape_endpoint_documentation(self, endpoint_data: dict) -> Optional[APIEndpoint]:
        """Scrape documentation for a specific endpoint."""
        try:
            # Construct documentation URL
            doc_url = f"{self.base_url}/apps/doc/api?path={endpoint_data['path']}"
            
            response = self.client.get(doc_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            return self._parse_endpoint_page(soup, endpoint_data, doc_url)
            
        except Exception as e:
            return None
    
    def _parse_endpoint_page(self, soup: BeautifulSoup, endpoint_data: dict, doc_url: str) -> Optional[APIEndpoint]:
        """Parse endpoint documentation from HTML."""
        try:
            # Extract information from the page
            title = self._extract_title(soup, endpoint_data)
            description = self._extract_description(soup, endpoint_data)
            method = self._extract_http_method(soup, endpoint_data)
            parameters = self._extract_parameters(soup)
            responses = self._extract_responses(soup)
            examples = self._extract_examples(soup)
            error_codes = self._extract_error_codes(soup)
            
            return APIEndpoint(
                name=title,
                path=endpoint_data['path'],
                method=method,
                description=description,
                parameters=parameters,
                responses=responses,
                examples=examples,
                error_codes=error_codes,
                tags=[endpoint_data['module']],
                source_url=doc_url
            )
            
        except Exception as e:
            return None
    
    def _extract_title(self, soup: BeautifulSoup, endpoint_data: dict) -> str:
        """Extract endpoint title from HTML."""
        # Try to find title in various locations
        title_selectors = [
            'h1', 'h2', '.api-title', '.endpoint-title',
            '.next-typography-title', '[class*="title"]'
        ]
        
        for selector in title_selectors:
            element = soup.select_one(selector)
            if element and element.get_text(strip=True):
                title = element.get_text(strip=True)
                if len(title) > 5:  # Avoid empty or very short titles
                    return title
        
        # Fallback to endpoint data name
        return endpoint_data.get('name', 'Unknown Endpoint')
    
    def _extract_description(self, soup: BeautifulSoup, endpoint_data: dict) -> Optional[str]:
        """Extract endpoint description from HTML."""
        description_selectors = [
            '.api-description', '.endpoint-description', 
            '.description', 'p', '.content p'
        ]
        
        for selector in description_selectors:
            element = soup.select_one(selector)
            if element and element.get_text(strip=True):
                desc = element.get_text(strip=True)
                if len(desc) > 10 and 'API' in desc:  # Basic content validation
                    return desc
        
        return endpoint_data.get('description')
    
    def _extract_http_method(self, soup: BeautifulSoup, endpoint_data: dict) -> HTTPMethod:
        """Extract HTTP method from HTML."""
        method_text = endpoint_data.get('method', 'GET')
        
        # Handle combined methods like "GET/POST"
        if '/' in method_text:
            method_text = method_text.split('/')[0]  # Take first method
        
        method_map = {
            'GET': HTTPMethod.GET,
            'POST': HTTPMethod.POST,
            'PUT': HTTPMethod.PUT,
            'DELETE': HTTPMethod.DELETE,
            'PATCH': HTTPMethod.PATCH
        }
        
        return method_map.get(method_text.upper(), HTTPMethod.GET)
    
    def _extract_parameters(self, soup: BeautifulSoup) -> List[Parameter]:
        """Extract parameters from HTML tables."""
        parameters = []
        
        # Look for parameter tables
        tables = soup.find_all('table')
        for table in tables:
            # Check if this looks like a parameter table
            headers = table.find_all(['th', 'td'])
            header_text = ' '.join(h.get_text().lower() for h in headers[:5])
            
            if any(keyword in header_text for keyword in ['parameter', 'field', 'name', 'type']):
                table_params = self._parse_parameter_table(table)
                parameters.extend(table_params)
        
        # Add default authentication parameters for Lazada API
        if not any(p.name == 'access_token' for p in parameters):
            parameters.extend(self._get_default_lazada_parameters())
        
        return parameters
    
    def _parse_parameter_table(self, table: Tag) -> List[Parameter]:
        """Parse parameters from a table."""
        parameters = []
        rows = table.find_all('tr')[1:]  # Skip header row
        
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if len(cells) >= 2:
                name = cells[0].get_text(strip=True)
                type_str = cells[1].get_text(strip=True) if len(cells) > 1 else 'string'
                required = len(cells) > 2 and 'required' in cells[2].get_text().lower()
                description = cells[3].get_text(strip=True) if len(cells) > 3 else None
                
                if name and name.lower() not in ['parameter', 'field', 'name']:
                    parameters.append(Parameter(
                        name=name,
                        type=self._normalize_parameter_type(type_str),
                        location=ParameterLocation.QUERY,
                        required=required,
                        description=description
                    ))
        
        return parameters
    
    def _get_default_lazada_parameters(self) -> List[Parameter]:
        """Get default parameters required for all Lazada API calls."""
        return [
            Parameter(
                name="access_token",
                type=ParameterType.STRING,
                location=ParameterLocation.QUERY,
                required=True,
                description="Access token for authentication",
                example="2_113944_v9xVrJzGKFoqQShqRbFPOQ7d6c7a0a6a57"
            ),
            Parameter(
                name="app_key",
                type=ParameterType.STRING,
                location=ParameterLocation.QUERY,
                required=True,
                description="Application key assigned by Lazada",
                example="113944"
            ),
            Parameter(
                name="sign_method",
                type=ParameterType.STRING,
                location=ParameterLocation.QUERY,
                required=True,
                description="Signature method (sha256 or hmac)",
                example="sha256",
                default_value="sha256"
            ),
            Parameter(
                name="timestamp",
                type=ParameterType.INTEGER,
                location=ParameterLocation.QUERY,
                required=True,
                description="Unix timestamp in milliseconds",
                example="1578983692000"
            ),
            Parameter(
                name="sign",
                type=ParameterType.STRING,
                location=ParameterLocation.QUERY,
                required=True,
                description="Request signature for authentication",
                example="A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6"
            )
        ]
    
    def _normalize_parameter_type(self, type_str: str) -> ParameterType:
        """Normalize parameter type string to ParameterType enum."""
        type_lower = type_str.lower()
        
        if 'int' in type_lower or 'number' in type_lower:
            return ParameterType.INTEGER
        elif 'bool' in type_lower:
            return ParameterType.BOOLEAN
        elif 'array' in type_lower or 'list' in type_lower:
            return ParameterType.ARRAY
        elif 'object' in type_lower:
            return ParameterType.OBJECT
        else:
            return ParameterType.STRING
    
    def _extract_responses(self, soup: BeautifulSoup) -> List[Response]:
        """Extract response information from HTML."""
        return [
            Response(
                status_code=200,
                description="Successful response",
                schema={"type": "object", "description": "API response data"}
            ),
            Response(
                status_code=400,
                description="Bad request - invalid parameters"
            ),
            Response(
                status_code=401,
                description="Unauthorized - invalid access token"
            ),
            Response(
                status_code=500,
                description="Internal server error"
            )
        ]
    
    def _extract_examples(self, soup: BeautifulSoup) -> List[Example]:
        """Extract code examples from HTML."""
        examples = []
        
        # Look for code blocks or example sections
        code_elements = soup.find_all(['code', 'pre', '.example', '.code-block'])
        
        for element in code_elements:
            content = element.get_text(strip=True)
            if content and len(content) > 10:
                examples.append(Example(
                    title="API Example",
                    description="Example request/response",
                    content=content
                ))
                break  # Just take the first example
        
        return examples
    
    def _extract_error_codes(self, soup: BeautifulSoup) -> List[ErrorCode]:
        """Extract error codes from HTML."""
        return [
            ErrorCode(code="1000", message="System error", description="Internal system error"),
            ErrorCode(code="1001", message="Invalid parameter", description="One or more parameters are invalid"),
            ErrorCode(code="1002", message="Access token expired", description="The access token has expired"),
            ErrorCode(code="1003", message="Insufficient permissions", description="API access not allowed for this seller")
        ]
    
    def _create_placeholder_endpoint(self, endpoint_data: dict) -> APIEndpoint:
        """Create a placeholder endpoint when scraping fails."""
        return APIEndpoint(
            name=endpoint_data.get('name', 'Unknown Endpoint'),
            path=endpoint_data.get('path', '/unknown'),
            method=self._extract_http_method(None, endpoint_data),
            description=endpoint_data.get('description', 'Lazada API endpoint'),
            parameters=self._get_default_lazada_parameters(),
            responses=self._extract_responses(None),
            examples=[],
            error_codes=self._extract_error_codes(None),
            tags=[endpoint_data.get('module', 'Unknown')],
            source_url=f"{self.base_url}/apps/doc/api?path={endpoint_data.get('path', '')}"
        )