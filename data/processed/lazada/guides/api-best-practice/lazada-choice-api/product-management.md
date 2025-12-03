The APIs required for Choice sellers to get their items are different from regular sellers. And currently Choice sellers are not supported to use the API to rack your Choice items.

# Get Products

Developers can use the GetChoiceProducts and GetChoiceProductItem APIs to get the latest information about the products in the choice store and synchronize it to display in their own system.

## API List

API Name| API Path| Description  
---|---|---  
GetChoiceProducts| /choice/products/get| Batch query eligible products based on time, status and other conditions.  
GetChoiceProductItem| /choice/product/item/get| Queries information about a single product based on item id.  
  
## Response Example

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"data": {

"created_time": "1703644237397",

"updated_time": "1721167453427",

"images": [

"https://id-live.slatic.net/p/a794dcee12e2da315f217ab429194898.jpg"

],

"skus": [

{

"Status": "active",

"quantity": 119,

"Images": [

"https://id-live.slatic.net/p/5a2a43ff78fb57a192d5e4f04a3dbefe.png"

],

"SellerSku": "12312312",

"ShopSku": "7940514630_ID-14353516624",

"special_time_format": "yyyy-MM-dd HH:mm:ss",

"currency_unit": "IDR",

"saleProp": {

"color_family": "Olive"

},

"multiWarehouseInventories": [

{

"occupyQuantity": 0,

"quantity": 0,

"totalQuantity": 0,

"withholdQuantity": 0,

"warehouseCode": "dropshipping",

"sellableQuantity": 0

}

],

"package_width": "1.00",

"special_to_time": "2028-12-27 10:11:53",

"sku_supply_price": "12.00",

"color_family": "Olive",

"special_from_time": "2023-12-27 10:11:53",

"package_height": "1.00",

"fblWarehouseInventories": [

{

"occupyQuantity": 1,

"quantity": 119,

"totalQuantity": 120,

"withholdQuantity": 0,

"warehouseCode": "AChoice-ID-V-JIT",

"sellableQuantity": 119

}

],

"channelInventories": [

],

"package_length": "1.00",

"special_from_date": "2023-12-27",

"Available": 119,

"package_weight": "1",

"SkuId": 14353516624,

"special_to_date": "2028-12-27"

}

],

"item_id": 7940514630,

"bizSupplement": {

"item_type": "4"

},

"variation": {

"Variation1": {

"name": "color_family",

"options": [

"Olive"

],

"hasImage": true,

"label": "Color Family",

"customize": false

}

},

"trialProduct": false,

"primary_category": 10100234,

"marketImages": [],

"attributes": {

"description_en": "<article class=\"lzd-article\"><p style=\"line-height:1.7;text-align:left;text-indent:0;margin-left:0;margin-top:0;margin-bottom:0\"><span>1</span></p></article>",

"name": "localjit testlocaljit test",

"description": "<article class=\"lzd-article\"><p style=\"line-height:1.7;text-align:left;text-indent:0;margin-left:0;margin-top:0;margin-bottom:0\"><span>1</span></p></article>",

"source": "gsp",

"brand": "No Brand"

},

"status": "Active"

},

"code": "0",

"request_id": "210030a417255167682538883"

}

**Field Analysis**

Field Name| Field Description  
---|---  
Images| The Images property is used to upload images for this product.The Image field in the Images property must be of the array type, with a maximum of 8 images passed into each Image field.Putting Images in the sku attribute indicates that the image is a variant image, and putting it outside indicates an SPU image.  
name| Product Title.  
brand| Product Brand  
primary_category| Product category ID, call [GetCategoryTree API](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Ftree%2Fget>) to view the full category tree.  
item_id| The id generated after the product is created.Current country unique.An item id can be associated with multiple sku ids.  
created_time| The time when the product was created.  
updated_time| The time when the product was updated.  
Status| The current status of the SKU.Enum:active、inactive、deleted  
skus| A list of SKUs for the current product.  
skus.Status| The current status of the SKU.Enum:active、inactive、deleted  
quantity| The total inventory of the current SKU.  
SellerSku| Customizable by the seller, unique in the store.  
SkuId| Sku id created by Lazada at the time of product creation.  
multiWarehouseInventories| A seller may have multiple warehouses, and the inventory of each warehouse for the current SKU will be displayed in this list.  
occupyQuantity| This inventory will be increased when the item is purchased and payment is successful.  
withholdQuantity| This inventory will increase when an item is purchased but not yet paid for.  
SellableQuantity| The quantity of stock that can be purchased by buyers.  
totalQuantity| Total inventory(SellableQuantity+WithholdQuantity+OccupyQuantity).  
item_type| Inventory management model for products.JIT (platform-controlled Virtual inventory) : Inventory is managed by the seller.VMI (Platform-controlled physical inventory) : The platform manages inventory with local physical stock.Enum: cn vmi ：1local vmi ：2cn jit：3local jit：4  
  
  


  


**Inventory Management**

API Name| API Path| Description  
---|---|---  
EditChoiceSkuStock| /choice/stock/edit| This API can be called to update the sellable inventory of a Choice Sku.