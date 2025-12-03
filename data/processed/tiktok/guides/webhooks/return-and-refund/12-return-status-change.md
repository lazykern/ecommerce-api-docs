# 1. Trigger scenario
The **return status change** webhook is triggered when the `return_status` of an order changes:

* The `BUYER` initiates a return or refund request and is pending `SELLER` review: `RETURN_OR_REFUND_REQUEST_PENDING`
* The `SELLER` declines the `BUYER`'s return or refund request: `REFUND_OR_RETURN_REQUEST_REJECT`
* The return request is approved and the `SELLER` is waiting for the `BUYER` to return the approved items: `AWAITING_BUYER_SHIP`. If the `BUYER` doesn't ship the items to the `SELLER` before the deadline, the request will be closed automatically.
* To return the items to the `SELLER`, the `BUYER` drops off the package successfully or the `BUYER` ships the package and uploads the tracking number: `BUYER_SHIPPED_ITEM`
* The `SELLER` declines the refund request for the return: `REJECT_RECEIVE_PACKAGE`
* The `SELLER` accepts the refund request or issues a refund for the return: `RETURN_OR_REFUND_REQUEST_SUCCESS`
* The `BUYER` or `SYSTEM` closes the return or refund request: `RETURN_OR_REFUND__REQUEST_CANCELLED`
* The return or refund is successful: `RETURN_OR_REFUND_REQUEST_COMPLETE`

Additionally, a `BUYER` may request an identical replacement item instead of a refund:

* The `BUYER` initiates a replacement request and is pending `SELLER` review: `REPLACEMENT_REQUEST_PENDING`
* The `SELLER` declines the `BUYER`'s replacement request: `REPLACEMENT_REQUEST_REJECT`
* The `SELLER` decides to issue a refund to the `BUYER` without replacement: `REPLACEMENT_REQUEST_REFUND_SUCCESS`
* The `BUYER` cancels the replacement request: `REPLACEMENT_REQUEST_CANCEL`
* The `SELLER` approves the replacement request: `REPLACEMENT_REQUEST_COMPLETE`

# 2. Data business parameters
| **Parameter** | **Description** | **Sample** |
| --- | --- | --- |
| order_id | The identification of a TikTok Shop order | 577087614418520388 |
| return_role | Return or refund request user, with possible values: <br>  <br> * BUYER <br> * SELLER <br> * SYSTEM | BUYER |
| return_type | The return or refund request type, with possible values: <br>  <br> * REFUND <br> * REPLACEMENT <br> * RETURN_AND_REFUND | REFUND |
| return_status | The return status for a request, with possible values: <br>  <br> * AWAITING_BUYER_SHIP <br> * BUYER_SHIPPED_ITEM <br> * REFUND_OR_RETURN_REQUEST_REJECT <br> * REJECT_RECEIVE_PACKAGE <br> * REPLACEMENT_REQUEST_CANCEL <br> * REPLACEMENT_REQUEST_COMPLETE <br> * REPLACEMENT_REQUEST_PENDING <br> * REPLACEMENT_REQUEST_REFUND_SUCCESS <br> * REPLACEMENT_REQUEST_REJECT <br> * RETURN_OR_REFUND_REQUEST_CANCEL <br> * RETURN_OR_REFUND_REQUEST_COMPLETE <br> * RETURN_OR_REFUND_REQUEST_PENDING <br> * RETURN_OR_REFUND_REQUEST_SUCCESS | RETURN_OR_REFUND_REQUEST_PENDING |
| return_id | The identifier of a specific return | 4035318504086604100 |
| create_time | The time when the request was created. | 1627587600 |
| update_time | The time when return order status update, represented as a Unix timestamp (seconds). | 1627587600 |
## Event example
```JSON
{
  "type": 12,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "order_id": "576486316948490001",
    "return_role": "BUYER",
    "return_type": "REFUND",
    "return_status": "RETURN_OR_REFUND_REQUEST_PENDING",
    "return_id": "576486316948490001",
    "create_time": 1627587600
    "update_time": 1644412885
  }
}
```