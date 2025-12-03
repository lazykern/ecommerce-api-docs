# API Link:

**GetOrders**

[ https://open.lazada.com/apps/doc/api?path=%2Forders%2Fget](<https://open.lazada.com/apps/doc/api?path=%2Forders%2Fget>)

Description:Use this API to get the list of items for a range of orders1..

**GetOrderitems**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fitems%2Fget](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fitems%2Fget>)

Description:Use this API to get the item information of an order.

**GetShipmentProvider**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fshipment%2Fproviders%2Fget](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fshipment%2Fproviders%2Fget>)

Description:Use this API to get the list of all active shipping providers, which is needed when working with the Pack API.

**Pack**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Ffulfill%2Fpack](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Ffulfill%2Fpack>)

Description:Use this API to mark an order item as being packed.

**RecreatePackage**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Frepack](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Frepack>)

Description:Use this API to mark a package item as being repack.

**PrintAWB**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Fdocument%2Fget](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Fdocument%2Fget>)

Description:Use this API to retrieve order-related documents, only for shipping labels.

**ReadyToShip**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Frts](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Frts>)

 _Description:_ Use this API to mark an order item as being ready to ship.

**ConfirmDeliveryForDBS**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Fsof%2Fdelivered](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Fsof%2Fdelivered>)

 _Des_ _cription:_ Use this API to mark an sof order item as being delivered.

**FailedDeliveryForDBS**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Fsof%2Ffailed_delivery](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Fsof%2Ffailed_delivery>)

 _Des_ _cription:_ Use this API to mark an sof order item as being delivered failed

**DeliverDigital**

