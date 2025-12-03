Property | Value | Comment
---|---|---
msg_type | 13 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

Triggered when Seller status is change. 
    
    
    {
        "seller_id": "100053528",
        "message_type": 13,
        "data": {
            "status": "normal" //status enumration
        },
        "timestamp": 1627038397,
        "site": "lazada_sg"
    }

Status Enumration :

normal 

close : Seller is closed. Most of the daily operation are banned.