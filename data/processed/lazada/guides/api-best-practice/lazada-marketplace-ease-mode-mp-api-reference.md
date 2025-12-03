# 什么是Marketplace Ease Mode （MP商家半托管）

Marketplace Ease is a program in which merchants provide product supply prices, platform sales and order fulfilments by themselves. Orders payment are settled based on the product supply price, without any additional commissions or fees except during Mega Campaigns.

MarketPlace商家半托管模式是一个商家提供产品供货价、完成订单履约，Lazada平台制定销售价和负责营销的模式。根据产品供应价格结算，除了在Mega Campaign期间，没有额外的佣金或费用。

# MP半托管商家可调用的OpenAPI接口

Feature Description | API Name | API Path  
---|---|---  
Listing | CreateProduct | /product/create  
Update Product | UpdateProduct | /product/update  
Update Inventories | AdjustSellableQuantity | /product/stock/sellable/adjust  
UpdateSellableQuantity | /product/stock/sellable/update  
UpdatePriceQuantity | /product/price_quantity/update  
Brand | GetBrandByPages | /category/brands/query  
Get Product Information | GetProductItem/GetProducts | /product/item/get/products/get  
Upload Images | UploadImage | /image/upload  
MigrateImage | /image/migrate  
MigrateImages | /images/migrate  
GetResponse | /image/response/get  
Delete/Deactive Products | DeactivateProduct | /product/deactivate  
RemoveSku | /product/sku/remove  
RemoveProduct | /product/remove  
Category | GetCategoryTree | /category/tree/get  
GetCategoryAttributes | /category/attributes/get  
GetCategorySuggestion/GetCategorySuggestionInBulk | /product/category/suggestion/get/product/category/suggestion/get/batch  
GetQCAlertProducts | /product/qc/alert/list  
SizeChart | GetSizeChartTemplate | /size/chart/template/get  
BatchUpdateSizeChart | /size/chart/batch/update  
Order | GetMultipleOrderItems | /orders/items/get  
GetOrderItems | /order/items/get  
GetOrder | /order/get  
GetOrders | /orders/get  
GetDocument | /order/document/get  
SetInvoiceNumber | /order/invoice_number/set  
Fulfillment/Logistics | GetOrderTrace | /logistic/order/trace  
Pack | /order/fulfill/pack  
ReadyToShip | /order/package/rts  
PrintAWB | /order/package/document/get  
RecreatePackage | /order/package/repack  
GetShipmentProvider | /order/shipment/providers/get  
Seller | GetSeller | /seller/get  
GetWarehouseBySellerId | /rc/warehouse/get  
QueryWarehouseDetailInfoBySellerId | /rc/warehouse/detail/get  
IM | GetMessages | /im/message/list  
GetSessionDetail | /im/session/get  
GetSessionList | /im/session/list  
MessageRecall | /im/message/recall  
OpenSession | /im/session/open  
ReadSession | /im/session/read  
SendMessage | /im/message/send  
Finance | GetPayoutStatus | /finance/payout/status/get  
QueryTransactionDetails | /finance/transaction/details/get  
QueryAccountTransactions | /finance/transaction/accountTransactions/query  
QueryLogisticsFeeDetail | /lbs/slb/queryLogisticsFeeDetail  
  
除上述接口外，其他OpenAPI接口调用均会报错

# 调用建议

## 1\. 商品管理

### 1.1 查询可用的商品属性 

创建和更新商品前，你需要知道你的商品属于哪个类目，该类目中有哪些属性可以使用。

### 1.1.1 查询类目树

在创建商品前，开发者需要先调用[GetCategoryTree](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Ftree%2Fget>) API来获取Lazada的完整类目树

#### 字段描述

  


字段 | 描述  
---|---  
children | Lazada的类目是梳妆结构的，如果当前类目存在子类目，那么将会展示在当前类目的"children"字段中。  
name | 类目名称。  
leaf | 枚举：true/false。用于检查当前类目名称是不是叶子类目，只有叶子类目(leaf = true)才可以在创建商品或更新商品时使用。  
category_id | 当前类目的ID，需要在创建或更新商品时使用此ID向Lazada声明当前商品的所属类目。  
  
  


