# What is the Market Ease Model

Marketplace Ease is a program in which merchants provide product supply prices, platform sales and order fulfilments by themselves. Orders payment are settled based on the product supply price, without any additional commissions or fees except during Mega Campaigns.

# Market Ease Model OpenAPI List

Feature Description| API Name| API Path  
---|---|---  
Listing| CreateProduct| /product/create  
Update Product| UpdateProduct| /product/update  
Update Inventories| AdjustSellableQuantity| /product/stock/sellable/adjust  
UpdateSellableQuantity| /product/stock/sellable/update  
UpdatePriceQuantity| /product/price_quantity/update  
Brand| GetBrandByPages| /category/brands/query  
Get Product Information| GetProductItem/GetProducts| /product/item/get/products/get  
Upload Images| UploadImage| /image/upload  
MigrateImage| /image/migrate  
MigrateImages| /images/migrate  
GetResponse| /image/response/get  
Delete/Deactive Products| DeactivateProduct| /product/deactivate  
RemoveSku| /product/sku/remove  
RemoveProduct| /product/remove  
Category| GetCategoryTree| /category/tree/get  
GetCategoryAttributes| /category/attributes/get  
GetCategorySuggestion/GetCategorySuggestionInBulk| /product/category/suggestion/get/product/category/suggestion/get/batch  
GetQCAlertProducts| /product/qc/alert/list  
SizeChart| GetSizeChartTemplate| /size/chart/template/get  
BatchUpdateSizeChart| /size/chart/batch/update  
Order| GetMultipleOrderItems| /orders/items/get  
GetOrderItems| /order/items/get  
GetOrder| /order/get  
GetOrders| /orders/get  
GetDocument| /order/document/get  
SetInvoiceNumber| /order/invoice_number/set  
Fulfillment/Logistics| GetOrderTrace| /logistic/order/trace  
Pack| /order/fulfill/pack  
ReadyToShip| /order/package/rts  
PrintAWB| /order/package/document/get  
RecreatePackage| /order/package/repack  
GetShipmentProvider| /order/shipment/providers/get  
Seller| GetSeller| /seller/get  
GetWarehouseBySellerId| /rc/warehouse/get  
QueryWarehouseDetailInfoBySellerId| /rc/warehouse/detail/get  
IM| GetMessages| /im/message/list  
GetSessionDetail| /im/session/get  
GetSessionList| /im/session/list  
MessageRecall| /im/message/recall  
OpenSession| /im/session/open  
ReadSession| /im/session/read  
SendMessage| /im/message/send  
Finance| GetPayoutStatus| /finance/payout/status/get  
QueryTransactionDetails| /finance/transaction/details/get  
QueryAccountTransactions| /finance/transaction/accountTransactions/query  
QueryLogisticsFeeDetail| /lbs/slb/queryLogisticsFeeDetail  
  
Other than the above APIs, all other OpenAPI interfaces report errors when called.

# Calling suggestions

## 1\. Product Management

### 1.1 Query available product attributes

Before creating and updating items, you need to know which category your item belongs to and what attributes are available in that category.

### 1.1.1 Query Category Tree

Before creating a product, developers need to call the [GetCategoryTree API](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Ftree%2Fget>) to get Lazada's full category tree first.

#### Field Description

  


Field| Description  
---|---  
children| Lazada's categories are tree-structured, and if there are children in the current category, they will be displayed in the "children" field of the current category.  
name| Category Name.  
leaf| Enum: true/false.Used to check if the current category name is a leaf category, only leaf categories (leaf = true) can be used when creating a product or updating a product.  
category_id| The ID of the current category, you need to use this ID to declare to Lazada the category to which the current item belongs when you create or update the item.  
  
  


#### Response Example

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

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

.......

],

"var": false,

"name": "Mobiles & Tablets",

"leaf": false,

"category_id": 2

}

]

}

**Note** ：Category tree and category IDs may be different in different countries.

### 1.1.2 Query Category Attributes

In order to create or update a product, the developer needs to request the [GetCategoryAttributes API](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Fattributes%2Fget>) based on the category ID queried in the previous step to query the complete list of category attributes in order to display editable attributes to sellers.

#### Field Description

  


