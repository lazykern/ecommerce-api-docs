# What is changing?
We are excited to announce the release of version 202309 (v202309) of TikTok Shop Open API.


The new version includes all functionality previously from API versions pre-Sept 2023, along with the following improvements:

* New APIs - in response to developers' and sellers' business requirement
* Standardized API specs - HTTP method, naming convention, enumerate value type, cursor-pagination
* New documentation - All APIs will include clear documentation and continuously maintained


We have released new documentation for the v202309 API:

* The [API reference](get-authorized-shops) provides complete, up-to-date details on all v202309 resources and endpoints.
* The [Developer Guide](tts-developer-guide) and [Partner Guide](about-partner-center-console) have been redesigned and revised to be more usable, comprehensive, and understandable. They cover essential API usage tutorials, integration solutions, and the app creation/publishing process
* A new [Upgrade Guide](upgrading-to-api-version-202309) which provides the necessary information to successfully upgrade your app to v202309

## New features and enhancement
### Products
| API name | Changes | Available in which markets |
| --- | --- | --- |
| [Create Product](create-product) | * New HTML tags are available in the product description: `<strong>`, `<b>`, `<em>`, `<i>`, `<br>`, `<u>` <br> * These new tags are available in product descriptions in all the versions of Create Product endpoint. | Local and cross-border sellers in all markets |
| [Partial Edit Product](partial-edit-product) | * New API endpoint for partially editing product product resources instead of requiring full product objects. | Local and cross-border sellers in all markets |
| [Get Brand](get-brands) | * New property `brand_status` adding to `brand_list` component, used to indicate whether the seller can use this brand to list products in the selected category. | Local and cross-border sellers in all markets |
| [Get Categories](get-categories), [Get Attributes](get-attributes), [Get Global Categories](get-global-categories) | * New `locale` adding to the request parameter. Product category or attribute information will be returned in the corresponding language based on the specified locale. <br>  | Local and cross-border sellers in all markets |
| [Get Product List](get-order-list) | * Request parameter `seller_skus` supports the input of multiple seller SKUs, as a filtering condition used for product search. This parameter allows you to search for all products that contain these Seller SKUs. | Local and cross-border sellers in all markets |
| [Get Product Detail](get-product) | * New property `suggestions` adding to `qc_reasons` component. When the product status is `failed`, `suggestions` property will contain the specific reason for auditing failure. | Local and cross-border sellers in all markets |
| [Product Audit Update](5-product-status-change) | * More types of messages sent from this webhook. For example, product deletion and product deactivation. <br> * The name of the webhook changing to "Product Status Update" | Local and cross-border sellers in all markets |
### Orders
| API name | Changes | Available in which markets |
| --- | --- | --- |
| [Get Order List](get-order-list) | * Properties of order detail are returned from the API. | Local and cross-border sellers in all markets |
|  | * The data of sample orders is returned from the API. New property `is_sample_order` adding to the response, indicating whether the order is an sample order. | Will be available on the following dates for different markets: <br>  <br> * Available for local and cross-border sellers in the UK market on Sept 21. <br> * Available for local sellers in the US market on Sept 27. <br> * Available for ID, PH, MY, VN, SG, TH markets on Oct 9. <br>  |
| [Get Order Detail](get-order-detail) | * The `district_info_list` property is nested in the `recipient_address` component. | Local and cross-border sellers in all markets |
|  | * The data of sample orders is returned from the API. New property `is_sample_order` adding to the response, indicating whether the order is an sample order. Sample orders can be retrieved and indicated from all versions of the Get Order Detail API. | Will be available on the following dates for different markets: <br>  <br> * Available for local and cross-border sellers in the UK market on Sept 21. <br> * Available for local sellers in the US market on Sept 27. <br> * Available for ID, PH, MY, VN, SG, TH markets on Oct 9. |
|  | * For local sellers in the US and UK markets, the `package_id` and `package_status` property will not be returned before the package is shipped | Only available for local sellers in the US market |
### Fulfillment
| API name | Changes | Available in which markets |
| --- | --- | --- |
| [Mark Package as Shipped](mark-package-as-shipped) | * A new endpoint for sellers who fulfill orders through their own selected/preferred logistics carrier. This API allows sellers to upload valid package information, orders/order line items, to TikTok Shop. <br> * This new endpoint supports item level split shipping | As of now, the API endpoint is only available for local sellers in the US market <br>  <br> Will be available for local sellers in the UK market before October 30, 2023 |
| [Get Eligible Shipping Service](get-eligible-shipping-service) | * For the "shipped via platform" shipping option, use `order_id` and `order_line_item_id`to query the list of available shipping services. <br>  | Only available for local sellers in the US market |
| [Create Packages](create-packages) | * For the "shipped via platform" shipping option, use `order_id` and `order_line_item_id`to purchase labels and ship orders. <br> * Newly supports item level split shipping with this endpoint. | Only available for local sellers in the US market |
### Return, refund, cancellation
Since after-sale solutions and policies around returns, refunds, and cancellations differ across markets, the availability of certain API features also varies by market. Developers should understand the specific solutions and policies in their target market before using the corresponding APIs.


