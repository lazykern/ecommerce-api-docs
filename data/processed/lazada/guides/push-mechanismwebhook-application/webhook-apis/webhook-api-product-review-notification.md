Property | Value | Comment
---|---|---
msg_type | 21 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

  

Triggered when an item has a comment
    
    
    {
        "seller_id":"1000042284",
        "message_type":21,
        "data":{
            "item_id":2306372942, // Product Id
            "id":122598400472942, // Review Id
            "order_id":83314300176414 // Order Id
            },
        "timestamp":1660705811, //time when notify(seconds)
        "site":"lazada_sg" //site
    }