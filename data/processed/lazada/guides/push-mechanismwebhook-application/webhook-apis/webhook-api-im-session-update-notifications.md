Property | Value | Comment  
---|---|---  
msg_type | 19 | field to determine message type.  
Retry times | 12 | Retry times when client failed to response  
Retry Interval | 30 min | delay between two retries  
Auth Required | true | This notification need authorization  
  
  

    
    
    {
        "data": {
           {
        "sync_type": "SESSION_UPDATE",          // 事件类型
        "user_account_id": "100094063",         // 卖家账号id
        "user_account_type": 2,                 // 2=seller 1=buyer
        "session_id": "100094063_2_1011822749_1_103",
        "unread_count": 0,                      // 未读数
        "to_position": 1596550789323,           // 对方已读时间
        "self_position": 1596550789323,         // 己方已读时间
        "site_id": "SG"
    }
        },
       "seller_id":20240305, 
       "message_type":19
    }