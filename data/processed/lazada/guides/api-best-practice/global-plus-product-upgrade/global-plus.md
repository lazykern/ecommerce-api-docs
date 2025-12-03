API：[/product/global/semi/udpate](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fglobal%2Fsemi%2Fupdate>)

?

**请求参数：**

**参数** | **类型** | **描述**  
---|---|---  
payload | Payload | 请求内容json，全局商品则返回所有国家；非全局商品只返回传入的国家。  
      
    
    {
          "global_item_id": 180226526, //查询itemIds时,如果能查到globalItem,则返回
          "item_id": 13243454, //查询global时此字段为空
          "abs":"2.0",//订单中平均包含商品数量设置；重量小于0.01kg的轻小件商品需要设置此参数
          "country":["SG","MY"],
          "skus": [
              {
                "item_id": 13243454, //查询global时此字段为空
                "seller_sku": "test2022 02",
                "sku_id": 314525867, //查询global时此字段为空        
                "package_height": "10",
                "package_length": "10",
                "package_width": "10",
                "package_weight": "0.5",
                "country_info": [
                  {
                  "market": "LAZADA_MY",
                  "quantity": 10, //库存数量，非必填，为null 则不同步更新库存
                  "no_postage_price": "9", //不含邮价
                  "price": "32", //原价 划线价
                  "currency","MYR"
                  },
                  {
                  "market": "LAZADA_VN",
                  "quantity": 5,//库存数量，非必填，为null 则不同步更新库存
                  "no_postage_price": "3800", //不含邮价
                  "price": "7500", //原价 划线价
                  "currency","VND"
                  },
                  { //gsp发布的商品才有这一条信息
                  "market": "GLOBAL_CB",
                  "quantity": 15,//库存数量，非必填，为null 则不同步更新库存
                  "no_postage_price": "5", //不含邮价
                  "price": "8", //原价 划线价
                  "currency","CNY"
                  }
                ]
                
              }
            ]
    }

  


**响应参数：**
    
    
    {
      "error_msg": "null",
      "code": "0",
      "data": {
         "product_id": "10002019"
      },
      "success": "true",
      "error_code": "null",
      "request_id": "0ba2887315178178017221014"
    }

  


**错误码：**

**错误码** | **错误描述**  
---|---  
10001 | Illegal parameters参数不合法  
10002 | System error 系统异常  
10003 | Item not found商品未找到  
10004 | price need to be lower than the original price价格需低于零售价  
10005 | 商品已升级  
10006 | 商品校验失败，无法升级