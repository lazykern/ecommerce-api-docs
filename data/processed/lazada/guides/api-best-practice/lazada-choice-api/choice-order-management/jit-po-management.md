![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误1_1728887611580__whyy.jpg)

# 1\. Query PO List

## 1.1. path

[/jit/purchase_order/query_list](<https://open.lazada.com/apps/doc/api?path=%2Fjit%2Fpurchase_order%2Fquery_list>)

## 1.2. request

**Name**| **Type**| **Required or not**| **Description**  
---|---|---|---  
gmt_create_begin| String| Yes| PO creation start time, the time range (i.e. end-begin) needs to be within 90 days. {yyyy-MM-dd HH:mm:ss}  
gmt_create_end| String| Yes| The PO creates the end time, and the time range (i.e. end-begin) needs to be within 90 days. {yyyy-MM-dd HH:mm:ss}  
purchase_order_no_list| String[]| No| Purchase Order (PO) list, 20 max.{["POJ1001","POJ1002"]}  
logistics_no_list| String[]| No| List of logistics orders, maximum 10.{["LBX1001","LBX1002"]}  
order_status| String| No| PO Status 10:To Pack; 20:Ready To Ship; 22:To Put Away; 25:Arrive ata Warehouse; 40:Completed; -100610:Timeout cancellation; -100:Buyer Cancellation;Without this parameter the API will respond to all state POs by default.  
page_index| Number| No| Current page, default 1.  
page_size| Number| No| Pagination size, maximum 50, default 20.  
  
## 1.3. response

result|   
|   
| Object|   
  
---|---|---|---|---  
  
| data|   
| Object|   
  
  
|   
| gmt_modified| Number| Updated time  
  
|   
| supplier_id| Number| Supplier ID  
  
|   
| delivery_method| String| Shipping method:parcel: express; truck: truck delivery or other; pickup: door-to-door;   
  
|   
| store_contact_name| String| Warehouse contact name  
  
|   
| supplier_code| String| Supplier Code  
  
|   
| purchase_order_no| String| Purchase Order No  
  
|   
| gmt_arrive_time| Number| Actual arrival time at the warehouse  
  
|   
| seller_id| String| Seller id  
  
|   
| total_quantity| Number| Purchase quantity  
  
|   
| total_sku_count| Number| SKU quantity  
  
|   
| store_name| String| Store name  
  
|   
| biz_status| String| PO status  
  
|   
| supplier_name| String| Supplier name  
  
|   
| creator| String| creator id  
  
|   
| gmt_create| Number| Created time  
  
|   
| gmt_except_arrive_time| Number| Expected time of arrival  
  
|   
| trade_order_id_list| String[]| order id  
  
|   
| pickup_order_no| String| Pick up order number(PUO)  
  
|   
| store_contact_phone| String| Store Contact Phone Number  
  
|   
| logistics_no_list| String| List of logistics order numbers  
  
|   
| store_address| String| Store Address  
  
|   
| site_id| String| Recipient's country  
  
|   
| store_code| String| Warehouse Code  
  
| page_index|   
| Number| Current page number  
  
| page_size|   
| Number| Page size  
  
| total_page|   
| Number| Total pages  
  
| total_count|   
| Number| Total number of records  
  
| success|   
| Boolean| isSuccess  
  
| error_message|   
| String| error msg  
  
| error_code|   
| String| error code  
  
## 1.4. demo

### 1.4.1. Normal Situation

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"current_page_count": 0,

"data": [

{

"supplier_name": "yuyin test company123",

"gmt_modified": 1697772940000,

"creator": "500403648032",

"supplier_id": 1000000000351423,

"delivery_method": null,

"store_contact_name": "test11",

"supplier_code": "12981579",

"gmt_create": 1697772919000,

"gmt_except_arrive_time": 1697945719000,

"purchase_order_no": "POJ2310202023123807",

"gmt_arrive_time": null,

"trade_order_id_list": [

"726365100368364"

],

"pickup_order_no": null,

"store_contact_phone": null,

"logistics_no_list": [],

"seller_id": "500403648032",

"total_quantity": 3,

"store_address": "Dummy, Fuyuan 1 Road, Tangwei Street, Fuyong Town",

"total_sku_count": 1,

"site_id": "PH",

"store_name": "Lazada Vmi Test",

"biz_status": "10",

"store_code": "RMCW-CHOICE-CN-TEST-1"

},

{

"supplier_name": "yuyin test company123",

"gmt_modified": 1698228047000,

"creator": "500403648032",

"supplier_id": 1000000000351423,

"delivery_method": "parcel",

"store_contact_name": "test11",

"supplier_code": "12981579",

"gmt_create": 1697772919000,

"gmt_except_arrive_time": 1697945719000,

"purchase_order_no": "POJ2310202023132402",

"gmt_arrive_time": 1698228047000,

"trade_order_id_list": [

"721516401568364"

],

"pickup_order_no": null,

"store_contact_phone": null,

"logistics_no_list": [

"LBX0040984508297"

],

"seller_id": "500403648032",

"total_quantity": 2,

"store_address": "Dummy, Fuyuan 1 Road, Tangwei Street, Fuyong Town",

"total_sku_count": 1,

"site_id": "PH",

"store_name": "Lazada Vmi Test",

"biz_status": "25",

"store_code": "RMCW-CHOICE-CN-TEST-1"

}

],

"page_index": 1,

"need_pagination": true,

"total_page": 1,

"success": true,

"error_message": null,

"page_size": 20,

"error_code": null,

"total_count": 96

}

