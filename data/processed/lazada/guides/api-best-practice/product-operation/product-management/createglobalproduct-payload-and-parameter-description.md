## Payload sample

**Note** : The attribute name is case sensitive.

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<?xml version="1.0" encoding="utf-8"?>

<Request>

<Product>

<PrimaryCategory>3238</PrimaryCategory>

<SPUId/>

<AssociatedSku/>

<AutoAllocateStock>false</AutoAllocateStock>

<Ventures>

<Venture>MY</Venture>

<Venture>SG</Venture>

<Venture>TH</Venture>

</Ventures>

<SemiUpgradeVentures>

<Venture>MY</Venture>

<Venture>SG</Venture>

</SemiUpgradeVentures> //创建GlobalPlus商品时，必填

<Images>

<Image>https://sg-test-11.slatic.net/p/58eabcc6fe1526e622e451898f7a6819.jpg</Image>

</Images>

<Attributes>

<propCascades>

<propCascade>

<cascadeId>26</cascadeId>

<path>120013644:162,100006867:160387</path>

</propCascade>//行业属性库，语雀文档：https://www.yuque.com/alipay2088702898225450/kb/pk1np0?singleDoc# 《Product API -行业属性库API》

</propCascades>

<name>api create product test sample</name>

<video>video id</video>

<short_description>This is a nice product</short_description>

<description>This is a nice product description</description>

<brand>Remark</brand>

<model>Test</model>

<kid_years>Kids (6-10yrs)</kid_years>

<package_length>11</package_length>

<package_height>22</package_height>

<package_weight>0.1</package_weight>

<package_width>44</package_width>

<package_content>this is what's in the box</package_content>

<light_item_abs>

<my>1.11</my>

<sg>1.11</sg>

</light_item_abs> //订单中平均包含商品数量设置；重量小于0.01kg的轻小件商品需要设置此参数，选填

</Attributes>

<variation>

<variation1>

<name>color_family</name>

<hasImage>true</hasImage>

<customize>false</customize>

<options>

<option>Green</option>

</options>

</variation1>

<variation2>

<name>size</name>

<hasImage>false</hasImage>

<customize>false</customize>

<options>

<option>40</option>

</options>

</variation2>

</variation> //创建多个sku时，必填

<Skus>

<Sku>

<SellerSku>17ssapi-create-test1-11</SellerSku>

<color_family>Green</color_family>

<size>40</size>

<quantity>120</quantity>

<sg_retail_price>388.50</sg_retail_price>

<sg_sales_price>308.50</sg_sales_price>

<retail_price>388.50</retail_price>

<sales_price>308.50</sales_price>

<sg_no_fee_price>308.50</sg_no_fee_price>

<no_fee_price>308.50</no_fee_price> //创建GlobalPlus商品时，必填

<tax_class>default</tax_class>

<Images>

<Image>https://sg-test-11.slatic.net/p/58eabcc6fe1526e622e451898f7a6819.jpg</Image>

</Images>

</Sku>

</Skus>

</Product>

</Request>

## Parameter description

The following table lists the parameters that are required for creating a global product.

Name | Type | Description
---|---|---
Product | subsection | The product data node. Mandatory
PrimaryCategory | integer | The ID of the primary category for the product. To get the ID for each of the system’s categories, call GetCategoryTree. Mandatory. It’s optional if ‘AssociatedSku’ is provided.
SPUId | integer | The ID of the SPU. Optional
AssociatedSku | subsection | The unique identifier of a product that is already in the system, with which this product should be associated. Optional
Images | string | Spu level product image.Contains most 8 images URL. Optional
AutoAllocateStock | string | Support automatical stock allocation between sites when the stock of a site is 0. The stock allocation rule is transferring 1/2 stock from the one with the most stock quantity.
ventures | subsection | The target site to create the product, with MY as mandatory option. Optional values are SG, TH, PH, ID, and VN. If no value is specified, the prdocut will be created to all sites that the seller has permission.
SemiUpgradeVentures | subsection | The target site to upgrade the product to global plus Optional values are MY, SG, TH, PH, ID, and VN. If no value is specified, the prdocut will be created as normal product.
Attributes | subsection | All common attributes of products. Mandatory. It’s optional if ‘AssociatedSku’ is provided.
Skus | subsection | An array contains at least one SKU. Mandatory

  

﻿The content of the ’Attributes" fields are dynamic. To view all available attributes, call the GetCategoryAttributes API. The following table provides some examples.