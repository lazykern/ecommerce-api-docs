1) We recommend cross-border sellers who have upgraded CNSC/KRSC to read the following articles to create products:

  * [_Product creation preparation_](<https://open.shopee.com/developer-guide/209>)
  * [ _Creating global product_](<https://open.shopee.com/developer-guide/213>)
  * [ _Publish global product_](<https://open.shopee.com/developer-guide/215>)



2）For other types of sellers, we recommend reading the following articles:

  * [_Product creation preparation_](<https://open.shopee.com/developer-guide/209>)
  * [ _Create product_](<https://open.shopee.com/developer-guide/211>)



# API call flow overview

 _*Solid line is required process, dashed line is not required process_

## 1\. Creating Product

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=h6oVTrljpWY5S0tzciqOnG9YqfQGBKY0kK2R7CZfSaYxi3MuWqsNzSN%2BPL50gXxhG1ImXimQ2aQtAhsB2uRKEA%3D%3D&image_type=png)

## 2\. Creating global product

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Gu3z%2FttxxOY0eNPh7vBiitjykBI5B9m4U%2FJjIQu1hZGBw%2FSLdo2rBIjGjIgRnHUYaizhVXpQd7iTSbqmKX6dIw%3D%3D&image_type=png)

## 3\. Publishing global product

 

 

 

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=canaYd%2FLXy8qTVaTeWvYhivWE4ZMNJtKdBdYo0dtqMLMRjGozjA9Zb3KWiKAkWccuhYqnfzgxeLv1KWH2tPxHw%3D%3D&image_type=png)

# Data Definition

# Attribute value data type 

(input_validation_type)

  * INT_TYPE
  * STRING_TYPE
  * ENUM_TYPE
  * FLOAT_TYPE
  * TIMESTAMP_TYPE 
  * DATE_TYPE 



## Attribute input type 

(input_type)

  * DROP_DOWN
  * TEXT_FILED
  * COMBO_BOX
  * MULTIPLE_SELECT
  * ﻿MULTIPLE_SELECT_COMBO_BOX



## Logistics type 

(fee_type)

  * SIZE_SELECTION
  * SIZE_INPUT
  * FIXED_DEFAULT_PRICE
  * CUSTOM_PRICE



## Item status type

 (item_status)

  * NORMAL
  * DELETED
  * BANNED
  * UNLIST



## Translation language 

(language)

  * zh-hans：Simplified Chinese
  * zh-hant: Traditional Chinese
  * ms-my：Malay
  * en-my: English (Malaysia)
  * en: English
  * id: Indonesian
  * vi: Vietnamese
  * th: Thai
  * pt-br: Portuguese
  * es-mx: Spanish (Mexican)
  * pl: Polish
  * es-CO: Spanish (Colombia)
  * es-CL: Spanish (Chile)



## Stock type 

(stock_type)

  * 1: Shopee Warehouse stock
  * 2: Seller stock



## Product promotion type

 (promotion_type)

  * Campaign
  * Discount Promotions
  * Flash Sale
  * Whole Sale
  * Group Buy
  * Bundle Deal
  * Welcome Package
  * Add-on Discount
  * Brand Sale
  * In ShopFlash Sale
  * Gift with purchase
  * ﻿Exclusive Price



## Market Code

  * SG: Singapore
  * MY: Malaysia
  * TW: Taiwan
  * ID: Indonesia
  * VN: Vietnam
  * TH: Thailand
  * BR: Brazil
  * PH: Philippines
  * MX: Mexico
  * CO: Colombia
  * CL: Chile
  * PL: Poland