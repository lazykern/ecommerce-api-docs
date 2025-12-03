## Summary
We're introducing a couple of new `pre_sale` product types to better support TikTok Shop seller needs. There are a couple key business logic distinctions based on the market, as follows:

For the **US** market, this includes pre-order and made-to-order products:

* **Pre-order**: The buyer can place an order for a product before a **fixed** release date set by the seller.
* **Made-to-order**: The buyer can place an order for a customized product that is made-to-order. The shipping lead time depends on the order placement date/time, as well as the production time required for each individual order, rather than a fixed release date.
* **Custom**: The seller can select a specific SKU and set a handling time that's longer than the platform policy of 3 business days. The estimated delivery time and late dispatch evaluation will be based on the handling time set.

For the **UK** and **SEA** markets, this is currently limited to pre-order products only:

* **Pre-order**: The buyer can place an order for a product before release, but the shipping lead time depends on the order placement date/time and the production time required for each individual order, rather than a fixed release date.

## Affected markets and versions
This change applies to the following market(s):

* United States (US)
* United Kingdom (UK)
* Southeast Asia (SEA)

This change applies to the following API version(s):

* 202309 (and later)

## What's changing?
### Product APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * [Get Category Rules](get-category-rules) | New response parameter, `allowed_special_product_types`: The list of special product types that are allowed for your shop in this category. If no special types are allowed, this parameter is omitted. |
| * [Create Product](create-product#Back%20To%20Top) <br> * [Edit Product](edit-product) <br> * [Partial Edit Product](partial-edit-product) | New request body parameter, `pre_sale`: SKU pre-sale information, used to tag a product as a pre-sale product based on its pre-sale type. Applicable only if `allowed_special_product_types` from Get Category Rules is not empty. |
| * [Check Product Listing](check-product-listing#Back%20To%20Top) <br> * [Search Products](search-products) <br> * [Get Product](get-product) | New response parameter, `pre_sale`: SKU pre-sale information, used to tag a product as a pre-sale product based on its pre-sale type. If this is not returned, it indicates that the product is a regular (not pre-sale) item. |
## Related changes

* [US market: Pre-order, made-to-order, back-order functionality; delivery SLA](us-market-pre-order-made-to-order-back-order-functionality-delivery-sla)