## Summary
We're rolling out some updates to our Product, Fulfillment, and Return and Refund APIs in order to better support our Global Selling Platform Open Plan (GS POP) in the Mexico (MX) market.
## Impact
|  |  |
| --- | --- |
| Impacted market(s) | * Mexico (MX-CB) |
| Impacted version(s) | * 202309 (and later) |
## Changes
### Product APIs
#### Product listing rules
To list GS POP products for MX, call [POST Create Global Product](https://partner.tiktokshop.com/docv2/page/create-global-product-202309) first, then publish to local shops (this is the same workflow as GS POP for other markets).

Field value validation:

* Product title: `[1, 300]` characters
* Product price range (oversea local warehouse): `[1, 50000]`
* Product price range (oversea direct mail): `[1, 4560]`

| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * [GET Global Categories](https://partner.tiktokshop.com/docv2/page/get-global-categories-202309) | * Returns the category tree information for MX market <br> * Added `es-MX` as a possible value for the locale parameter |
| * [GET Global Category Rules](https://partner.tiktokshop.com/docv2/page/get-global-category-rules-202309) <br> * [GET Global Attributes](https://partner.tiktokshop.com/docv2/page/get-global-attributes-202309) | * Support using MX market category ID to retrieve category and attribute rules <br> * Added `es-MX` as a possible value for the locale parameter |
| * [POST Recommend Global Categories](https://partner.tiktokshop.com/docv2/page/recommend-global-categories-202309) | * `product_title` should be within `[1, 300]` characters |
| * [POST Create Global Product](https://partner.tiktokshop.com/docv2/page/create-global-product-202309) <br> * [PUT Edit Global Product](https://partner.tiktokshop.com/docv2/page/edit-global-product-202309) | * `product_title` should be within `[1, 300]` characters <br> * Max SKUs: 100 |
| * [POST Publish Global Product](https://partner.tiktokshop.com/docv2/page/publish-global-product-202309) | * `publish_target.region`: Added `MX` as a possible region value <br> * `skus.price.currency`: Added `MXN` as a possible currency value |
### Fulfillment APIs
#### Fulfillment workflow
For MX GS POP orders, apps need to evaluate whether the order needs to be split first.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/MX%20GS%20POP/whiteboard_exported_image%20(26).png)

1. Call [GET Order Detail](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309) or [POST Get Order List](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) to retrieve order details.
2. Call [GET Order Split Attributes](https://partner.tiktokshop.com/docv2/page/get-order-split-attributes-202309) to evaluate whether the order must be split (`must_split=true`), and obtain split rules (`must_split_reasons`) if so.
3. Call [POST Split Orders](https://partner.tiktokshop.com/docv2/page/split-orders-202309) to split the order into multiple packages. Obtain the `package_id` and `splittable_group_id` from the API response. For MX GS POP orders, you **must** split the order to meet the required conditions in a single API call.
4. Call [POST Ship Package](https://partner.tiktokshop.com/docv2/page/ship-package-202309) or [POST Batch Ship Packages](https://partner.tiktokshop.com/docv2/page/batch-ship-packages-202309) using the `package_id` from the previous step.

| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * [GET Order Split Attributes](https://partner.tiktokshop.com/docv2/page/get-order-split-attributes-202309) | Added the following new parameters: <br>  <br> * `must_split`: Indicates whether the order needs to be split <br> * `must_split_reasons`: Limitations on the maximum number of items per package and category-specific item quantity limits <br> * `must_split_reasons.type` <br> * `must_split_reasons.category_id` <br> * `must_split_reasons.max_count` |
| * [POST Split Orders](https://partner.tiktokshop.com/docv2/page/split-orders-202309) | Added error code `21003002: Split order failed due to platform limitations. Use the Get Order Split Attributes endpoint to find out the exact reason` |
| * [POST Ship Package](https://partner.tiktokshop.com/docv2/page/ship-package-202309) <br> * [POST Batch Ship Packages](https://partner.tiktokshop.com/docv2/page/batch-ship-packages-202309) | Added error code `21004024: Ship order failed due to platform limitations. Use the Split Orders endpoint to split the order before attempting to ship` |
### Return and Refund APIs
#### Cancel reasons
For order cancellations initiated by MX sellers, the available cancel reasons are different. Compared to other markets, the following options are not supported as cancel reasons for sellers in Mexico:

* Pricing error - `seller_cancel_unpaid_reason_wrong_price`
* For local shops, if the cancellation reason is already in use, it must be discontinued to avoid potential issues.

When order is in `UNPAID`, `ON_HOLD`, or `AWAITING_SHIPMENT`, supported cancel reasons are:

**UNPAID**:

* Out of stock: `seller_cancel_unpaid_reason_out_of_stock`
* Buyer did not pay on time: `seller_cancel_unpaid_reason_buyer_hasnt_paid_within_time_allowed`
* Buyer requested cancellation: `seller_cancel_unpaid_reason_buyer_requested_cancellation`

**ON_HOLD** and **AWAITING_SHIPMENT**:

* Out of stock: `seller_cancel_reason_out_of_stock`
* Unable to deliver to buyer address: `seller_cancel_paid_reason_address_not_deliver`
* Buyer requested cancellation: `seller_cancel_paid_reason_buyer_requested_cancellation`