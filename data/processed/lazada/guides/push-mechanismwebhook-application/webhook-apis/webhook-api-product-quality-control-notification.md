Triggered when product quality control status is updated. 

  

Property | Value | Comment
---|---|---
msg_type | 1 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

  

    
    
    {
        "seller_id": "500176629136",
        "message_type": 1,
        "data": {
            "date": 1627451616614,
            "itemId": 2202832065, //product item id
            "reason": "You have violated the Prohibited and Controlled Products Policy - ${riskcategory}. As a result, your product has been locked. For more information, please refer to  https://sellercenter.lazada.com.ph/seller/helpcenter/what-is-prohibited-and-controlled-products-policy.html. To appeal, please click on the appeal button.<br/>\u0001\u0001",
            "seller_id": 500176629136,
            "status": "Lock" //status enumeration
        },
        "timestamp": 1627451616,
        "site": "lazada_ph"
    }

Status Enumeration : 

PENDING : Pending for approval

APPROVED : Live approved

REJECTED : Rejected. Refer to "reason"

LIVE_REJECTED : A sanction happend on live product. The product would be offline and editable.

LOCK : A sanction happend on live product. The product would be uneditable.