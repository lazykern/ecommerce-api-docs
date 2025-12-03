# Summary
Recently in the SEA market, following last year's rollout in the US market, TikTok Shop introduced an increase to the levels in the category tree, from **three** to at-most **seven**, with the aim of improving product information quality. 

Beginning this week, we will be introducing this product category expansion in the **UK**, **EU**, and **JP** markets. This changelog will provide a quick overview of API changes you may need to implement.

**For a more detailed walkthrough on how to implement the necessary changes, please read** [our L7 category expansion migration guide](https://partner.tiktokshop.com/docv2/page/category-expansion-l7-migration-guide)**.**
# Impact
|  |  |
| --- | --- |
| Impacted market(s) | * United Kingdom (UK) - Local and cross-border <br> * Europe (EU) - Local and cross-border <br> * Japan (JP) - Local and cross-border |
| Impacted version(s) | * 202309 (and later) |
# Listing new L7 products
When listing new products:
– Use **`category_version=V1`** for **L3** category tree
– Use **`category_version=V2`** for **L7** category tree

This applies to the following Product APIs:
– [GET Categories](https://partner.tiktokshop.com/docv2/page/get-categories-202309)
– [POST Recommend Category](https://partner.tiktokshop.com/docv2/page/recommend-category-202309)
– [GET Category Rules](https://partner.tiktokshop.com/docv2/page/get-category-rules-202309)
– [GET Attributes](https://partner.tiktokshop.com/docv2/page/get-attributes-202309)
– [GET Brands](https://partner.tiktokshop.com/docv2/page/get-attributes-202309)
– [POST Create Product](https://partner.tiktokshop.com/docv2/page/create-product-202309)
– [PUT Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202309)
– [POST Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502)

**Note:** Since the global product publishing (GS POP) workflow is also undergoing changes, developers are advised to directly upgrade to the new GS POP workflow instead of adapting the L7 category using the original Global Product APIs. Please refer to our [official changelog](https://partner.tiktokshop.com/docv2/page/a5crrkzs) for more details.
# Upgrade existing products to L7
To upgrade existing products, please use our category upgrade API. This endpoint accepts a Shop Code as a trigger, and will upgrade all active products in that shop to the new categories. We will send a webhook event when categories are being upgraded that includes product ID, old leaf category ID, and new leaf category ID. The following table lists all relevant APIs:
| **API/webhook name** | **Type** | **Description** |
| --- | --- | --- |
| * [POST Create Category Upgrade Task](https://partner.tiktokshop.com/docv2/page/create-category-upgrade-task-202407) | RESTful API | * Upgrades active products to the L7 category.  <br> * **Note**: For newly listed active products, you must wait 24 hours before upgrading the category. |
| * [Product category change](https://partner.tiktokshop.com/docv2/page/18-product-category-change) | Webhook | * Used for monitoring product category changes. <br> * After the upgrade task is created, developers need to receive webhooks to confirm the result of the category upgrade. |
| * [POST Search Products](https://partner.tiktokshop.com/docv2/page/search-products-202502) | RESTful API | * After receiving the webhook, developers should query the product information for secondary confirmation to verify whether the L7 category has been successfully updated. |
# Related changes
| **Changelog** | **Description** |
| --- | --- |
| * [US market: Product category expansion](https://partner.tiktokshop.com/docv2/page/us-market-product-category-expansion) | * Original changelog for US market rollout of L7 product category expansion. |
| * [SEA market: Product category expansion](https://partner.tiktokshop.com/docv2/page/npb6fvbh) | * Changelog for SEA market rollout of L7 product category expansion. |
| * [GS POP product listing workflow revamp](https://partner.tiktokshop.com/docv2/page/a5crrkzs) | * New changelog for the Global Product API workflow revamp. |