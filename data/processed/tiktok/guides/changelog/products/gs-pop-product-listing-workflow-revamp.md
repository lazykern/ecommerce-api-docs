# Summary
On **August 19th, 2025**, we will be launching a revamp of the product listing API workflow for Global Selling Platform Open Plan (**GSPOP**) sellers in order to improve product listing efficiency and overall experience.
# Impact
|  |  |
| --- | --- |
| Impacted market(s) | * Platform Open Plan (POP) - All markets |
| Impacted version(s) | * 202309 (and later) |
# Changes
For a more detailed look at our API changes, please visit our [fields description](https://bytedance.sg.larkoffice.com/docx/RWcsdWydkoAL7UxSUnlloVHdgMh#share-EZ6Cd8XCmorQdcx9lE0lQnVGgbO) of the new workflow, and/or our [API documents preview](https://bytedance.sg.larkoffice.com/docx/RWcsdWydkoAL7UxSUnlloVHdgMh#share-QAFMdxjWboY6dOxbdfYlFIWpg6f).
## New APIs
The following endpoints and webhooks have been newly launched:
| Endpoint/webhook | Description |
| --- | --- |
| GET Global Listing Rules | New endpoint to query the product listing method and warehouse inventory rules for GS POP sellers. |
| POST Replicate Product | Use this new endpoint to replicate a product from one country's (e.g. US) local shop to another country's (e.g. Mexico, Indonesia, Germany) shop(s). |
| GET Global Replicated Products | Use this endpoint by passing a `product_id` to find all the replicated products related to the `product_id`. |
| Global replication status change webhook | Sends a message when the status of a product replication has changed (both replication success and failure). |
| Global listing method change webhook | When a GS POP seller upgrades the product listing mode to the new workflow, this webhook will send a message informing developers that the seller has upgraded. |
## Updated APIs
The following endpoints have been updated to support the new workflow:
| Endpoint | Changes |
| --- | --- |
| [POST Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309) | Previously, this endpoint was used exclusively for local sellers to create products. In the new workflow, GS POP sellers will also need to use this endpoint. |
| [POST Check Product Listing](https://partner.tiktokshop.com/docv2/page/check-product-listing-202309) | Previously, this endpoint was used exclusively for local sellers to validate product information. In the new workflow, GS POP sellers may also use this endpoint. |
| [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) | Added `return_draft_version=true` parameter to filter product information that is in `DRAFT` status.  <br> Added `is_replicated` to indicate whether the product was created or upgraded to the new workflow. |
| [POST Update Inventory](https://partner.tiktokshop.com/docv2/page/update-inventory-202309) | Developers will need to use this endpoint to update inventory for GS POP sellers.  |
## Deprecated APIs
With the introduction and adoption of the new workflow, most GS POP sellers will upgrade and use the new workflow to manage products. We plan to deprecate the following endpoints in the future. All deprecation plans will be announced and communicated in advance, on a per API basis.

* [GET Global Categories](https://partner.tiktokshop.com/docv2/page/get-global-categories-202309)
* [GET Global Category Rules](https://partner.tiktokshop.com/docv2/page/get-global-category-rules-202309)
* [GET Global Attributes](https://partner.tiktokshop.com/docv2/page/get-global-attributes-202309)
* [POST Create Global Product](https://partner.tiktokshop.com/docv2/page/create-global-product-202309)
* [POST Publish Global Product](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309)
* [PUT Edit Global Product](https://partner.tiktokshop.com/docv2/page/edit-global-product-202309)
* [DEL Delete Global Products](https://partner.tiktokshop.com/docv2/page/delete-global-products-202309)
* [GET Global Product](https://partner.tiktokshop.com/docv2/page/get-global-product-202309)
* [POST Search Global Products](https://partner.tiktokshop.com/docv2/page/search-global-products-202312)
* [POST Update Global Inventory](https://partner.tiktokshop.com/docv2/page/update-global-inventory-202309)

# Next steps

* Learn more about the revamped GS POP product listing workflow from our [Seller Center Academy](https://seller.tiktokglobalshop.com/university/essay?identity=1&role=1&knowledge_id=7387509823162129&from=feature_guide).
* Refer to the [new API workflow use case guide](https://bytedance.sg.larkoffice.com/docx/RWcsdWydkoAL7UxSUnlloVHdgMh) to design your app integration and seller UX.
* Test and implement the new and updated APIs with your app to help sellers using new workflow manage products