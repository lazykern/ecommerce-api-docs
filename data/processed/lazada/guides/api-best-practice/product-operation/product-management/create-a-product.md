# **Create Product Workflow**

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde52ef312c6b880d85132f96f361e0e04c975b8339e1c4c24831b75b38faadcd24bec177c308ebd53046e523c78283d930d194cfedeed0c6f7fb9da14a435a0ecd67b26e5584327e15a07e88bb89e35541d4fb4c8ed7016461c?tmpCode=c2245063-7b90-4daf-88e2-b107fd8f6406)

# **Create Product Example**

The category used in this example is the Smartphones category in Malaysia ("category_id": 3)

Note: The API request method is POST, so the request parameters other than the request URL need to be placed in the body to avoid the URL being too long and causing an error.

## **Json Request Example**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"Request": {

"Product": {

"PrimaryCategory": "10002019",

"AssociatedSku":"Existing SkuId in seller center", 

//When adding some SKUs to existing product,need to use this label

"Images": {

"Image": [

"https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg"

]

},

"disableAutoFillAttribute": false,

"Attributes": {

"propCascade": {

"26": "120013644:162,100006867:160387"

}, 

"name": "test 2022 02", 

"description": "TEST",

"brand": "No Brand", // "brand" will be deprecated please use "brand_ id"

"brand_id":"30768", 

"model": "test",

"waterproof": "Waterproof",

"warranty_type": "Local seller warranty",

"warranty": "1 Month",

"short_description": "cm x 1efgtecm<br /><brfwefgtek",

"Hazmat": "None",

"material": "Leather",

"laptop_size": "11 - 12 inches",

"delivery_option_sof": "No",

"gift_wrapping": "Yes",

"name_engravement": "Yes", 

"preorder_enable":"Yes", 

"preorder_days":"25"

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

"price": "35",

"special_price": "33",

"special_from_date": "2022-06-20 17:18:31",

"special_to_date": "2025-03-15 17:18:31",

"package_height": "10",

"package_length": "10",

"package_width": "10",

"package_weight": "0.5",

"package_content": "laptop bag",

"Images": {

"Image": [

"https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg"

]

},

{

"SellerSku": "test2022 02 - 1",

"saleProp":{

"color_family":"Gree - 1n",

"size":"10 - 1"

},

......

}

]

}

}

}

}

## **XML Request Example**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

<?xml version="1.0" encoding="UTF-8" ?>

<Request>

<Product>

<PrimaryCategory>3</PrimaryCategory>

<AssociatedSku>Existing SKUID in seller center</AssociatedSku>

<!--When adding some SKUs to existing product,need to use this label-->

<Images>

<Image>https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg</Image>

<Image>https://my-live-02.slatic.net/p/c905f479d04a3be36da4300ffd0abd87.jpg</Image>

</Images>

<Attributes>

<name>test 2022 026 29</name>

<description>TEST Long Description</description>

<short_description>Test Short Description</short_description>

<brand>No Brand</brand>

<!--"brand" will be deprecated please use "brand_ id"\-->

<brand_id>40516</brand_id>

<disableAttributeAutoFill>false</disableAttributeAutoFill>

<model>N/A</model>

<video>30073704787</video>

<phone_type>Smartphone</phone_type>

<warranty_type>Local Manufacturer Warranty</warranty_type>

<Hazmat>None</Hazmat>

<gift_wrapping>Yes</gift_wrapping>

<name_engravement>Yes</name_engravement>

<preorder_enable>Yes</preorder_enable>

<preorder_days>25</preorder_days>

</Attributes>

<Skus>

<Sku>

<SellerSku>test2022 06 29 01</SellerSku>

<quantity>3</quantity>

<price>35</price>

<saleProp>

<color_family>Green</color_family>

<size>10</size>

</saleProp>

<special_price>33</special_price>

<special_from_date>2022-06-30 17:00:00</special_from_date>

<special_to_date>2025-03-15 17:00:00</special_to_date>

<package_height>10</package_height>

<package_length>10</package_length>

<package_width>10</package_width>

<package_weight>0.5</package_weight>

<package_content>laptop bag</package_content>

<Images>

<Image>https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg</Image>

<Image>https://my-live-02.slatic.net/p/c905f479d04a3be36da4300ffd0abd87.jpg</Image>

</Images>

</Sku>

<Sku>

<SellerSku>test2022 06 29 02</SellerSku>

<quantity>3</quantity>

<price>35</price>

<saleProp>

<color_family>Green</color_family>

<size>11</size>

</saleProp>

<special_from_date>2022-06-30 17:00:00</special_from_date>

<special_to_date>2025-03-15 17:00:00</special_to_date>

<package_height>10</package_height>

<package_length>10</package_length>

<package_width>10</package_width>

<package_weight>0.5</package_weight>

<package_content>laptop bag</package_content>

<Images>

<Image>https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg</Image>

<Image>https://my-live-02.slatic.net/p/c905f479d04a3be36da4300ffd0abd87.jpg</Image>

</Images>

</Sku>

</Skus>

</Product>

<Request>

## **Response Example**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"data": {

"item_id": 3069252927,

"sku_list": [

{

"shop_sku": "3069252927_MY-15298395971",

"seller_sku": "test2022 06 29 02",

"sku_id": 15298395971

},

{

"shop_sku": "3069252927_MY-15298395970",

"seller_sku": "test2022 06 29 01",

"sku_id": 15298395970

}

]

},

