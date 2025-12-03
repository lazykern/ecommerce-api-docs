### 一、概述

该文档只适用于中国区大陆卖家。

先实现和对接能够满足业务基本需求的接口，然后再实现优化功能。

为了让一些当前实操中尚没有组包流程的中小商家更容易接受，我们暂时不做小包-大包-交接单的三层关系，只实现小包-大包的关联关系，也就是说可以认为，一个交接单只有一个大包，下文中提到的交接单其实基本等同于大包。

#### 1、大包创建

/logistics/cnpms/bigbag/commit

**（1）接口说明**

通过该接口提交大小包关系以及揽收、退货地址。

如选择集货点组包即type:pickup_collection，则collectionInfo必填且非空，pickUpCode的取值通过集货点接口查询

菜鸟侧会对提交的小包做有效性校验，调用方应至少实现以下校验，减少以商家组包后的额外操作：

  * 参加组包的小包必须已经成功RTS；
  * 参加组包的小包状态不为取消状态；
  * 目前大件海运包裹不提供官方揽收服务，应排除FM49的包裹。

此外，为避免揽收CP拒收，应对大包内的小包件数和大包重量作控制。

**（2）接口请求参数及响应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Fbigbag%2Fcommit>

注：

揽收type新增选项：self-send，如果是自行送货的商家，可以回传该类型

pickup type | 组包页面可以选择的揽收方式 | 说明
---|---|---
cainiao_pickup(菜鸟揽收) | 免费揽收 | 菜鸟揽收，包括免费揽收和付费揽收，这两种都是上门揽收
付费揽收 |  | 
pickup_collection(集货) | 自送至集货点 | 集货是菜鸟在义乌，深圳，和泉州开的几个集货点，针对集货点附近的小商家，未达到免费揽收的条件，可以把货物自行送到这几个集货点，我们会从集货点统一送到当地的分拨中心
self_send（自送） | 自送至分拨中心 | 自送是商家您使用自己的工具（非第三方快递公司）将货物自行送至对应的分拨中心
self_post(自寄) | 快递至分拨中心 | 自寄是商家您这边自己找的快递，寄到我们的分拨中心

 

2）新增/修改字段

Name | Type | Required | Demo Value | Description
---|---|---|---|---
courierCompany | String | false | 申通 | 快递公司。可不回传
receiverPhone | String | false | 1888888888 | 收件人手机号。 尽量回传，部分快递公司物流信息查询需要使用手机号，不回传可能会导致查询不到物流信息，自寄包裹无法上网从而影响时效
fmReverseOption | String | false | 1 | 退件方式 1-退回，2-销毁
sellerTrackingNumber | String | false | B20127000438 | 大包号/快递单号 当pickuptype=自寄时，使用则该字段回传快递单号

 

#### 2、大包取消

/logistics/cnpms/bigbag/cancel

**（1）接口说明**

调用方通过该接口取消大包。即使商家没有取消大包，如果72小时后没有发生揽收，菜鸟系统在也会主动发起关单。

**（2）****接口请求参数及响应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Fbigbag%2Fcancel>

#### 3、查询大包详情

/logistics/cnpms/bigbag/query

**（1）接口说明**

调用方通过该接口获取大包的履行状态，以及重量、费用等信息。

菜鸟还可以提供页面的方式展示大包的履行状态，如果需要可以与对接的同学联系。

**（2）****接口请求参数及响应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Faddress%2Fquery>

#### 4、获取面单PDF文件数据

/logistics/cnpms/bigbag/lable/getPdf

**（1）接口说明**

调用方通过该接口获取大包面单PDF数据的字节流信息

**（2）****接口请求参数及响应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Fbigbag%2Flable%2FgetPdf>

#### 5、商家授权

/logistics/cnpms/account/bind

**（1）接口说明**

调用方通过该接口进行商家授权，实现跨店铺组包

**（2）****接口请求参数及响应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Faccount%2Fbind>

#### 6、地址查询

