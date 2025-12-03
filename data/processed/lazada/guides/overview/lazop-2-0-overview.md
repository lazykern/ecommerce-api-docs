# Background

Dear partners, we are delighted to announce that we are launching the new LazOP 2.0! As the market grows, the current features and API defects are becoming blockers for our mutual growth. In order to provider better services and further empower our partners, we've done an upgrade to our current Open API.

With the release of LazOP 2.0, users will get access to a wide range of platform features and capabilities through API, including promotion tools; Lazada Push; reverse order, product reviews and more. In addition, we've done a lot of optimizations to our existing API features to address the pain points that we collected from users.

Additional Notes: https://www.yuque.com/docs/share/cb77f1a4-a614-4649-8453-4574475ee5e7?# 《LazOP 2.0 Overview》

# New API Features Release！

## 1\. Product Review API

<https://open.lazada.com/apps/doc/api?path=%2Freview%2Fseller%2Flist>

Now users will be able to retrieve and reply to Product ratings and reviews through our new API functionalities.

Step 1: GetProducts/GetOrderItems: Get the Itemid that you would like to get reviews for.

Step 2: **GetProductReviewList** : Input Itemid with filter options, we will return the list of review details.

Step 3: **SubmitSellerReply** : User this API to reply to a specific review. Input reviewid and reply content.

API title | Path | Description
---|---|---
GetProductReviewList | /review/seller/list | Get the list of review for specific seller
SubmitSellerReply | /review/seller/reply/add | Reply to a specific review

 

## 2\. Seller API

<https://open.lazada.com/apps/doc/api?path=%2Fseller%2Fget>

The previous end point is getting outdated data for seller performance. We are updating the API to return back the most up-to-date data for seller performance related metrics.

API title | Path | Description
---|---|---
GetSellerMetricsById | /seller/metrics/get | Updated data source to get the most up to date seller performance data.
GetSeller | /seller/get | Added new parameter: is_active to indicate seller is active or not.

 

## 3\. Media Center API

<https://open.lazada.com/apps/doc/api?path=%2Fmedia%2Fvideo%2Fblock%2Fcreate>

Users now will be able upload video content into Lazada Media Center through this API and get the corresponding VideoID. After that, user can attach the videoID on CreateProduct step when listing products on Lazada.

API title | API path | Description
---|---|---
InitCreateVideo | /media/video/block/create | Initiate a create video task
UploadVideoBlock | /media/video/block/upload | Upload video block
CompleteCreateVideo | /media/video/block/commit | Complete your video creation tasks
GetVideoDetail | /media/video/get | Retrieve video details
RemoveVideo | /media/video/remove | Remove video
GetVideoQuota | /media/video/quota/get | Get the video quota for seller

 