Field| Description  
---|---  
is_key_prop| When the value of this field is 1, it means that the current attribute is a key attribute of an item and filling it in will increase the rating of the item.Enum: 0/1  
is_sale_prop| If the value of this field is 1, this means that the current attribute is a variant attribute, which is used to differentiate between SKUs when creating items with variants such as specification or color.ENUM: 0/1  
name| Attribute name.When name appears as an attribute name it must be English.When name appears as the options attribute enumeration, the corresponding language is displayed according to the language_code set at the time of the request.  
input_type| This field determines the input restrictions for the current attribute, enumerated below:1: singleselect: single-select is not customizable;2: multiselect: multiselect is not customizable (commas are used to separate multiple options);3: enuminput: both single-select and customizable inputs;4: multienuminput: can be both multi-selected and customized;5: text: only text input is supported;6: numeric: Supports only numeric input;7: date: only supports date input;8: richText: support input rich text, such as HTML format;9: img: only supports inputting Lazada image link.  
options| When the attribute's input_type is singleselect, multiselect, enuminput, multienuminput, the field will display all optional enumerations as an array.  
en_name| The name of the enumeration in the options attribute will be displayed in English regardless of the language_code setting at the time of the request.  
is_mandatory| Indicates whether the current attribute is required or not, when it is 1, it is a required attribute, if you don't fill in the attribute when creating the product, it will report an error.Enum: 0/1  
attribute_type| Used to describe whether the current attribute is SKU level or SPU level.When the value is normal, it means this attribute is SPU level, no matter how many SKUs the current product has, it only needs to be set once.When the value is sku, it means this attribute is SKU level, if the current product has more than one SKU, then each SKU needs to be set once.Enum：normal/sku  
label| The name of the attribute that the front-end displays to the seller cannot be used as a parameter in the request.  
  
  


#### Seller Center Display Example

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1712717533577_jiM0MW75)

#### Response Example

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

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

**Note**

  1. Due to the large number of individual category attributes, not all of them are shown here, and developers can use the [API testing tool](<https://isvconsole.lazada.com/apps/console/test_api?spm=a1zq7z.man.api_detail.2.11547c73m3JwXF#/category/attributes/get>) to test them proactively.
  2. Since the category attribute API does not distinguish between seller types, the response will be attributes of different sellers, and semi-managed sellers cannot use some of these attributes, specifically: price, special_price, special_from_date, special_to_date; these fields should be modified to supply_price, the Specific usage examples will be shown when creating products.



### 1.2 Image Upload

All images used in Lazada products must be Lazada inlinks, so before creating and updating products, developers need to convert sellers' local images or external image links to Lazada inlinks using the API. Please refer to [this document](<https://open.lazada.com/apps/doc/doc?nodeId=30718&docId=120947>) for more details.

### 1.3 Create a product

According to the previous steps, we get the necessary information needed to create a product, combine all the necessary information into a JSON payload and request the [Createproduct API](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fcreate>) successfully to complete the creation of a product.

#### Payload Example

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

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

"brand": "No Brand", //If the product does not have a brand, please fill in No Brand

//If you want to use a brand, please call GetBrandByPages API first to check whether the corresponding brand exists in Lazada brand library.

"model": "test",

"warranty_type": "Local seller warranty",

"warranty": "1 Month",

"short_description": "cm x 1efgtecm<br /><brfwefgtek",

"Hazmat": "None"

},

