Property | Value | Comment
---|---|---
msg_type | 0 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

Triggered when a order status change except return and refund.
    
    
    {
     "seller_id":"1234567",  //seller Id
     "message_type":0,
       "data":{
          "order_status":"unpaid", //Order Status
          "trade_order_id":"260422900198363", //trade order Id
          "trade_order_line_id":"260422900298363", //sub order Id
          "status_update_time":1603698638 //update time (seconds)
       },
       "timestamp":1603766859530, //time when notify(seconds)
       "site":"lazada_vn" //site
    }

  

Triggered when a order status change to return and refund.
    
    
    {
       "seller_id":"1000114855", 
       "message_type":0,
       "data":{
          "order_status":"returned",
          "reverse_order_id":"501977696648153",    //reverse order id
          "reverse_order_line_id":"502491640048153", //reverse order line id
          "status_update_time":1603703663,  //status update time
          "trade_order_id":"252883361348153", // order id
          "trade_order_line_id":"252883361948153" //order line id
       },
       "timestamp":1603715010436,
       "site":"lazada_vn"
    }