![](https://tida.alicdn.com/oss_1631157170364_null_YrbK3R0A.png)

Step 1: **InitCreateVideo** \- Initiate a create video task, response the **uploadID**. (Max video size: 100mb)

Step 2: User divide video into multiple blocks. (Max block size: 10mb, **we recommend < 3mb per block)**

Step 3: **UploadVideoBlock** \- Use this API to upload your video blocks and retrieve all the corresponding **eTag** for each block.

Step 4: **CompleteCreateVideo** \- Finish your video creation tasks by adding more info including:

a. Upload ID from Step 1. b. eTag for each vidoe block. c. Video title. d. Video cover image.

After creation success, you will get the corresponding **VideoID** as the unique idenfier for this video.

Step 5: **CreateProduct** \- now you can create your product with the videoID get from above steps and attach the video to your products.

**GetVideoDetai** l：Use this API to get the details of your video Including video status; video title; video cover image and video URL.

**RemoveVideo** ：Remove your video from Lazada Media center by inputting your video ID.

**GetVideoQuota** ：Retrieve the video quota for specific seller.

## 4\. Promotion Tools API

![](https://tida.alicdn.com/oss_1631158330021_null_Kr7twFU1.png)

### 4.1 Seller Voucher:

<https://open.lazada.com/apps/doc/api?path=%2Fpromotion%2Fvouchers%2Fget>

We recommend you read through below article to understand the business rules of Seller Voucher before integrating with our API :

[https://university.lazada.com.my/course/detail?spm=lzd_university_my.course_search.courserlist_courses.34.5e834984YpwT0p&id=1159&type=series](<https://university.lazada.com.my/course/detail?spm=lzd_university_my.course_search.courserlist_courses.34.5e834984YpwT0p&id=1159&type=series>)

Users now will be able to create, update, activate, deactivate and get vouchers through API. In addition, you will be able to manager your voucher rules on sku level.

**_Vouchers_** need to be collected by buyer in order to redeem it. From set up perspective, vouchers are the type of promotion product which contains only 1 discount criteria, and apply 1 discount type.

![](https://tida.alicdn.com/oss_1631158367833_null_foZT8umH.png)

API Group | API title | API Path | Description
---|---|---|---
Seller Voucher | CreateVoucher | /promotion/voucher/create | Create voucher
UpdateVoucher | /promotion/voucher/update | Updaet voucher | 
GetVoucher | /promotion/voucher/get | Get the details of a specific voucher. | 
GetVoucherList | /promotion/vouchers/get | Get voucher list. | 
ActivateVoucher | /promotion/voucher/activate | Activate voucher | 
DeactivateVoucher | /promotion/voucher/deactivate | Deactivate voucher | 
GetVoucherProducts | /promotion/voucher/products/get | Get list of product that voucher can be applied. | 
AddVoucherSku | /promotion/voucher/product/sku/add | Add sku under a specific voucher rule | 
RemoveVoucherSku | /promotion/voucher/product/sku/remove | Remove sku from specific voucher rule | 

 

### 4.2 Free Shipping: 

<https://open.lazada.com/apps/doc/api?path=%2Fpromotion%2Ffreeshipping%2Fcreate>

We recommend you read through below article to understand the business rules of Free Shipping before integrating with our API : [https://university.lazada.com.my/course/learn?spm=lzd_university_my.course_detail.module-list.1.39b31fd6L5PpzQ&id=3027&sid=628&type=article](<https://university.lazada.com.my/course/learn?spm=lzd_university_my.course_detail.module-list.1.39b31fd6L5PpzQ&id=3027&sid=628&type=article>)

**_Free Shipping_** is the type of promotion tool that enables user to set up their free shipping rules flexibly.

API Group | API title | API Path | Description
---|---|---|---
Free shipping | CreateFreeshipping | /promotion/freeshipping/create | Create free shipping rule
UpdateFreeshipping | /promotion/freeshipping/update | Update free shipping rule | 
GetFreeshipping | /promotion/freeshipping/get | Get free shipping infomation | 
GetFreeshippingList | /promotion/freeshippings/get | Get free shipping list | 
AcitveFreeshipping | /promotion/freeshipping/activate | Activate freeshipping rule | 
DeactiveFreeshipping | /promotion/freeshipping/deactivate | Deactivate freeshipping rule | 
GetFreeshippingProducts | /promotion/freeshipping/products/get | Get list of products can be applied to freeshipping rule | 
AddFreeshippingSku | /promotion/freeshipping/product/sku/add | Add sku into freeshipping rule. | 
RemoveFreeshippingSku | /promotion/freeshipping/product/sku/remove | Remove sku from freeshipping rule. | 

 

### 4.3 Flexicombo:

<https://open.lazada.com/apps/doc/api?path=%2Fpromotion%2Fflexicombo%2Fcreate>

We recommend you read through below article to understand the business rules of Flexicombo before integrating with our API :   
[https://university.lazada.com.my/course/learn?spm=lzd_university_my.course_search.courserlist_courses.3.64f94984BEqLE9&id=3187&type=article](<https://university.lazada.com.my/course/learn?spm=lzd_university_my.course_search.courserlist_courses.3.64f94984BEqLE9&id=3187&type=article>)

**Flexicombo** allows you to combine your promotion criteria and discount rules flexibly, percent off, buy 3 get 1 free, dollars off etc. We've updated and enabled Flexicombo related APIs to match with seller center.

API Group | API title | API Path | Description
---|---|---|---
Flexicombo | CreateFlexicombo | /promotion/flexicombo/create | Create flexicombo
GetFlexicomboDetails | /promotion/flexicombo/details | Get flexicombo detials | 
UpdateFlexicombo | /promotion/flexicombo/update | Update flexicombo | 
GetFlexicomboList | /promotion/flexicombo/list | Get flexicombo list | 

 

## 5 ReverseOrder Management

ReverseOrder API enables user to manage their reverse orders including return, refund and reject. Please find below our best practices for different senarios:

### 5.1 Cancel Order:

Step 1: ReverseOrderCancelValidate, input order id to validate if the order can be canceled by seller, generally, orders can be canceled by seller before RTS.

Case A Yes, **obtain cancel reason from response** go to Step 2.

Case B No -> End, this order cannot be canceled.

Step 2: InitReverseOrderCancel, input order id and cancel reason to cancel the order.

![](https://tida.alicdn.com/oss_1631158414948_null_Bt5AwGS7.png)

### 5.2 Manage ReverseOrders (Buyer initiated a cancelation)

![](https://tida.alicdn.com/oss_1631158464807_null_eJIVpp0N.png)

Step 1: _GetReverseOrderList_ retreive the list of reverse orders.

Step 2: _GetReverseOrderDetail_ （optional）

Step 3: **ReverseOrderReturn****Update,** update action on reverse order.

**Option 1 Seller agreed to refund** (seller do not need buyer to return product), call _ReverseOrderReturnUpdate_ -> End

**Option 2 Seller agreed to return product.** Buyer will return the product.

**Case A Return product to Lazada Warehouse**

Case A.1 seller agreed to refund buyer, call _ReverseOrderReturnUpdate_ -> End

Case A.2 seller refuse to refund buyer, call _ReverseOrderReturnUpdate_ to reject -> End

**Case B Return product to seller**

Case A.1 seller agreed to refund buyer, call _ReverseOrderReturnUpdate_ -> End

Case A.2 seller refuse to refund buyer, call _ReverseOrderReturnUpdate_ to reject -> End

**Option 3 Seller refuse to refund** , call _ReverseOrderReturnUpdate_ to reject -> End

Buyer can dispute an reverse order, user can call _GetReverseOrderHistoryList_ to look up the communication details.

**All reject actions need to input the reject reason getting from**** _GetReverseOrderReasonList_****API.**

#### Infomation Look Up

_GetReverseOrderList_ \- Get the reverse order list.

_GetReverseOrderDetail_ \- User can use this API to get the reserse order details.

_GetReverseOrderHistoryList_ \- User can use this API to get the communication history list for a reverse order.

_GetReverseOrderReasonList_ \- User can use this API to get all the reject reasons.

API title | API Path | Description
---|---|---
ReverseOrderCancelValidate | /order/reverse/cancel/validate | Seller can check whether the order can be canceled through this API and get corresponding reasons if not.
InitReverseOrderCancel | /order/reverse/cancel/create | Seller initiate a cancelation.
ReverseOrderReturn Update | /order/reverse/return/update | Seller can use this API to action on return and refund related.
GetReverseOrdersForSeller | /reverse/getreverseordersforseller | Get the list of reversed order for a specific seller
GetReverseOrderDetail | /order/reverse/return/detail/list | Get the detailed infomation for a specific reverse order
GetReverseOrderHistoryList | /order/reverse/return/history/list | Get the communication history of the reverse order
GetReverseOrderReasonList | /order/reverse/reason/list | Get the list of reject reason. Need to be used in all refuse refund actions

 

## 6 Lazada Push (Webhook)

[https://open.lazada.com/apps/doc/doc?nodeId=29526&docId=120168](<https://open.lazada.com/apps/doc/doc?nodeId=29526&docId=120168>)

6.1 Why Push?

Consider a situation that you are fetching new orders, you are calling GetOrders API thousand times an hour(You may get throttled if your step over the limit.). Even you do that, you are not able to get the most up-to-date data. Similar situation for product management. Connecting to Lazada Push allows you to synchronize your data with Lazada at ease.

### 6.2 4 Easy steps to set up your push today

Step1: Prepare your callback url to receive notifications from Lazop.

Step2: Understand push mechanism details include authorization, retry, etc.. and finish your coding.

Step3: Fill your url in and verify it.

Step4: Subscribe to the push messages.

### 6.3 Push message overview:

Push Messages | Description
---|---
Order Status Change | The subscriber will receive a push message from Lazada when order staus changed.
Product QC status change | The subscriber will receive a push message from Lazada when the product QC status chenged.
Product creation notification | The subscriber will receive a push message from Lazada when create product success.
Product edit notification | The subscriber will reveive a push message from Lazada when product details like: changed.
Product delete notification | The subscriber will reveive a push message from Lazada when products are removed from Lazada.
Low stock notification | The subscriber will reveive a push message from Lazada when product qualitify control review status is updated.
Video status change | The subscriber will receieve a push message from Lazada when uploaded video status is updated
Auth alert Notification | The subscrier will receieve a push message from Lazada when the authorization expires in x days.
Reverse order status | The subscriber will reveive a push message from Lazada once the ReverseOrder status changed.
Category Tree notification | The subsciber will receive a push message from Lazada once there's an update on Category Tree.

 

### 6.4 LazOP App console to set up your push message with Lazada

![](https://tida.alicdn.com/oss_1659072983411_null_jlxXjl96)

#### 6 Lazada Instant Message (IM) API

Find more details below.

[https://www.yuque.com/docs/share/07c0a597-46e1-4bdc-86ec-b5391abdb011?#](<https://www.yuque.com/docs/share/07c0a597-46e1-4bdc-86ec-b5391abdb011>)

API title | API Path | Description
---|---|---
GetMessages | /im/message/list | Return the list of messages for a specific session(conversation) id.
SendMessage | /im/message/send | Send a reply to a specific conversation.
GetSessionList | /im/session/list | Seller can use this API to get the list of Sessions(conversations)
GetSessionDetail | /im/session/get | Return the details of a conversation
ReadSession | /im/session/read | Mark the conversation as read
IM push | push | we will push the message to you if there's an incoming message.

 

# Existing API Upgrade!

## 1 Product Management Upgrade:

### 1.1 Updates on stock management related API.

**Updated API list:**

API Name | API path | Description
---|---|---
GetProductItem | /product/item/get | New parameters added
GetProducts | /products/get | New parameters added
UpdatePriceAndQuantity | /product/price_quantity/update | New parameters added

 

#### New parameters added for APIs mentioned above:

Perameter Name | Description
---|---
fblWarehouseInventories | The stock from lazada warehouse - cannot be edited through UpdateQuantityAndPrice API.
multiWarehouseInventories | Only available for multiware house seller, the stock from user's each ware house.
sellableQuantity | Stock available for sale, buyer can place order.
withholdQuantity | Whithholding stock, when buyer placed an order but payment is not complete, we will withhold the stock for 30mins, a fter that the stock will be released.
occupyQuantity | After the buyer finished payment, the withhold stock will turn into occupy stock.
totalQantity | totalQantity = sellableQuantity + withholdQuantity + occupyQuantity
quantity | same as totalQuantity
channelInventories | The inventory that's occupied by campaigns.
CampaignName | The name of the campaign.

 

New response example:

[{ "Status": "active",

"SkuId": 314525867,

"Images": ["http://sg-live-01.slatic.net/p/BUYI1-catalog.jpg", "", "", "", "", "", "", ""],

"SellerSku": "39817:01:01",

"ShopSku": "BU565ELAX8AGSGAMZ-1104491",

"Url": "https://alice.lazada.sg/asd-1083832.html",

"quantity": 50,

"fblWarehouseInventories":[{

"sellableQuantity": 20,

"withholdQuantity": 20,

"occupyQuantity": 20,

"totalQantity": 60

}],

"multiWarehouseInventories": [{

"warehouseCode": "warehouseTest1",

"sellableQuantity": 20,

"withholdQuantity": 20,

"occupyQuantity": 20,

"totalQantity": 60,

"quantity": 20

}, {

"warehouseCode": "warehouseTest2",

"sellableQuantity": 30,

"withholdQuantity": 20,

"occupyQuantity": 20,

"totalQantity": 70,

"quantity": 30

}],

///In case when skus are signed up for campaigns, you will get the below details in campaign level.///

"channelInventories":[{ 

"sellableQuantity": 20,

"CampaignName": 60,

"startTime":"2020-02-03 00:00",

"endTime""2020-02-03 00:00"

},

{

"sellableQuantity": 20,

"CampaignName": 60,

"startTime":"2020-02-03 00:00",

"endTime":"2020-02-03 00:00"

}]

}]

In case when your skus are occupied by campaigns, when changing your inventory, sum of sellable inventory in all warehouse must be greater than sum of campaign inventory, otherwise update will fail.

![](https://tida.alicdn.com/oss_1631158560877_null_vf0ol535.png)

#### Case 1: I only have 1 warehouse and I'm not using Lazada's warehouse, how should I update my stock?

{

"Product":{

"Skus":{

"Sku":[

{

"ItemId":"1755203881",

"SkuId":"8915369747",

"SellerSku":"19501893",

"Quantity":"11" 

},

{

"ItemId":"1755250705",

"SkuId":"8915387475",

"SellerSku":"19429524",

"Quantity":"18"

}

]

}

}

}

You can update your stock as shown above, the **Quantity** here is same with sellable quantity user get from response.

#### Case 2: I'm a multiware hosue seller and I'm not using Lazada's warehouse, how should I update my stock?

request：

{

"Product":{

"Skus":{ 

"Sku":{

"ItemId":"234234234",

"SkuId":"234",

"SellerSku":"Apple-SG-Glod-64G",

"MultiWarehouseInventories":{

"MultiWarehouseInventory":[

{

"WarehouseCode":"warehouseTest1",

"Quantity":"20"

},

{

"WarehouseCode":"warehouseTest2",

"Quantity":"30"

}

]

}

}

}

}

}

You can update your stock as shown above per warehouse level.

#### Case 3: I'm using my own logistics , how should I update my stock

It depends on what warehouse you are using, not related to logistics options.

#### Case 4: I'm using Lazada's warehouse, how should i update my stock?

_You will not be able to update your stock through this API._

### 1.2 DeactivateProduct API

Details:<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fdeactivate>

API Path：/product/deactivate

Currently users are using UpdateProduct API to active and deacticate products which all needs to go through QC status check. In order to simplify the process, we've opened a new API for deactivating products.

You will be able to deactivate your product through this API in either SPU/Item level or SKU level. The deactivate product actions through this API will not go through QC checks.

<Request>

<Product>

<ItemId>3211321</ItemId>

<Skus> <!--If you delete this tag, the item will be offline-->

<SellerSku>test</SellerSku>

</Skus>

</Product>

</Request>

### 1.3 CreateProduct API updates

#### 1.3.1 Support add Item/SPU level images in CreateProduct request.

Requst Example：

<Request>

<Product>

<PrimaryCategory>6614</PrimaryCategory>

<SPUId/>

<AssociatedSku/>

<Images>

<Image>https://my-live-02.slatic.net/p/765888ef9ec9e81106f451134c94048f.jpg</Image>

<Image>https://my-live-02.slatic.net/p/9eca31edef9f05f7e42f0f19e4d412a3.jpg</Image>

</Images>

<Attributes>

<name>api create product test sample</name>

<short_description>This is a nice product</short_description>

<brand>Remark</brand>

<model>asdf</model>

<kid_years>Kids (6-10yrs)</kid_years>

<delivery_option_sof>Yes</delivery_option_sof>

<!--should be set as ‘Yes’ only for products to be delivered by seller-->

</Attributes>

<Skus/>

</Product>

</Request>

## 2 Order Management

### 2.1 Order API Update

  1. We've updated order staus get from OrderAPI to align Seller Center and OrderAPI for **Failed Delivered** related status as below：
  2. Bug fix: By inputing order status in the request, now you will be only getting matched results.
  3. Added order status flow chart and notes for DG, COD, FBL type of orders. Added flow chart for **Failed Delivered** related status and API call flow best practices.

### 2.2 Order status flow chart:

Please find below the updated order status flow and pay attention to different types of order.

![](https://tida.alicdn.com/oss_1631158638375_null_uF1OCLDV.png)

### 2.3 Failed Delivered related Order Status Flow Chart

![](https://tida.alicdn.com/oss_1631158725064_null_VTZcuJYq.png)

![](https://tida.alicdn.com/oss_1631158788852_null_ssjbXdxY.png)

### 2.4 API call flow

![](https://tida.alicdn.com/oss_1697525461431_null_xGCGCKoI)

### 2.5 Repack API

Newly added API to support user to repack their packages.

<https://open.lazada.com/apps/doc/api?path=%2Forder%2Ffulfill%2Fpack>

### 2.6 PrintAWB

Use this API to get shipping label in PDF or HTML format in order resolve printing farmating issues.

<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Fdocument%2Fget>

#  LazOP Website Revemp

**Brand new LazOP homepage and website: Hightlighting ISV partners，easy access to announcement page and developer community live！**

![](https://tida.alicdn.com/oss_1659073439640_null_DxocYBA1)

### 1 New __LazOP announcement page__. Get the most updated API changes! 

![](https://tida.alicdn.com/oss_1659073524831_null_qAv7B2P2)

### 2 New __Developer Community__ live.

Post you questions here and our LazOP tech support team(or your fellow developer friends) will reply! Find popular integration tricks and articles to help you quickly onboard with Lazada Open API or new features 

![](https://tida.alicdn.com/oss_1659073654462_null_8b7rA3XE)

### 3 Shortcuts for reporting bugs and system issues.

![](https://tida.alicdn.com/oss_1659073836687_null_ZTYqMwAh)

#### A. Create a ticket and report to LazOP for system defects and issues.