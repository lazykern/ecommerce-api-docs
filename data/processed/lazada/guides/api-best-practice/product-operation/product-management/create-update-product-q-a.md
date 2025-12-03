This document will list common problems and solutions encountered when creating products, and QA will add to it from time to time.

# Error Response Analysis

![1.jpg](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1686294876413_rJWVV0h9)

  * Please refer to the Error Code section of the API reference document for open platform business code enumeration.
  * When the value of the Open Platform error code is 500 or 501, check the error response and business error code. 500 or 501 indicates a generic error code.
  * Some errors may not have business error code.



# Q&A

In this section, I will indicate in each QA the open platform error code and the business error code for that issue. You can use the Web Find (Ctrl + F) function to find the issue you are experiencing.

  


**Q1:** The parameters are not in JSON format

**Code** :1001

**A1** :This error means that the JSON format you requested does not match the format required by the API.

For example the Images.Image field must be of array type and the Image field must be present. the same requirement applies to the Skus.Sku field.

![2.jpg](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1686294876679_uxilHlzT)

  


**Q2:** This variation attribute size is not found in the variation label,please make sure that this attribute is declared

**Open Platform Error Code** : 4143

**Business Error Code** : BIZ_CHECK_SALEPROP_ATTRIBUTE_INVALID

**A2** :This error means that the variant property you set is not a standard variant attribute of the current class or does not match the name of the custom variant property you set.

**Q3** :The message field value is 4142 when the product is created

**Open Platform Error Code** : 500 

**A3** :Please check if the brand or brand ID in your request exists in the current country. Brand names or brand IDs are not common to different countries.

Brand ID of "No Brand" in different countries：

![3.jpg](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1686294876883_TYXYfxx0)

  


**Q4** :This sale prop attribute xxx is not support thumbnail image

**Open Platform Error Code** : 4146

**Business Error Code** : BIZ_CHECK_SALEPROP_NOT_SUPPORT_THUMBNAIL 

**A4** :Thumbnail tags are not available for custom variants and some standard variants.

**Q5** :Sku edit was blocked by tag/ This product is under campaign participation and cannot be edited during campaign period. 

**Open Platform Error Code** : 501

**Business Error Code** : THD_IC_ERR_F_IC_ABILITY_PG_004:THD_IC_ERR_F_IC_ABILITY_PG_004/THD_IC_ERR_F_IC_ABILITY_PG_003

**A5** :The product or SKU is in a campaign and is locked by the campaign with product information that cannot be edited until the campaign ends.

**Q6** :Insert sku outer id relation failed, outerId already exists, sell ID:xxxxx,sku ID:xxxxxx,outer ID:xxxxxx,serverIP:xxxxx

**Open Platform Error Code** : 4135

**Business Error Code** : THD_IC_ERR_F_IC_INFRA_PRODUCT_036

**A6** :There is a used seller sku in the SKU you created, please check the outer id field in the response to see which seller sku is duplicated and make changes.

**Q7** :To ensure stability of service, this API service is disabled, please get more information from Notice.

**Open Platform Error Code** : 998

**A7** :This error is a traffic restriction, usually this error occurs at the beginning of Mega Campaign, please refer to the downgrade announcement before the Campaign starts for details.

**Sample Announcement** :[LAZADA D6 Campaign Downgrade Plan](<https://open.lazada.com/apps/announcement/detail?spm=a1zq7z.27201205.0.0.20377c73haBza3&docId=1849>)

  


**Q8** :negative sellable on channel inventory

**Open Platform Error Code** : 501

**A8** :This SKU signed up for Campaign and was partially locked out of saleable inventory by Campaign. This error occurs when you update the available inventory to be less than the available inventory locked by the Campaign.

[Lazada Inventory Analysis](<https://open.lazada.com/apps/doc/doc?nodeId=42714&docId=121233>)

**Q9** :Call to GetBrandByPages API is successful but response is empty

**GetBrandByPages API Total QPS** : 30

**A9** :This is in the API stability considerations set QPS, when the interface QPS reached the upper limit will intercept the request.

**Q10** : Api access frequency exceeds the limit. this ban will last 1 seconds. 

**Open Platform Error Code** : ApiCallLimit

**A10** :API level traffic limit, each API will have a different traffic limit, if the current API receives too much traffic in one second, then this error will occur. Please wait for the next second to retry.

**Q11** : Total sale prop more than maxItems 2. 

**Open Platform Error Code** : 500 

**Business Error Code** : BIZ_CHECK_TOTAL_SALE_PROP_MAX_ITEMS 

**A11** :The number of variant attributes that can be used is different for each category. If this problem occurs when calling the CreateProduct API, check the number of variant properties you set. If you get this error when calling UpdateProduct API, please check if you have added variant attributes that are not used by the original SKU. UpdateProduct API cannot delete variant attributes, you need to call Remove Sku API to delete old variant attributes to add new variant attributes.

**Q11** : Total sale prop more than maxItems 2. 

**Open Platform Error Code** : ServiceTimeout 

**A11** :A small number of timeout errors are normal, this may be caused by a high number of current requests or a large amount of data, please try again later.

If this error occurs in the product update/create API, please check if your request contains too many SKUs, if a single request contains more than 50 SKUs then it will time out. Please reduce the number of SKUs and request in batches, recommended 20 at a time.

If you encounter this error when using the GetProducts API, please first check in Seller Central to see if the seller has more than 10 variant SKUs for a single product. if so, please reduce the limit to ensure that the data in a single request is not too large to cause a timeout error.

**Q12** : How to add a new variant SKU to an existing product

A12: Add the "AssociatedSku" tag to the payload, and add one of the existing Seller Sku in the target product to the "AssociatedSku" tag and request it, so that the sku in your payload will not be published as a new product, but will be added to the existing product as a SKU.

![4.jpg](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1686294877101_Q7TWTrGW)

Notes:

Please make sure the original product has used variant attributes, if the original product does not use variant attributes, you cannot add a new SKU

  


**Q13** : Seller's online product count 1000 has reach limit 1000

**Open Platform Error Code** : 500 

**Business Error Code** : THD_APPROVAL_RULE_CENTER_ERR_PRE_QC_LISTING_LIMIT_ERROR 

A13: There is a cap on the number of items in active status in each seller's store. When the number reaches the upper limit, you will not be able to create new items in the active state, otherwise you will get this error.

![5.jpg](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1686294877334_M05RLWaC)

**Q14** : How to modify seller sku

A14: API does not support modifying Seller Sku