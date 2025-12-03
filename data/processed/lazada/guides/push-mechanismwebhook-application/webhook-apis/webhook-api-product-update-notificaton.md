Property| Value| Comment  
---|---|---  
msg_type| 3| field to determine message type.  
Retry times  
| 12| Retry times when client failed to response  
Retry Interval| 30min| delay between two retries  
Auth Required| true| This notification need authorization  
  
  


Triggered when new product/sku is added(includes publish and edit)

  

    
    
    {
      seller_id : "1234567", 
      message_type : 3, 
      
      data :{
        "item_id": "232611001", //product id
        "sku_list": [
          {
            "shop_sku": "232611001_SGAMZ-356805001", 
            "seller_sku": "api-create-test-111", 
            "sku_id": "356805001" 
          },
          {
            "shop_sku": "232611001_SGAMZ-356805001",
            "seller_sku": "api-create-test-111",
            "sku_id": "356805001"
          }
        ]},
        "action":"EDITED_UPDATED",  //operation type : PUBLISHED(product publish), EDITED_INSERTED(edit)
        "status_update_time":1623238942696,
      "timestamp" : 1606130634,
      "site" : "lazada-sg"
    }

Property| Value| Comment  
---|---|---  
msg_type| 4| field to determine message type.  
Retry times  
| 12| Retry times when client failed to response  
Retry Interval| 30min| delay between two retries  
Auth Required| true| This notification need authorization  
  
Triggered when a product is edited()
    
    
    {
      "seller_id": "100072361",
      "message_type": 4,
      "data": {
        "item_id": 1760954113,
        "sku_list": [{
          "shop_sku": "1760954113_SGAMZ-8975502010",
          "seller_sku": "1760954113-1621404701289-0",
          "sku_id": 8975502010
        }],
        "action": "EDITED_UPDATED",//edit except insert and delete
        "status_update_time": 1623232569146
      },
      "timestamp": 1623232569,
      "site": "LAZADA_SG"
    }

  


  


Property| Value| Comment  
---|---|---  
msg_type| 5| field to determine message type.  
Retry times  
| 12| Retry times when client failed to response  
Retry Interval| 30min| delay between two retries  
Auth Required| true| This notification need authorization  
  
Triggered when a product is deleted or a sku is deleted
    
    
    {
      "seller_id": "100056775",
      "message_type": 5,
      "data": {
        "item_id": 1807508328,
        "sku_list": [{
          "shop_sku": "1807508328_SGAMZ-9541954106",
          "seller_sku": "11111111",
          "sku_id": 9541954106
        }, {
          "shop_sku": "1807508328_SGAMZ-9542176118",
          "seller_sku": "22222223",
          "sku_id": 9542176118
        }, {
          "shop_sku": "1807508328_SGAMZ-9542176119",
          "seller_sku": "33333333",
          "sku_id": 9542176119
        }],
        "action": "EDITED_DELETED", //operation type DELETED(delete product) EDITED_DELETED(delte sku)
        "status_update_time": 1623230820094
      },
      "timestamp": 1623230820,
      "site": "LAZADA_SG"
    }