### 1.4.2. Abnormal Situation1

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"current_page_count": 0,

"data": null,

"need_pagination": true,

"page_index": 1,

"total_page": 0,

"success": false,

"error_message": "the input param gmt_create_begin '2023-10-01 00:00:00:00', can not format to {yyyy-MM-dd HH:mm:ss} lzd_trace:2104c51616993671384778760ea687",

"page_size": 50,

"error_code": "INVALID_PARAM",

"total_count": 0

}

### 1.4.3. Abnormal Situation2

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"current_page_count": 0,

"data": null,

"need_pagination": true,

"page_index": 1,

"total_page": 0,

"success": false,

"error_message": "CG_CC_ILLEGAL_ARGUMENT:gmtCreateLeft和gmtCreateRight的时间间隔不能超过90天 lzd_trace:2104c51616993671864004557ea687",

"page_size": 50,

"error_code": null,

"total_count": 0

}

# 2\. Query the list of PO items

## 2.1. path

[/jit/purchase_order/query_list_purchase_item](<https://open.lazada.com/apps/doc/api?path=/jit/purchase_order/query_list_purchase_item>)

## 2.2. request

**Name**| **Type**| **Required or not**| **Description**  
---|---|---|---  
purchase_order_no| String| Yes| JIT purchase order number  
page_index| Number| No| Current page, default 1.  
page_size| Number| No| Pagination size, maximum 200, default 20.  
  
## 2.3. response

result|   
|   
| Object|   
  
---|---|---|---|---  
  
| data|   
| Object|   
  
  
|   
| product_id| String| Product id  
  
|   
| sc_item_code| String| Product code  
  
|   
| buyer_qty| Number| Number of purchases  
  
|   
| sc_item_id| Number| sc_item_id  
  
|   
| barcodes| String[]| barcodes  
  
|   
| received_normal_qty| Number| Number of products received in good condition  
  
|   
| img_url| String| Product preview image  
  
|   
| product_title| String| Product name  
  
|   
| sc_item_name| String| 货品名称  
  
|   
| seller_sku| String| sellerSku  
  
|   
| sku_id| String| sku id  
  
|   
| received_defective_qty| Number| Number of damaged items received  
  
| page_index|   
| Number| Current page number  
  
| page_size|   
| Number| Page size  
  
| total_page|   
| Number| Total pages  
  
| total_count|   
| Number| Total number of records  
  
| success|   
| Boolean| is success  
  
| error_message|   
| String| error msg  
  
| error_code|   
| String| error code  
  
## 2.4. demo

### 2.4.1. Normal Situation

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"current_page_count": 0,

"data": [

{

"product_id": "2413692053",

"sc_item_code": "1694487877029",

"buyer_qty": 2,

"sc_item_id": 722815306851,

"barcodes": [

"408405000606005"

],

"received_normal_qty": 2,

"product_title": "UVCUVCUVC",

"img_url": "https://my-live-01.slatic.net/p/4269a91e90549471277b82e1fcee8d03.jpg",

"sc_item_name": "bala test 234",

"seller_sku": "test1234",

"sku_id": "11853722049",

"received_defective_qty": null

}

],

"page_index": 1,

"need_pagination": true,

"total_page": 1,

"success": true,

"error_message": null,

"page_size": 50,

"error_code": null,

"total_count": 1

}