#### 响应示例
    
    
    {
      "data": [
        {
          "children": [
            {
              "var": false,
              "name": "Smartphones",
              "leaf": true,
              "category_id": 3
            },
            {
              "var": false,
              "name": "Tablets",
              "leaf": true,
              "category_id": 7
            },
            {
              "var": false,
              "name": "Landline Phones",
              "leaf": true,
              "category_id": 49
            },
            {
              "var": false,
              "name": "Feature Phones",
              "leaf": true,
              "category_id": 42006401
            }
          ],
          "var": false,
          "name": "Mobiles & Tablets",
          "leaf": false,
          "category_id": 2
        }
        ......
      ]
    }

**注** ：不同国家的类目树和类目ID可能是不同的

### 1.1.2 查询类目属性

为了创建或更新产品，开发者需要依据上一步查询到的类目ID来请求[GetCategoryAttributes](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Fattributes%2Fget>) API，来查询完整的类目属性列表，以便于向卖家展示可编辑的属性。

#### 字段解析

  


字段名 | 字段描述  
---|---  
is_key_prop | 当该字段值为1时，这意味着当前属性是一个商品的关键属性，填写该属性将会提高商品的评分。枚举：0/1  
is_sale_prop | 如果该字段值为1，这意味着当前属性是一个变体属性，该属性用于创建商品时区分SKU之间的规格或颜色等变体的属性。枚举：0/1  
name | 属性名称。当name作为属性名称出现时一定是英文。当name作为options属性枚举出现时，会根据请求时设置的language_code来展示对应的语言。  
input_type | 该字段决定了当前属性的输入限制，枚举如下：1: singleselect: 单选不可自定义；2: multiselect: 多选不可自定义（以逗号来区分多个选项）；3: enuminput: 既可以单选，也可以自定义输入；4: multienuminput: 既可以多选，也可以自定义输入；5: text: 仅支持输入文本；6: numeric: 仅支持输入数字；7: date: 仅支持输入日期；8: richText: 支持输入富文本，如HTML格式；9: img: 仅支持输入Lazada图片链接  
options | 当属性的input_type是singleselect、multiselect、enuminput、multienuminput时，该字段将会以数组的形式展示所有的可选枚举。  
en_name | options属性中的枚举名称，不论请求时language_code设置任何语言，都将展示英文名称。  
is_mandatory | 代表当前属性是否必填，当只为1时就是必填属性，在创建商品时不填写该属性将会报错。枚举：0/1  
attribute_type | 用于描述当前属性是SKU级别还是SPU级别。当值为normal时，意味着这个属性是SPU级别的，不论当前商品有几个SKU，都只需要设置一次。当值为sku时，意味着这个属性是SKU级别的，当前商品如果有多个SKU，那么每个sku都需要设置一次。枚举：normal/sku  
label | 前端展示给卖家的属性名称，无法在请求时作为参数使用。  
  
  


#### 卖家中心展示示例

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1712717500300_V4aUM6fd)

#### 响应示例
    
    
    {
        "data": [
            ......
            {
                "advanced": {
                    "is_key_prop": 0
                },
                "is_sale_prop": 0,
                "name": "quantity",
                "input_type": "numeric",
                "is_mandatory": 0,
                "attribute_type": "sku",
                "label": "Bundle Size",
                "id": 21
            },
            {
                "advanced": {
                    "is_key_prop": 0
                },
                "is_sale_prop": 0,
                "name": "price",
                "input_type": "numeric",
                "is_mandatory": 1,
                "attribute_type": "sku",
                "label": "Price",
                "id": 30106
            },
            {
                "advanced": {
                    "is_key_prop": 0
                },
                "is_sale_prop": 0,
                "name": "special_price",
                "input_type": "numeric",
                "is_mandatory": 0,
                "attribute_type": "sku",
                "label": "Special Price",
                "id": 30047
            },
            {
                "advanced": {
                    "is_key_prop": 0
                },
                "is_sale_prop": 0,
                "name": "description_en",
                "input_type": "richText",
                "is_mandatory": 0,
                "attribute_type": "normal",
                "label": "English Long Description (optional)",
                "id": 40036
            },
            {
                "advanced": {
                    "is_key_prop": 0
                },
                "is_sale_prop": 0,
                "name": "name_en",
                "input_type": "text",
                "is_mandatory": 0,
                "attribute_type": "normal",
                "label": "Name in English language",
                "id": 40039
            }
        ],
        "code": "0",
        "request_id": "21222aec17066029964048645"
    }

