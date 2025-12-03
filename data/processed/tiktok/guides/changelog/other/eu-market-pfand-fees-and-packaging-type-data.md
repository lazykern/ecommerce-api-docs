# Summary
A Pfand is a refundable deposit applied to certain products, typically beverage containers (e.g., bottles or cans), in countries with a deposit return system like Germany. The customer pays the deposit when purchasing the product and can reclaim it by returning the empty container to a designated return point. This system incentivizes recycling and proper disposal of packaging.

Packaging type refers to the specific kind of container material and reusability (e.g., single-use vs. multi-use) influence the deposit value and whether the packaging qualifies under the national deposit scheme.

From **October 13, 2025,** Pfand fee and packaging type fields will be available in the EU for select categories. They’ll be required only in Germany for now, but this may change in the future. 
# Impact
|  |  |
| --- | --- |
| Impacted market(s) | * Europe (EU) - Local and cross-border |
| Impacted version(s) | * 202309 (and later) |
# What's new?
The following API endpoints have been updated to support Pfand fees and packaging type data: 
| **API** | **Updates** |
| --- | --- |
| [Get Category Rules](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9?external_id=6509c0febace3e02b74594a9#%E5%9B%9E%E5%88%B0%E9%A1%B6%E9%83%A8) | New subfield `fees` to `skus` field in ++response++ body. Mandatory in DE market |
| [Create Product](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a?external_id=6502fc8da57708028b42b18a) | New subfield `fees` to `skus` field in ++request++ body. |
| [Check Product Listing](https://partner.tiktokshop.com/docv2/page/650a0ee8f1fd3102b91c6493?external_id=650a0ee8f1fd3102b91c6493) | New subfield `fees` to `skus` field in ++request++ body. |
| [Edit Product](https://partner.tiktokshop.com/docv2/page/6509da7d0fcef602bf1caddf?external_id=6509da7d0fcef602bf1caddf) | New subfield `fees` to `skus` field in ++request++ body. |
| [Partial Edit Product](https://partner.tiktokshop.com/docv2/page/650a98d74a0bb702c06c3289?external_id=650a98d74a0bb702c06c3289#%E5%9B%9E%E5%88%B0%E9%A1%B6%E9%83%A8) | New subfield `fees` to `skus` field in ++request++ body. |
| [Get Product](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda?external_id=6509d85b4a0bb702c057fdda) | New subfield `fees` to `skus` field in ++response++ body. |
| [Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | New subfield `fees` to `skus` field in ++response++ body. |
| [Publish Global Product](https://partner.tiktokshop.com/docv2/page/650a64d6defece02be678fd6?external_id=650a64d6defece02be678fd6) <br>  | New error code and error message for missing Pfand in DE. `fee` field required in the EU markets. |
| [Get Order List](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) | New subfield `pfand_fee` to `line_items` field in ++response++ body. |
| [Get Order Detail](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309) | New subfield `pfand_fee` to `line_items` field in ++response++ body. |
## [Get Category Rules](https://partner.tiktokshop.com/docv2/page/get-category-rules-202309)
New pair of `type` and`is_required` stands for `fees` if the shop is in the DE market.
| **Properties** | **Type** | **Sample** | **Properties description** |
| --- | --- | --- | --- |
| code | int |  |  |
| message | string |  |  |
| request_id | string |  |  |
| data | object |  |  |
| └ fees | []object |  | Product fees related rules. |
| └└ type | string | Pfand | The type of fee. <br> Possible values: PFAND |
| └└ is_required | bool | TRUE | A flag to indicate whether information about the fee is required. |

## Fees subfield example
| **Properties** | **Type** | **Sample** | **Properties description** |
| --- | --- | --- | --- |
| skus | []object |  |  |
| └ fees | []object |  | The fees required for this product based on TikTok Shop policies. Fees are required only for certain product categories, retrieve the requirements from the [Get Category Rules API](https://partner.tiktokshop.com/docv2/page/get-category-rules-202309). |
| └└ type | string | Pfand | The type of fee. <br> Possible values: PFAND |
| └└ amount | string | 0.00~6300.00 | The fee amount. <br> Valid range: <br> - Pfand: [0.00 - 6300.00] |
| └└ additional attribute | string | for Pfand <br> SINGLE_USE (EINWEG), <br> REUSABLE (MEHRWEG), <br> NOT_APPLICABLE | An optional attribute that provides additional context for the fee. The accepted values may vary by fee type and market. <br>  <br> Possible values for Pfand: <br> - SINGLE_USE <br> - REUSABLE <br> - NOT_APPLICABLE |
# Next steps

1. **Sync product category fields** with updated required attribute rules to avoid product creation and update errors.
2. **Pass and process** **`pfand_fee`** in your integration, ensuring safe handling of additional response fields.


*General recommendation: Product categories are updated frequently, so it's recommended to call the API in real time to ensure you are using the latest category data. Caching category data locally may result in using outdated information, leading to errors when creating products.