"code": "0",

"request_id": "2101554016564826049331260"

}

## **Create Product Parameter Analysis**

### **Payload structure analysis image**

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde52ef312c6b880d85132f96f361e0e04c975b8339e1c4c24831b75b38faadcd24bec177c308ebd5304b57e81504c2e629228c7a407460cc9dbd563b7126b670881121cbf50ff84728ff7f93a30c7f6356e4fb4c8ed7016461c?tmpCode=c2245063-7b90-4daf-88e2-b107fd8f6406)

### **Partial field descriptions**

Field Name | Require | Field Description
---|---|---
Images | Optional | The Images property is used to upload images for this product. The Image field in the Images property must be of the array type, with a maximum of 8 images passed into each Image field. Putting Images in the sku attribute indicates that the image is a variant image, and putting it outside indicates an SPU image.
name | Mandatory | Product name. Maximum 255 characters.
AssociatedSku | Optional | In existing product,add some SKUs, this label is required for association. Note: the associated SKU must be displayed in the seller center normally
description | Optional | Maximum 25000 characters. HTML tags are allowed. Only Lazada image URLs are allowed, no external URLs.
short_description | Optional | Only text.images and URLs will be automatically filtered;Short descriptions can only use <ul> <li> or <ol> <li>
brand | Mandatory | "brand" will be deprecated please use "brand_ id"
brand_id | Mandatory | Use the "brand_id" field of the GetBrandByPages API as the value
video | Optional | After uploading the video, fill in the video id of the GetVideo or CompleteCreateVideo response, and the video status must be AUDIT_SUCCESS
gift_wrapping | Optional | Note: Whitelist function, if you need this function please contact PSC for more information. Enum: Yes/No
name_engravement | Optional | Note: Whitelist function, if you need this function please contact PSC for more information. Enum: Yes/No
preorder_enable | Optional | PreOrder switch for turning on or off products. ENUM: Yes/No
preorder_days | Optional | When PreOrder is on, it is used to enter the estimated number of processing days. The maximum and minimum values will change with the seller. This range is configured by Lazada operations staff, please contact PSC if you need to change it.
disableAutoFillAttribute | Optional | When the field value is true, the auto-fill feature will not be enabled. When creating products via the Open API endpoint, an auto-fill mechanism (enabled by default) may automatically populate unused product attributes in the payload based on algorithmic recommendations. Enum: true/false(default)
SellerSku | Mandatory | Customizable by the seller, unique in the same item.
price | Mandatory | The retail price of the product, which will be displayed if the "special price" field is not filled or expired
special_price | Optional | The actual sales price of the product, if the "special_from_date" and "special_to_date" fields are not filled in, then the validity time is Long Time(Permanent validity).
special_from_date | Optional | Special price start time. If this parameter is passed, then "special_price" is mandatory.
special_to_date | Optional | Special price end time. If this parameter is passed, then "special_price" is mandatory.
package_height | Mandatory | Maximum two decimal places. Unit:cm
package_length | Mandatory | Maximum two decimal places. Unit:cm
package_width | Mandatory | Maximum two decimal places. Unit:cm
package_weight | Mandatory | Maximum two decimal places. Unit:kg
package_content | Optional | Package details
saleProp | Optional | Sales attributes are divided into "saleProp" fields under SKU, used to distinguish sales attributes or non sales attributes
color_family | Optional | This is a standard variant attribute of this category, which is Optional when only one sku is created, but required when multiple sku are created. The standard variant property is different for each category, it may be "size" or something else, see this document for an explanation of the "is_sale_prop" property. If the current category does not have a standard variant property, please refer to this document to create a custom variant.
color_thumbnail | Optional | Variant thumbnail tags, only available when the SKU variant is a standard sales attribute.

## **What else needs to be done before creating a product？**

Get the category tree

Use this API to obtain the catalog library information of each country.

[API Usage Documentation](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Ftree%2Fget>)

### **1、GetCategorySuggestion**

Get product's category suggestion by product title.

We strongly recommend you to include this step for the following reasons:

a. This feature helps you identify the most suitable categories of your listings from Lazada's category tree

b. Mis-categorized products are subject to deactivation according to Lazada's policy

[API Usage Documentation](<https://open.lazada.com/apps/doc/api?spm=a1zq7z.man120945.site_detail.2.21107c73zwPD8A&path=%2Fproduct%2Fcategory%2Fsuggestion%2Fget>)

### **2、Get the attributes available for the target category**

After getting the category ID, use the category ID to call the GetCategoryAttributes API to get the attributes that can be filled in a category.

[API Usage Documentation](<https://open.lazada.com/apps/doc/doc?nodeId=30717&docId=120946>)

### **3、Get the brand id (if not, ignore)**

Call the GetBrandByPages API to get the list of lazada brands and extract the "brand_id" field of the brand to be used and use it when creating the product.

Note: The brand list is different from country to country.

### **4、Upload images**

External image URLs or local images cannot be used directly when creating or updating products, please refer to this document to convert images to Lazada image URLs.

[API Usage Documentation](<https://open.lazada.com/apps/doc/doc?nodeId=30718&docId=120947>)

### **5、Upload video (if no video, please ignore)**

Please refer to this document to upload a video and get the video id.

[API Usage Documentation](<https://open.lazada.com/apps/doc/doc?nodeId=30719&docId=120948>)