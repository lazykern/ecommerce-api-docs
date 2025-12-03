## **1\. Workflow**

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误1_1721701641867__UQQr.jpg)

isv should use long-pulling to make message push to seller realtime.

## **2 Messages**

### **2.1 GetMessages**

PATH /im/message/list

#### **Request**

name | Type | Required | Demo Value | rule | Description
---|---|---|---|---|---
session_id | String | true | 100094063_2_1011822749_1_103 |  | session id
start_time | long | true | 1555937067614 | when request the first page pls input current timestamp，get the next page pls input previous page response field next_start_time | begin timestamp
last_message_id | String | false | 24jFlAu0BtRbP47190 | it could be null when get the first page, get the next page pls input previous page response field last_message_id | 
page_size | int | true | 20 | limit 20 | page size

#### **Response**

  

name | Type | Demo Value | Description
---|---|---|---
has_more | Boolean | true | Identifies whether there has more page，use this field to determine whether you need to continue to pull
next_start_time | Long | 1624862839559 | the begin timestamp of next page，When pulling the next page, it needs to be passed in as an input parameter
last_message_id | String | 24jFlAu0BtRbP47190 | The ID of the last message on this page. When pulling the next page, it needs to be passed in as an input parameter
message_list | Object[] | [] | 
|-message_id | String | 1zYOS7N0cuIqw96026 | message id
|- content | String | {\"txt\":\"你好\",\"translatText\":\"hello\"} | message content in json format
|- from_account_id | String | 1891549323 | sender account id
|-from_account_type | Number | 1 | sender account type, 1 represents the buyer, 2 represents the seller
|-send_time | long | 1596550789323 | message send timestamp
|-template_id | Number | 1 | message template id, 1: normal text message, 3: picture message, 4: emoji message, 10006: represents item message, 10007: represents order message 10008: represents voucher message 10010: represents invite to follow message 6: represents video message, use this API to get video paly url
|-to_account_type | Number | 2 | receiver account type, 1 represents the buyer, 2 represents the seller
|-to_account_id | String | 231135951 | receiver account id
|-type | Number | 1 | 1: message come from user 2: message come from system
|- process_msg | String | NOTE: The message has not been sent. Please be polite and aware that you are required to comply with local laws & policies | If this field is not empty, it means that this message has not passed the security interception verification, which means that this message is only visible to the seller, and the ISV needs to display this prompt information to the seller on the screen
|-status | Number | 0 | 0: message status normal 1: message has been recalled by sender
|- auto_reply | Boolean | false | true: it is a auto reply message. false: it is not a auto reply message
|-site_id | String | SG | country code

  

### **2.2 SendMessage**

  

PATH /im/message/send

#### **Request**

name | Type | Required | Demo Value | rule | Description
---|---|---|---|---|---
template_id | Number | true | 1 |  | message template id, 1: normal text message 3: picture message 4: emoji message 10006: item message 10007: order message 10008: voucher message 10010: invite buyers to follow the store 6: video message, use this API to upload video (The video duration is greater than 3s and less than 180s)
session_id | String | true | 100094063_2_1011822749_1_103 |  | session id
txt | String | false | test message content |  | 
img_url | String | false | https://xxx.jpg |  | 
width | Number | false | 10 |  | 
height | Number | false | 20 |  | 
item_id | String | false | 1762013406 |  | 
sku_id | String | false | 89123912 |  | not support
order_id | String | false | 1762013406 |  | 
promotion_id | String | false | 91471122606001 |  | 
video_id | String | false | 3443534 |  | 

  1. text message example

template_id: 1, session_id: xxxxxx, txt: test

  1. picture message example

template_id: 3, session_id: xxxxxx, imgUrl: <https://sg-live.slatic.net/other/im/7e7a4185f2e3f27e071621067f321587.png,> width: 445, height: 168

  1. emoji message example

template_id: 4, session_id: xxxxxx, txt: [confused]

  1. item message example

template_id: 10006, session_id: xxxxxx, itemId: 1762013406

  1. order message example

template_id: 10007, session_id: xxxxxx, orderId: 1762013406

  1. Invite buyers to follow the store message example 

Use this [API](<https://open.lazada.com/doc/api.htm?spm=a2o9m.11193495.0.0.74e8130cEbcqx4#/api?cid=2&path=/shop/follow/status/batch/query>) to determine whether the buyer is a shop fan

template_id: 10010, session_id: xxxxxx

  1. voucher message example

Use this [API](<https://open.lazada.com/doc/api.htm?spm=a2o9m.11193495.0.0.74e8130cEbcqx4#/api?cid=30&path=/promotion/vouchers/get>) to get voucher list

template_id: 10008, session_id: xxxxxx, promotion_id: 91471122422003

  1. video message example

Use this [API](<https://open.lazada.com/doc/api.htm?spm=a2o9m.11193487.0.0.3ac413felykKHs#/api?cid=32&path=/media/video/block/create>) to upload video

template_id: 6, session_id: xxxxxx, video_id: 3334313, width:220, height: 720

#### **Response**

name | Type | Demo Value | Description
---|---|---|---
message_id | String | 21d0fLE0BtkPL79071 | message id
error_code | String |  | 0
error_msg | String |  | 

  

### **2.3 RecallMessage**

PATH /im/message/recall

#### **Request**

name | Type | Required | Demo Value | rule | Description
---|---|---|---|---|---
session_id | String | true | 100094063_2_1011822749_1_103 |  | conversation id
message_id | String | true | 21d0fLE0BtkPL79071 | 1）Cannot be recalled more than two minutes since the message has been sent 2）system message could not be recalled | the id of message that need to be recalled

#### **Response**

name | Type | Demo Value | Description
---|---|---|---
error_code | String |  | 0
error_msg | String |  | 

  

## **3 Session**

  

### **3.1 GetSessionList**

PATH /im/session/list

#### **Request**

name | Type | Required | Demo Value | rule | Description
---|---|---|---|---|---
start_time | Long | true | 1618991702208 | when pull first page pls input current timestamp， when pull next page pls input last page response field next_start_time | timestamp
last_session_id | String | false | 100094063_2_1011822321_1_103 | it could be null when pull first page，when pull next page pls input last page response field last_session_id | The id of the last conversation on the previous page
page_size | Number | true | 20 | limit 20 | page size

#### **Response**

name | Type | Demo Value | Description
---|---|---|---
has_more | boolean | true | Identifies whether there has more page，use this field to determine whether you need to continue to pull
next_start_time | String | 1618971891953 | the begin timestamp of next page，When pulling the next page, it needs to be passed in as an input parameter
last_session_id | String | 100094063_2_1011822321_1_103 | The last session id on this page, it needs to be passed in as an input parameter when pulling the next page
session_list | Object[] | [] | 
|-session_id | String | 100094063_2_1011822749_1_103 | session id
|-summary | String | test message | the summary of session
|-title | String | wangermazi | user nick name
|-head_url | String | https://sg-live-02.slatic.net/p/0dc6fb4898f7e991bf44c45471dca9c9.jpg | user head picture url
|-last_message_id | String | 21cZj5X0BtkHT42670 | last message id
|-last_message_time | Long | 1621495731445 | last message born time
|- buyer_id | Long | 1011822749 | buyer userId
|-unread_count | Number | 8 | unread count
|-self_position | Long | 1621495410182 | self read time
|-to_position | Long | 1621495410182 | The other party's read time
|-tags | List<String> | ["official"] | session tag
|-site_id | String | SG | country code

  

### **3.2 GetSessionDetail**

  

PATH /im/session/get

#### **Request**

name | Type | Required | Sample | rule | Description
---|---|---|---|---|---
session_id | String | true | 100094063_2_1011822749_1_103 |  | session id

#### **Response**

name | Type | Demo Value | Description
---|---|---|---
|-session_id | String | 100094063_2_1011822749_1_103 | session id
|-content | String | test message | session summary
|-title | String | wangermazi | buyer nick name
|-head_url | String | https://sg-live-02.slatic.net/p/0dc6fb4898f7e991bf44c45471dca9c9.jpg | buyer head url
|-last_message_id | String | 21cZj5X0BtkHT42670 | last message id of session
|-last_message_time | Long | 1621495731445 | last message send time of session
|- buyer_id |  | 1011822749 | buyer user id
|-unread_count | Number | 8 | unread count
|-self_position | Long | 1621495410182 | self read time
|-to_position | Long | 1621495410182 | The other party's read time
|-tags | List<String> | ["official"] | session tag
|-site_id | String | SG | country code

  

### **3.3 ReadSession**

PATH /im/session/read

#### **Request**

name | Type | Required | Sample | rule | Description
---|---|---|---|---|---
session_id | String | true | 100094063_2_1011822749_1_103 |  | session id
last_read_message_id | String | true | 1621498479918 |  | last message id of user readed

#### **Response**

name | Type | Demo Value | Description
---|---|---|---
data | Object | { "success": true, "err_code": "0", "err_message": "SUCCESS" } | 

  

### **3.4 OpenSession**

PATH /im/session/open

When the order created by the buyer in the store is not more than 7 days old, the seller can initiate a conversation. Use this API to get session_id, and then invoke SendMessage API to send message.

#### **Request**

name | Type | Required | Sample | rule | Description
---|---|---|---|---|---
order_id | Long | true | 232432432423 |  | orderId

#### **Response**

name | Type | Demo Value | Description
---|---|---|---
session_id | String | 100148681_2_500210868055_1_103 | unique id of a conversation

## **4 Push**

### **4.1 Message**

  

message body

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"session_id" : "100094063_2_1011822749_1_103",

"message_id": "1zYOS7N0cuIqw96026", //messageId use to trace problem

"content": "{\"txt\":\"hello world!\"}",

"from_account_id": "1891549323", 

"from_account_type": 1, // 2=seller 1=buyer

"send_time": 1596550789323, 

"template_id": 1, // 1=txt card 2=SystemTxt 3=ImageCard

"to_account_id": "231135951", 

"to_account_type": 1, // 2=seller 1=buyer

"type": 1, // 1=userSend 2=systemSend

"site_id": "SG", // country code

"process_msg": "xxxx", // If this field is not empty, it means that this message has not passed the security interception verification, which means that this message is only visible to the seller, and the ISV needs to display this prompt information to the seller on the screen

"auto_reply": false, // true: it is a auto reply message, false: it is not a auto reply message

"status": 0 // 0: message status normal, 1: message has been recalled by sender

}

  

### **4.2 Session Update**

  

message body

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"sync_type": "SESSION_UPDATE", // 事件类型

"user_account_id": "100094063", // 卖家账号id

"user_account_type": 2, // 2=seller 1=buyer

"session_id": "100094063_2_1011822749_1_103",

"unread_count": 0, // 未读数

"to_position": 1596550789323, // 对方已读时间

"self_position": 1596550789323, // 己方已读时间

"site_id": "SG"

}

  

## **5\. MessageConent**

  

### **templateId=1 normal text**

normal text: {"txt":"${txt}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721702410874__NC1v.jpg)

crossborder seller normal text: 

{"translateTxt":"${translateTxt}","txt":"${txt}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721702441218__nzCg.jpg)

### **templateId=2 system message**

{"txt":"${txt}","recallContent":"${recallContent}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706116926__WdSn.jpg)

message recall: 

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706136733__u7Ap.jpg)

### **templateId=3 picture**

{"imgUrl":"${imgUrl}","osskey":"${osskey}","width":"${width}","height":"${height}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706153383__x3jY.jpg)

### **templateId=4 emoji**

emoji: {"imgUrl":"${imgUrl}","smallImgUrl":"${smallImgUrl}","txt":"${txt}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706170824__BgbM.jpg)

#### **tab1**

icon：<https://sg-live-01.slatic.net/other/im/dc9375aeaba4435212341c2c71bb2c52.png>

  1. happy

{

"txt": "[happy]",

"imgUrl": "<https://sg-live.slatic.net/original/0e048d1c6d42835cdc386241b2a855c8.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/30ff084a270eae973a02ec74e216ba51.png">

}

  1. veryhappy

{

"txt": "[veryhappy]",

"imgUrl": "<https://sg-live.slatic.net/original/bc42a3eff1a2ea9cda78e70ba85ca600.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/bfc697859931b2257f956680bff82a47.png">

}

  1. laughing

{

"txt": "[laughing]",

"imgUrl": "<https://sg-live.slatic.net/original/d66d57245a5a53bfce17c7ee9f305dea.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/0bbb09ff7d823c4566044b615c0c214c.png">

}

  1. smirking

{

"txt": "[smirking]",

"imgUrl": "<https://sg-live.slatic.net/original/35f56b5e6b4cb8cd7ece01a486990758.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/f62c5bdb92d703450d58733928a5e08e.png">

}

  1. inlove

{

"txt": "[inlove]",

"imgUrl": "<https://sg-live.slatic.net/original/c1af284b49ca2855b6250da001eb86ff.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/87b1950d4a6f7e02d08065f2d2e9189c.png">

}

  1. thumbsup

{

"txt": "[thumbsup]",

"imgUrl": "<https://sg-live.slatic.net/original/41bbcbce0b13176ad4cfa9781a935f30.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/f82b6725f3618cb4e9a90a35d043a75f.png">

}

  1. surprised

{

"txt": "[surprised]",

"imgUrl": "<https://sg-live.slatic.net/original/ed3e32239214313a5f88b7f5522e8009.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/81272c3b99b9ae6b719647ec68ab222d.png">

}

  1. shocked

{ 

"txt": "[shocked]",

"imgUrl": "<https://sg-live.slatic.net/original/e795a481618af187f6b7df0f68feb527.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/b96d057d60b5d4df9471f6d021b10830.png">

}

  1. sad

{ 

"txt": "[sad]",

"imgUrl": "<https://sg-live.slatic.net/original/1ba2df5142564a44966551027b9c6bbc.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/a17e7b66e101f6eafff7ea27f63f31e6.png">

}

  1. crying

{

"txt": "[crying]",

"imgUrl": "<https://sg-live.slatic.net/original/6c7e93fd7740f72bfbccff77504a30d9.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/b37b721709875f5c4e245cf331da2987.png">

}

  1. confused

{ 

"txt": "[confused]",

"imgUrl": "<https://sg-live.slatic.net/original/1eca1d0994cb93f2df2408ffa749c18d.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/2e13c266a9e7fdd4d2a840e2a1939dd9.png">

}

  1. shy

{ 

"txt": "[shy]",

"imgUrl": "<https://sg-live.slatic.net/original/cc2b0c1db5ae9014de532155fb114a3e.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/5986d2f2c30c09a981bf971485285aeb.png">

}

  1. angry

{

"txt": "[angry]",

"imgUrl": "<https://sg-live.slatic.net/original/3825aa88b59a9209053655fede4d1131.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/633bee4754d1e298dbf3a38053c75dd5.png">

}

  1. disgust

{

"txt": "[disgust]",

"imgUrl": "<https://sg-live.slatic.net/original/5b23d7bee1985418de4a084e72c16e47.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/e398d006343bfdf2efd665ac726604b3.png">

}

  1. heart

{

"txt": "[heart]",

"imgUrl": "<https://sg-live.slatic.net/original/9715a92a20bc87a07988eb4825bf15ca.png",>

"smallImgUrl": "<https://sg-live.slatic.net/original/012b57eeed968cf2787cd944ab733427.png">

}

#### **tab2**

icon：<https://sg-live.slatic.net/other/im/edd7b121015dfc3743316c1e132cecb7.png>

  1. thank you

{ 

"txt": "[thank you]",

"imgUrl": "<https://sg-live.slatic.net/other/im/ac34173dd76c7b099064aa0859d9aeb8.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/55db78f572521414ef5b98c1dfddf63f.png">

}

  1. cheer up

{

"txt": "[cheer up]",

"imgUrl": "<https://sg-live.slatic.net/other/im/901116c5359491b3bfe57fdb299f893f.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/5e917d78922de317df3a25c2a3c13aa6.png">

}

  1. red pocket

{

"txt": "[red pocket]",

"imgUrl": "<https://sg-live.slatic.net/other/im/2ef57a7e72c344f5347da78efc704451.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/72c2d2a7da6b3481c9c19fe62fb17a3d.png">

}

  1. yummy

{

"txt": "[yummy]",

"imgUrl": "<https://sg-live.slatic.net/other/im/122730d703f7ca3b27c73a97788eef9a.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/cb9f07cb5c7f6801ea1ce830d3397bd4.png">

}

  1. dance

{ 

"txt": "[dance]",

"imgUrl": "<https://sg-live.slatic.net/other/im/a87ad57918b0d593fbd97381afcbe5cf.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/c90c72a4a3f2fd71514cde42ee91a6bb.png">

}

  1. bye

{

"txt": "[bye]",

"imgUrl": "<https://sg-live.slatic.net/other/im/2a693f4624ae1491d6ba5743fd8a3ee9.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/94cbeb5083a622e4d400e489371bbc14.png">

}

  1. gift

{

"txt": "[gift]",

"imgUrl": "<https://sg-live.slatic.net/other/im/d9155fd8aff7b428d17c47d5fd8e9642.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/36d49a2e1eb206160f7de6a4d1000e73.png">

}

  1. thirsty

{

"txt": "[thirsty]",

"imgUrl": "<https://sg-live.slatic.net/other/im/c999fa373bab823d8c3f1256d0e810cd.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/6eaa18380e90d049228221d6425f8a7d.png">

}

  1. sleepy

{ 

"txt": "[sleepy]",

"imgUrl": "<https://sg-live.slatic.net/other/im/8cef0edb766d587e2cfd29c67e6a48e4.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/a278243d7012ae9bef524c11fc56ded6.png">

}

  1. fountain

{ 

"txt": "[fountain]",

"imgUrl": "<https://sg-live.slatic.net/other/im/3d09b64b8fb3599e11f38602a080fc3e.gif",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/ee2d4cacb05ae9b26f56052d9bd782cc.png">

}

#### **tab3**

icon：<https://sg-live.slatic.net/other/im/daa33e1afebefd388e616e82a7dc2071.png>

  1. Lazzie yeah

{

"txt": "[Lazzie yeah]",

"imgUrl": "<https://sg-live.slatic.net/other/im/9506b5dfcad5de538d711dca50b379f3.png",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/f4ed96d29cbd41f16c30ec712c5cd9db.png">

}

  1. Lazzie gift

{

"txt": "[Lazzie gift]",

"imgUrl": "<https://sg-live.slatic.net/other/im/9f13596921fa5b2000a8266b557018a9.png",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/b079af4db32da2e90ef8e394018958f3.png">

}

  1. Lazzie heart

{

"txt": "[Lazzie heart]",

"imgUrl": "<https://sg-live.slatic.net/other/im/b8fb565cb055897c3029b7cd011c9a6b.png",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/dfb9e3ffcb5f9ee243276d4ad33eeb57.png">

}

  1. Christmas

{

"txt": "[Christmas]",

"imgUrl": "<https://sg-live.slatic.net/other/im/1461eb044cbe81614582a83e8efa7bf7.png",>

"smallImgUrl": "<https://sg-live.slatic.net/other/im/ca0af297239dd70e507fbd80ccc28f84.png">

}

### **templateId=10006 item message**

{"itemId":"${itemId}","price":"${price}","oldPrice":"${oldPrice}","actionUrl":"${actionUrl}","discount":"${discount}","iconUrl":"${iconUrl}","title":"${title}","skuId":"${skuId}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706218894__lQPD.jpg)

### **templateId=10007 order message**

{"title":"${title}","content":"${content}","status":"${status}","iconUrl":"${iconUrl}","orderId":"${orderId}","actionUrl":"${actionUrl}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706235274__Shck.jpg)

  

### **templateId=10008 coupon message**

{"period":"${period}","appBuyerUrl":"${appBuyerUrl}","sellerMasterUserId":"${sellerMasterUserId}","voucherType":"${voucherType}","discountUnit":"${discountUnit}","cardType":"${cardType}","actionUrl":"${actionUrl}","discount":"${discount}","discountAmount":"${discountAmount}","title":"${title}","pcSellerUrl":"${pcSellerUrl}","pcBuyerUrl":"${pcBuyerUrl}","sellerId":"${sellerId}","minOrderAmount":"${minOrderAmount}","voucherId":"${voucherId}","action":"${action}","appSellerUrl":"${appSellerUrl}","actionCode":"${actionCode}","currency":"${currency}","iconUrl":"${iconUrl}","currencyCode":"${currencyCode}","desc":"${desc}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706250420__fjZP.jpg)

### **templateId= 10010 follow message**

The seller sends this message to guide the buyer to become a fan of the store

{"sellerId":"${sellerId}","mallIconUrl":"${mallIconUrl}","actionUrl":"${actionUrl}","action":"${action}","sellerUserId":"${sellerUserId}","targetUserId":"${targetUserId}","shopId":"${shopId}","iconUrl":"${iconUrl}","title":"${title}","desc":"${desc}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706265410__CG3z.jpg)

  

### **templateId=10015 auto reply message**

{"txt":"${txt}","sellerId":"${sellerId}","sellerMasterUserId":"${sellerMasterUserId}","buyerUserId":"${buyerUserId}","actionSize":"${actionSize}","action1Txt":"${action1Txt}","action1Code":"${action1Code}","action2Txt":"${action2Txt}","action2Code":"${action2Code}","action3Txt":"${action3Txt}","action3Code":"${action3Code}","action4Txt":"${action4Txt}","action4Code":"${action4Code}","action5Txt":"${action5Txt}","action5Code":"${action5Code}","action6Txt":"${action6Txt}","action6Code":"${action6Code}","action7Txt":"${action7Txt}","action7Code":"${action7Code}","action8Txt":"${action8Txt}","action8Code":"${action8Code}","action9Txt":"${action9Txt}","action9Code":"${action9Code}","action10Txt":"${action10Txt}","action10Code":"${action10Code}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706284655__cQ0a.jpg)

  

### **templateId=10011 Refund order card**

when buyer refun his order, seller will receive this msg card.

{ "subOrderIcon" : "${subOrderIcon}","subOrderSKU" : "${subOrderSKU}", "orderTotalCount" : "${orderTotalCount}", "orderTotalPrice" : "${orderTotalPrice}", "refundOrderDate" : "${refundOrderDate}", "viewUrl4Seller" : "${viewUrl4Seller}", "subOrderTitle" : "${subOrderTitle}", "title" : "{\"${language}\":\"${title}\"}", "subOrderPriceUnit" : "${subOrderPriceUnit}", "refundOrderReason" : "${refundOrderReason}", "viewAPPUrl4Buyer" : "${viewAPPUrl4Buyer}", "viewAPPUrl4Seller" : "${viewAPPUrl4Seller}", "refundOrderId" : "${refundOrderId}", "sellerId" : "${sellerId}", "subOrderCount" : "${subOrderCount}", "subOrderPrice" : "${subOrderPrice}", "buyerUserId" : "${buyerUserId}", "orderTotalPriceUnit" : "${orderTotalPriceUnit}", "viewUrl4Buyer" : "${viewUrl4Buyer}"}

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706301054__Lr50.jpg)

  

### **templateId=6 Video message**

message content like this:

{"imgUrl":"<https://sg-live.slatic.net/other/im/fff286502dddb18c004ce247ea87f387.png","txt":"normal> video.mp4","videoDuration":3,"videoUrl":"","width":720,"videoId":"30071484392","height":1280}

use this [API](<https://open.lazada.com/doc/api.htm?spm=a2o9m.11193487.0.0.3ac413felykKHs#/api?cid=32&path=/media/video/get>) to get video play url.

  

## **6 Session validity**

1) The conversation could be initiated by the buyer, and the seller can initiate the conversation if buyer has order within 7 days;

2) The conversation is within the validity period. If the buyer does not reply to the message within a day, the seller can only send a maximum of 5 messages to the buyer; if the buyer has a reply, there is no limit on the number of times;

Session aging rules:![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误_1721706343565__Tt6E.jpg)

## **7 API best practices**

/im/message/list | Please do not poll call these two interfaces, because there is a PUSH channel, the call volume of these two interfaces should be very low, if an ISV polling call is found, the API permissions will be immediately reclaimed.Best practice: After the seller successfully authorizes the ISV, it will trigger the synchronization of historical conversations and historical messages on the platform side (synchronize the conversations within one month and the total number does not exceed 3000, and each conversation synchronizes the messages within one month). It is recommended that ISV use these two interfaces to pull the seller’s historical conversations and historical messages within 10-15 minutes after the seller’s authorization is completed. Do not call the interface after the authorization is completed, because the platform side has not yet synchronized the historical data.
---|---
/im/session/list | 
/im/message/send | The seller responds to the message in the ISV system, that is, the interface is called
/im/session/get | When the ISV receives the PUSH notification, it judges whether the session exists locally according to the session_id field in the message body, and if it does not exist, the interface is called to synchronize the session.
/im/session/read | When the seller clicks on an unread conversation in the ISV system, this interface is called.The role of this interface: 1) The read status of the session is synchronized to the ASC, so that when the seller enters the ASC, the status of the session seen is consistent with the ISV system 2) Synchronize the read status of the seller session to the buyer
PUSH Message | After receiving the PUSH, the ISV should put the message body into its own MQ queue, and then give the pusher a response, and try to avoid synchronization after receiving the PUSH.In order to ensure the efficiency and sequence of MQ consumption, it is recommended that ISV set up multiple partions in the MQ queue and hash to different partions according to the session ID.
PUSH Session Update | when buyer read conversation or seller read conversation on ASC, ISV will receive the PUSH

  

**Message recall**

1) When seller recall the message, the ISV will receive two PUSHs, one is the message that has been recalled (status is 1), and the other is the system message.

2) When buyer recall the message, the ISV will receive two PUSHs, one is the message that has been recalled (status is 1), and the other is the system message.

Therefore, the ISV needs to de-duplicate according to the sessionId + messageId. After receiving the PUSH, if the messageId already exists in the database, the status of the message should be updated.