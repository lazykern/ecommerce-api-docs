## LPM简介：

Lazada Push Mechanism 是Lazada开放平台向服务商(ISV)/卖家提供订单消息状态推送服务。目前Lazada的订单同步方式采用ISV轮询的机制，存在被限流，低效率浪费资源等问题。配置Lazada Push Mechanism后，订单状态变更会以Http报文的形式推送到ISV设置的回调URL上。

 

**说人话就是，以前是App不停的问开放平台有没有订单，有没有订单，然后有的话就给你特定时间的所有单号。 LPM接入后改成 ：App坐着等待，当有你的订单(订单状态有更新)的时候，开放平台会把你的订单送到你的回调地址上面。**

 

 

 

看到这里你有可能有的问题：

  1. 什么情况下出发推送，推送的状态有哪些？



Lazada推送的状态可以参考Lazada Seller Center 的订单ASC状态。一般比较关心的状态有 ： shipped

delivered, pending, ready_to_ship, unpaid, canceled。 当状态有改变的时候就会推送至少一条消息。

  1. 推送是实时的吗？ 



是的。

  1. 在XXXXX的情况下会推送吗？



除了订单正常的正向推进和逆向推进之外，不要试图使用此消息捕捉其他信息 ： 比如订单信息变化，物流转包等。

如果你还有其他的问题的话，我们不妨带着问题往下看，文末的常见一定会有。

 

 

## 怎么快速接入：

这部分内容包括以下内容：

  1. 准备一个Https回调接口，并了解报文示例内容，签名鉴权，以及推送成功确认与失败补偿机制。
  2. 在app console 上测试回调接口，并提交接入。



### 1\. 准备一个回调接口来接消息：**准备一个Https回调URL，例如：https://www.example.com**

这里你可能有的问题是：

  1. 必须是Https吗？ 答：必须是。
  2. 证书有什么要求吗 ？ 答 ：请各位核对一下自己的CA证书。需要 CA 颁发的证书(自签不行)，需要OV/EV级别的证书，DV的不行。证书扫盲传送门 ：<https://zhuanlan.zhihu.com/p/84047911>
  3. 关于IP白名单/网关流量过滤等需求需要提供推送机IP的：



Lazop提供了请求签名验证来防止回调接口来防止被灌数据，如仍需过滤IP等方式过滤流量，请自行联系阿里云新加坡寻找机房域名/IP, 平台不提供支持。

#### a.了解回调报文示例(这是收到的推送Http回调请求的示例。)：

下面的实例是两条消息，一条正向，一条逆向。第一条消息体从第4行到第21行，第二条消息从第25行到第44行。

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

#Header:Header中关注Authorization的部分，具体内容下面会说

  


#1.正向交易信息示例(下单，付款，发货，收货等正向交易行为产生)

POST /example/uri HTTP/1.1

Host: www.example.com

Content-Type: application/json

Content-Length: 1238

Authorization: 34f7b258df045d4ed9341850ca85b866f34828fd7d51862f11137216294a894c

#正向交易消息体

{

"seller_id":"1234567", #卖家ID

"message_type":0,

"data":{

"order_status":"unpaid", #订单状态

"trade_order_id":"260422900198363", #主单Id

"trade_order_line_id":"260422900298363", #子单id

"status_update_time":1603698638 #订单状态更新时间 时间戳

},

"timestamp":1603766859530, #推送时间 时间戳

"site":"lazada_vn" # 站点信息

}

  


  


#2.逆向交易信息示例(取消，退货退款，等逆向交易行为产生)

POST /example/uri HTTP/1.1

Host: www.example.com

Content-Type: application/json

Content-Length: 1238

Authorization: 34f7b258df045d4ed9341850ca85b866f34828fd7d51862f11137216294a894c

#逆向交易消息体

{

"seller_id":"1000114855", 

"message_type":0,

"data":{

"order_status":"canceled",

"reverse_order_id":"501977696648153", #逆向主单id

"reverse_order_line_id":"502491640048153", #逆向子单id

"status_update_time":1603703663,

"trade_order_id":"252883361348153", #关联正向单id

"trade_order_line_id":"252883361948153" #关联正向子单id

},

"timestamp":1603715010436,

"site":"lazada_vn"

}

你可能会问：

  1. trade_order_id 对应API的哪个字段 ： order_id
  2. 子单号有用吗？ 接口取数据主单号即可。



#### b. 了解签名鉴权Authorizaiton：

签名由HMAC-SHA256算法基于AppKey，AppSecret和消息体生成。用于校验消息的来源以及消息完整性。要求接入方校验签名。

生成后进行HEX编码生成的字符串，接收方应该校验签名，确认消息的完整性：

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

/*

其中Base = {your_app_key} + "{message_body_you_receieved}"

Secret = {your_app_Secret};

*/

Authorization = HEX_ENCODE(HMAC-SHA256(Base, Secret));

#### c. 签名产生Sample Code ：

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

import org.slf4j.Logger;

import org.slf4j.LoggerFactory;

  


import javax.crypto.Mac;

import javax.crypto.spec.SecretKeySpec;

  


