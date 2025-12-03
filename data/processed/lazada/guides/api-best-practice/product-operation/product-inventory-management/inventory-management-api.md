This document will introduce the API related to product inventory management and show usage examples.

If you need to understand the inventory logic of Lazada products, _[check this document](<https://open.lazada.com/apps/doc/doc?spm=a1zq7z.man121234.site_detail.1.7dee7c73pHnf38&nodeId=42714&docId=121233>)_.

# **UpdatePriceQuantity**

 _[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fprice_quantity%2Fupdate>)_

Use this API to update the total inventory of the corresponding warehouse for an product.

## **Request Example**

### **Single-warehouse format (used by single-warehouse sellers, only updates dropshipping warehouse).**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<Request>

<Product>

<Skus>

<Sku>

<ItemId>6718170187</ItemId>

<SkuId>12761620980</SkuId>

<Quantity>200</Quantity>

<!--Negative numbers cannot be used-->

</Sku>

</Skus>

</Product>

</Request>

#### **Note**

  1. Since this document is used to introduce inventory management, all other optional fields are omitted.
  2. Supports batch update of total inventory of dropshipping warehouse for different sku's under different products in one request.
  3. The updated inventory quantity must be greater than or equal to the inventory locked by the withhold + occupy + campaign (channelInventories), otherwise an error will be reported.
  4. A maximum of 50 SKUs can be added per request, adding more SKUs will result in a timeout error.
  5. Each seller can only call the inventory API 50 times per second, more than 50 may cause the request to fail due to traffic limitation.
  6. Quantity cannot be negative.



### **Multi-warehouse format (used by multi-warehouse sellers, can update dropshipping and multi-warehouse warehouses at the same time).**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<Request>

<Product>

<Skus>

<Sku>

<ItemId>234234234</ItemId>

<SkuId>234</SkuId>

<MultiWarehouseInventories>

<MultiWarehouseInventory>

<WarehouseCode>Dropshipping</WarehouseCode>

<Quantity>20</Quantity>

</MultiWarehouseInventory>

<MultiWarehouseInventory>

<WarehouseCode>warehouseTest2</WarehouseCode>

<Quantity>30</Quantity>

</MultiWarehouseInventory>

</MultiWarehouseInventories>

</Sku>

</Skus>

</Product>

</Request>

#### **Note**

  1. Since this document is used to introduce inventory management, all other optional fields are omitted.
  2. Single-warehouse sellers should not use the multi-warehouse format, otherwise an error may be reported.
  3. The updated inventory quantity must be greater than or equal to the inventory locked by the withhold + occupy + campaign (channelInventories), otherwise an error will be reported.
  4. A maximum of 50 SKUs can be added per request, adding more SKUs will result in a timeout error.
  5. Each seller can only call the inventory API 50 times per second, more than 50 may cause the request to fail due to traffic limitation.
  6. Quantity cannot be negative.



# **UpdateProduct**

 _[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fupdate>)_

Use this API to update product information and product sellable inventory in the dropshipping warehouse.

## **Request Example**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"Request": {

"Product": {

"ItemId": "6718170187",

"Attributes": {},

"Skus": {

"Sku": [

{

"SkuId": "123456",

"quantity": "1" //Negative numbers cannot be used

}

]

}

}

}

## }**Note**

  1. Since this document is used to introduce inventory management, all other optional fields are omitted.
  2. The sku inventory updated by this API must belong to the same product, and does not support updating the inventory of multiple different products.
  3. The updated inventory quantity must be greater than or equal to the inventory locked by the campaign (channelInventories), otherwise an error will be reported.
  4. Quantity cannot be negative.



# **UpdateSellableQuantity**

 _[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fstock%2Fsellable%2Fupdate>)_

Use this API to update the sellable inventroy of SKUs in an overriding manner.

## **Request Example**

### **Single-warehouse format (used by single-warehouse sellers, only updates dropshipping warehouse).**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<Request>

<Product>

<Skus>

<Sku>

<ItemId>234234234</ItemId>

<SkuId>234</SkuId>

<SellableQuantity>20</SellableQuantity>

</Sku>

</Skus>

</Product>

</Request>

#### **Note**

  1. Supports batch update of total inventory of dropshipping warehouse for different sku's under different products in one request.
  2. The updated sellable inventory quantity must be greater than or equal to the inventory locked by the campaign (channelInventories), otherwise an error will be reported.
  3. A maximum of 50 SKUs can be added per request, adding more SKUs will result in a timeout error.
  4. Each seller can only call the inventory API 50 times per second, more than 50 may cause the request to fail due to traffic limitation.
  5. Quantity cannot be negative.



