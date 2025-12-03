Property| Value| Comment  
---|---|---  
msg_type| 8| field to determine message type.  
Retry times| 12| Retry times when client failed to response  
Retry Interval| 30 min| delay between two retries  
Auth Required| true| This notification need authorization  
  
This notification is triggered if ：

  1. The app subscribed this notificaiton.
  2. The token is still valid and will expired in 48 hours.



  


Note that this notificaton is a off-line notification which means that it would only occur once a day. 
    
    
    {
        "seller_id": "null",
        "message_type": 8,
        "data": {
            "app_key": "115527",
            "auth_expiry_time": 1627542238,  //expiry time
            "seller_id": "1000165972"
        },
        "timestamp": 1627416758,
        "site": "lazada_ph"
    }