/logistics/cnpms/address/query

**（1）接口说明**

调用方通过该接口查询菜鸟标准地址库id，用于大包创建接口时指定地址id，对应的参数为returnInfo.addressId和pickupInfo.addressId

**（2）****接口请求参数及响应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Faddress%2Fquery>

#### 7、大包更新(暂时不要用)

/logistics/cnpms/bigbag/update

**(1) 接口说明**

通过该接口更新实现对应大包新增小包的功能，实现大小包关系的更新绑定

**(2) 接口请求参数及相应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Fbigbag%2Fupdate>

注：

1、该接口，仅仅实现更新大包的大小包关系绑定功能

2、只允许在已提交、等待分配运单号，待揽收三个大包状态下进行更新操作

#### 8、集货点查询

/logistics/cnpms/bigbag/querycollection

**(1) 接口说明**

通过该接口查询可用集货点信息

**(2) 接口请求参数及相应内容**

<https://open.lazada.com/apps/doc/api?path=%2Flogistics%2Fcnpms%2Fbigbag%2Fquerycollection>

### 五、FAQ

#### 1、接口怎么对接？

文档中涉及的接口均通过Lazada开放平台进行对接、调用，Lazada开放平台的相关介绍及接口对接的详细方法见：

[ https://open.lazada.com/apps/doc/doc?nodeId=10534&docId=108130](<https://open.lazada.com/apps/doc/doc?nodeId=10534&docId=108130>)

#### 2、商家授权接口是做什么用的？需要在什么时候调用？

用于跨店铺组包场景，在调用大包创建接口时，系统会校验是否存在跨店铺组授权关系。

对于存量（已经授权）的商家，可在初次调用大包创建接口之前调用该接口进行批量授权，后续有新增授权时，再进行调用。

#### 3、appUserKey字段填什么？

接口里面的这个appUserKey并不是平台分配的，是ISV那边的一个值（这个值需要确保在ISV那里唯一，可以是商家在ISV那里的唯一ID）。

比如说有A、B、C、D四个商家。创建大包时A这个商家允许组B、C、D的包裹。那实际调用的接口逻辑为：

1、调商家授权接口，将B、C、D给A授权，appUserKey传A商家在你们那里的唯一值，我们这边记录授权关系。

2、以A商家为主体创建大包，大包中包含了A、B、C、D四个商家的包裹，调大包创建接口时，也向我们传这个appUserKey，我们在校验的时候就能知道A商家是允许组B、C、D的包裹

另：其实appUserKey也可以理解为分组的概念，表示一组授权关系

#### 4、client字段填什么？

接口调用方名称，不做强校验

ISV：ISV英文或拼音名称、商家ERP：SELLER-商家英文或拼音名称

#### 5、我是免费Milkrun的商家，我应该怎么办？

开放平台中传递的sellerID判断是我们判断要把订单路由给免费揽收CP还是收费揽收CP的一个参数。所以如果你这边享受免费揽收服务，请在对接的时候尽量主动告知该情况，并把你们会在请求时使用到的sellerID清单提供给我们。

#### 6、addressID字段填什么？

addressID指的是商家地址所对应的地址库ID，我们需要根据这个ID判断揽收地址是否在揽收范围内，以及在哪个揽收CP的揽收范围内。

可通过地址查询接口进行查询（/logistics/cnpms/address/query）

#### 7、我们的实操流程中需要直接生成面单，不能调取你们的面单怎么办？

不同的揽收服务，可能解决的途径不同:

i.如果是免费揽收，可以通过把大包创建后我们返回的大包号和对应的条码展示在你们自己发货标签上明显位置，同时在单号和条码上方标注“揽收扫描条码”，方便司机扫描；也可以参考收费CP场景下的解决方案；

![](https://tida.alicdn.com/oss_1661505249799_null_3qgRfL7U)

ii.如果是收费揽收，可以先创建大包，调用面单PDF文件，然后使用更新接口更新大小包关系。