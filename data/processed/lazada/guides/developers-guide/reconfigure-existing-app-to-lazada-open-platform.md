The Seller Center APIs have been migrated to Lazada Open Platform. The current applications that call the Seller Center APIs need to be reconfigured for the migration. This section aims at helping you migrate your existing applications to the new platform.

## Recommendation

We strongly recommend you to use the official SDK to call Lazada Open Platform APIs ([download link](<https://open.lazada.com/app/index.htm#/sdk/download>)), which saves your efforts in resolving the protocols. The official SDK will be continuously upgraded to support more programming languages and APIs. If you do not use the official SDK, you will need to understand the following API protocol updates. For more detailed information, refer to the [API Reference Documentation](<https://open.lazada.com/doc/api.htm?spm=a2o9m.11193531.0.0.60139348Fc9LnX>).

## Updated API protocol

Lazada Open Platform API has updated protocol than the Seller Center API. The differences between the request URLs, parameters, and responses are shown in the table below.

Items | Seller Center API | Lazada Open Platform API | Description
---|---|---|---
Request URL | https://api.sellercenter.lazada.{sg} | https://api.lazada.{sg}/rest | One URL for each venture
Parameters | ?Action=GetBrands | /brands/get? | API name: RESTful
&Timestamp=2015-07-01T11:11+0000 | &timestamp=2018-01-07+15%3A53%3A16 | Timestamp: supporting UTC format | 
&Version=1.0 | N/A |  | 
&Signature=01286525c2fdba61ed1f5e | &sign_method=hmac &sign=3ECA2FD80065FB779761F75F6D09D2C6 | Signature algorithm (Lazada Open Platform supports HMAC_SHA256) | 
&Format=XML / JSON | &format=json | LAZOP supports json format only | 
&UserID=a@b.c | &app_key=4272 &partner_id=top-apitools &session=61003091b65c3d405 | Identity: APP：non -> app_key ISV：non -> partner_id user：UserEmail -> log in auth seesion | 
&Limit=100 | &limit=100 | Changed to lowercase. For example, OrderId will be changed to order_id | 
&Offset=0 | &offset=0 | Changed to lowercase | 
Post body | <xml>...</xml> | <xml>...</xml> | No change
Success response | Refer to the sample below | Refer to the sample below | Removed the "SuccessResponse", "Head", and "Body" tags The "RequestId" is on the same level with the results
Error response | Refer to the sample below | Refer to the sample below | Kept the "ErrorResponse" tag Removed the "Head" tag
SDK | For Java | For Java, C#, PHP, Ruby, and Python | 

 

## Seller Center API

#### Request：

[`https://api.sellercenter.lazada.sg?Action=GetBrands&Format=json&Limit=2&Offset=0&Timestamp=2018-01-07T08%3A34%3A58%2B00%3A00&UserID=test%40xxx.com&Version=1.0&Signature=8d4bdfedb8c6164430de8405cf6998f9ffeb018e26344c6d0e1ea6e6f6621652`](<https://api.sellercenter.lazada.co.th/?Action=GetBrands&Format=json&Limit=2&Offset=0&Timestamp=2018-01-07T08%3A34%3A58%2B00%3A00&UserID=dapeng.zdp%40alibaba-inc.com&Version=1.0&Signature=8d4bdfedb8c6164430de8405cf6998f9ffeb018e26344c6d0e1ea6e6f6621652>)

#### Response：
    
    
    {
        "SuccessResponse": {
            "Head": {
                "RequestId": "0bb606c315153141103028143eff59",
                "RequestAction": "GetBrands",
                "ResponseType": "Brands",
                "Timestamp": "2018-01-07T08:35:10+00:00"
            },
            "Body": {
                "Brands": [
                    {
                        "BrandId": 3635,
                        "Name": "3Dconnexion",
                        "GlobalIdentifier": "3dconnexion"
                    },
                    {
                        "BrandId": 3636,
                        "Name": "3M",
                        "GlobalIdentifier": "3m"
                    }
                ]
            }
        }
    }
    

#### Error Response
    
    
    {
        "ErrorResponse": {
            "Head": {
                "RequestId": "0bb606d615153145206778830e1230",
                "RequestAction": "GetBrands",
                "ErrorType": "Sender",
                "ErrorCode": 20,
                "ErrorMessage": "E020: %s Invalid Limit,limit MaxSize 1000"
            }
        }
    }
    

## Lazada Open Platform API

#### Request:

[`http://api.lazada.sg/rest/brands/get?app_key=576214&offset=0&limit=100&sign_method=hmac&sign=3ECA2FD80065FB779761F75F6D09D2C6&timestamp=1517830235276`](<http://api.lazada.sg/rest/brands/get?app_key=576214&offset=0&limit=100&sign_method=hmac&sign=3ECA2FD80065FB779761F75F6D09D2C6&timestamp=1517830235276>)

#### Response
    
    
    {
      "request_id": "cwxtlxt98lvy",
      "code": "0",
      "data": [
          {
            "brand_id": 161266,
            "global_identifier": "test_carmen",
            "name": "test carmen"
          },
          {
            "brand_id": 161267,
            "global_identifier": "2k_games",
            "name": "2K Games"
          }
        ]
    }
    

#### Error Response
    
    
    {
        "request_id": "cwxtly2mw54o",
        "code": "15",
        "type":"ISV|platform|ISP",
        "message": "Remote service error"
    }
    

## API name mapping

Lazada Open Platform APIs are RESTful APIs. The following table shows the mapping of the API method name and the Lazada Open Platform API path.

API | API path
---|---
GetBrands | /brands/get
GetCategoryAttributes | /category/attributes/get
GetCategoryTree | /category/tree/get
GetPayoutStatus | /finance/payout/status/get
GetTransactionDetails | /finance/transaction/detail/get
GetDocument | /order/document/get
GetFailureReasons | /order/failure_reason/get
GetMultipleOrderItems | /orders/items/get
GetOrder | /order/get
GetOrderItems | /order/items/get
GetOrders | /orders/get
GetShipmentProviders | /shipment/providers/get
SetInvoiceNumber | /order/invoice_number/set
SetStatusToCanceled | /order/cancel
SetStatusToPackedByMarketplace | /order/pack
SetStatusToReadyToShip | /order/rts
CreateProduct | /product/create
GetProducts | /products/get
GetQcStatus | /product/qc/status/get
GetResponse | /image/response/get
MigrateImage | /image/migrate
MigrateImages | /images/migrate
RemoveProduct | /product/remove
SetImages | /images/set
UpdatePriceQuantity | /product/price_quantity/update
UpdateProduct | /product/update
UploadImage | /image/upload
SellerUpdate | /seller/update
UserUpdate | /user/update