/**

* 签名工具类

* @author jianyan

* @date 2020/12/01

*/

public class SignatureUtil {

private static final String HMAC_SHA256 = "HmacSHA256";

  


private static final Logger LOGGER = LoggerFactory.getLogger(SignatureUtil.class);

  


/**

* 产生基于Hmac-SHA256，并经过16进制编码的签名。

* @param base {AppKey} + {messageBody}

* @param secret {AppSecret}

* E.g.: AppKey = 123456, AppSecret = 3412gyo124goi3124

* 收到的消息体Json ：{"seller_id":"1234567", "message_type":0, "data":{...}..}

*

* base = "123456" + "{\"seller_id\":\"1234567\", \"message_type\":0, "data":{...}..}"

* secret = 3412gyo124goi3124

* signature = getSignature(base, secret);

* signature = f3d2ca947f16a50b577c036adecd18bec126ea19cadedd59816e255d3b6104ab

* @return 签名

*/

public static String getSignature(String base, String secret) {

try {

Mac sha256Hmac = Mac.getInstance(HMAC_SHA256);

SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(), HMAC_SHA256);

sha256Hmac.init(secretKey);

return byteArraytoHexString(sha256Hmac.doFinal(base.getBytes()));

} catch (Exception e) {

LOGGER.error("Failed to generate signature");

}

return null;

  


}

  


/**

* 十六进制Encode

* @param bytes

* @return

*/

private static String byteArraytoHexString(byte[] bytes) {

if(bytes == null) {

return null;

}

StringBuilder sb = new StringBuilder();

String stmp;

for (byte aByte : bytes) {

stmp = Integer.toHexString(aByte & 0XFF);

if (stmp.length() == 1) {

sb.append('0');

}

sb.append(stmp);

}

return sb.toString().toLowerCase();

}

}

看到这里你可能会问 ： 

  1. 签名强制吗 ？ 答 ： 不强制，但是墙裂推荐。
  2. 这是干啥的 ？ 我该怎么用这段代码？ 答： 这是一种生成一段字符串的算法，收到消息之后，客户端通过使用相同的算法可以重新生成出一样的字符串，与服务器发来的字符串进行对比即可验证消息的完整性和发出端的身份。



如果你是Java 的话，直接复制代码收到请求后，用这个代码按照说明生成签名，与Header中的Authorization进行比较。

#### d. 了解成功接收与失败重试

**要求客户端接收到数据返回200.OK(HTTP状态码，不是Body内容)确认消息收到** 。 如果超过500ms服务端未收到200确认，服务端则认为消息推送失败。失败后消息会在半个小时后重试推送，一直重试12次直到彻底失败放弃推送。

由于失败重试会放大消息量消耗更多的系统资源，请接入的APP在接收后做好buffer，不要直接处理，减少失败。如果一个APP推送失败率超过50%，推送机会停止对该地址的推送。

看到这里你可能问：

  1. 成功了还会再推吗？ 不会。
  2. 失败了过了半个小时，推过来的状态是最新的吗？ 是的，重试之前会先查一下最新状态。



 

### 2.App Console 自主测试，自主接入

登入open.lazada.com, 登录后进入Push Mechanism选项卡。

#### ![](https://tida.alicdn.com/oss_1666935477843_null_01nTFkUx)

1.填入回调地址，点击Verify。 Verify会自动发送一条测试消息到填入的地址，如果返回符合预期则提示成功。

注：接入人请手动进入后台确认:测试消息，包括确认测试内容，确认签名等，此处的签名是真实的。

2.验证成功后，选择订阅的消息类型，并单击右上角的保存。

 

## 接入之后如何使用，最佳实践(必看)：

某ERP 服务商，现有的订单同步方式是通过每一个小时对服务的所有卖家进行一次/orders/get接口获取订单信息，然后再调用/order/items/get获取订单item详情。效率低，API接口经常被限流，API返回有时候还是空，莫名其妙调用失败， 失败重试又被限流， 陷入绝望。

 

配置回调联调上线之后，现已形成：

 

先消费消息，获取订单号后，对订单调用/order/get 接口查询订单详情，后用订单号调用/order/items/get获取item详情后，再进行业务处理。 每隔6小时进行一次补拉，调用/orders/get接口获取全量订单，比对有消息已经处理过的，将消息中的漏单，进行统一处理。

 

回顾整个过程，该ERP服务商采取的是逐步放量策略 ： 现有拉取频率不降，把消息消费融入业务逻辑中。 即消费消息，也进行拉取。

之后再逐步将补拉时间下降： 从1小时一拉，变成2小时一拉，逐步减少拉取频率。

 

另一ERP服务商听说后，也火速接入了推送，采取了不同的灰度策略 ： 选取部分店铺，他们的订单直接采取消费推送+低频补拉的方式。观察一段时间没有问题后，再进行灰度店铺的不断放量最终到全量店铺。

## 接入常见问题：

### 某个SellerId没有接到推送：

 

推送机在推送前会检查该SellerId 和APPKey在平台的授权关系是否有效，如果出现某个SellerId 没有收到推送的情况，验证一下该Seller和App的Token的有效性。

 

