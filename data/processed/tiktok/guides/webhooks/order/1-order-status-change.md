# 1. Trigger scenario
The **order status change** webhook is triggered when the `order_status` of an order changes.
# 2. Data business parameters
| **Parameter name** | **Sample** | **Description** |
| --- | --- | --- |
| order_id | 576462377512830168 | The identification of a TikTok Shop order |
| order_status | CANCEL | The most recent order status, with possible values: <br>  <br> * `UNPAID` <br> * `ON_HOLD` <br> * `AWAITING_SHIPMENT` <br> * `AWAITING_COLLECTION` <br> * `CANCEL` <br> * `IN_TRANSIT` <br> * `DELIVERED` <br> * `COMPLETED` |
| is_on_hold_order | false | Indicates whether the order has experienced or will experience `ON_HOLD` status |
| update_time | 1627587505 | The order status update time, represented as a Unix timestamp (seconds). |
## Event example
```json
{
    "type":1,
    "tts_notification_id": "7327112393057371910",
    "shop_id":"7494049642642441621",
    "timestamp":1644412885,
    "data":{
        "order_id":"576486316948490001",
        "order_status":"UNPAID",
        "is_on_hold_order": false,
        "update_time":1644412885
    }
}
```