# What is SIP?

The full name of SIP is Shopee International Platform (Shopee International Platform). After participating in the SIP project, Shopee will help you operate the shop , including setting up and submitting marketing activities according to the characteristics of the local market. After opening the shop, you only need to bind the receiving account in advance, regularly check the product inventory, participate in various promotion to confirm the price, and deliver the goods according to the delivery time limit!

# Terminology:

**P shop (primary shop)** : In the SIP agent operation mode, the shop independently operated by the seller is also called the primary shop;

**A shop (affiliated shop)** : Shopee helps the seller to operate the agency shop, also known as the affiliated shop;

**CB SIP (cross border SIP)** : If cross-border sellers operated the primary shop, we call that CB SIP mode ;

**Local SIP** ：If local sellers operated the primary shop, we call that local SIP mode ;

**SIP rate** : Applies to CBSIP only. The SIP price adjustment ratio refers to the discount rate set by the seller for the affiliated shop based on the cost price of the product. When the product is sold in the affiliated shop, Shopee will automatically calculate the final settlement price for the seller based on the cost price of the product and the SIP price adjustment ratio.

**SIP Item price** : The cost price of the product, based on which Shopee will calculate the selling price of the A shop product and the settlement price of the product.

**Settlement price** : The settlement price of the product, Shopee will settle to the seller based on this price.

# 1.SIP Shop Authorization

## 1.1 non CNSC Seller 

### 1.1.1 Authorization process

 

Please refer to article [_Authorization and Authentication_](<https://open.shopee.com/developer-guide/20>). When the seller login the SIP P Shop account, enters the authorization page and clicks to confirm the authorization, SIP P Shop will be authorized this APP.

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=yLwnS3C1k8%2Fg1GDJDl6bD6%2F%2Fsh05qS4kIyA09ui8PuLlEGKYnnraA64V2QkaEHI3vmLqL6ysjRdp5IaCyZ3xTw%3D%3D&image_type=png)

### 1.1.2 Getting code

After the authorization is successful, you can directly get the shop_id of P Shop and the available code through the callback url.

### 1.1.3 Getting P shop token

 

