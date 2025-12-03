# 1. Trigger scenario
The **cancellation status change** webhook is triggered when the `cancel_status` of an order changes:

* An order cancellation is initiated: `CANCELLATION_REQUEST_PENDING`
* An order cancellation is accepted by the `SELLER` or `SYSTEM`: `CANCELLATION_REQUEST_SUCCESS`
* An order cancellation is closed by the `BUYER` or `SYSTEM`: `CANCELLATION_REQUEST_CANCELLED`
* An order cancellation is successful and a refund is issued: `CANCELLATION_REQUEST_COMPLETE`

# 2. Data business parameters
| **Parameter name** | **Sample** | **Description** |
| --- | --- | --- |
| order_id | 577087614418520388 | The identification of a TikTok Shop order |
| cancellations_role | BUYER | The user who initiated a cancellation, with possible values: <br>  <br> * BUYER <br> * SELLER <br> * SYSTEM |
| cancel_status | CANCELLATION_REQUEST_PENDING | Order cancellation status, with possible values: <br>  <br> * CANCELLATION_REQUEST_PENDING <br> * CANCELLATION_REQUEST_SUCCESS <br> * CANCELLATION_REQUEST_CANCELLED <br> * CANCELLATION_REQUEST_COMPLETE |
| cancel_id | 4035318504086604100 | The identifier of a specific order cancellation |
| create_time | 1627587600 | The time when the buyer initiated the cancellation request, represented as a Unix timestamp (seconds). |
## Event example
```JSON
{
  "type": 11,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "order_id": "576486316948490001",
    "cancellations_role": "BUYER",
    "cancel_status": "CANCELLATION_REQUEST_PENDING",
    "cancel_id": "4035318504086604100",
    "create_time": 1627587600
  }
}
```