**注**

  * 由于单个类目属性较多，这里就不全部展示了，开发者可以使用[API测试工具](<https://isvconsole.lazada.com/apps/console/test_api?spm=a1zq7z.man.api_detail.2.11547c73m3JwXF#/category/attributes/get>)来主动测试。
  * 由于类目属性API不区分卖家类型，因此响应的将会是不同卖家的属性，半托管卖家无法使用其中的部分属性，具体为：price、special_price、special_from_date、special_to_date；这些字段应修改为supply_price，具体使用示例会在创建商品时展示。



### 1.2 图片上传

Lazada商品使用的图片都必须是Lazada内链，因此在创建和更新商品前，开发者需要将卖家的本地图片或者外部图片链接使用API转换为Lazada内链。详情请参考[此文档](<https://open.lazada.com/apps/doc/doc?nodeId=30718&docId=120947>)。

### 1.3 创建商品

根据前几步，我们得到了创建商品所需要的必要信息，将所有必要的信息组合为一个JSON payload并请求[Createproduc](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fcreate>) API成功就完成了一个商品的创建。

#### Payload 示例
    
    
    {
      "Request": {
        "Product": {
          "PrimaryCategory": "10002019",
          "Images": {
            "Image": [
              "https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg"
            ]
          },
          "Attributes": {
            "name": "test 2022 02",
            "description": "TEST",
            "brand": "No Brand", //如果商品没有品牌，请填写No Brand。如需使用品牌，请先调用GetBrandByPages API检查对应品牌是否存在于Lazada品牌库。
            "model": "test",
            "warranty_type": "Local seller warranty",
            "warranty": "1 Month",
            "short_description": "cm x 1efgtecm<br /><brfwefgtek",
            "Hazmat": "None",
          },
          "Skus": {
            "Sku": [
              {
                "SellerSku": "test2022 02",
                "saleProp":{
                        "color_family":"Green",
                        "size":"10"
                        },
                "quantity": "3",
                "supply_price": "35",
                "package_height": "10",
                "package_length": "10",
                "package_width": "10",
                "package_weight": "0.5",
                "package_content": "laptop bag",
                "Status": "active",
                "Images": {
                  "Image": [
                     "https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg"
                  ]
                }
              }
            ]
          }
        }
      }
    }

#### 响应示例
    
    
    {
        "data": {
            "item_id": 3069252927,
            "sku_list": [
                {
                    "shop_sku": "3069252927_MY-15298395971",
                    "seller_sku": "test2022 02",
                    "sku_id": 15298395971
                }
            ]
        },
        "code": "0",
        "request_id": "2101554016564826049331260"
    }

#### Payload参数解析

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1712717500846_W2SpAGtQ)

#### 字段解析

  


字段名 | 是否必填 | 字段描述  
---|---|---  
Images | Optional | 用于上传商品主图以及SKU图片。Images字段下一定要添加Image字段且值必须是字符串数组类型。将Images字段加入Sku参数中将会为当前SKU添加SKU图片。将Images字段加入Product参数中，将会为当前商品添加主图。每个Images字段仅能传入八张图片，并且不能重复。  
name | Mandatory | 商品名称。最大可输入255个字符。  
description | Optional | 最大可输入25000个字符。支持HTML格式富文本。仅支持Lazada内链，不允许其他外部链接。  
short_description | Optional | 仅支持文本以及<ul> <li> 和 <ol> <li>标签。其他HTML标签不允许使用，将会被忽略。  
brand | 使用该字段则brand_id选填 | 商品品牌名，可调用[GetBrandByPages API](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Fbrands%2Fquery>)查询。  
brand_id | 使用该字段则brand选填 | 商品品牌对应Lazada品牌库的ID，可调用[GetBrandByPages API](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Fbrands%2Fquery>)查询。  
SellerSku | Mandatory | 卖家自定义的SKU编码，同一个商品的SKU质检不能重复。禁止以下特殊字符： \"*^~<>/|\   
supply_price  | Mandatory | 商品供货价。  
package_height | Mandatory | 最大支持小数点后三位。Unit:cm  
package_length | Mandatory | 最大支持小数点后三位。Unit:cm  
package_width | Mandatory | 最大支持小数点后三位。Unit:cm  
package_weight | Mandatory | 最大支持小数点后三位。Unit:kg  
package_content | Optional | 包裹内容  
saleProp | Optional | SKU的变体属性集合，如果一个商品需要有多个SKU，那么必须在这个字段中依据查询到的类目属性来定义变体属性或者自定义变体属性。如果不定义变体属性，那么一个商品只允许存在一个SKU。  
color_family | Optional | 这是一个标准变体属性的示例，但是并不是通用的变体属性。不同的类目可能会有不同的变体属性如果当前类目没有标准变体属性或者没有你想要使用的标准变体属性，那么你可以使用自定义变体属性，详情请参考[此文档](<https://open.lazada.com/apps/doc/doc?nodeId=30712&docId=120259>)。  
  
  


### 1.4 更新商品

更新商品需要调用[UpdateProduct API](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fupdate>)，API的参数与1.3部分创建商品的Payload是相同的，但是大部分商品属性变更为非必填，不填不更新。只是在更新商品时，需要填入目标商品的sku id。

#### payload示例
    
    
    {
      "Request": {
        "Product": {
          "Attributes": {
            "name": "test 2022 02",
          },
          "Skus": {
            "Sku": [
              {
                "SkuId": "15298395971",
                "quantity": "3",
                "package_content": "laptop bag",
                "Status": "active",
              }
            ]
          }
        }
      }
    }

### 1.5 库存管理

在更新库存前，建议前阅读[此文档](<https://open.lazada.com/apps/doc/doc?nodeId=42714&docId=121233>)理解Lazada的库存逻辑以及库存种类。

#### API请求示例

（除示例中的两个API外，其他API均不可更新半托管卖家的库存）

##### UpdateProduct API
    
    
    {
      "Request": {
        "Product": {
          "Attributes": {},
          "Skus": {
            "Sku": [
              {
                "SkuId": "2351235125",
                "quantity": "3"
              }
            ]
          }
        }
      }
    }

  1. 在这里UpdateProduct API仅用于更新库存，因此删除了其他非库存相关的可更新字段；
  2. UpdateProduct API不支持在一个请求中更新多个不同商品的SKU库存，单个请求中的所有SKU都应该属于同一个商品；
  3. 数量不能是负数。



##### AdjustSellableQuantity API
    
    
    <Request>
      <Product>
        <Skus>
          <Sku>
            <SkuId>234</SkuId>
            <SellableQuantity>-20</SellableQuantity>
          </Sku>
          <Sku>
            <SkuId>234</SkuId>
            <SellableQuantity>-20</SellableQuantity>
          </Sku>
        </Skus>
      </Product>
    </Request>

  1. 如果一个SKU的原始可售库存为20，那么在请求中将SellableQuantity设置为1时，最终该SKU的可售库存数量将被更新为21(20+1)；
  2. 如果一个SKU的原始可售库存为20，那么在请求中将SellableQuantity设置为-1时，最终该SKU的可售库存数量将被更新为19(20+(-1))；
  3. 更新后的最终可售库存结果必须大于或等于0；
  4. 支持在一个请求中加入多个属于不同商品的SKU；
  5. 单条请求最大可更新50个SKU，超过50个SKU将会报错，推荐单次更新20个SKU。



  


  


### 1.6 尺码表

请参考[此文档](<https://open.lazada.com/apps/announcement/detail?spm=a1zq7z.27201188.search_panel.3.13e47c73oEyNkc&docId=1951>)

  


## 2\. 订单管理和履约

### 2.1. [Get Order](<https://open.lazada.com/apps/doc/doc?nodeId=43452&docId=121327>)

### 2.2. [Order Status Flow](<https://open.lazada.com/apps/doc/doc?nodeId=29484&docId=120167>)

### 2.3. Fulfillment orders

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1712717501354_irI8EwvB)

[Detail Document](<https://open.lazada.com/apps/doc/doc?nodeId=43453&docId=121328>)