### 2.4.2. Abnormal Situation

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"current_page_count": 0,

"data": null,

"need_pagination": true,

"page_index": 1,

"total_page": 0,

"success": false,

"error_message": "the input param page_size is : 2000, max support 200 lzd_trace:2104c51616993672904545557ea687",

"page_size": 50,

"error_code": "INVALID_PARAM",

"total_count": 0

}

# 3\. Pack

## 3.1. path

[/jit/purchase_order/package](<https://open.lazada.com/apps/doc/api?path=%2Fjit%2Fpurchase_order%2Fpackage>)

## 3.2. request

**Name**| **Type**| **Required or not**| **Description**  
---|---|---|---  
purchase_order_no_list| String[]| Yes| Purchase order list, max 100.{["POJ1001","POJ1002"]}  
  
## 3.3. response

result|   
|   
| Object|   
  
---|---|---|---|---  
  
| data|   
| Object|   
  
  
|   
| status| String| 'success'  
  
| success|   
| Boolean| is success  
  
| error_message|   
| String| errror msg  
  
| error_code|   
| String| error code  
  
## 3.4. demo

### 3.4.1. Normal Situation

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"data": {

"status": "success"

},

"success": true,

"error_message": null,

"error_code": null

}

### 3.4.2. Abnormal Situation

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"data": null,

"success": false,

"error_message": "Has packed. Plz refresh lzd_trace:212b4c3b16993554806748351eb42d",

"error_code": null

}

# 4\. Shipment

## 4.1. path

