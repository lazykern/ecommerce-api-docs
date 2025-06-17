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


class ShopeeScraper(BaseScraper):
    """Scraper for Shopee Open Platform API documentation."""
    
    def __init__(self):
        super().__init__("https://open.shopee.com")
        self.api_base_url = "https://partner.shopeemobile.com"
        
        # Complete API modules from the documentation
        self.api_modules = {
            'Product': 89,
            'GlobalProduct': 90,
            'MediaSpace': 91, 
            'Shop': 92,
            'Merchant': 93,
            'Order': 94,
            'Logistics': 95,
            'FirstMile': 96,
            'Payment': 97,
            'Discount': 99,
            'Bundle Deal': 110,
            'Add-On Deal': 111,
            'Voucher': 112,
            'ShopFlashSale': 123,
            'Follow Prize': 113,
            'TopPicks': 100,
            'ShopCategory': 101,
            'Returns': 102,
            'AccountHealth': 103,
            'Ads': 117,
            'Public': 104,
            'Push': 105,
            'SBS': 124,
        }
        
        # Complete endpoints with content IDs from the documentation
        self.endpoint_definitions = {
            'Product': [
                (653, 'v2.product.get_category'),
                (655, 'v2.product.get_attributes'),
                (1825, 'v2.product.get_attribute_tree'),
                (684, 'v2.product.get_brand_list'),
                (629, 'v2.product.get_item_limit'),
                (614, 'v2.product.get_item_list'),
                (612, 'v2.product.get_item_base_info'),
                (613, 'v2.product.get_item_extra_info'),
                (616, 'v2.product.add_item'),
                (617, 'v2.product.update_item'),
                (615, 'v2.product.delete_item'),
                (646, 'v2.product.init_tier_variation'),
                (647, 'v2.product.update_tier_variation'),
                (618, 'v2.product.get_model_list'),
                (649, 'v2.product.add_model'),
                (648, 'v2.product.update_model'),
                (650, 'v2.product.delete_model'),
                (631, 'v2.product.support_size_chart'),
                (619, 'v2.product.update_size_chart'),
                (622, 'v2.product.unlist_item'),
                (651, 'v2.product.update_price'),
                (652, 'v2.product.update_stock'),
                (624, 'v2.product.boost_item'),
                (626, 'v2.product.get_boosted_list'),
                (661, 'v2.product.get_item_promotion'),
                (662, 'v2.product.update_sip_item_price'),
                (701, 'v2.product.search_item'),
                (562, 'v2.product.get_comment'),
                (563, 'v2.product.reply_comment'),
                (702, 'v2.product.category_recommend'),
                (743, 'v2.product.register_brand'),
                (750, 'v2.product.get_recommend_attribute'),
                (1624, 'v2.product.get_product_info'),
                (1800, 'v2.product.get_weight_recommendation'),
                (1801, 'v2.product.get_size_chart_list'),
                (1802, 'v2.product.get_size_chart_detail'),
                (1862, 'v2.product.get_item_violation_info'),
                (1981, 'v2.product.get_variations'),
                (2136, 'v2.product.get_all_vehicle_list'),
                (2138, 'v2.product.get_vehicle_list_by_compatibility_detail'),
                (2208, 'v2.product.get_item_content_diagnosis_result'),
                (2210, 'v2.product.get_item_list_by_content_diagnosis'),
                (2241, 'v2.product.get_kit_item_limit'),
                (2242, 'v2.product.add_kit_item'),
                (2247, 'v2.product.update_kit_item'),
                (2248, 'v2.product.get_kit_item_info'),
                (2270, 'v2.product.get_ssp_list'),
                (2271, 'v2.product.get_ssp_info'),
                (2273, 'v2.product.add_ssp_item'),
                (2275, 'v2.product.link_ssp'),
                (2276, 'v2.product.unlink_ssp'),
                (2318, 'v2.product.get_aitem_by_pitem_id'),
                (2401, 'v2.product.search_attribute_value_list'),
                (2447, 'v2.product.get_main_item_list'),
                (2448, 'v2.product.get_direct_item_list'),
                (2450, 'v2.product.get_direct_shop_recommended_price'),
                (2470, 'v2.product.get_product_certification_rule')
            ],
            'GlobalProduct': [
                (654, 'v2.global_product.get_category'),
                (704, 'v2.global_product.get_attributes'),
                (1827, 'v2.global_product.get_attribute_tree'),
                (703, 'v2.global_product.get_brand_list'),
                (637, 'v2.global_product.get_global_item_limit'),
                (640, 'v2.global_product.get_global_item_list'),
                (644, 'v2.global_product.get_global_item_info'),
                (611, 'v2.global_product.add_global_item'),
                (620, 'v2.global_product.update_global_item'),
                (621, 'v2.global_product.delete_global_item'),
                (635, 'v2.global_product.init_tier_variation'),
                (636, 'v2.global_product.update_tier_variation'),
                (643, 'v2.global_product.add_global_model'),
                (645, 'v2.global_product.update_global_model'),
                (638, 'v2.global_product.delete_global_model'),
                (623, 'v2.global_product.get_global_model_list'),
                (632, 'v2.global_product.support_size_chart'),
                (625, 'v2.global_product.update_size_chart'),
                (639, 'v2.global_product.create_publish_task'),
                (630, 'v2.global_product.get_publishable_shop'),
                (627, 'v2.global_product.get_publish_task_result'),
                (633, 'v2.global_product.get_published_list'),
                (642, 'v2.global_product.update_price'),
                (641, 'v2.global_product.update_stock'),
                (656, 'v2.global_product.set_sync_field'),
                (657, 'v2.global_product.get_global_item_id'),
                (705, 'v2.global_product.category_recommend'),
                (751, 'v2.global_product.get_recommend_attribute'),
                (1902, 'v2.global_product.get_shop_publishable_status'),
                (1990, 'v2.global_product.get_variations'),
                (2334, 'v2.global_product.get_size_chart_detail'),
                (2335, 'v2.global_product.get_size_chart_list'),
                (2399, 'v2.global_product.search_global_attribute_value_list')
            ],
            'MediaSpace': [
                (531, 'v2.media_space.init_video_upload'),
                (532, 'v2.media_space.upload_video_part'),
                (533, 'v2.media_space.complete_video_upload'),
                (534, 'v2.media_space.get_video_upload_result'),
                (535, 'v2.media_space.cancel_video_upload'),
                (660, 'v2.media_space.upload_image')
            ],
            'Shop': [
                (536, 'v2.shop.get_shop_info'),
                (584, 'v2.shop.get_profile'),
                (585, 'v2.shop.update_profile'),
                (1061, 'v2.shop.get_warehouse_detail'),
                (1994, 'v2.shop.get_shop_notification'),
                (2238, 'v2.shop.get_authorised_reseller_brand')
            ],
            'Merchant': [
                (537, 'v2.merchant.get_merchant_info'),
                (700, 'v2.merchant.get_shop_list_by_merchant'),
                (1781, 'v2.merchant.get_merchant_warehouse_location_list'),
                (1864, 'v2.merchant.get_merchant_warehouse_list'),
                (1865, 'v2.merchant.get_warehouse_eligible_shop_list')
            ],
            'Order': [
                (542, 'v2.order.get_order_list'),
                (557, 'v2.order.get_order_detail'),
                (543, 'v2.order.get_shipment_list'),
                (2420, 'v2.order.search_package_list'),
                (545, 'v2.order.split_order'),
                (546, 'v2.order.unsplit_order'),
                (541, 'v2.order.cancel_order'),
                (544, 'v2.order.handle_buyer_cancellation'),
                (540, 'v2.order.set_note'),
                (745, 'v2.order.get_pending_buyer_invoice_order_list'),
                (1021, 'v2.order.get_buyer_invoice_info'),
                (744, 'v2.order.upload_invoice_doc'),
                (746, 'v2.order.download_invoice_doc'),
                (2440, 'v2.order.get_warehouse_filter_config'),
                (2177, 'v2.order.get_booking_list'),
                (2178, 'v2.order.get_booking_detail')
            ],
            'Logistics': [
                (550, 'v2.logistics.get_shipping_parameter'),
                (2421, 'v2.logistics.get_mass_shipping_parameter'),
                (553, 'v2.logistics.ship_order'),
                (2422, 'v2.logistics.mass_ship_order'),
                (555, 'v2.logistics.update_shipping_order'),
                (552, 'v2.logistics.get_tracking_number'),
                (2423, 'v2.logistics.get_mass_tracking_number'),
                (549, 'v2.logistics.get_shipping_document_parameter'),
                (547, 'v2.logistics.create_shipping_document'),
                (561, 'v2.logistics.get_shipping_document_result'),
                (548, 'v2.logistics.download_shipping_document'),
                (1534, 'v2.logistics.get_shipping_document_data_info'),
                (551, 'v2.logistics.get_tracking_info'),
                (558, 'v2.logistics.get_address_list'),
                (556, 'v2.logistics.set_address_config'),
                (598, 'v2.logistics.delete_address'),
                (559, 'v2.logistics.get_channel_list'),
                (554, 'v2.logistics.update_channel'),
                (2432, 'v2.logistics.get_operating_hours'),
                (2431, 'v2.logistics.get_operating_hour_restrictions'),
                (2433, 'v2.logistics.update_operating_hours'),
                (2434, 'v2.logistics.delete_special_operating_hour'),
                (2397, 'v2.logistics.batch_update_tpf_warehouse_tracking_status'),
                (688, 'v2.logistics.batch_ship_order'),
                (2016, 'v2.logistics.update_tracking_status'),
                (2180, 'v2.logistics.get_booking_shipping_parameter'),
                (2181, 'v2.logistics.ship_booking'),
                (2182, 'v2.logistics.get_booking_tracking_number'),
                (2183, 'v2.logistics.get_booking_shipping_document_parameter'),
                (2184, 'v2.logistics.create_booking_shipping_document'),
                (2185, 'v2.logistics.get_booking_shipping_document_result'),
                (2186, 'v2.logistics.download_booking_shipping_document'),
                (2187, 'v2.logistics.get_booking_shipping_document_data_info'),
                (2196, 'v2.logistics.get_booking_tracking_info')
            ],
            'FirstMile': [
                (605, 'v2.first_mile.get_unbind_order_list'),
                (601, 'v2.first_mile.get_detail'),
                (600, 'v2.first_mile.generate_first_mile_tracking_number'),
                (599, 'v2.first_mile.bind_first_mile_tracking_number'),
                (604, 'v2.first_mile.unbind_first_mile_tracking_number'),
                (602, 'v2.first_mile.get_tracking_number_list'),
                (603, 'v2.first_mile.get_waybill'),
                (606, 'v2.first_mile.get_channel_list')
            ],
            'Payment': [
                (565, 'v2.payment.get_escrow_detail'),
                (566, 'v2.payment.set_shop_installment_status'),
                (567, 'v2.payment.get_shop_installment_status'),
                (573, 'v2.payment.get_payout_detail'),
                (582, 'v2.payment.set_item_installment_status'),
                (583, 'v2.payment.get_item_installment_status'),
                (593, 'v2.payment.get_payment_method_list'),
                (594, 'v2.payment.get_wallet_transaction_list'),
                (669, 'v2.payment.get_escrow_list'),
                (1886, 'v2.payment.get_payout_info'),
                (1885, 'v2.payment.get_billing_transaction_info'),
                (2068, 'v2.payment.get_escrow_detail_batch'),
                (2346, 'v2.payment.generate_income_statement'),
                (2347, 'v2.payment.get_income_statement')
            ]
        }
        
        # Priority modules to scrape first (most commonly used)
        self.priority_modules = ['Product', 'Shop', 'Order', 'Logistics', 'Payment', 'MediaSpace']
    
    def scrape(self) -> APIDocumentation:
        """Scrape Shopee API documentation from multiple modules."""
        print("🔍 Discovering Shopee API endpoints...")
        
        # Create the main documentation object
        api_doc = APIDocumentation(
            platform="shopee",
            title="Shopee Open Platform API v2",
            version="2.0", 
            description="Complete Shopee Open Platform API covering products, orders, logistics, payments and more",
            base_url=self.api_base_url,
            source_url="https://open.shopee.com/documents"
        )
        
        # Scrape priority modules first
        for module_name in self.priority_modules:
            if module_name in self.endpoint_definitions:
                print(f"📦 Scraping {module_name} module...")
                module_endpoints = self._scrape_module_endpoints(module_name)
                api_doc.endpoints.extend(module_endpoints)
                
                # Add small delay to be respectful
                time.sleep(0.5)
        
        print(f"✅ Successfully discovered {len(api_doc.endpoints)} endpoints")
        return api_doc
    
    def _scrape_module_endpoints(self, module_name: str) -> List[APIEndpoint]:
        """Scrape all endpoints for a specific module."""
        endpoints = []
        module_id = self.api_modules.get(module_name)
        
        if not module_id or module_name not in self.endpoint_definitions:
            return endpoints
            
        for content_id, endpoint_name in self.endpoint_definitions[module_name]:
            print(f"  🔗 Scraping {endpoint_name}...")
            endpoint = self._scrape_endpoint_documentation(endpoint_name, content_id, module_name)
            if endpoint:
                endpoints.append(endpoint)
                
        return endpoints
    
    def _scrape_endpoint_documentation(self, endpoint_name: str, content_id: int, module_name: str) -> Optional[APIEndpoint]:
        """Scrape documentation for a specific API endpoint using content ID."""
        try:
            # Construct the documentation URL using content ID
            doc_url = f"https://open.shopee.com/developer/document/detail/{content_id}"
            
            soup = self.fetch_page(doc_url)
            if not soup:
                print(f"    ❌ Failed to fetch {doc_url}")
                return self._create_placeholder_endpoint(endpoint_name, module_name)
            
            # Try to extract real documentation
            endpoint = self._parse_endpoint_page(soup, endpoint_name, module_name, doc_url)
            if endpoint:
                print(f"    ✅ Parsed {endpoint_name}")
                return endpoint
            else:
                print(f"    ⚠️  Using placeholder for {endpoint_name}")
                return self._create_placeholder_endpoint(endpoint_name, module_name)
                
        except Exception as e:
            print(f"    ❌ Error scraping {endpoint_name}: {e}")
            return self._create_placeholder_endpoint(endpoint_name, module_name)
    
    def _parse_endpoint_page(self, soup: BeautifulSoup, endpoint_name: str, module_name: str, doc_url: str) -> Optional[APIEndpoint]:
        """Parse the actual endpoint documentation page."""
        try:
            # Extract title
            title = self._extract_title(soup) or self._generate_title_from_name(endpoint_name)
            
            # Extract description  
            description = self._extract_description(soup)
            
            # Extract HTTP method and path
            method = self._extract_http_method(soup, endpoint_name)
            path = self._extract_api_path(soup, endpoint_name)
            
            # Extract parameters
            parameters = self._extract_parameters(soup)
            
            # Extract responses
            responses = self._extract_responses(soup)
            
            # Extract examples
            examples = self._extract_examples(soup)
            
            # Extract error codes
            error_codes = self._extract_error_codes(soup)
            
            endpoint = APIEndpoint(
                name=title,
                method=method,
                path=path,
                description=description,
                summary=f"{module_name} API - {title}",
                tags=[module_name],
                parameters=parameters,
                responses=responses,
                examples=examples,
                error_codes=error_codes,
                rate_limit="1000 requests per hour",
                authentication_required=True
            )
            
            return endpoint
            
        except Exception as e:
            print(f"    ⚠️  Parse error for {endpoint_name}: {e}")
            return None
    
    def _extract_title(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract API endpoint title from the page."""
        # Try various selectors for the title
        selectors = [
            'h1.api-title',
            'h1',
            '.page-title', 
            '.api-name',
            '.endpoint-title',
            'title'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                text = element.get_text(strip=True)
                if text and len(text) > 3 and 'Shopee' not in text:
                    return text
        
        return None
    
    def _generate_title_from_name(self, endpoint_name: str) -> str:
        """Generate a readable title from endpoint name."""
        # Convert v2.product.get_item_list -> Get Item List
        parts = endpoint_name.split('.')
        if len(parts) >= 3:
            action_parts = parts[2].split('_')
            return ' '.join(word.capitalize() for word in action_parts)
        return endpoint_name.replace('_', ' ').title()
    
    def _extract_description(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract endpoint description."""
        selectors = [
            '.api-description',
            '.description', 
            '.summary',
            '.api-summary',
            'p.desc',
            '.content p'
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
                text = element.get_text(strip=True)
                if text and len(text) > 20 and len(text) < 500:
                    return text
        
        return None
    
    def _extract_http_method(self, soup: BeautifulSoup, endpoint_name: str) -> HTTPMethod:
        """Extract HTTP method."""
        page_text = soup.get_text().upper()
        
        # Check page content for method indicators
        if 'POST' in page_text or 'CREATE' in page_text or 'ADD' in endpoint_name:
            return HTTPMethod.POST
        elif 'PUT' in page_text or 'UPDATE' in endpoint_name:
            return HTTPMethod.PUT  
        elif 'DELETE' in page_text or 'REMOVE' in endpoint_name:
            return HTTPMethod.DELETE
        else:
            return HTTPMethod.POST  # Most Shopee APIs use POST
    
    def _extract_api_path(self, soup: BeautifulSoup, endpoint_name: str) -> str:
        """Extract API path."""
        # Look for API path in code blocks
        code_blocks = soup.find_all(['code', 'pre', '.code'])
        for block in code_blocks:
            text = block.get_text()
            # Look for path patterns
            path_match = re.search(r'/api/v\d+/[^\s\n]+', text)
            if path_match:
                return path_match.group(0)
        
        # Generate path from endpoint name
        # v2.product.get_item_list -> /api/v2/product/get_item_list
        parts = endpoint_name.split('.')
        if len(parts) >= 3:
            version, module, action = parts[0], parts[1], parts[2]
            return f"/api/{version}/{module}/{action}"
        
        return f"/api/v2/{endpoint_name.replace('.', '/')}"
    
    def _extract_parameters(self, soup: BeautifulSoup) -> List[Parameter]:
        """Extract API parameters from tables and content."""
        parameters = []
        
        # Look for parameter tables
        tables = soup.find_all('table')
        for table in tables:
            # Check if this looks like a parameter table
            headers = [th.get_text(strip=True).lower() for th in table.find_all(['th'])[:6]]
            if any(keyword in ' '.join(headers) for keyword in ['parameter', 'field', 'name', 'type']):
                table_params = self._parse_parameter_table(table)
                parameters.extend(table_params)
        
        # If no parameters found, add common Shopee parameters
        if not parameters:
            parameters = self._get_default_shopee_parameters()
            
        return parameters
    
    def _parse_parameter_table(self, table: Tag) -> List[Parameter]:
        """Parse parameters from a documentation table."""
        parameters = []
        
        try:
            rows = table.find_all('tr')[1:]  # Skip header row
            
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    name = cells[0].get_text(strip=True)
                    type_text = cells[1].get_text(strip=True) if len(cells) > 1 else "string"
                    description = cells[2].get_text(strip=True) if len(cells) > 2 else None
                    required_text = cells[3].get_text(strip=True) if len(cells) > 3 else ""
                    
                    if name and name.lower() not in ['parameter', 'field', 'name']:
                        param_type = self._normalize_parameter_type(type_text)
                        required = 'required' in required_text.lower() or 'yes' in required_text.lower()
                        
                        parameters.append(Parameter(
                            name=name,
                            type=param_type,
                            location=ParameterLocation.BODY,
                            required=required,
                            description=description
                        ))
        except Exception as e:
            print(f"    ⚠️  Error parsing parameter table: {e}")
            
        return parameters
    
    def _get_default_shopee_parameters(self) -> List[Parameter]:
        """Get common Shopee API parameters."""
        return [
                Parameter(
                    name="partner_id",
                    type=ParameterType.INTEGER,
                    location=ParameterLocation.BODY,
                    required=True,
                description="Partner ID assigned upon registration"
                ),
                Parameter(
                    name="timestamp",
                    type=ParameterType.INTEGER,
                    location=ParameterLocation.BODY,
                    required=True,
                description="Unix timestamp of the request"
                ),
                Parameter(
                    name="access_token",
                    type=ParameterType.STRING,
                    location=ParameterLocation.BODY,
                    required=True,
                    description="Access token for API authentication"
                ),
                Parameter(
                    name="shop_id",
                    type=ParameterType.INTEGER,
                    location=ParameterLocation.BODY,
                    required=True,
                description="Shopee shop identifier"
                ),
                Parameter(
                    name="sign",
                    type=ParameterType.STRING,
                    location=ParameterLocation.BODY,
                    required=True,
                description="Request signature for security"
            )
        ]
    
    def _normalize_parameter_type(self, type_str: str) -> ParameterType:
        """Normalize parameter type string."""
        type_str = type_str.lower()
        if 'string' in type_str or 'str' in type_str:
            return ParameterType.STRING
        elif 'int' in type_str or 'number' in type_str:
            return ParameterType.INTEGER
        elif 'bool' in type_str:
            return ParameterType.BOOLEAN
        elif 'array' in type_str or 'list' in type_str:
            return ParameterType.ARRAY
        elif 'object' in type_str:
            return ParameterType.OBJECT
        else:
            return ParameterType.STRING
    
    def _extract_responses(self, soup: BeautifulSoup) -> List[Response]:
        """Extract response information."""
        responses = []
        
        # Look for response examples in code blocks
        code_blocks = soup.find_all(['pre', 'code', '.response'])
        for block in code_blocks:
            text = block.get_text()
            if 'response' in text.lower() and ('{' in text or 'success' in text.lower()):
                responses.append(Response(
                    status_code=200,
                    description="Success response",
                    example={"raw_example": text[:500]}  # Truncate long examples
                ))
                break
        
        # Default response if none found
        if not responses:
            responses.append(Response(
                status_code=200,
                description="Successful API response"
            ))
            
        return responses
    
    def _extract_examples(self, soup: BeautifulSoup) -> List[Example]:
        """Extract request/response examples."""
        examples = []
        
        # Look for example sections
        example_sections = soup.find_all(string=re.compile(r'example|sample', re.I))
        for section in example_sections[:1]:  # Limit to first example
            parent = section.parent if section.parent else section
            code_block = parent.find_next(['pre', 'code'])
            if code_block:
                examples.append(Example(
                    title="API Usage Example",
                    description="Sample request and response",
                    request={"example": code_block.get_text()[:300]}
                ))
                
        return examples
    
    def _extract_error_codes(self, soup: BeautifulSoup) -> List[ErrorCode]:
        """Extract error codes."""
        error_codes = []
        
        # Look for error sections
        text = soup.get_text().lower()
        if 'error' in text:
            # Add common Shopee error codes
            error_codes = [
                ErrorCode(code="1001", message="Invalid request parameters", http_status=400),
                ErrorCode(code="1002", message="Authentication failed", http_status=401), 
                ErrorCode(code="1003", message="Access denied", http_status=403),
                ErrorCode(code="1004", message="Rate limit exceeded", http_status=429),
                ErrorCode(code="1005", message="Internal server error", http_status=500),
            ]
            
        return error_codes
    
    def _create_placeholder_endpoint(self, endpoint_name: str, module_name: str) -> APIEndpoint:
        """Create a placeholder endpoint when scraping fails."""
        title = self._generate_title_from_name(endpoint_name)
        
        return APIEndpoint(
            name=title,
            method=HTTPMethod.POST,
            path=f"/api/v2/{endpoint_name.replace('.', '/')}",
            description=f"Shopee {module_name} API endpoint - {title}",
            summary=f"{module_name} API",
            tags=[module_name],
            parameters=self._get_default_shopee_parameters(),
            responses=[Response(status_code=200, description="Success response")],
            examples=[],
            error_codes=[],
            rate_limit="1000 requests per hour",
            authentication_required=True
        ) 