Learn more about how to use the above APIs from Cancel/Return/Refund API Overview
| API name | Changes | Available in which markets |
| --- | --- | --- |
| [Search Cancellation](search-cancellations) | New API endpoint to retrieve one or more order cancellations. | Local and cross-border sellers in all markets |
| [Cancel Order](cancel-order) | New API endpoint to cancel an order on behalf of a seller. <br> Currently, this new endpoint supports item level cancellation for local and cross-border sellers in the US market. | The API endpoint is available for local and cross-border sellers in all markets <br>  <br> As of now, item level cancellation is only available for local and cross-border sellers in the US market. |
| [Approve Cancellation](approve-cancellation) | New API endpoint to approve a buyer's order cancellation request. | Local and cross-border sellers in all markets |
| [Reject Cancellation](reject-cancellation) | New API endpoint to reject a buyer's order cancellation request. | Local and cross-border sellers in all markets |
| [Search Returns](search-returns) | New API endpoint to retrieve one or more returns. | Local and cross-border sellers in all markets |
| [Create Return](create-return) | New API endpoint to initiate a return request on behalf of the buyer. | Local sellers in the US and UK markets |
| [Approve Return](approve-return) | New API endpoint to approve a buyer's return request. | Local and cross-border sellers in all markets |
| [Reject Return](reject-return) | New API endpoint to reject a buyer's return or refund request. | Local and cross-border sellers in all markets |
| [Get Return Records](get-return-records) | New API endpoint to query a list of processing steps of order return or cancellation records. | Local and cross-border sellers in all markets |
| [Calculate Refund](calculate-refund) | New API endpoint to check order refundable amounts. | Local and cross-border sellers in all markets |
| [Get Aftersale Eligibility](get-aftersale-eligibility) | New API endpoint to check the eligible after-sales solution for an order. Such as whether the seller can initiate refund, return or cancel a specific order. | Local and cross-border sellers in all markets |
| [Get Reject Reasons](get-reject-reasons) | New API endpoint to get eligible cancel or return order reject reason. The seller is required to give reason, when the seller rejects the cancel, refund and return request. | Local and cross-border sellers in all markets |
| [Cancellation Status Change Webhook](11-cancellation-status-change) | New webhook type to obtain the order cancellation status. | Local and cross-border sellers in all markets |
| [Return Status Change Webhook](12-return-status-change) | New webhook type to obtain the order return/refund status. | Local and cross-border sellers in all markets |
### Finance
| API name | Changes | Available in which markets |
| --- | --- | --- |
| [Get Order Statement Transactions](get-transactions-by-order) | New API endpoint to retrieve a list of transactions associated with an order specified by the order ID. It also returns the SKU level transaction details. | Local sellers in the US and UK markets |
| [Get Statements](get-statements) | New API endpoint to get the list of statements records of the specified date range, which is settled on a daily basis. You can filter the statements based on payment status. | Local sellers in the US and UK markets |
| [Get Statement Transactions](get-transactions-by-statement) | New API endpoint to get a list of transactions based on statement_id. We will return a list of orders. If you require the SKU level transaction details, pass in the order_id to Get Order Statement Transactions. | Local sellers in the US and UK markets |
| [Get Payments](get-payments) | New API endpoint to get the list of payments based on date range, including the current payment status. Use this list to reconcile payments with the Seller's bank account. | Local sellers in the US and UK markets |
| [Get Withdrawals](get-statements) | New API endpoint to get the list of the withdrawal records (when Seller's withdraw money from TikTokShop) based on the specified date range. | Local and cross-border sellers in the SG, PH, MY, TH, VN markets. <br> Local sellers in the ID markets |
## Technical specification updates
### Making requests
To make requests to the 202309 API endpoints, use URIs with the new structure. Specify the version name (e.g. 202309) in the path instead of as a query parameter. The new version also introduces the resource identifier as a path parameter.


For example, https://open-api.tiktokglobalshop.com/fulfillment/202309/orders/576619223164029995/packages


The URI for each version 202309 endpoint is specified in the [API reference](get-authorized-shops). Check the API reference for the exact endpoint URIs.
### Enumerate data types
We've improved the general concept of statuses to be more descriptive. Previously, order statuses were mapped to codes, which required developer interpretation. We have removed these `int` based codes, and developed `string` based ENUM statuses, such as "UNPAID" and "AWAITING_SHIPMENT" to simplify the development process.


For example:

* v202305 of Get Order Detail API, `order_status` property values are in the `int` type: `100` mean `UNPAID`, `111` means `AWAITING_SHIPMENT`
* v202309 of Get Order Detail API, `order_status` property values are in the `string` type. `UNPAID` and `AWAITING_SHIPMENT` are returned from API.

### Pagination
For standardized expression and performance assurance, we have introduced token-based pagination into our API design. The v202309 API only supports pagination using the `page_size` and `page_token` parameters. The `offset` parameter is no longer supported.
### Authorization
We have deprecated `access_token` usage in the query and now require it to be passed in the HTTP header `x-tts-access-token` for security improvement.
### Signature
The v202309 of the API expands signature protection beyond just path and query parameters. Signatures will now also cover request bodies for POST APIs. To generate the signature for the v202309 APIs, developers need to use the new method.
### Content type
The v202309 APIs now only support `application/json` for non-binary requests. Binary requests should use `multipart/form-data` to ensure efficiency and standards compliance.
### Improved documentation
The API reference pages now include fully populated Errorcode sections at the bottom with the latest error codes and corresponding error description for each endpoint.
# Which markets are affected?
Some new features and enhancement are only available for certain markets or seller types. Refer to "Available in which markets" column in the table above for availability details.


The technical specification updates apply to local and cross-border sellers in all markets.
# Who is affected?
New apps should only use the new v202309 of all API endpoints.


All existing developers are not immediately affected. All legacy APIs will continue functioning. Existing developers are encouraged to upgrade as soon as possible. New APIs in v202309 offer additional capabilities and enhancements.
# What action is required?
Legacy API versions (pre-Sept 2023) will no longer be supported or maintained from **June 30, 2024** and will be retired on **December 31, 2024**. Existing apps can continue using legacy versions until then, but should upgrade to v202309 as soon as possible.


The following is a list of resources with which developers can learn and upgrade apps with v202309 APIs:

* [API Reference](get-authorized-shops)
* [Developer Guide](tts-developer-guide)
* [Upgrade Guide](upgrading-to-api-version-202309)
* Use [Mapping APIs from legacy to v202309](upgrading-to-api-version-202309#Mapping%20APIs%20from%20legacy%20to%20v202309) to find out what new endpoints to replace with the current legacy API endpoints you are using


After **December 31, 2024** all requests to legacy API versions will fail. Developers should upgrade apps to using v202309 and make sure all requests are on v202309.