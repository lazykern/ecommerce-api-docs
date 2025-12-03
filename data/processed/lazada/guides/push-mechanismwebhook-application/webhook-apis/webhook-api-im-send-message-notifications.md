Property | Value | Comment  
---|---|---  
msg_type | 2 | field to determine message type.  
Retry times | 12 | Retry times when client failed to response  
Retry Interval | 30 min | delay between two retries  
Auth Required | true | This notification need authorization  
  
  

    
    
    {
        "data": {
           {
      "session_id" : "100094063_2_1011822749_1_103",
      "message_id": "1zYOS7N0cuIqw96026",  //messageId use to trace problem
      "content": "{\"txt\":\"hello world!\"}",
      "from_account_id": "1891549323", 
      "from_account_type": 1,     //  2=seller 1=buyer
      "send_time": 1596550789323, 
      "template_id": 1,         // 1=txt card  2=SystemTxt 3=ImageCard
      "to_account_id": "231135951", 
      "to_account_type": 1,     // 2=seller 1=buyer
      "type": 1, // 1=userSend 2=systemSend
      "site_id": "SG", // 站点ID
      "process_msg": "xxxx", // 该字段不为空的情况下，代表本条消息没有通过安全拦截校验，
                                                 // 意味着本条消息只有卖家自己可见，ISV需要把这个提示信息上屏展示给卖家
      "auto_reply": false,   // true: 这是一条自动回复消息，false: 这不是一条自动回复消息                       
      "status": 0            // 0：正常，1：消息已撤回
    }
        },
      "seller_id":20240305, 
     "message_type":2
    }