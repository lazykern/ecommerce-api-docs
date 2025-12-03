## Summary
It is important for sellers to be able to match their TikTok Shop products with external e-commerce platforms that act as a "source of truth" as they can be used in various business operations such as product reviews syndication, ads attribution, etc. Please provide an external identifier as a value for the `external_product_id` field so that TikTok Shop can tie attribution for these business operations.
## Required Actions
As Connector App managing products for sellers, we need your support in syncing sellers' external product IDs to TikTok Shop products.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/teh7svth/19133a66-485c-4a51-9625-1ab8e9416aa6.png)
| Ext Platform Field | Ext. Platform Field Description | TikTok Shop Field | Relevant API |
| --- | --- | --- | --- |
| product.id | Represents a product | external_product_id | Create API, Partial Edit Product API |
| variants.id | Represents a SKU | external_sku_id | Create API, Partial Edit Product API |
| variants.barcode | Represents an identifier code | identifier_code.code | Create API, Partial Edit Product API |
**NOTE**:

* When passing the Shopify barcode values to TikTok Shop, using `identifier_code.type` = `GTIN`
* The value format should be 8, 12, 13, 14 digits, or exactly 9 digits followed by an uppercase `X`

Please ensure all TikTok Shop products created by your App are populated with external_product_id and external_sku_id. The ideal result of the above actions should be: all TikTok products synced or managed by your Apps are populated with external product IDs.