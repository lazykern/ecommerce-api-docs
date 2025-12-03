# Summary
More sellers are deploying ShopAds. To make sure your connector app is ads-ready, please ensure two fields are included when you are calling the Create Product and Edit Product API: external_sku_id (The SKU ID in the other platform) and external_url (The product listing page URL). All TikTok 1P connector apps are making this update as well.

These two fields are under [Create Product API / Edit Product API -> Skus](create-product).

To construct the external_url, you can combine store domain with product handle using the relevant APIs from the connector platform.