### **Multi-warehouse format (used by multi-warehouse sellers, can update dropshipping and multi-warehouse warehouses at the same time).**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<Request>

<Product>

<Skus>

<Sku>

<ItemId>234234234</ItemId>

<SkuId>234</SkuId>

<MultiWarehouseInventories>

<MultiWarehouseInventory>

<WarehouseCode>warehouseTest1</WarehouseCode>

<SellableQuantity>20</SellableQuantity>

</MultiWarehouseInventory>

<MultiWarehouseInventory>

<WarehouseCode>warehouseTest2</WarehouseCode>

<SellableQuantity>30</SellableQuantity>

</MultiWarehouseInventory>

</MultiWarehouseInventories>

</Sku>

</Skus>

</Product>

</Request>

#### **Note**

  1. Single-warehouse sellers should not use the multi-warehouse format, otherwise an error may be reported.
  2. The updated sellable inventory quantity must be greater than or equal to the inventory locked by the campaign (channelInventories), otherwise an error will be reported.
  3. A maximum of 50 SKUs can be added per request, adding more SKUs will result in a timeout error.
  4. Each seller can only call the inventory API 50 times per second, more than 50 may cause the request to fail due to traffic limitation.
  5. Quantity cannot be negative.



# **AdjustSellableQuantity**

 _[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fstock%2Fsellable%2Fadjust>)_

Use this API to update the sellable inventory of SKUs by summing positive and negative numbers.(A positive number is an increase in inventory and a negative number is a decrease in inventory)

## **Request Example**

### **Single-warehouse format (used by single-warehouse sellers, only updates dropshipping warehouse).**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<Request>

<Product>

<Skus>

<Sku>

<ItemId>234234234</ItemId>

<SkuId>234</SkuId>

<SellableQuantity>-20</SellableQuantity>

</Sku>

</Skus>

</Product>

</Request>

#### **Note**

  1. The SellableQuantity field can be set to a negative number.
  2. If the original inventory is 1 and the SellableQuantity field is passed in at 20, then the sellable inventory for this SKU will be updated to 21 (20 + 1).
  3. If the original inventory is 20 and the SellableQuantity field is passed in at -1, then the sellable inventory for this SKU will be updated to 19 (20 + (-1)).
  4. The updated final saleable inventory must be greater than or equal to 0, otherwise an error will be reported.
  5. Supports batch update of total inventory of dropshipping warehouse for different sku's under different products in one request.
  6. The updated sellable inventory quantity must be greater than or equal to the inventory locked by the campaign (channelInventories), otherwise an error will be reported.
  7. A maximum of 50 SKUs can be added per request, adding more SKUs will result in a timeout error.
  8. Each seller can only call the inventory API 50 times per second, more than 50 may cause the request to fail due to traffic limitation.



### **Multi-warehouse format (used by multi-warehouse sellers, can update dropshipping and multi-warehouse warehouses at the same time).**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<Request>

<Product>

<Skus>

<Sku>

<ItemId>234234234</ItemId>

<SkuId>234</SkuId>

<MultiWarehouseInventories>

<MultiWarehouseInventory>

<WarehouseCode>warehouseTest1</WarehouseCode>

<SellableQuantity>20</SellableQuantity>

</MultiWarehouseInventory>

<MultiWarehouseInventory>

<WarehouseCode>warehouseTest2</WarehouseCode>

<SellableQuantity>-30</SellableQuantity>

</MultiWarehouseInventory>

</MultiWarehouseInventories>

</Sku>

</Skus>

</Product>

</Request>

#### **Note**

  1. The SellableQuantity field can be set to a negative number.
  2. If the original inventory is 1 and the SellableQuantity field is passed in at 20, then the sellable inventory for this SKU will be updated to 21 (20 + 1).
  3. If the original inventory is 20 and the SellableQuantity field is passed in at -1, then the sellable inventory for this SKU will be updated to 19 (20 + (-1)).
  4. The updated final saleable inventory must be greater than or equal to 0, otherwise an error will be reported.
  5. Single-warehouse sellers should not use the multi-warehouse format, otherwise an error may be reported.
  6. The updated sellable inventory quantity must be greater than or equal to the inventory locked by the campaign (channelInventories), otherwise an error will be reported.
  7. A maximum of 50 SKUs can be added per request, adding more SKUs will result in a timeout error.
  8. Each seller can only call the inventory API 50 times per second, more than 50 may cause the request to fail due to traffic limitation.
  9. Quantity cannot be negative.