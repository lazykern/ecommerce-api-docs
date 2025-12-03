# What is Seller Notification

Seller notifications refer to various types of shop related messages sent to sellers by Lazada. Such as order cancellation notifications, items sold out, etc.

# Seller Centre notification page

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1715650001669_V7trBKRm)

# Required API

**SellerCenterMsgList**

/sellercenter/msg/list

Note: Currently, only active enquiry is supported, no push service is provided.

## API Request Parameter Analysis

Field name | Type | Required or not | Description
---|---|---|---
language | String | No | Set the language of API response, default response is English. ENUM: en_US,en_SG,th_TH,id_ID,vi_VN,fil_PH,ms_MY. Note: If the current country or field does not support the requested language it will respond in English.
page | String | No | Current page number, default value: 1.
pageSize | String | No | The number of messages that can be displayed on the current page. Default value: 10, Maximum value: 100.

## API Response Parameter Analysis

Field name | Description
---|---
current | Number of current pages
total | Total number of notifications
pageSize | Current Page Size
appLink | Mobile link to the corresponding page in the Lazada Seller Centre
webLink | Link to the corresponding page in the web-end Seller Centre
description | Content of the notice
title | Title of the notice
categoryName | Category name of the current message ENUM: Orders, Logistics, Store, System, Lazada Program, Learn & Grow, Customer Care
picture | If the notification is accompanied by an image, a link to the image will be displayed here.
id | ID of the current notification
time | Time of publication of the notice

## API Response Example

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"result": {

"data": {

"pageInfo": {

"current": 1,

"total": 1922,

"pageSize": 2

},

"dataSource": [

{

"message_content": {

"appLink": "lazadaseller://com.sc.lazada/order/detail?orderId=426156492043475",

"webLink": "https://sellercenter.lazada.com.my/apps/order/detail?tradeOrderId=426156492043475",

"description": "Order Number: 426156492043475",

"title": "You've got a new order",

"categoryName": "Orders",

"picture": "https://sg-test-11.slatic.net/p/27d8c13365fad957be26147004b95c3c.jpg"

},

"id": "6637458862986875594",

"time": "10 minutes ago"

},

{

"message_content": {

"appLink": "lazadaseller://com.sc.lazada/order/v3/detail?orderid=426169263243475",

"webLink": "https://sellercenter.lazada.com.my/apps/order/list?oldVersion=1&spm=a1zawf.23708326.navi_right_sidebar.d_combine_my_country.117d4edfrGPVMO&status=toRespond",

"description": " Order Number:426169263243475",

"title": "Cancellation request",

"categoryName": "Logistics",

"picture": "https://th-live-01.slatic.net/p/d77dcd100239922b2ca1d93a52e9f2eb.png"

},

"id": "6636045009145092834",

"time": "32 minutes ago"

}

]

},

"success": true

},

"code": "0",

"request_id": "2102ebef17155792298968514"

}

# Q&A

## Why is the link displayed in "webLink" sometimes incomplete?

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

"message_content": {

"appLink": "lazadaseller://com.sc.lazada/lightpublish/presentSemi?productid=4088796117",

"webLink": "/apps/product/publish?productId=4088796117#sku",

"description": "T.H.E. Short 7 NULUX Lined - Solid ... is sold out, click to replenish or list another product.",

"title": "Your product is out of stock! ",

"categoryName": "Store"

}

Some of the modules cannot be fully linked for technical reasons, you can use the following domain names to complete the links in "webLink" according to your seller's country.

  

MY：https://sellercenter.lazada.com.my

ID：https://sellercenter.lazada.co.id

PH：https://sellercenter.lazada.com.ph

SG：https://sellercenter.lazada.sg

TH：https://sellercenter.lazada.co.th

VN：http://sellercenter.lazada.vn