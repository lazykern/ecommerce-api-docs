# 1\. Getting product list

## 1.1 Getting all shop products

**API:**[**_v2.product.get_item_list_**](<https://open.shopee.com/documents/v2/v2.product.get_item_list?module=89&type=1>)

 

This API allows you to get a list of all the products in the shop or filter by **update_time** range and item status

 

## 1.2 Searching for item_id 

**API:**[**_v2.product.search_item_**](<https://open.shopee.com/documents/v2/v2.product.search_item?module=89&type=1>)

 

This API allows you to search for a list of item_id based on some specific conditions, including

  * A list of **item_id** containing the product name keyword
  * A list of **item_id** containing the sku keyword
  * A list of **item_id** lacking required attributes
  * A list of **item_id** lacking optional attributes



 

# 2\. Getting product information

**API:**[**_v2.product.get_item_base_info_**](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>)**+**[**_v2.product.get_model_list_**](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>)

 

If the product has no variants, you only need to call [_v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) to get the product base information, otherwise you also need to call [_v2.product.get_model_list_](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>) API to get the variants price and stock.

 

The field “**has_model** ” in [_v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) API indicates whether the product has variants or not.

 

# 3\. Getting the data of product

**API:**[**_v2.product.get_item_extra_info_**](<https://open.shopee.com/documents/v2/v2.product.get_item_extra_info?module=89&type=1>)

 

This API can get the data of views, likes, sales, ratings, and star rating from a product.

The data of views is from the last 30 days' statistics, the sales data is the cumulative value.

 

# 4\. Getting product promotion information

**API:**[**_v2.product.get_item_promotion_**](<https://open.shopee.com/documents/v2/v2.product.get_item_promotion?module=89&type=1>)

 

This API allows you to get information about all ongoing or upcoming promotions that the product is added in. If the product is added into multiple promotions, the **promotion_id** field of [_v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) will return one of the **promotion_id** , and we suggest you continue to call API [_v2.product.get_item_promotion_](<https://open.shopee.com/documents/v2/v2.product.get_item_promotion?module=89&type=1>) to get all the promotions information.

 

# 5\. Updating product information

**API:**[**_v2.product.update_item_**](<https://open.shopee.com/documents/v2/v2.product.update_item?module=89&type=1>)

 

1\. This API supports updating product information except for the **size_chart** /**price** /**stock** /**model** information. Fields that are uploaded will be updated, and fields that are not uploaded will not be updated.

 

2\. For **item_sku** /**wholesale** /**video_upload_id** , we support the delete operation, you can upload the null string then we will delete it.

Example of deleting item_sku:

{

    "item_id": 800182459,

    "item_sku": ""

}

 

3\. Please refer to the [_FAQ_](<https://open.shopee.com/faq?top=162&sub=166&page=1&faq=218>) about updating extended descriptions.

 

4\. If you did not update some fields but encountered a prompt that these fields are filled in incorrectly, this situation is normal because every time you update, we will verify the legitimacy of all the product information, so if it does not meet the requirements, please modify it.

# 6\. Unlisting or deleting product 

**API:**[**_v2.product.unlist_item_**](<https://open.shopee.com/documents/v2/v2.product.unlist_item?module=89&type=1>)

 

“**unlist** ” : true means the product will be unlist,“**unlist** ” : false, means the product will be re-listed.

 

**API:**[**_v2.product.delete_item_**](<https://open.shopee.com/documents/v2/v2.product.delete_item?module=89&type=1>)

This API can change **item_status** to be “deleted”, please note that after the deletion, you will not be able to update the product, and the seller can not view this item through the Seller Center. 

 

For Shopee deleted and Seller deleted products, within 90 days, you can still get the product information through API, after 90 days, the product data will be permanently deleted in Shopee database, you can not query any information about this product, if you need, please save the product information in time.

 

# 7\. Updating size chart image

**API:**[**_v2.product.update_size_chart_**](<https://open.shopee.com/documents/v2/v2.product.update_size_chart?module=89&type=1>)

This API can be used to add or update the image size chart of the product, if you encounter the error "Your shop can not edit image size chart", please check the [_announcement_](<https://open.shopee.com/announcements/548>).

 

# 8\. Registering Brand

**API:**[**_v2.product.register_brand_**](<https://open.shopee.com/documents/v2/v2.product.register_brand?module=89&type=1>)

 

Sellers can register their own brands through this API. If Shopee audits this brand successfully, you will get a valid **brand_id** for adding or updating products.

For the specific audit process, please check the [_FAQ_](<https://open.shopee.com/faq?top=162&sub=166&page=1&faq=211>)

 

 

_*The following content is only applicable to CNSC/KRSC sellers._

 

# 9\. Getting global product list

**API:**[**_v2.global_product.get_global_item_list_**](<https://open.shopee.com/documents/v2/v2.global_product.get_global_item_list?module=90&type=1>)

 

This API allows you to get a list of all **global_item_id** or filter by **update_time** range under the merchant. This API will not return a list of deleted **global_item_id**.

 

# 10\. Getting a global product ID

**API:**[**_v2.global_product.get_global_item_id_**](<https://open.shopee.com/documents/v2/v2.global_product.get_global_item_id?module=90&type=1>)

 

By calling this API, you can quickly find the **global_item_id** of a shop product.

# 11\. Getting global product information

**API:**[**_v2.global_product.get_global_item_info_**](<https://open.shopee.com/documents/v2/v2.global_product.get_global_item_info?module=90&type=1>)**+**[**_v2.global_product.get_global_model_list_**](<https://open.shopee.com/documents/v2/v2.global_product.get_global_model_list?module=90&type=1>)

 

1\. If the global product does not contain variants, you only need to call [_v2.global_product.get_global_item_info_](<https://open.shopee.com/documents/v2/v2.global_product.get_global_item_info?module=90&type=1>) to get the global product information, otherwise you also need to call [_v2.global_product.get_global_model_list_](<https://open.shopee.com/documents/v2/v2.global_product.get_global_model_list?module=90&type=1>) to get the variants stock and price information.

 

2\. Product data and promotion information are not saved on global products.

You can call [_v2.product.get_item_extra_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_extra_info?module=89&type=1>) to get the shop product data and [_v2.product.get_item_promotion_](<https://open.shopee.com/documents/v2/v2.product.get_item_promotion?module=89&type=1>) to get the promotion data of shop products.

 

# 12\. Updating global products

**API:**[**_v2.global_product.update_global_item_**](<https://open.shopee.com/documents/v2/v2.global_product.update_global_item?module=90&type=1>)

 

1\. Since some fields can be managed by global products and shop products together, you can check the article "[_Creating global product_](<https://open.shopee.com/developer-guide/213>)" for details. You can set the fields synchronization through [_v2.global_product.set_sync_field_](<https://open.shopee.com/documents/v2/v2.global_product.set_sync_field?module=90&type=1>) API, then Shopee will automatically synchronize to shop products after you update the global product.

# 13\. Deleting global product

**API:**[**_v2.global_product.delete_global_item_**](<https://open.shopee.com/documents/v2/v2.global_product.delete_global_item?module=90&type=1>)

Global products do not support unlist, but can only be deleted. After the global products are deleted, all published shop products will also be deleted.

# 14\. Updating the size chart image

**API:**[**_v2.global_product.update_size_chart_**](<https://open.shopee.com/documents/v2/v2.global_product.update_size_chart?module=90&type=1>)

 

This API allows you to add or update the size chart of global products. If you want to update the size chart of a shop product individually, you can call [_v2.product.update_size_chart_](<https://open.shopee.com/documents/v2/v2.product.update_size_chart?module=89&type=1>) API.

 

You can check this [_FAQ_](<https://open.shopee.com/faq/162>) to learn more about which product module interface permissions CNSC/KRSC sellers have.