[/jit/purchase_order/batch_pickup_deliver](<https://open.lazada.com/apps/doc/api?cid=52&path=%2Fjit%2Fpurchase_order%2Fbatch_pickup_deliver>)

## 4.2. Pre-conditions for successful API call

When calling this API, the PO state must be 20 (to pack).

The API checks that the JIT PO's current status is 20.

  


Call [3.Pack] first, then [4.Shipment].

[3.Pack] is an asynchronous update, the current state may not be 20, and the call to [4.Shipment] will fail. You must confirm that the current state is 20 before calling [4.Shipment]. Otherwise it will increase the flow limit value and cause subsequent calls to limit the flow.

  


NOTE: Currently the asynchronous processing time is 5~10 seconds.

Under normal condition, call [3.Pack] n(5~10) seconds and then call [4.Shipment], it can be called normally. Otherwise, it can be considered as a stuck order.

## 4.3. How to determine if the current PO status is 20?

Method 1 (Synchronization):

  


1\. Query the current PO list status through the Query API.

Rely on: [1. Query PO List] to query the PO list.

  


Method 2 (asynchronous):

Wait for JIT PO status to push pack_completed. 

This interface is called when the push state, pack_completed, has been packaged.

Dependency: [6. Push] Push JIT PO status.

## 4.4. request

**Name**| **Type**| **Required or not**| **Description**  
---|---|---|---  
purchaseOrderNoList| String[]| Yes| The purchase order list, maximum input of 500.{["POJ1001","POJ1002"]}_No cross-warehouse or cross-store allowed._  
shipperAreaCode| String| Yes| Address area for pickup contact .ENUM: CN，VN，TH，PH，ID，MY  
shipperAddressId| Number| Yes| Address id of pickup contact.It is necessary to check the Division ID of the corresponding country according to the excel sheet (it must be the last level).[📎TH_Divisions.xlsx](<https://www.yuque.com/attachments/yuque/0/2024/xlsx/22221212/1728455909495-c0dfe307-37e0-4910-bc90-edfc8655ff6d.xlsx>)[📎VN_Divisions.xlsx](<https://www.yuque.com/attachments/yuque/0/2024/xlsx/22221212/1728455504368-b5d180a2-d69b-486f-8490-dac702a1a75e.xlsx>)[📎MY_Divisions.xlsx](<https://www.yuque.com/attachments/yuque/0/2024/xlsx/22221212/1728455406609-f8b19c5f-5342-4f40-935c-8b84cb61a475.xlsx>)[📎ph_Divisions.xlsx](<https://www.yuque.com/attachments/yuque/0/2024/xlsx/22221212/1728455408491-56c2b310-351a-4939-8ed9-cb7846511268.xlsx>)[📎ID_Divisions.xlsx](<https://www.yuque.com/attachments/yuque/0/2024/xlsx/22221212/1728455409011-49ea8912-05f6-4444-a692-4ffb7aa8af56.xlsx>)If you are unable to download excel using this method, please submit a ticket inquiry on the open platform to get excel from another source.  
shipperAddressDetail| String| Yes| Detailed address for pickup.  
shipperMobilePhone| String| Yes| Contact phone number for pickup.  
shipperName| String| Yes| Name of the contact person for the pickup.  
estimatedPickupDate| String| No| Appointment Pickup Date {yyyy-MM-dd}, Mandatory if shipperAreaCode value is CN.  
  
## 4.5. response

API Param Name| Param Type| Description| API Param Name  
---|---|---|---  
result| Object| result| result  
data| Object[]| data| data  
status| String| success| status  
error_message| String| error msg for single purchase order | error_message  
pickup_no| String| pickup number| pickup_no  
purchase_order_no| String| purchase order number| purchase_order_no  
allow_date_range| String[]| Range of allowable collection dates| The format is {yyyy-MM-dd}  
success| Boolean| true|   
  
error_message| String| error msg|   
  
error_code| String| error code|   
  
  
# 5\. Print PO and product barcodes

## 5.1. path

[/jit/purchase_order/print](<https://open.lazada.com/apps/doc/api?path=/jit/purchase_order/print>)

## 5.2. request

**Name**| **Type**| **Required or not**| **Description**  
---|---|---|---  
pdf_size| String| Yes| pdf style.{A4/6030/100150}  
purchase_order_no_list| String[]| Yes| List of purchase order numbers, max 20.{["POJ1001","POJ1002"]}  
print_order| Boolean| Yes| Whether or not to print the PO.{true/false}  
print_barcode| String| Yes| Whether to print the product barcode.{true/false}  
  
## 5.3. response

result|   
|   
| Object|   
  
---|---|---|---|---  
  
| data|   
| Object|   
  
  
|   
| file| String| Pdf file download path. {file download url has an expiration time, after the expiration of the need to re-call the generated file url}  
  
| success|   
| Boolean| is success  
  
| error_message|   
| String| errror msg  
  
| error_code|   
| String| error code  
  
## 5.4. demo

### 5.4.1. Normal Situation

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"data": {

"file": "https://ascp-choice.oss-accelerate.aliyuncs.com/ACHOICE_JIT_PO_BARCODE_POJ2310012009218603.pdf?Expires=1699370145&OSSAccessKeyId=LTAI5tPJA5BtV4TJQJ2NZ55U&Signature=jNEEqfT2utnB5SzjIqRR6ETKleg%3D"

},

"success": true,

"error_message": null,

"error_code": null

}

### 5.4.2. Abnormal Situation

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"data": null,

"success": false,

"error_message": "not support print_barcode when pdf_size is A4. lzd_trace:2104c51616993664761641592ea687",

"error_code": "INVALID_PARAM"

}

# 6\. PO status update push

Please read this document to learn about the Webhook standard for the Lazada Open Platform and subscribe to the messages you need in the specified locations.

[Lazada Push Mechanism](<https://open.lazada.com/apps/doc/doc?nodeId=29526&docId=120168>)

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误2_1728887669807__t0PI.jpg)

## 6.1. State list

State Enumeration| Description  
---|---  
created| PO creation completed  
pack_completed| PO Packaging Completed  
arrived| PO has arrived at the warehouse  
closed| PO has been closed  
cancel_by_trade| PO transaction canceled  
cancel_by_timeout| PO timeout canceled  
  
## 6.2. demo

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"seller_id":"1234567",

"message_type":35,

"data":{

"orderStatus":"arrived",

"purchaseOrderNo":"POJX11111111111",

"sellerId":"1234567",

"statusUpdateTime":"1709012975923"

},

"timestamp":1603766859530,

"site":"lazada_vn"

}