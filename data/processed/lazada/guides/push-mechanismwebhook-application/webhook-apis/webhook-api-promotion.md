Property | Value | Comment
---|---|---
msg_type | 11 | field to determine message type.
Retry times | 3 | Retry times when client failed to response
Retry Interval | 5 min | delay between two retries
Auth Required | true | This notification need authorization

  

Triggered 72 hours before the end of the voucher
    
    
    {
        "expireTime": 1628079408927, // Expiration timestamp
        "notifyTime": 1628153676218, // Notification timestamp
        "promotionId": 900000001107894,  // Promotion ID
        "promotionType": "SELLER_VOUCHER",  // Promotion type:SELLER_VOUCHER、FLEXI_COMBO、FREE_SHIPPING
        "sellerId": 100191757  // Seller ID
    }

  

Seller Voucher Stock Notification
    
    
    {
        "left": "100",  // Remaining total amount of promotion budget
        "notifyTime": 1628158481068, // Notification timestamp
        "promotionId": 900000001107894,  // Promotion ID
        "promotionType": "SELLER_VOUCHER",  // Promotion type:SELLER_VOUCHER、FLEXI_COMBO、FREE_SHIPPING
        "sellerId": 100191757,  // Seller ID
        "total": "1000", // Total promotion budget
        "used": "900" // Promotion budget used total
    }