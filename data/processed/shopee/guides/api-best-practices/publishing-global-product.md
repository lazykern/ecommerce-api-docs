_*This article applies to cross-border sellers who have upgraded CNSC/KRSC_

After creating a global product, you can publish the global product to each market, but the global product can only have one shop product in each market.

 

Below we will explain the API call flow.

# Step 1: Getting the list of publishable shops

API: [_v2.global_product.get_publishable_shop_](<https://open.shopee.com/documents/v2/v2.global_product.get_publishable_shop?module=90&type=1>)

You can get the list of publishable shops for global products through this API, but we will not return the corresponding shops for the following cases:

  * shops that have not done the shop authorization
  * SIP affiliated shops
  * Shops of published market



# Step 2: Getting the shop channel

API: [_v2.logistics.get_channel_list_](<https://open.shopee.com/documents/v2/v2.logistics.get_channel_list?module=95&type=1>)

You need to call [_v2.logistics.get_channel_list_](<https://open.shopee.com/documents/v2/v2.logistics.get_channel_list?module=95&type=1>) API and select the channel with **enable=true and mask_channel_id=0** for shop products. If you publish global products without uploading shop channels, we will choose the enabled and available shop channels for you by default.

# Step 3: Publishing global product

API: [_v2.global_product.create_publish_task_](<https://open.shopee.com/documents/v2/v2.global_product.create_publish_task?module=90&type=1>)

For the optional fields of [_v2.global_product.create_publish_task_](<https://open.shopee.com/documents/v2/v2.global_product.create_publish_task?module=90&type=1>) , if you do not upload, Shopee will do some processing and upload to shop products. If you upload, it will be a custom value and Shopee will not do any processing. The specific logic is as follows:

Field Name| Upload the custom value  
---|---  
**item_name**| **YES** : Seller need to translate into local language then upload **NO** : Shopee will help translate into the local language  
description_info/description| **YES** : Seller need to translate into local language then upload**NO** : Shopee will help translate into the local language  
original_price| **YES** : Seller need to upload the price in local currency**NO** : Shopee calculates local prices based on the price of global products and calculation formulas.  
tier_variation--name| **YES** : Seller need to translate into local language then upload**NO** : Shopee will help translate into the local language  
tier_variation--option_list--option| **YES** : Seller need to translate into local language then upload**NO** : Shopee will help translate into the local language  
image| **YES** : Seller uploads the custom images**NO** : Shopee will copy the images of global products  
  
 

After a successful API call, you will get a publish_task_id.

API: [_v2.global_product.get_publish_task_result_](<https://open.shopee.com/documents/v2/v2.global_product.get_publish_task_result?module=90&type=1>)

This API will return whether the publish task was successful or not. If it succeeds, it will return the item_id, shop_id, and region information, if it fails, it will return the specific reason for the failure.

 

Please note: If the published shop is the SIP primary shop, then after the successful publication, Shopee will automatically publish the global product to the affiliated shops under the SIP primary shop.

# Step 4: Getting the list of published shop products

API: [_v2.global_product.get_published_list_](<https://open.shopee.com/documents/v2/v2.global_product.get_published_list?module=90&type=1>)

API will return the item_id and shop_id of all the shops that have been successfully published for this global product, including the shop products that Shopee automatically publishes to the affiliated shops.

 

Please note: This API does not return shop products that have been published but have not done the shop authorization.