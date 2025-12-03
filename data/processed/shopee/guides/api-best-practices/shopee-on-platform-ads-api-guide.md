# What is Shopee Ads

Shopee Ads allow you to create ads within Shopee’s platform to increase exposure for your products and shop. 

 

Learn Shopee Ads：[ _https://ads.shopee.sg/learn/faq/96/195_](<https://ads.shopee.sg/learn/faq/96/195>)

# **Ads Open API Usage** Rules

 

When using the advertising  API, you need to abide by the following rules we have listed so that Shopee can create a fair and safe market for all sellers:

  1. When processing advertising data, you need to comply with the platform's [_data protection policy_](<https://open.shopee.com/developer-guide/32>).
  2. The advertising API is limited to Shopee's official cooperative ISVs and is used with platform sellers. It can be used for shop advertising operations and official cooperation agency operation projects. The advertising API cannot be used for other purposes.
  3. shop data may not be used for any purpose other than shop operations and official Shopee cooperation projects.
  4. To retrieve seller shop data through the ISV API, you need to obtain the consent of the platform seller through the authorization process.



 

Tips: If you fail to comply with our norms and rules, you will receive a warning email from Shopee; if you fail to modify it in time, you may face our penalties.

 

# Ads Open API Instruction

 

**  Retrieve Ad Balance and Shop Settings**

  * [v2.ads.get_total_balance](<https://open.shopee.com/documents/v2/v2.ads.get_total_balance?module=117&type=1>): Use this API to retrieve the seller's real-time total ad credit balance, including both paid and free credits. Sellers can monitor their balance status through this API to ensure that the balance is sufficient for normal ad operations.
  * [v2.ads.get_shop_toggle_info](<https://open.shopee.com/documents/v2/v2.ads.get_shop_toggle_info?module=117&type=1>): Use this API to retrieve the shop’s ad settings, such as whether auto top-up and ad price optimization features are enabled.  
  
 



**Top_Up Toggle** : Enable/disable auto top-up  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=9OMZeNtLbZcBM31kOeptGJGOL9b%2FLOdIc%2BgqF5qOaCsWxSijHmVQULhecM61qncKgbVL%2BnJHmRBIfdTDtzNegg%3D%3D&image_type=png)

 

 

Campaign_Surge: Turn on/off ads price optimization in the campaign period

  * **Campaign_Surge** : Enable/disable ad price optimization  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=EmzpqKbRbsT5BPTregyG0gWD1ZHePMd4P4K8v17vMp85gdaV17e7Dlh3r4MPJ61f%2FDanJ970UPyrTtDb1paPdA%3D%3D&image_type=png)

 

**3\. Retrieve Recommended Keywords and Product Data**

  * [v2.ads.get_recommended_keyword_list](<https://open.shopee.com/documents/v2/v2.ads.get_recommended_keyword_list?module=117&type=1>): Use this API to retrieve a list of recommended keywords per item, along with optional search keywords. Sellers can also view keyword quality scores, search volume, and suggested bids.
  * [v2.ads.get_recommended_item_list](<https://open.shopee.com/documents/v2/v2.ads.get_recommended_item_list?module=117&type=1>): Use this API to retrieve a list of recommended SKUs (shop-level) with specific tags such as Hot Search, Best Seller, or Best ROI.  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=EbgTp9dVAnH68GfpojbO8W6vLlGyoWxR5F200%2Bhl%2Fivn%2B2WxNm2SYU8BhDr6ux9%2FVnReUVSBOmvNeZFphZtX8Q%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=ix5VrxQckCczwqVU%2Brwl2ZBwIZ7icdmdS5bBpXileSC8Xw8JTp6eGkL1YLsl6Fq2kxs0Iap%2BKJL5QaykSzVjqQ%3D%3D&image_type=png)

 

 

 

**4\. Retrieve Campaign-Level Data**

  * [v2.ads.get_product_level_campaign_id_list](<https://open.shopee.com/documents/v2/v2.ads.get_product_level_campaign_id_list?module=117&type=1>): Use this API to get the list of ad campaigns associated with a specific product.
  * [v2.ads.get_product_level_campaign_setting_info](<https://open.shopee.com/documents/v2/v2.ads.get_product_level_campaign_setting_info?module=117&type=1>): Use this API to retrieve detailed settings for a specific ad campaign.
  * v2.ads.get_product_campaign_daily_performance and v2.ads.get_product_campaign_hourly_performance: Use these APIs to obtain daily/hourly performance data for product-level ad campaigns.  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Z%2BrMDlvue5btmgKoCnuBY9HmvZe9y6RIKUy0QPaoFaniZpxImMcdctZhtBNVtCqNK6291zdpKJdFT4MquG7gzw%3D%3D&image_type=png)

 

**5\. Create Auto Product Ads**

  * [v2.ads.create_auto_product_ads](<https://open.shopee.com/documents/v2/v2.ads.create_auto_product_ads?module=117&type=1>) (Whitelist shop required)  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=hEbifLY5Gn3QHjJZgaR4sH6h%2FDS5AupcTKA%2BEd7D5q3mDBpyJm1fI6mc6qS2%2FQu1st2QKv5IUqJnYtN5%2FOVsow%3D%3D&image_type=png)

 

**6\. Create GMV Max and Manual Product Ads**

  * [v2.ads.create_manual_product_ads](<https://open.shopee.com/documents/v2/v2.ads.create_manual_product_ads?module=117&type=1>)  

    * To create GMV Max ads, pass bidding_method=auto
    * To create Manual ads, pass bidding_method=manual

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=U%2BsIj%2B%2Bwt6tDyxSF1%2B1dV2xukqxVTK9CQ4bNjK7PZkFHYq3r3QNKcAHOj5zMR%2FjwU%2Fdup651olL13%2Bu7rtJX4Q%3D%3D&image_type=png)

When creating manual ads (bidding_method=manual), you can use v2.ads.get_recommended_item_list and v2.ads.get_recommended_keyword_list to get suggested products and keywords for advertising. Then, input the budget, placement, and other necessary parameters to launch the ads.

 

 

**7\. Retrieve Ad Budget and ROAS**

  * [v2.ads.get_product_recommended_roi_target](<https://open.shopee.com/documents/v2/v2.ads.get_product_recommended_roi_target?module=117&type=1>): Get the ROAS (Return on Ad Spend) value when creating GMV Max ads.
  * [v2.ads.get_create_product_ad_budget_suggestion](<https://open.shopee.com/documents/v2/v2.ads.get_create_product_ad_budget_suggestion?module=117&type=1>): Retrieve budget suggestions for creating product ads.



 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=rOCfmsOIc8GuvPIIFE7OY0WnrPJvwmfRgjLftqsa2r%2FGo1Y8jV%2BuWEReIePPGQmzfm4g5i2CW23s0x%2FRNCRp6Q%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=rKnjqlBiUT9RmgKx9zuUJEqqlAogiMiq5PaoUJu6%2BHqxD8tCQVTQr4st4moQUGcdgcIkBjd9RZjX9grM9uaerQ%3D%3D&image_type=png)

 

If you encounter problems, it is recommended to check the [_Developer Guide_](<https://open.shopee.com/developer-guide/8>)and search for [_FAQ_](<https://open.shopee.com/faq?categoryId=2011>).

If you encounter problems, please log in to the Open Platform Console to [_Raise a ticket_](<https://open.shopee.com/myconsole/ticket-system/raise-ticket>).

 

 

 

**Ads service API Permission** ：<https://open.shopee.cn/faq/281>