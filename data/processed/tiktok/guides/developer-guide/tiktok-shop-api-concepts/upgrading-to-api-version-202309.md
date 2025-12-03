This guide is used for existing developers to learn about changes in and upgrade to version 202309 (v202309). Before reading the guide, we assume you have learned and developed apps with TikTok Shop Open APIs.
# Benefits of v202309
TikTok Shop Open API 202309 release (v202309) includes all functionality previously from API versions pre-Sept 2023, along with the following improvements:

* New APIs - in response to developers' and sellers' business requirement
* Technical specifications have been updated to more closely adhere to RESTful design principles
* New documentation - All APIs will include clear documentation and continuously maintained

# New documentation
We have released new documentation for the v202309 API:

* The [API reference](get-authorized-shops) provides complete, up-to-date details on all v202309 resources and endpoints.
* The [Developer Guide](tts-developer-guide) and [Partner Guide](about-partner-center-console) have been redesigned and revised to be more usable, comprehensive, and understandable. They cover essential API usage tutorials, integration solutions, and the app creation/publishing process.

# Retiring the legacy API versions
Legacy API versions (pre-Sept 2023) will no longer be supported or maintained from **June 30, 2024** and will be retired on **December 31, 2024**.


New apps should use v202309 exclusively and not legacy versions.


After **December 31, 2024**, all requests to legacy API versions will fail.
# Summary of changes
## New features and enhancement
### Products
| API name | Changes |
| --- | --- |
| [Create Product](create-product) | * New HTML tags are available in the product description: `<strong>`, `<b>`, `<em>`, `<i>`, `<br>`, `<u>` <br> * These new tags are available in product descriptions in all the versions of Create Product endpoint. |
| [Partial Edit Product](partial-edit-product) | * New API endpoint for partially editing product product resources instead of requiring full product objects. |
| [Get Brand](get-brands) | * New property `brand_status` adding to `brand_list` component, used to indicate whether the seller can use this brand to list products in the selected category. |
| [Get Categories](get-categories), [Get Attributes](get-attributes), [Get Global Categories](get-global-categories) | * New `locale` adding to the request parameter. Product category or attribute information will be returned in the corresponding language based on the specified locale. |
| [Get Product List](search-products) | * Request parameter `seller_skus` supports the input of multiple seller SKUs, as a filtering condition used for product search. This parameter allows you to search for all products that contain these Seller SKUs. |
| [Get Product Detail](get-product) | * New property `suggestions` adding to `qc_reasons` component. When the product status is `failed`, `suggestions` property will contain the specific reason for auditing failure. |
| [Product Audit Update](5-product-status-change) | * More types of messages sent from this webhook. For example, product deletion and product deactivation. <br> * The name of the webhook changing to "Product Status Update" |
### Orders
| API name | Changes |
| --- | --- |
| [Get Order List](get-order-list) | * Properties of order detail are returned from the API. |
|  | * The data of sample orders is returned from the API. New property `is_sample_order` adding to the response, indicating whether the order is an sample order. |
| [Get Order Detail](get-order-detail) | * The `district_info_list` property is nested in the `recipient_address` component. |
|  | * The data of sample orders is returned from the API. New property `is_sample_order` adding to the response, indicating whether the order is an sample order. Sample orders can be retrieved and indicated from all versions of the Get Order Detail API. |
|  | * For local sellers in the US and UK markets, the `package_id` and `package_status` property will not be returned before the package is shipped |
### Fulfillment
| API name | Changes |
| --- | --- |
| [Mark Package as Shipped](mark-package-as-shipped) | * A new endpoint for sellers who fulfill orders through their own selected/preferred logistics carrier. This API allows sellers to upload valid package information, orders/order line items, to TikTok Shop. <br> * This new endpoint supports item level split shipping |
| [Get Eligible Shipping Service](get-eligible-shipping-service) | * For the "shipped via platform" shipping option, use `order_id` and `order_line_item_id`to query the list of available shipping services. <br>  |
| [Create Packages](create-packages) | * For the "shipped via platform" shipping option, use `order_id` and `order_line_item_id`to purchase labels and ship orders. <br> * Newly supports item level split shipping with this endpoint. |
### Return, refund, cancellation
Since after-sale solutions and policies around returns, refunds, and cancellations differ across markets, the availability of certain API features also varies by market. Developers should understand the specific solutions and policies in their target market before using the corresponding APIs.


