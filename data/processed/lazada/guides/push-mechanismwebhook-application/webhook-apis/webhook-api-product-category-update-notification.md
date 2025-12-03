Property| Value| Comment  
---|---|---  
msg_type| 12| field to determine message type.  
Retry times| 12| Retry times when client failed to response  
Retry Interval| 30 min| delay between two retries  
Auth Required| false| This notification DOES NOT need authorization  
  
Triggered when the product category tree were updated. 

Note :

1.This is a broad cast notification which does not require seller authorization.

2.There is no seller_id inside message body since all sellers share the same categories.

3.The site would only be lazada_sg since all sites share the same cateogries.
    
    
    {
        "message_type": 12,
        "data": {
            "status": "finish",
            "status_update_time": 1627203600000
        },
        "timestamp": 1627203600,
        "site": "lazada_sg"
    }