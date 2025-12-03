With the rollout of new fast delivery services across SEA (including Next Day Delivery, Instant, and Same Day), it's important to help merchants prioritize these fast delivery orders effectively. 
We recommend developers to update your **default sorting logic** to support merchants with better order processing prioritization.
The sorting will **require 2 layers**:

1. Shipping SLA (`tts_sla_time`)
2. Logistics Priority (`fulfillment_priority_level`)

For comprehensive details about this change and the required actions, please review the following content. The change will be effective on September 30, 2025.
# Which markets are affected?
The updates of the requirements apply to the local sellers in the ID, SG, PH, VN, TH and MY markets.
# What action is required
Developers need to adjust your default sorting logic to follow platform strategy.
# API changes
## Fulfillment APIs
| **Sorting layer** | **API** | **Field name** | **Type** | **Field Value** | **Changing log** |
| --- | --- | --- | --- | --- | --- |
| Primary | [Get Order Detail](https://partner.tiktokshop.com/docv2/page/get-order-detail-202309), <br> [Get Order List](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) | `tts_sla_time` | `int` | The latest collection time specified by the platform. Unix timestamp. | * For "Next day delivery" order, tts_sla_time is fast delivery deadline. <br> * For other orders, there is no change. |
| Secondary |  | `fulfillment_priority_level` <br>  | `int` <br>  | Fulfillment priority value that can be used for sorting. <br> Available values: <br> `100` = Instant <br> `200` = Sameday 8 hours <br> `300` = Sameday <br> `400` = Next Day Delivery <br> `500` = Express <br> `600` = Standard <br> `700` = Economy <br> `800` = Cargo | This is a new field added |