[ https://open.lazada.com/apps/doc/api?path=%2Forder%2Fdigital%2Fdelivered](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fdigital%2Fdelivered>)

 _Des_ _cription:_ Use this API to mark a digital order item as being delivered.

  

  

![image](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/18456689/1660559427898-a59bb5d6-5f60-4027-9565-c9a1512bc912.png)

## 2.2 API details

#### 2.2.1 GetShipmentProvider

Common Parameters

**Service Endpoints**

Region | Endpoint
---|---
Philippines | https://api.lazada.com.ph/rest
Vietnam | https://api.lazada.vn/rest
Indonesia | https://api.lazada.co.id/rest
Thailand | https://api.lazada.co.th/rest
Singapore | https://api.lazada.sg/rest
Malaysia | https://api.lazada.com.my/rest

**Common Request Parameters**

Name | Type | Required | Description
---|---|---|---
app_key | String | true | Unique app ID issued by LAZOP console when you apply for an app category
timestamp | String | true | The time stamp of the request e.g. 1517820392000 (which translates to 5 February 2018 08:46:32) with less than 7200s difference from UTC time
access_token | String | true | API interface call credentials
sign_method | String | true | The HMAC hash algorithm you are using to calculate your signature
sign | String | true | Part of the authentication process that is used for identifying and verifying who is sending a request (click here for details)

Request Parameters

Name | Type | Required | Description
---|---|---|---
orders | list | true | [ {"orderId":"3423","orderItemIds":["23423","234234"]},{"orderId":"3423","orderItemIds":["23423","234234"]} ]
-order_id | string | true | 
-order_item_ids | list | true | 
shipping_allocate_type | string | true | NTFS/TFS TFS available to Local only, NTFS available to CB only

Common Response Parameters

Name | Type | Required | Description
---|---|---|---
 |  |  | 

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-platform_default | int | true | 1=platform allocation 0/other=need seller choose
-shipment_providers | list | optional | 
--name | string | true | 
-shipping_allocate_type | string | true | TFS/NTFS

Request Example

Response Example

Error Example

Error Codes

  

#### 2.2.2 Pack

  

Request Parameters

Name | Type | Required | Description
---|---|---|---
shipment_provider_id | string | optional | depend on getShipmentProvider API, if platform_default!=1 , field is M
delivery_type | string | true | dropship
pack_order_list | list | true | {"pack_order_list":[{"order_id":23432,"order_item_id": ["23423","3243"]}]}
-order_id | string | true | 
-order_item_list | list | true | 
--order_item_id | string |  | 

  

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-pack_order_list | list | optional | 
--order_id | string | true | 
--order_item_list | list |  | 
---package_id | string | optional | when item_error_code==0 exist
---shipment_provider | string | optional | when item_error_code==0 exist
---tracking_number | string | optional | when item_error_code==0 exist
---item_err_code | string | true | 0 =success other=fail
---msg | string | optional | when item_error_code !=0 exist

  

  

#### 2.2.3 RecreatePackage

Request Parameters

Name | Type | Required | Description
---|---|---|---
packages | list | true | [{"package_id":"FP23423"},{"package_id":"FP23423"}]
-package_id | string | true | 

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-packages | list | optional | 
--package_id | string | true | 
--item_err_code | string | true | 0 =success other=fail
--msg | string | optional | when item_error_code !=0 exist

  

#### 2.2.4 PrintAWB

Request Parameters

Name | Type | Required | Description
---|---|---|---
pacakges | list | true | [{"package_id":"FP23423"},{"package_id":"FP23423"}]
-package_id | string | true | 
doc_type | string | true | HTML/PDF
 |  |  | Support AWB with Full item list and AWB without Item list

Common Response Parameters

Name | Type | Required | Description
---|---|---|---
 |  |  | 

Response Parameters

All parcels Awb will be combined in one file，To improve performance and maintain the original experience, Separate each package if required，need request one by one

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-file | string | optional | 
-doc_type | string | optional | PDF/HTML
-pdf_url | string | optional | exist when doc_type is PDF

#### 2.2.5 ReadyToShip

Request Parameters

Name | Type | Required | Description
---|---|---|---
packages | list | true | [{"package_id":"FP23423"},{"package_id":"FP23423"}]
-package_id |  |  | 

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-packages | list | optional | 
--package_id | string | true | 
--item_err_code | string | true | 0 =success other=fail
--msg | string | optional | when item_error_code !=0 exist

#### 2.2.6 ConfirmDeliveryForDBS

Request Parameters

Name | Type | Required | Description
---|---|---|---
packages | list | true | [{"package_id":"FP23423"},{"package_id":"FP23423"}]
-pacakge_id | string | true | 

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-packages | list | optional | 
--package_id | string | true | 
-- item_err_code | string | true | 0 =success other=fail
--msg | string | optional | when item_error_code !=0 exist

#### 2.2.7 FailedDeliveryForDBS

Request Parameters

Name | Type | Required | Description
---|---|---|---
packages | list | true | [{"package_id":"FP23423"},{"package_id":"FP23423"}]
-package_id | string | true | 

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-packages | list | optional | 
--package_id | string | true | 
-- item_err_code | string | true | 0 =success other=fail
--msg | string | optional | when item_error_code !=0 exist

  

#### 2.2.8 DeliverDigital

Request Parameters

Name | Type | Required | Description
---|---|---|---
orders | list | true | [{"order_id":"32423"," order_item_list ":["23423","342342"]}]
-order_id | string | true | 
-order_item_list | list | true | 

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
- orders | list | optional | 
--order_id | string | true | 
--order_id_list | string | true | 
---msg | string | optional | when item_error_code !=0 exist
---item_err_code | string | true | 0 =success other=fail
---order_item_id | string | true | 

#### 2.2.9 GetPackageInfo [Not Available Right Now]

Request Parameters

Name | Type | Required | Description
---|---|---|---
order_item_ids | list | true | ["23423","3243"]

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
order_item_ids | list | true | ["23423","3243"]

  

Response Parameters

Name | Type | Required | Description
---|---|---|---
errorCode | string | true | 
errorMsg | string | optional | 
success | bool | true | 
data | Object |  | 
-order_items | list | optional | 
--order_item_id | string | true | 
--package_id | string | optional | when item_error_code ==0 exist
--code | string | true | 0 =success other=fail
--msg | string | optional | when item_error_code !=0 exist