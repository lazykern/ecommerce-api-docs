## Summary
As of today, developers can start using TikTok Shop APIs to build apps for the Japan market. The APIs and workflows are generally consistent with other regions/markets, but there are a few JP-specific updates worth calling out.
**Note**: Before building order management modules, developers should familiarize themselves with our [Orders API overview](order-api-overview) and our [Fulfillment API overview](fulfillment-api-overview).
## Affected markets and versions
This change applies to the following market(s):

* Japan (JP)

This change applies to the following API version(s):

* 202309 (and later)

## API changes
### Product APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * Create Product <br> * Edit Product <br> * Partial Edit Product <br> * Check Product Listing <br> * Diagnose and Optimize Product <br> * Recommend Category | * Each product can contain up to 300 SKUs <br> * The product price range should be within [1, 500,000] JPY <br> * The characters of the product title should be within [1,255] <br> * Use GRAM as the package weight unit for product listing |
| * Publish Global Product <br> * Edit Global Product <br> * Edit Product <br> * Partial Edit Product <br> * Update Price <br> * Get Global Product | Added **mandatory** parameter `sale_price`, indicating the SKU's local selling price displayed on the product page before any discounts, inclusive of taxes. The `sale_price` parameter is only applicable to cross-border (GS-POP) sellers, and is optional in other markets. |
| * Get Categories <br> * Get Category Rules <br> * Get Attributes <br> * Update Price <br> * Search Size Chart <br> * Search Products | Added parameter values related to locale `ja-JP`, currency `JPY`, and regions `JP` have been added. |
| * Get Global Categories <br> * Get Global Category Rules <br> * Get Global Attributes | Added parameter values related to locale `ja-JP` and region `JP`. |
### Get Order Detail, Get Order List
Two response parameters have been added under `recipient_address`:

* `first_name_local_script`: first name in katakana
* `last_name_local_script`: last name in katakana

### Manage Shipments
Four response parameters have been added:

* `first_name`: first name in kanji
* `last_name`: last name in kanji
* `first_name_local_script`: first name in katakana
* `last_name_local_script`: last name in katakana

### Customer service APIs
All customer service API endpoints have been updated to support sending and receiving messages in Japanese.
### Fulfillment APIs
#### Local sellers
By default, local sellers in the Japan market should follow the seller shipping (3PL) workflow (see the [Fulfillment API overview](fulfillment-api-overview) for more details). Sellers must use the following integrated carriers for shipping:

* Yamato
* Sagawa Express
* Japan Post
* Seino Transportation
* Seino Super Express

For local sellers, the seller shipping workflow should generally follow these steps:

1. The seller ships the package and obtains the shipment tracking number from the shipping carrier.
2. Use the [Get Shipping Providers](get-shipping-providers) endpoint to retrieve the shipping service provider IDs supported by TikTok Shop.
3. Use the [Mark Package as Shipped](mark-package-as-shipped) endpoint to upload the tracking number and shipping provider ID.

#### China cross-border (GS-POP) sellers
China cross-border sellers should use the following fulfillment workflows:
| **Shipping type** | **Endpoint(s)** |
| --- | --- |
| Oversea warehouse | 1. The seller ships the package and obtains the shipment tracking number from the shipping carrier. <br> 2. Use the [Get Shipping Providers](get-shipping-providers) endpoint to retrieve the shipping service provider IDs supported by TikTok Shop. <br> 3. Use the [Mark Package as Shipped](mark-package-as-shipped) endpoint to upload the tracking number and shipping provider ID. |
| Direct shipping | 1. The seller schedules the package handover time and method with the shipping provider. <br> 2. Use the [Ship Package](ship-package) endpoint to schedule the package handover time and method. <br> 3. Use the [Get Package Shipping Document](get-package-shipping-document) endpoint to get the shipping label. |