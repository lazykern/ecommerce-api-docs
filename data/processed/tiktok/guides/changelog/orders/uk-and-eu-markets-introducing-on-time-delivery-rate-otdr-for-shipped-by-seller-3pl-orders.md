# Summary
**On Time Delivery Rate** (OTDR) is a measurement used to assess a seller's ability to fulfill customer orders within the promised delivery timeframe. OTDR is defined as the percentage of all packages (delivered over a period of 7 calendar days) that take less than **5 business days** to be delivered. 

From **August 25th, 2025**, sellers in the UK and EU using the **Shipped by Seller** (3PL) fulfillment method will receive `delivery_sla_time` data with each order, enabling better management of delivery expectations. OTDR will impact shop health in the future.
# Impact
|  |  |
| --- | --- |
| Impacted market(s) | * United Kingdom (UK) - Local and cross-border <br> * Europe (EU) - Local |
| Impacted version(s) | * 202309 (and later) |
# What's new?
While we aren't introducing any new endpoints or parameters, the existing`delivery_sla_time `parameter in the **** [POST Get Order List ](https://partner.tiktokshop.com/docv2/page/get-order-list-202309)and **** [GET Order Details](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507) APIs will be populated with data in the **UK** and **EU** going forward.
| Parameter | Type | Sample | Description |
| --- | --- | --- | --- |
| `delivery_sla_time` <br>  | int64 | 1678389618 | Order should arrive by this date to be considered on-time and to avoid late delivery penalties. |
# Next steps
Ensure your application can safely handle the additional field data in the response.
Update your integration to **pass** **`delivery_sla_time` back to your Order Management System (OMS)** so that sellers are aware of the delivery SLA time for each order.
# Related changes
| **Changelog** | **Description** |
| --- | --- |
| [US market: Pre-order, made-to-order, back-order functionality; delivery SLA](https://partner.tiktokshop.com/docv2/page/us-market-pre-order-made-to-order-back-order-functionality-delivery-sla) | Original changelog for US market introduction of `delivery_sla_time `parameter. |