You can call [_v2.public.get_access_token_](<https://open.shopee.com/documents/v2/v2.public.get_access_token?module=104&type=1>) API and upload the shop id and code of P shop after successful authorization. API will return the access token and refresh token which are available to P shop.

### 1.1.5 Refresh Access token

 

At this time, the access token and refresh token obtained in the third step can be used in P shops. Then you can call [_v2.public.refresh_access_token_](<https://open.shopee.com/documents/v2/v2.public.refresh_access_token?module=104&type=1>) API and refresh the access token and refresh token of P shop.

 

Note ⚠️:

1\. After the new access_token is generated, the old access_token is still valid within 5 minutes.

2\. Re-authorization will trigger refreshing refresh_token and access_token.

3\. Call the Refreshaccesstoken interface within the validity period of the authorization.

4\. If the new refresh_token and access_token returned are lost, please check [_FAQ_](<https://open.shopee.com/faq?top=177&sub=180&page=1&faq=216>)

 

## 1.2 CNSC Seller

### 1.2.1 Authorization process

 

Please refer to article [_Authorization and Authentication_](<https://open.shopee.com/developer-guide/20>). When the seller logs in to the main account and enters the authorization page, the shop list under each merchant will display the label "SIP" for the SIP P Shop, and you can click "view" to see all the A Shops Information and Authorization Status. Check the SIP P Shop and click “Confirm Authorization”, then all SIP A Shops under the P shop at this time will be automatically authorized to this APP.

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=p7VFHqvLGexYcmw3aC9B%2Bl%2FWh9BkEgcD3eFrEbuggMlJjt30PAznJKXU7lB%2F7g%2BjYBIlR3K%2FW3qiLzgf4MSpkw%3D%3D&image_type=png)

 

Note ⚠️

All shops that are not bound to a merchant in a main account will be listed under the "Unupgraded Shop Group" list. If the shops in the Unupgraded Shop Group list have SIP logos, it also means that they are SIP P Shops.

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=FVuWEyV%2BTn2dLLVzaxrZR%2BEtGCIsL0RCRxchMk3Hohl9KODaAtsnaTG1hfJr0%2F9cttmv7B0hn1sWC5N6Oo8QMA%3D%3D&image_type=png)

### 1.2.2 Getting code

 

After the authorization is successful, you can directly get the main_account_id and the available code through the callback url.

 

### 1.2.3 Getting token

 

You can call [_v2.public.get_access_token_](<https://open.shopee.com/documents/v2/v2.public.get_access_token?module=104&type=1>) API，and upload the main_account_id and code after successful authorization. The merchant_id_list will return all the currently authorized merchants, and the shop_id_list will return all the currently authorized shops, including SIP P shop, A shop and non-SIP shop ids. Access_token and Refresh_token can be shared by all merchant ids and shop ids at that time.

 

### 1.2.4 Getting shop relationship

Then you need to call [_v2.merchant.get_shop_list_by_merchant_](<https://open.shopee.com/documents/v2/v2.merchant.get_shop_list_by_merchant?module=93&type=1>) API，to get the list of authorized shops associated with a merchant, and call [_v2.shop.get_shop_info_](<https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1>) API. Then you will get information like 1)Whether the shop belongs to the SIP shop. 2)The A shop list under one P shop.

 

  * If it is an normal shop, is_sip=false and the sip_affi_shops field won’t be returned;
  * If it is a SIP P shop, is_sip=true, the sip_affi_shops field will be returned and will be the A shop id list;
  * If it is a SIP A shop, is_sip=true and the sip_affi_shops field won’t be returned.



 

### 1.2.5 Refresh Access Token

Please note that the access_token and refresh_token of each shop id and each merchant id need to be saved separately. When you call [_v2.public.refresh_access_token_](<https://open.shopee.com/documents/v2/v2.public.refresh_access_token?module=104&type=1>) API, please refresh the access token and refresh token of each shop id and each merchant id respectively. 

# 2\. Product Management

## 2.1 Product information logic

 

Info| Sync logic  
---|---  
Item base info (item name/description.etc)| Create: After the seller creates a P shop product, Shopee will automatically translate the product information into the local A shop language and create an A shop product.  
 Update: If the seller modifies the P shop product, Shopee will automatically synchronize the new product information to the A shop product.  
Item status| If the P shop product is unlisted or deleted, the A shop product will also be unlisted or deleted. Seller cannot update the item status of the A shop product.  
Item stock| The product stock of P shop is equal to the product stock of A shop. For example, there are 2 A shops under P shop, A shop1 and A shop2, and the stock of P shop=10, then the stock of A shop1= A shop2=10. When A shop1 sells 1 item, the stock of P shop=A shop1=A shop2=9.  
Item price| When the seller updates the product price in P shop, Shopee will synchronize it to the product price in A shop.  
  
## 2.2 Price logic

SIP Item Price

[ _v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) And [_v2.product.get_model_list_](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>) API response: 

 "price_info": [

                    {

                        "currency": "MYR",

                        "original_price": 179.58,

                        "current_price": 179.58                   

                       **"sip_item_price_currency": "CNY",**

                       **"sip_item_price": 230.87,**

                       **"sip_item_price_source": "auto"**

                    }

Note⚠️

  * If the item is a P shop item and does not contain variations, please call the [_v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) API to get the sip_item_price/sip_item_price_source/sip_item_price_currency of item。
  * If the item is a P shop item and does not contain variations, please call the [_v2.product.get_model_list_](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>) API to get the sip_item_price/sip_item_price_source/sip_item_price_currency of model。
  * If the item is a non SIP P shop item sip_item_price/sip_item_price_source/sip_item_price_currency fields will not return by [_v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) and [_v2.product.get_model_list_](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>) API



# 3\. Order management

## 3.1 Order synchronization logic

### 3.1.1 CB SIP

Please obtain the SIP P shop order list and the SIP A shop order list respectively for fulfillment. in:

  * The order in SIP A shop will not expose the buyer_total_amount to the P shop seller in order detail.
  * For orders in SIP A shop, the currency in the get_order_detail API will be CNY or USD.



 

### 3.1.2 Local SIP

 

Shopee automatically synchronizes the SIP A shop order to the SIP P shop, so you only need to obtain and fulfill the SIP P shop order list. Those P shop orders generated by A shop, the recipient of the order is the Shopee transshipment warehouse located in Local, the Shopee transshipment warehouse will carry out cross-border delivery and finally send it to the Buyer.

 

 

Note⚠️

For the [order push mechanism.](<https://open.shopee.com/push-mechanism/1>) The orders of P shops and A shops will be pushed at the same time. For CB SIP sellers, they need to pay attention to the push of P shops and A shops. For Local SIP sellers, they only need to pay attention to the push of P shops.

 

For more order fulfillment procedures, please refer to: [_https://open.shopee.com/developer-guide/229_](<https://open.shopee.com/developer-guide/229>)

 

# 4\. Order income

 

  1. [_v2.payment.get_escrow_detai_](<https://open.shopee.com/documents/v2/v2.payment.get_escrow_detail?module=97&type=1>) API will return the order amount of A shop currency and the corresponding P shop currency at the same time.
  2. The order income in Local SIP A shop is also converted into P currency by default, which is no different from P shop orders.



 

Please focus on the parameter of [_v2.payment.get_escrow_detail_](<https://open.shopee.com/documents/v2/v2.payment.get_escrow_detail?module=97&type=1>) API as below:

 

“✓” means api will return this parameter.

“×” means api won’t return this parameter.

Fields| SIP P shop order| SIP A shop order  
---|---|---  
escrow_amount| escrow_amount=buyer_total_amount+shopee_discount+voucher_from_shopee+coins+payment_promotion-buyer_transaction_fee-cross_border_tax-commission_fee-service_fee-seller_transaction_fee-seller_coin_cash_back-escrow_tax-final_product_vat_tax-final_shipping_vat_tax-drc_adjustable_refund-reverse_shipping_fee+rsf_seller_protection_fee_claim_amount-rsf_seller_protection_fee_premium_amount+final_shipping_fee(could be postitive/negtive).| escrow_amount=sum of all Asku's settlement price - service_fee - commission_fee -seller_return_refund - drc_adjustable_refund.  
buyer_total_amount| ✓| ×  
actual_shipping_fee| ✓| ×  
buyer_paid_shipping_fee| ✓| ×  
buyer_transaction_fee| ✓| ×  
estimated_shipping_fee| ✓| ×  
campaign_fee| ✓| ×  
coins| ✓| ×  
cross_border_tax| ✓| ×  
escrow_tax| ✓| ×  
final_product_protection| ✓| ×  
final_product_vat_tax| ✓| ×  
final_shipping_fee| ✓| ×  
final_shipping_vat_tax| ✓| ×  
seller_transaction_fee| ✓| ×  
order_chargeable_weight| ✓| ×  
original_cost_of_goods_sold| ✓| ×  
original_shopee_discount| ✓| ×  
payment_promotion| ✓| ×  
reverse_shipping_fee| ✓| ×  
rsf_seller_protection_fee_claim_amount| ✓| ×  
rsf_seller_protection_fee_premium_amount| ✓| ×  
seller_coin_cash_back| ✓| ×  
seller_discount| ✓| ×  
seller_lost_compensation| ✓| ×  
seller_shipping_discount| ✓| ×  
seller_transaction_fee| ✓| ×  
shipping_fee_discount_from_3pl| ✓| ×  
shopee_discount| ✓| ×  
shopee_shipping_rebate| ✓| ×  
voucher_from_seller| ✓| ×  
voucher_from_shopee| ✓| ×  
aff_currency| ×| ✓  
commission_fee_pri| ×| ✓  
drc_adjustable_refund_pri| ×| ✓  
escrow_amount_pri| ×| ✓  
original_price_pri| ×| ✓  
refund_amount_to_buyer_pri| ×| ✓  
seller_return_refund_pri| ×| ✓  
service_fee_pri| ×| ✓  
sip_subsidy_pri| ×| ✓  
pri_currency| ×| ✓  
sip_subsidy| ×| ✓  
  
#  

# 5\. API permission

 

Currently, SIP A shop can only call some APIs, please check the detailed [_list_](<https://open.shopee.com/faq?top=162&sub=166&page=1&faq=214>).