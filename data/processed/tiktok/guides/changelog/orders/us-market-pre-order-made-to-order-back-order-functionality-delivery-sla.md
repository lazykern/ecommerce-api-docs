## Summary
In the US market, we're adding the capability to specify new order types in our Order APIs, namely pre-order, made-to-order, and back-order.

Compared to normal orders, these orders will sit longer in the **Ship To** tab of Order Management. Sellers now have the ability to filter for these new order types quickly to assess the necessary next steps in fulfillment.

Specifically for back-orders, Order Management has enabled tracking and visibility against incoming inventory. Back-orders have SLAs that are extended to allow sellers more time to fulfill the order. At the time of purchase, the **Ship By** date is calculated based on the replenishment days associated with the inventory counted as back-order inventory. Beyond this **Ship By** date, all other existing governance and fulfillment policies are unchanged.

Finally, we're adding visibility for an on-time delivery rate calculation, `delivery_sla_time`, that should help sellers avoid late delivery penalties, especially with the rollout of the aforementioned order types.
## Affected markets and versions
This change applies to the following market(s):

* United States (US)

This change applies to the following API version(s):

* 202309 (and later)

## API changes
### Order APIs
For the [POST Get Order List](get-order-list) and [GET Get Order Detail](get-order-detail) endpoints, we're introducing a new `order_type` response parameter.
| **New** **`order_type` value** | **Definition** |
| --- | --- |
| `PRE_ORDER` | An advance order for items that are not yet available or released. **Fulfillment starts on a specific date in the future.** |
| `MADE_TO_ORDER` | An order for items that are produced only after the order is received. **Fulfillment starts after the product is produced.** |
| `BACK_ORDER` | An order for items that are out of stock but expected to be restocked. **Fulfillment starts after the product is restocked.** |

We've also added and deprecated a couple of response parameters to support these new order types and business logic.
| **Response parameter** | **Details** | **Status** |
| --- | --- | --- |
| `delivery_sla_time` | The date an order should arrive by to be considered on-time and to avoid late delivery penalties. | **NEW** |
| `release_date` | The date on which order handling starts and the status of the order changes to [AWAITING_SHIPMENT](order-api-overview). Applicable only if the `order_type` is `PRE_ORDER`. **Note**: When a pre-order status is `ON_HOLD`, the product is still awaiting release, so payment will only be authorized 1 day before the release. | **NEW** |
| `handling_duration` | The duration for the seller to process the order and hand it over to a shipping carrier after the order is placed. Applicable only if the `order_type` is `MADE_TO_ORDER` or `BACK_ORDER`. | **NEW** |
| `handling_duration_days` | Replaced by `handling_duration`. | **DEPRECATED** |
| `sku_type` | Replaced by `order_type`. | **DEPRECATED** |