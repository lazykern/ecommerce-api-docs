## Summary
Previously, the TikTok Shop Seller Center only allowed draft editing prior to publishing a listing. We've recently expanded this feature to additionally enable sellers to edit and save drafts for products that have already been listed, and are now ensuring it is reflected in our APIs.

## Impact
|  |  |
| --- | --- |
| Impacted market(s) | * United States (US) - Local <br> * United Kingdom (UK) - Local <br> * Europe (EU) - Local <br> * Southeast Asia (SEA) - Local <br> * Japan (JP) - Local <br> * Platform Open Plan (POP) - US, UK, EU, SEA |
| Impacted version(s) | 202309 (and later) |
## Changes
### Product APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * [PUT Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202309) <br> * [POST Partial Edit Product](https://partner.tiktokshop.com/docv2/page/partial-edit-product-202309) | New request parameter: `save_mode` <br> Possible values: <br>  <br> * `AS_DRAFT`: Save the product as a draft for future editing. <br> * `LISTING`: Immediately list the product in the shop. |
| * [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) <br> * [POST Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | New request parameter: `return_draft_version` <br> Filter products to show only those that have a draft. <br>  <br> * `true`: Returns products in their draft version only. Excludes those without a draft. <br> * `false`: Returns all products regardless of whether they have a draft. |
| * [POST Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | New response parameter: `has_draft` <br> Indicates whether the product has a draft. <br>  <br> * `true`: It has a draft. <br> * `false`: It does not have a draft. |
## Next steps
For more details on the new parameters, please visit our individual API documentation for each endpoint, as linked above.