"Skus": {

"Sku": [

{

"SellerSku": "test2022 02",

"saleProp": {

"color_family": "Green",

"size": "10"

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

#### Response Example

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

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

#### Payload Parameter Analysis

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1712717534071_tMU9QidN)

#### Field Description

  


Field| Mandatory| Description  
---|---|---  
Images| Optional| Used to upload the main image of the product and SKU images.The Image field must be added under the Images field and the value must be of string array type.Adding Images field to Sku parameter will add SKU image for current SKU.Adding Images field to Product parameter will add main image for current product.Only eight images can be passed into each Images field, and they cannot be duplicated.  
name| Mandatory| Trade Name.A maximum of 255 characters can be entered.  
description| Optional| Maximum input of 25000 characters.Supports rich text in HTML format.Only Lazada internal links are supported, no other external links are allowed.  
short_description| Optional| Only text and <ul> <li> and <ol> <li> tags are supported.Other HTML tags are not allowed and will be ignored.  
brand| Brand_id is optional if this field is used.| The brand name of the product, which can be queried by calling the [GetBrandByPages API](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Fbrands%2Fquery>).  
brand_id| If this field is used, the brand field is optional.| The product brand corresponds to the ID of the Lazada brand library, which can be queried by calling the [GetBrandByPages API](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Fbrands%2Fquery>).  
SellerSku| Mandatory| Seller's customized SKU code cannot be repeated for different SKUs of the same item.The following special characters are prohibited: \"*^~<>/|\  
supply_price| Mandatory| Product supply price.  
package_height| Mandatory| Maximum support for three decimal places.Unit:cm  
package_length| Mandatory| Maximum support for three decimal places.Unit:cm  
package_width| Mandatory| Maximum support for three decimal places.Unit:cm  
package_weight| Mandatory| Maximum support for three decimal places.Unit:kg  
package_content| Optional| Package Contents  
saleProp| Optional| A collection of variant attributes for SKUs. If an item needs to have more than one SKU, then variant attributes must be defined or customized in this field based on the queried class attributes.If no variant attribute is defined, then only one SKU is allowed for an item.  
color_family| Optional| This is an example of a standard variant attribute, but not a generic variant attribute.Different categories may have different variant attributes.If the current category does not have a standard variant attribute or does not have a standard variant attribute that you want to use, then you can use a custom variant attribute, please refer to [this document](<https://open.lazada.com/apps/doc/doc?nodeId=30712&docId=120259>) for details.  
  
  


  


### 1.4 Updated product

To update a product, you need to call [UpdateProduct API](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fupdate>), the parameters of the API are the same as the 1.3 part of the Payload for creating a product, but most of the product attributes are changed to non-required, not filled in and not updated. When updating a product, you need to fill in the sku id of the target product.

#### Payload example

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"Request": {

"Product": {

"Attributes": {

"name": "test 2022 02"

},

"Skus": {

"Sku": [

{

"SkuId": "15298395971",

"quantity": "3",

"package_content": "laptop bag",

"Status": "active"

}

]

}

}

}

}

### 1.5 Inventory management

Before updating your inventory, it is recommended to read [this document](<https://open.lazada.com/apps/doc/doc?nodeId=42714&docId=121233>) to understand Lazada's inventory logic and the types of inventory.

#### API Request Example

(No other APIs can update the inventory of a Market Ease Model seller except the two in the example)

##### UpdateProduct API

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

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

  1. In this example the UpdateProduct API is only used to update inventory, so other non-inventory related updatable fields are removed;
  2. The UpdateProduct API does not support updating SKU inventory for multiple different products in a single request; all SKUs in a single request should belong to the same product;
  3. The quantity cannot be negative.



##### AdjustSellableQuantity API

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<Request>

<Product>

<Skus>

<Sku>

<SkuId>234</SkuId>

<SellableQuantity>20</SellableQuantity>

</Sku>

<Sku>

<SkuId>234</SkuId>

<SellableQuantity>-20</SellableQuantity>

</Sku>

</Skus>

</Product>

</Request>

  1. If a SKU has an original SellableQuantity of 20, then when the SellableQuantity is set to 1 in the request, the final SellableQuantity for that SKU will be updated to 21(20+1);
  2. If a SKU has an original SellableQuantity of 20, then when the SellableQuantity is set to -1 in the request, the final SellableQuantity for that SKU will be updated to 19 (20+(-1));
  3. The updated final saleable inventory result must be greater than or equal to zero;
  4. Supports adding multiple SKUs belonging to different products in a single request;
  5. The maximum number of SKUs that can be updated in a single request is 50, more than 50 SKUs will report an error, it is recommended to update 20 SKUs in a single request.



### 1.6 Size Chart

Please refer to [this document](<https://open.lazada.com/apps/announcement/detail?spm=a1zq7z.27201188.search_panel.3.13e47c73oEyNkc&docId=1951>).

## 2\. Order management and fulfillment

### 2.1. [Get Order](<https://open.lazada.com/apps/doc/doc?nodeId=43452&docId=121327>)

### 2.2. [Order Status Flow](<https://open.lazada.com/apps/doc/doc?nodeId=29484&docId=120167>)

### 2.3. [Fulfillment orders](<https://open.lazada.com/apps/doc/doc?nodeId=43453&docId=121328>)

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1712717534517_rSE14tnG)