### 是否支持多端推送：

 

单一AppKey只能绑定一个推送地址。 如果Seller订阅了不止一个APP，并且都持有有效授权的话，所有App都可以收到该商家的订单。

 

### 推送只会有订单消息吗？

 

目前上线的只有订单消息，未来几月内会陆续上线，商品审核消息，履约消息，库存更新消息，商家增长消息等。

 

### 你们推送重试12次都失败了，我们如何获取失败的单子？ 有查询接口吗？

 

首先推送对于国内主流云服务器99.8%的单子在1次推送成功，100%的单子在3次内推送成功。没有12次失败的极端情况，由于十二次推送跨越6个小时的时间，及时是突然的网络抖动，也有足够的时间进行恢复，所以12次推送全部都失败的几率非常低。

要是万一呢？ 对于这种方式，我们仍然提供拉取接口给到App，可以进行定时补拉校对。但是对于其QPS的限制要比之前纯拉的时候更加严格。总而言之，我们推荐的消费方式是：以推为主，以拉兜底。

 

### 500ms是如何计算的，网络不好的时候经常超过500Ms怎么办 ？

 

不要同步消费订单消息，存入buffer中再消费。

基于目前观察，国内主流云服务器RT在200ms以内。对于抖动情况，有12次重试补偿机制。 

 

### 后续会对orders/get/限流吗，什么时候限流？

 

会，目前初定时间在春节后。

 

### 子订单Id有用吗？ 目前只用主单id可以吗？ 

 

是可以的，目前查询接口以及item查询接口都是用主单id

 

### 回调地址配置之后可以改吗？ 需要测试回调和生产回调区分吗？

 

首先回调地址可以改。测试回调的必要性不大，因为你们订单现有链路是以拉取的方式进行，与这个回调完全隔离，可以直接使用一个回调地址。

 

### 推送有重复 ？

如果你发现了大量重复，请核对一下重复消息中的trade_order_line_id字段是否一致。因为推送是以子单维度区分的。

推送服务是：至少一次投递 的，少量重复属于正常，请幂等消费。

 

### 我们签名用的你们提供的例子，但是签名就是对不上

很多童鞋都反应我们给的sample code有问题。如果下面所有的方式你都自查过了，仍然有问题的再来和我们交流。

  1. 不要将签名校验逻辑和业务逻辑耦合，我们推荐的签名校验设计方式可以采用责任链模式，签名校验作为责任链中的一环。很多童鞋，是用类库已经将body中的字段进行映射形成对象之后，再去序列化对象解析的方式，这种方式会依赖对象解析顺序，而且这种解析因解析的三方库而异，容易出现问题。 并且，这种写法将签名逻辑与业务逻辑，消息体深度耦合，当消息有更新迭代的时候，比较麻烦。
  2. 1没问题的话关注一下取到的AppSec，如果还有问题，重置一下AppSect.



 

### 我们收到了很久之前的订单/订单数据延迟

这种情况有可能是接口延迟造成的失败，数据大量补偿丢失实时性的情况。部分国内部署的服务器存在这种问题，可以考虑转发。

##  

## 商品相关Push消息??：

## 商品新增:

 

属性| 值| 解释  
---|---|---  
msg_type| 3| 消息体中用于区分消息类型的字段  
重试次数| 12| 推送失败后重试的次数  
重试间隔| 30分钟| 每次重试的间隔  
  
PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

seller_id : "1234567", //卖家id

message_type : 3, //消息类型

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

"action":"EDITED_UPDATED", //操作类型 PUBLISHED(商品发布), EDITED_INSERTED(已有商品增加SKU)

"status_update_time":1623238942696,

"timestamp" : 1606130634,

"site" : "lazada-sg"

}

#：action字段是指本次新增的渠道标记。 在商品新增中一共有两种渠道标分别是 : PUBLISHED （商品发布渠道）,EDITED_INSERTED (已有商品新增SKU)

 

## 商品删除：

属性| 值| 解释  
---|---|---  
msg_type| 5| 消息体中用于区分消息类型的字段  
重试次数| 12| 推送失败后重试的次数  
重试间隔| 30分钟| 每次重试的间隔  
  
PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

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

"action": "EDITED_DELETED", //操作类型 DELETED(商品删除) EDITED_DELETED(已有商品删除sku)

"status_update_time": 1623230820094

},

"timestamp": 1623230820,

"site": "LAZADA_SG"

}

#：action字段是指本次新增的渠道标记。 在商品新增中一共有两种渠道标分别是 : DELETED （商品删除）,EDITED_DELETED (已有商品删除SKU)

 

## 商品编辑:

属性| 值| 解释  
---|---|---  
msg_type| 5| 消息体中用于区分消息类型的字段  
重试次数| 12| 推送失败后重试的次数  
重试间隔| 30分钟| 每次重试的间隔  
  
PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

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

"action": "EDITED_UPDATED",//除sku新增删除之外的一切变更

"status_update_time": 1623232569146

},

"timestamp": 1623232569,

"site": "LAZADA_SG"

}

#action只有一种

#除商品新增和商品删除之外的所有商品更新都会触发此消息