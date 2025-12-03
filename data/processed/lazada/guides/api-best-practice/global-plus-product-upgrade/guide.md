API：[/product/global/extension](<https://open.lazada.com/apps/doc/api?cid=18&path=%2Fproduct%2Fglobal%2Fextension>)

 

**请求参数：**

**参数** |  **类型** |  **描述**  
---|---|---  
global_item_ids |  List<Long> |  根据globalId查询，返回所有国家的商品 // 优先使用这个进行查询 // 最多50个  
item_ids |  List<Long> |  //global_item_ids 为空时查询，必须与country一起查询 // 最多50个  
country |  String |  //global_item_ids 为空时查询，必须与item_ids一起查询  
      
    
    "global_item_ids": [180226526], // 优先使用这个进行查询
    "item_ids": [13243454], //查询global时此字段为空
    "country": "SG" //查询global时此字段为空

 

**响应参数：**
    
    
    {
      "code": "0",
      "data": {
        "global_item_id": "180226526", // 查询country item时这个字段为空
        "item_id": 13243454, // 查询global时这个字段为空  
        "abs": "1.4",//订单中平均包含商品数量设置；重量小于0.01kg的轻小件商品将返回此参数
        "products": [
          {
            "market": "LAZADA_VN",
            "item_id": 1234234,
            "semi_status": 1, // 1 则为半托管商品
            "skus": [
              {
                "sku_id":123412,
                "seller_sku": "ctf-a",
                "no_postage_fee": {
                  "amount": 3500,
                  "currency": "VND"
                },
                "special_price": {
                  "amount": 3800,
                  "currency": "VND"
                },
                "price": {
                  "amount": 7500,
                  "currency": "VND"
                }
              }
            ]
          }
        ]
      },
      "success": "true",
      "error_code": "10002",
      "error_msg": "get SKU failed",
      "request_id": "0ba2887315178178017221014"
    }