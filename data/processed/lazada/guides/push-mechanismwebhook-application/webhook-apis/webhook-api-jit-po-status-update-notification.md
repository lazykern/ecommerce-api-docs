Property | Value | Comment
---|---|---
msg_type | 35 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"seller_id":"123",

"message_type":35,

"data": {

"orderStatus": "closed",

"purchaseOrderNo": "POJ2310202013",

"sellerId": "500100",

"statusUpdateTime": 1697800663966

},

"timestamp":1706515141, //time when notify(seconds)

"site":"lazada_vn" //site

}

状态值 | 状态说明
---|---
created | 采购单已创建
pack_completed | 打包完成
arrived | 已到仓
cancel_by_trade | 买家取消
closed | 已完结
（空，即为NULL） | SLA更新 等场景