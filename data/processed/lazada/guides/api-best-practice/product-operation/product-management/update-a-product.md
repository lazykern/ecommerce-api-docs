# Updateproduct overview

Updateproduct API needs to be called to update products, the payload format used by Updateproduct API is the same as Createproduct API, but most of the fields are optional. And the Updateproduct API cannot delete all product attributes, only some of the product attributes are supported to be deleted using the Updateproduct API.

# Updateproduct API

## [API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fupdate>)

## Updateproduct API Common Fields Description

  

Field Name | Require | Removable | Field Description
---|---|---|---
PrimaryCategory | Optional | No | Fill in this field when calling the API to update the category of the product
AssociatedSku | Optional | N/A | This field is not a product attribute, but a Key attribute. When you want to add a new SKU to an existing product using the Updateproduct API, you need to fill in this field with a sku id that already exists for the target product.
Images | Optional | No | The Images attribute is used to update images for this product. The Image field in the Images property must be of the array type, with a maximum of 8 images passed into each Image field. Putting Images in the sku attribute indicates that the image is a variant image, and putting it outside indicates an SPU image. Images field cannot delete the image, only replace the old one with the new one. Must use lazada URL images, external URLs are not supported. Please refer to this document for image migration .
name | Optional | No | Product Title
description | Optional | Yes | Maximum 25000 characters HTML tags are allowed. Only Lazada image URLs are allowed, no external URLs.
d_description | Optional | N/A | Delete long description.
d_description_ms | Optional | N/A | Delete long description of existing Malay version.
d_description_en | Optional | N/A | Delete the long description of the English version that already exists.
short_description | Optional | Yes | Only text.images and URLs will be automatically filtered;Short descriptions can only use <ul> <li> or <ol> <li>
d_short_description_en | Optional | N/A | Delete the short description of the English version that already exists.
gift_wrapping | Optional | No | Note: Whitelist function, if you need this function please contact PSC for more information. Enum: Yes/No
name_engravement | Optional | No | Note: Whitelist function, if you need this function please contact PSC for more information. Enum: Yes/No
brand | Optional | No | The name obtained by calling the GetBrandByPages API
brand_id | Optional | No | The brand id obtained by calling the GetBrandByPages API
video | Optional | Yes | After uploading the video , fill in the video id of the GetVideo or CompleteCreateVideo response, and the video status must be AUDIT_SUCCESS. Add "remove_video": "Yes" to the payload to remove the product video
SkuId | Mandatory | No | Sku id created by Lazada at the time of product creation and used to locate the Sku or product that needs to be updated when the product is updated.
SellerSku | Optional | No | Customizable by the seller, unique in the store. Does not support using Updateproduct API to modify seller sku((before 15 November 2023)).
price | Optional | No | The retail price of the product, which will be displayed if the "special price" field is not filled or expired
special_price | Optional | No | The actual sales price of the product, if the "special_from_date" and "special_to_date" fields are not filled in, then the validity time is Long Time(Permanent validity).
special_from_date | Optional | No | Special price start time. If this parameter is passed, then "special_price" is mandatory.
special_to_date | Optional | No | Special price end time. If this parameter is passed, then "special_price" is mandatory.
Status | Optional | No | One of the following values: 'active','inactive' or 'deleted'. Optional. The default value is 'active'
package_height | Mandatory | No | Maximum two decimal places. Unit:cm
package_length | Mandatory | No | Maximum two decimal places. Unit:cm
package_width | Mandatory | No | Maximum two decimal places. Unit:cm
package_weight | Mandatory | No | Maximum two decimal places. Unit:kg
saleProp | Optional | No | Updateproduct can update the option of a variant or add a new variant. If you need to delete the variant, you need to call the Removesku api
color_thumbnail | Optional | No | Variant thumbnail tags, only available when the SKU variant is a standard sales attribute(Except size).

  

### Notes

  1. The list is only part of the general attributes, each category of goods may have different product attributes can be used, the product available attributes to obtain please refer to [this document](<https://open.lazada.com/apps/doc/doc?nodeId=30717&docId=120946>).
  2. Please make sure the SKU variant attributes are the same when updating products.
  3. SKU images do not support partial additions. If a SKU adds a SKU image, then other SKUs of this item also need to add images, and vice versa.

# Updateproduct API payload demo

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"Request": {

"Product": {

"PrimaryCategory": "10002019",

"AssociatedSku":"Existing SKU ID in seller center", 

//When adding some SKUs to existing product,need to use this label

"Images": {

"Image": [

"https://my-live-02.slatic.net/p/47b6cb07bd8f80aa3cc34b180b902f3e.jpg"

]

},

"Attributes": {

"propCascade": {

"26": "120013644:162,100006867:160387"

}, 

"name": "test 2022 02",

"description": "TEST",

"brand": "No Brand", //"brand" will be deprecated please use "brand_ id"

"brand_id":"30768", 

"model": "test",

"d_description": "Yes",

"d_short_description": "Yes",

"d_short_description_en": "Yes",

"waterproof": "Waterproof",

"warranty_type": "Local seller warranty",

"warranty": "1 Month",

"short_description": "cm x 1efgtecm<br /><brfwefgtek",

"Hazmat": "None",

"material": "Leather",

"laptop_size": "11 - 12 inches",

"delivery_option_sof": "No",

"remove_video": "Yes",

"gift_wrapping": "Yes",

"name_engravement": "Yes"

},

"Skus": {

"Sku": [

{

"SkuId": "20091437762",

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

Notes

●Except for Sku Id, all other product attributes are not mandatory.

●Attributes must be preserved but can be left out of any field.

●Updateproduct API can only add variants and modify options, not delete variant attributes.

●The Updateproduct api needs to be requested using the POST method, so please put the parameters in the http body, otherwise the request may fail because the URL is too long.