Learn more about how to use the above APIs from [Cancel/Return/Refund API Overview](return-refund-and-cancel-api-overview)
| API name | Changes |
| --- | --- |
| [Search Cancellation](search-cancellations) | New API endpoint to retrieve one or more order cancellations. |
| [Cancel Order](cancel-order) | New API endpoint to cancel an order on behalf of a seller. <br> Currently, this new endpoint supports item level cancellation for local and cross-border sellers in the US market. |
| [Approve Cancellation](approve-cancellation) | New API endpoint to approve a buyer's order cancellation request. |
| [Reject Cancellation](reject-cancellation) | New API endpoint to reject a buyer's order cancellation request. |
| [Search Returns](search-returns) | New API endpoint to retrieve one or more returns. |
| [Create Return](create-return) | New API endpoint to initiate a return request on behalf of the buyer. |
| [Approve Return](approve-return) | New API endpoint to approve a buyer's return request. |
| [Reject Return](reject-return) | New API endpoint to reject a buyer's return or refund request. |
| [Get Return Records](get-return-records) | New API endpoint to query a list of processing steps of order return or cancellation records. |
| [Calculate Refund](calculate-refund) | New API endpoint to check order refundable amounts. |
| [Get Aftersale Eligibility](get-aftersale-eligibility) | New API endpoint to check the eligible after-sales solution for an order. Such as whether the seller can initiate refund, return or cancel a specific order. |
| [Get Reject Reasons](get-reject-reasons) | New API endpoint to get eligible cancel or return order reject reason. The seller is required to give reason, when the seller rejects the cancel, refund and return request. |
| [Cancellation Status Change Webhook](11-cancellation-status-change) | New webhook type to obtain the order cancellation status. |
| [Return Status Change Webhook](12-return-status-change) | New webhook type to obtain the order return/refund status. |
### Finance
| API name | Changes |
| --- | --- |
| [Get Order Statement Transactions](get-transactions-by-order) | New API endpoint to retrieve a list of transactions associated with an order specified by the order ID. It also returns the SKU level transaction details. |
| [Get Statements](get-statements) | New API endpoint to get the list of statements records of the specified date range, which is settled on a daily basis. You can filter the statements based on payment status. |
| [Get Statement Transactions](get-transactions-by-statement) | New API endpoint to get a list of transactions based on statement_id. We will return a list of orders. If you require the SKU level transaction details, pass in the order_id to Get Order Statement Transactions. |
| [Get Payments](get-payments) | New API endpoint to get the list of payments based on date range, including the current payment status. Use this list to reconcile payments with the Seller's bank account. |
| [Get Withdrawals](get-withdrawals) | New API endpoint to get the list of the withdrawal records (when Seller's withdraw money from TikTokShop) based on the specified date range. |
## Making requests
To make requests to the 202309 API endpoints, use URIs with the new structure. Specify the version name (e.g. 202309) in the path instead of as a query parameter. The new version also introduces the resource identifier as a path parameter.


For example, https://open-api.tiktokglobalshop.com/fulfillment/202309/orders/576619223164029995/packages


The URI for each version 202309 endpoint is specified in the [API reference](get-authorized-shops). Check the API reference for the exact endpoint URIs.
## Enumerate data types
We've improved the general concept of statuses to be more descriptive. Previously, order statuses were mapped to codes, which required developer interpretation. We have removed these `int` based codes, and developed `string` based ENUM statuses, such as "UNPAID" and "AWAITING_SHIPMENT" to simplify the development process.
For example:

* v202305 of Get Order Detail API, `order_status` property values are in the `int` type: `100` mean `UNPAID`, `111` means `AWAITING_SHIPMENT`
* v202309 of Get Order Detail API, `order_status` property values are in the `string` type. `UNPAID` and `AWAITING_SHIPMENT` are returned from API.

## Pagination
For standardized expression and performance assurance, we have introduced token-based pagination into our API design. The v202309 API only supports pagination using the `page_size` and `page_token` parameters. The `offset` parameter is no longer supported.
## Authorization
We have deprecated `access_token` usage in the query and now require it to be passed in the HTTP header `x-tts-access-token` for security improvement.
## Signature
The v202309 of the API expands signature protection beyond just path and query parameters. Signatures will now also cover request bodies for POST APIs. To generate the signature for the v202309 APIs, developers need to use the new method.
## Content type
The v202309 APIs now only support `application/json` for non-binary requests. Binary requests should use `multipart/form-data` to ensure efficiency and standards compliance.
## Improved documentation
The API reference pages now include fully populated Errorcode sections at the bottom with the latest error codes and corresponding error description for each endpoint.
# Mapping APIs from legacy to v202309
With the new request URI structure and API naming changes in v202309, many legacy API endpoints have been replaced or retired in v202309.


Use the tables below to understand how legacy APIs map to the new v202309 endpoints:
## Seller (Legacy API known as Seller or Shop)
| Legacy APIs | API v202309 |
| --- | --- |
| `Get Authorized Shop` | [Get Authorized Shops](get-authorized-shops) |
| `Get Active Shop List` | [Get Active Shops](get-active-shops) |
| `Check Global Product Mode` | [Get Seller Permissions](get-seller-permissions) |
## Event (Legacy API known as Shop)
| Legacy APIs | API v202309 |
| --- | --- |
| `Create Webhook` | [Update Shop Webhook](update-shop-webhook) |
| `Get Webhooks` | [Get Shop Webhooks](get-shop-webhooks) |
| `Cancel Webhook` | [Delete Shop Webhook](delete-shop-webhook) |
## Product
| Legacy APIs | API v202309 |
| --- | --- |
| `Get Brands` | [Get Brands](get-brands) |
| `Create Brand` | [Create Custom](create-custom-brands)[Brands](create-custom-brands) |
| `Get Attributes` | [Get Attributes](get-attributes) |
| `Get Category Rule` | [Get Category Rules](get-category-rules) |
| `Get Categories` | [Get Categories](get-categories) |
| `Upload File` | [Upload Product File](upload-product-file) |
| `Category Recommended` | [Recommend Category](recommend-category) |
| `Upload Image` | [Upload Product Image](upload-product-file) |
| `Create Product` | [Create Product](create-product) |
| `Edit Product` | [Edit Product](edit-product) |
| `Update Price` | [Update Price](update-price) |
| `Update Stock` | [Update Inventory](update-inventory) |
| `Deactivate Product` | [Deactivate Products](deactivate-products) |
| `Activate Product` | [Activate Product](activate-product) |
| `Delete Product` | [Delete Products](delete-products) |
| `Recover Deleted Product` | [Recover Products](recover-products) |
| `Get Product List` | [Search Products](search-products) |
| `Create Draft Product` | No upgrade in this version. Can continue utilizing legacy version. If there are updates, they will be provided in future version. |
| `Get Product Stock` | [Inventory Search](inventory-search) |
| `Pre-check for Operating Product` | [Check Listing Prerequisites](check-listing-prerequisites) |
| `Get Product Detail` | [Get Product](get-product) |
| `Get Global Product Detail` | [Get Global Product](get-global-product) |
| Did not exist previously | [Partial Edit Product](partial-edit-product) |
## Order
| Legacy APIs | API v202309 |
| --- | --- |
| `Get Order List` | [Get Order List](get-order-list) |
| `Get Order Detail` | [Get Order Detail](get-order-detail) |
## Fulfillment
| Legacy APIs | API v202309 |
| --- | --- |
| `Search Package` | [Search Package](search-package) |
| `Get Package Detail` | [Get Package Detail](get-package-detail) |
| `Get Package Shipping Document` | [Get Package Shipping Document](get-package-shipping-document) |
| `Get Package Pickup Config` | [Get Package Handover Time Slots](get-package-handover-time-slots) |
| `Get Package Shipping Info` | [Get Tracking](get-tracking) |
| `Update Package Shipping Info` | [Update Package Shipping Info](update-package-shipping-info) |
| `Update Package Delivery Status` | [Update Package Delivery Status](update-package-delivery-status) |
| `Verify Order Split` | [Get Order Split Attributes](get-order-split-attributes) |
| `Confirm Order Split` | [Split Orders](split-orders) |
| `Search Pre Combine Pkg` | [Search Combinable Packages](search-combinable-packages) |
| `Confirm Precombine Package` | [Combine Package](combine-package) |
| `Remove Package Order` | [Uncombine Packages](uncombine-packages) |
| `Ship Package` | Use [Mark Package As Shipped](mark-package-as-shipped) or [Ship Package](ship-package) depending on your shop location |
| `Batch Ship Packages` | [Batch Ship Packages](batch-ship-packages) |
| `Fulfillment Upload Image` | [Fulfillment Upload Delivery Image](fulfillment-upload-delivery-image) |
| `Fulfillment Upload File` | [Fulfillment Upload Delivery File](fulfillment-upload-delivery-file) |
| `Get Shipping Service` | [Get Eligible Shipping Service](get-eligible-shipping-service) |
| `Create Label` | [Create Packages](create-packages) |
## Logistics
| Legacy APIs | API v202309 |
| --- | --- |
| `Get Subscribed Delivery Options` | [Get Warehouse Delivery Options](get-warehouse-delivery-options) |
| `Get Warehouse List` | [Get Warehouse List](get-warehouse-list) |
| `Get Shipping Provider` | [Get Shipping Providers](get-shipping-providers) |
| `Get Shipping Document` | No upgrade in this version. <br> Recommend using [Get Package Shipping Document](get-package-shipping-document) |
| `Get Shipping Info` | [Get Tracking](get-tracking) |
| `Update Shipping Info` | [Update Shipping Info](update-shipping-info) |
## Returns, Refunds, Cancellations (Legacy API known as Reverse)
| Legacy APIs (Reverse) | Returns, Refunds, and Cancellations API v202309 |
| --- | --- |
| `Cancel Order` | [Cancel Order](cancel-order) |
| `Get Reverse Order List` | [Search Cancellation](search-cancellations) <br> [Search Returns](search-returns) |
| `Confirm Reverse Request` | [Approve Return](approve-return) <br> [Approve Cancellation](approve-cancellation) |
| `Reject Reverse Request` | [Reject Return](reject-return) <br> [Reject Cancellation](reject-cancellation) |
| `Get Reject Reason List` | [Get Reject Reasons](get-reject-reasons) |
| Did not exist previously | [Get Aftersale Eligibility](get-aftersale-eligibility) |
| Did not exist previously | [Create Return](create-return) |
| Did not exist previously | [Get Return Records](get-return-records) |
| Did not exist previously | [Calculate Refund](calculate-refund) |
## Finance
| Legacy APIs | API v202309 |
| --- | --- |
| `Get Settlements` | [Get Statements](get-statements) <br> [Get Statement Transactions](get-transactions-by-statement) |
| `Get Transactions` | [Get Withdrawals](get-withdrawals) |
| `Get Order Settlements` | [Get Order Statement Transactions](get-transactions-by-order) |
| Did not exist previously | [Get Payments](get-payments) |
## Global Product
| Legacy APIs | API v202309 |
| --- | --- |
| `Get Global Categories` | [Get Global Categories](get-global-categories) |
| `Get Global Category Rule` | [Get Global Category Rules](get-global-category-rules) |
| `Get Global Attributes` | [Get Global Attributes](get-global-attributes) |
| `Edit Global Product` | [Edit Global Product](edit-global-product) |
| `Create Global Product` | [Create Global Product](create-global-product) |
| `Publish Global Product` | [Publish Global Product](publish-global-product) |
| `Delete Global Product` | [Delete Global Products](delete-global-products) |
| `Update Global Product Price` | No upgrade in this version. <br> Recommend using [Update Price](update-price) to edit the product price published in local shops, and using [Edit Product](edit-product) to edit the Global product price. |
| `Get Global Product List` | [Search Global Products](search-global-products) |
## Promotion
| Legacy APIs | API v202309 |
| --- | --- |
| `Add Promotion` | [Create Activity](create-activity) |
| `Update Basic Information` | [Update Activity](update-activity) |
| `Add/Update Discount Item` | [Update Activity Product](update-activity-product) |
| `Remove Promotion Item` | [Remove Activity Product](remove-activity-product) |
| `Deactivate Promotion` | [Deactivate Activity](deactivate-activity) |
| `Get Promotion List` | [Search Activities](search-activities) |
| `Get Promotion Details` | [Get Activity Detail](get-activity) |
## Supply chain
| Legacy APIs | API v202309 |
| --- | --- |
| `Package fulfillment data sync` | [Confirm Package Shipment](confirm-package-shipment) |
## Webhook
| Legacy APIs | API v202309 |
| --- | --- |
| `Type 1: Order Status Update` | [Order Status Update](1-order-status-change) |
| `Type 2: Reverse Status Update` | [Cancellation Status Change](11-cancellation-status-change) and [Return Status Change](12-return-status-change) |
| `Type 3: Recipient Address Update` | [Recipient Address Update](3-recipient-address-update) |
| `Type 4: Package Update` | [Package Update](4-package-update) |
| `Type 5: Product Audit Update` | [Product Status Update](5-product-status-change) |
| `Type 6: Seller Deauthorization` | [Seller Deauthorization](6-seller-deauthorization) |
| `Type 7: Auth Expire` | [Upcoming Authorization Expiration](7-upcoming-authorization-expiration) |