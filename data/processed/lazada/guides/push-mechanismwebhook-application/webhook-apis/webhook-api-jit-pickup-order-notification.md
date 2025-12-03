Property | Value | Comment
---|---|---
msg_type | 46 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"seller_id": "123",

"message_type": 46,

"data": {

"pickUpOrderNo": "PUO0001",

"purchaseOrderNoList": [

"POJ1001",

"POJ1002"

],

"orderStatus": "PICKED_UP",

"sellerId": "1001"

},

"timestamp": 1706515141, //time when notify(seconds)

"site": "lazada_vn" //site

}

状态值 | 状态说明
---|---
10 | 待揽收/PENDING_PICKUP
20 | 已派车/DISPATCHED_CAR
-20 | 揽收失败/PICKUP_FAILED
30 | 已揽收/PICKED_UP
40 | 已送达/RECEIVED
-10 | 已取消/CANCELLED