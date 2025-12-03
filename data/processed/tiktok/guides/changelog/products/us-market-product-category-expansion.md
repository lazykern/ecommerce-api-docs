# Summary
TikTok Shop will be rolling out an increase to the levels in the category tree (3 to at-most 7) with the aim of improving product information quality. There are new API endpoints and updates to existing Product API endpoints also launching very soon. Please adopt these API endpoints to enable a successful rollout of **category expansion** and **improve catalog quality** for sellers.
# Timelines
| **Date** | **API and Seller Center readiness** | **Developer actions** |
| --- | --- | --- |
| 5/30 | API endpoints and updates are available in Development Shops | Test and integrate L7 categories with Development Shops |
| 7/30 | L7 categories pre-release rollout to invited sellers (both Seller Center and API) | Developers who have integrated before this date have a chance to participate in a pre-release rollout |
| 9/05 | L7 categories generally available to all sellers within API and Seller Center | Roll out the L7 category integration to all sellers <br> <span style="color: rgb(216, 57, 49)">Note: before 09/06, not all sellers can use L7 categories.</span> |
| 9/16 | **Hard cut-off date** for APIs to accept both L3 and L7 categories | After 9/16, requests to create and edit products with L3 will result in errors |
| 10/08 | Shops that have not upgraded to the new category levels will have their shops auto-upgraded | <span style="color: rgb(216, 57, 49)">After 10/08, developers should use L7 categories for listing and editing for all products.</span> |
# Required Actions
<span style="color: red">For detailed information on how to implement the necessary changes, please read </span>[this guide](https://partner.tiktokshop.com/docv2/page/category-expansion-l7-migration-guide)
## Listing New Products with L7 Category
When listing new products, please use **`category_version=V2`** when making calls to Product related APIs. The product creation flow remains the same. These are the APIs that will change:
| <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>API/Webhook name</strong></span> | <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>Type</strong></span> | <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>Description</strong></span> |
| --- | --- | --- |
| [GET Recommend Category](recommend-category) | RESTful API | Use this API to get a recommended category. Sellers using recommended categories will not be subject to policy violations until the end of 2024. |
| [Get Categories](get-categories) | RESTful API | Use this API to get category list |
| [Get Category Rule](get-category-rules) | RESTful API | Use this api to get the category rule - whether this category supports COD, size chart, etc. |
| [Get Attributes](get-attributes) | RESTful API | Get the specific attributes based on the category |
| [Get Brands](get-brands) | RESTful API | Get the available brands based on the category |
| [Product Audit Update Webhook](5-product-status-change) | Webhook | When product audit results get updated, this push will be triggered |
| [Create Product](create-product) <br> [Edit Product](edit-product) | RESTful API | New parameter category_version. Use category_version = v2 for L7 Category IDs, use category_version = v1 or don't use this parameter for L3 Category IDs. |
### Upgrade Existing Products to L7 Category
To upgrade existing products, we provide a shop level trigger as an "Upgrade Category" API. This API accepts a Shop Code as a trigger, and will upgrade all active products in that shop to the new categories. We will send a webhook event when categories are being upgraded that includes product ID, old leaf category ID, and new leaf category ID. The following table lists all relevant APIs:
| <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>API/Webhook name</strong></span> | <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>Type</strong></span> | <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>Description</strong></span> |
| --- | --- | --- |
| Create Category Upgrade Task | RESTful API | Upgrades active products to the L7 category. **Note**: for newly listed active products, you must wait 24 hours before upgrading the category. |
| Product category change | Webhook | Changes to category information will be triggered and notified via a webhook, which will include the product ID, L3 category ID, and L7 category ID. |
| Search Products | RESTful API | Adding parameter category_version to search for products that are under L7 category. |
### Mapping Categories between TikTok Shop and another platform
You can avoid the need for mapping by implementing our [GET Recommend Category](recommend-category) API. If you would prefer to let the seller manually map categories between TikTok Shop and another platform, you can first call our GET Categories endpoint to retrieve all the categories. Check for leaf categories, and retrieve the necessary listing schema using the GET Listing Schema endpoint.
| <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>API/Webhook name</strong></span> | <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>Type</strong></span> | <span style="background-color: rgba(245, 246, 247, 0.9)"><strong>Description</strong></span> |
| --- | --- | --- |
| [Get Categories](get-categories) | RESTful API | Use this API to get the category list in TikTok Shop |