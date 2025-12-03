# 1\. Getting product price

  * If a product has no variants, please use [_v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) API to get price information.
  * If a product has variants, please use [_v2.product.get_model_list_](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>) API to get price information.



 

 

API response:

 

"price_info": [

                    {

                        "current_price": 7678,

                        "original_price": 13960,

                        "inflated_price_of_current_price": 9137,

                        "inflated_price_of_original_price": 16612,

                        "currency": "COP"

                    }

 

 

**Please note that:**

1\. If your product has ongoing promotion, **current_price** will show the promotion price during the promotion period. If not, current_price=original_price. **original_price** indicates the original price of the product.

 

2.If your product has multiple promotions, you can get each promotion price through [_v2.product.get_item_promotion_](<https://open.shopee.com/documents/v2/v2.product.get_item_promotion?module=89&type=1>) API.

 

3\. If you are an ID / CO / PL seller, **inflated_price_of_current_price** /**inflated_price_of_original_price** means the price with tax; if you are a seller from other regions, inflated_price_of_current_price=current_price, inflated_price_of_original_price=original_price.

 

# 2\. Updating product price

**API:**[**_v2.product.update_price_**](<https://open.shopee.com/documents/v2/v2.product.update_price?module=89&type=1>)

  * If a product has variants, you can upload multiple variants of this product to update the price in one call.
  * This API only supports updating one item_id in one call. if you need to update more than one item_id, you can request them multiple times.
  * Please check that the range of price can be updated by price_limit in the [_v2.product.get_item_limit_](<https://open.shopee.com/documents/v2/v2.product.get_item_limit?module=89&type=1>) API.



 

 

2.1 _Example of updating the price of a product without variants._

_{_

_"item_id": 1000,_

_"price_list": [{"original_price": 11.11}]_

_}_

 

2.2 _Example of updating the price of a product with variants._

_{_

_"item_id": 2000,_

_"price_list": [{"model_id": 3456, "original_price": 11.11}, {"model_id": 1234, "original_price": 22.22}]_

_}_

 

Note that if you are an ID / CO / PL seller, the original_price is updated to be the untaxed price.

 

# 3\. Updating global product price

 _*The following is only applicable to cross-border sellers who have upgraded CNSC/KRSC._

 

API: [_v2.global_product.update_price_](<https://open.shopee.com/documents/v2/v2.global_product.update_price?module=90&type=1>)

  * If a global product has variants, you can update the price of multiple variants of this global product in one call.
  * This API only supports updating one global_item_id in one call, if you need to update more than one global_item_id, you can request it multiple times.
  * For the price of the global product, please check the price currency first through the [_v2.merchant.get_merchant_info_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>) API.
  * If you want the price of global products automatically synchronized to shop products, please set the price synchronization toggle open through the [_v2.global_product.set_sync_field_](<https://open.shopee.com/documents/v2/v2.global_product.set_sync_field?module=90&type=1>) API . Shopee will automatically update based on the formula. If not, you can update the price through [_v2.product.update_price_](<https://open.shopee.com/documents/v2/v2.product.update_price?module=89&type=1>) API.



 

# 4\. Getting product stock

 

  * If a product has no variants, please use [_v2.product.get_item_base_info_](<https://open.shopee.com/documents/v2/v2.product.get_item_base_info?module=89&type=1>) API to get the stock information.
  * If a product has variants, please use [_v2.product.get_model_list_](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>) API to get the stock information.



 

API response:
    
    
    {      
    
                    "stock_info_v2": {
    
                        "summary_info": {
    
                            "total_reserved_stock": 0,
    
                            "total_available_stock": 389
    
                        },
    
                        "seller_stock": [
    
                            {
    
                                "location_id": "IDZ",
    
                                "stock": 90
    
                            }
    
                        ],
    
                        "shopee_stock": [
    
                            {
    
                                "location_id": "IDG",
    
                                "stock": 99
    
                            },
    
                            {
    
                                "location_id": "IDM",
    
                                "stock": 200
    
                            }
    
                        ]
    
                    }
    
                }

 

Please note:

  * Product may have both **seller_stock** and **shopee_stock** , or it may have stock from multiple locations.
  * For more stock calculation logic, please refer to the [_FAQ_](<https://open.shopee.com/faq?top=162&sub=166&page=1&faq=230>)



 

# 5\. Updating product stock

API: [_v2.product.update_stock_](<https://open.shopee.com/documents/v2/v2.product.update_stock?module=89&type=1>)

  * If a product has variants, you can upload multiple variants of this product to update the stock in one call.
  * This API only supports updating one item_id in one call, if you need to update more than one item_id, you can request it multiple times.
  * Sellers can only update **seller_stock** , cannot update **shopee_stock**.
  * Please check the stock_limit in the [_v2.product.get_item_limit_](<https://open.shopee.com/documents/v2/v2.product.get_item_limit?module=89&type=1>) API for the range of stock that can be updated.



 

5.1 _Example of updating the stock of a product with no variants._

_{_

_"item_id": 1000,_

_"stock_list": [{"seller_stock": [{"stock": 100}]}]_

_}_

 

5.2 _Example of updating the stock of a product with variants._

_{_

_"item_id": 2000,_

_"stock_list": [{"model_id": 3456, "seller_stock": [{"stock": 100}]}, {"model_id": 1234, "seller_stock": [{"stock": 100}]}]_

_}_

 

Please note：

  * If a product has variants, the price difference between the variations cannot exceed a certain multiple. For example, BR product, the price of the most expensive variations divided by the price of the cheapest variations cannot exceed 4.

Region| multiple  
---|---  
BR| 4  
SG/VN/TW/TH/PH/MX| 5  
ID/MY| 7  
CL/CO| 9  
CNSC| 7  
  
  * The product participates in certain promotion, sellers are not allow to modify the original price of the product. More detail please check FAQ: <https://open.shopee.com/faq/140>



  
 

# 6\. Updating global product stock

 _*The following is only applicable to cross-border sellers who have upgraded CNSC/KRSC._

 

API: [_v2.global_product.update_stock_](<https://open.shopee.com/documents/v2/v2.global_product.update_stock?module=90&type=1>)

  * If a global product has variants, you can update the stock of multiple variants of the global product in one call.
  * Since cross-border sellers who have upgraded CNSC/KRSC can only manage shop product stock through global product, it means you can only call the [_v2.global_product.update_stock_](<https://open.shopee.com/documents/v2/v2.global_product.update_stock?module=90&type=1>) API to update stock. After updating global product stock, it will be automatically synchronized to shop products. Using the [_v2.product.update_stock_](<https://open.shopee.com/documents/v2/v2.product.update_stock?module=89&type=1>) API to update the stock will result in an error.
  * This API only supports updating one global_item_id at a time, if you need to update more than one global_item_id, you can request it multiple times.
  * Please check the stock_limit in the [_v2.global_product.get_global_item_limit_](<https://open.shopee.com/documents/v2/v2.global_product.get_global_item_limit?module=90&type=1>) API for the range of stock that can be updated.