# 1\. What is CNSC

 

The full name of CNSC is the China Seller Center, is a customized seller backend for Chinese cross-border sellers including Hong Kong sellers, through which sellers can manage products, orders, marketing, etc. for multiple stores.For basic operation guide and introduction of CNSC, please visit [_here_](<https://shopee.cn/edu/article/4548>).

 

Important: CNSC Sellers and CNSC shops managing ERP developers (ISVs) need to pay attention who upgrade to CNSC need to pay attention that the product API needs to replace other APIs. The APIs you need to be developed include [_Global Product API_](<https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1>) and [_Merchant API_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>). And make sure that you have used V2.0 shop authorization.

If CNSC API - Global Product API and Merchant APIs are not integrated, CNSC upgraded shops cannot use API calls for Product listing related modules.

 

FAQ:

Q:How to judge whether a shop has been upgraded to CNSC?

A:You can query the v2.shop.get_shop_info API and the api returns the parameter merchant_id, then query the v2.merchant.get_merchant_info,  merchant_region=CN or HK, which means that the shop has been upgraded to CNSC.

 

Q:If my system does not have product-related functions, that is, it does not include product creation and product update functions, do I need to connect to do some adjustment?

A:No need, such as order-related API, there is no change for api call flow.

# 2\. How to integrate CNSC API

## 2.1 Register as a developer（If you already have a developer account, you can skip this step）

 

a. Click "Sign up" and read "Agreement", and register a Shopee Open Platform account by email. [_https://open.shopee.com/_](<https://open.shopee.com/>)

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=gGaCwUPLE2HHdS%2BBKjAz3ySj7NYswf%2B3WV9cZ7UQ7yC9tvDcdF1%2B1zkYmzGWrumcgbbNIOueDg4YLE2YoCo4Ng%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=NWLcz%2F945f1tPW7%2F%2BxNyNZKSujZsdsdjGB7mJ5syuLuasTv9Z31f%2BDodNmMRwapmi4a5fGWcEWBwTuoSN7UgqA%3D%3D&image_type=png)

 

b. You will receive a verification email, please verify your email and set a password.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=xm%2FYnhSZESYk6ogDZ0uGEfIHVp2ltciBoZ8MpjdqKdkY6T%2FVHbO4eNOhY5Vg6aTtn%2FwamSBxcluT3G7tX9pDkw%3D%3D&image_type=png)

 

c. Login with your account.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=mZHxLLvLsJRbucm2ZgmYdYEaBJ6MKwD4iuiBjvHfMIB2J%2BTwWq1KVrIWnQEsnWCGjt%2Bar20Bdsrf%2BLzpz9XMSQ%3D%3D&image_type=png)

## 2.2 Complete account information （If you already have an approved developer account, you can skip this step）

 

a. Please refer to this [_article_](<https://open.shopee.com/documents/v2/Introduction?module=87&type=2>) to find out what type of developer account you are. 

Login to Open Platform >> Console >> App List >> Select developer type >> Add

*Different types of developers will own different types of apps. For details, please refer to the [_App management_](<https://open.shopee.com/developer-guide/14>) __ page.

 

b. Complete the appropriate profile according to the type of developer you choose. The information needs to be reviewed by the Shopee platform.

## 2.3 Create an app

 

To call Shopee OpenAPI, you need to create an App first. You can create apps after the developer profile is approved.

 

**Noted**

*Original APP type does not support V2.0 api, If your existing app is Original type, please complete the app upgrade according to this [_announcement._](<https://open.shopee.com/announcements/553>)

*For other types of app types, please check the API permission according to this [_article_](<https://open.shopee.com/documents/v2/Developer%20Types%20and%20APP%20Types?module=87&type=2>).

 

If you don't have an app, you can create one through this path

**Path:** Open Platform >> [_Console_](<https://open.shopee.com/myconsole/management/app?from=header>) >> App List >> \+ Create App >> Fill in the information >> Submit

## 2.4 Go live app

 

You must make sure your app status is online. Click "Go-Live" to request to use the Live environment API.

Open Platform >> [_Console_](<https://open.shopee.com/myconsole/management/app?from=header>) >> App List >> Select the APP to be launched >> Click Go live >> Fill in the information >> Submit

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=fveY8Al28rmr0daw88InytN%2Fd6OuOpYQ0TonghsdhskzMZtmUbocpBp%2FDuP0kSs5nHTqXkTjhKhK7QJ9tAe7%2BQ%3D%3D&image_type=png)

 

APP will automatically complete the review after 24 hours and the APP status will change to the Online status, and the developer will obtain the Live Partner id and Partner Key of the Live environment.

## 2.5 Start API testing

 

1) To start testing, you should create a China merchant on [_Console_](<https://open.shopee.com/myconsole/tools/test-account>)  

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=DU%2BwmZ9N62QvhbZLBSuOMerNJdGUS%2BEd5qTIxApVenQA4WKpFom1ic%2BgXMtHsDzIF200jMhN%2BuksjT0kYKd%2Bjg%3D%3D&image_type=png)

 

2）Login [_https://seller.test-stable.shopee.cn_](<https://seller.test-stable.shopee.cn>). Please note that otp is 123456.

_** Note: Kindly use google translator to translate to English or Korean if needed._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Hl3wRM8dbccshnhBQD3fVIRGmcGv9wlBTVzPIB81ASe86XH8jIUadY9ZZfLop4G1Id%2Bq8Eny11zjp%2FB3BkAHPQ%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=IH7zbwmdYyuIISt4kBQ%2FS7%2BOUO97tiO5VbnOI1dkE0dL5RhRl4BbI8HIkUe4yU1e98M7GEgdoVT1gIraUHPMZA%3D%3D&image_type=png)

3)  Set the currency after login.

_** Note: When testing in the CNSC sandbox, only CNY currency is available.  _

_In the actual CNSC (Live environment), the currency options will be USD or CNY for now and support HKD in the future._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=SR8Fzkfv4QNb7e7EvU5zJZoB%2BLwOzl2rX1e6p4%2F3N7V%2FzNJWcTj9NTD1VNCchZrm2MQIVHfGIRPo2e5l2DVRDw%3D%3D&image_type=png)

 

4) Set the market rate. If you set the wrong number, we will prompt the correct range of the number as the screenshot shown.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=GVrPi9%2FAyhEg6MML1MF2hdHa5V6wBv8JZKHzac2RkyJBaeD4AkW0WyUBqdF0KlKRdNqEYPym48RYmEUZqOCetw%3D%3D&image_type=png)

5) Then, you can set the Interface language in [_Merchant setting page_](<https://seller.test-stable.shopee.cn/portal/merchant/setting/basic>) to English.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=9javNaKf8unhEUyxoBcgb8GA4w5%2FiadhKelJZlob8Z5Wxwhz1MlDxU8wLqmQgZ6WFNvHW8qRTR%2B6FlYiHnJ7Mw%3D%3D&image_type=png)

6) Check the [_Global SKU page_](<https://seller.test-stable.shopee.cn/portal/product/mtsku/list>). Please finish the setting and click the button “Start to upgrade to Global SKU”

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=BfcxgLWR%2BaNs3iGYEKyD4%2B43VVAMFbFvbpmAAGHUIeeLVmu26WDMKdsaoPSuF4hSp64EqyQ4L%2BKe%2BCpPX09tJg%3D%3D&image_type=png)

 

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=E0OsKUaufIv0%2Fef7ulzvFExmg4lkvZN6zRQSrC9Vp7yMjt4CNGeh%2FpbJqT6Vqy8gzwYMe4s9GzwaWBgdP5vBcw%3D%3D&image_type=png)

 

Then you can start to test open api. More details you can check the [_Sandbox Testing_](<https://open.shopee.com/developer-guide/8>) article.

 

b. When the seller logs in to CNSC and completes the upgrade for each shops’ products, [_v2.shop.get_shop_info_](<https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1>) will return merchant_id.then can query [_v2.merchant.get_merchant_info_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>) to check.

c.Test [_Global Product API_](<https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1>) and [_Merchant API_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>). You can check the API call flow from [_here_](<https://open.shopee.com/documents/v2/API%20Call%20Flows?module=87&type=2>)

##  2.6 Merchant & Shop Authorization

 

Because after the shop account is upgraded to CNSC, multiple shops will belong to merchants, you can learn more about the relationship between Merchant and shop through this [_FAQ_](<https://open.shopee.com/faq?top=162&sub=181&page=1&faq=222>). 

Therefore, in order for you to call the GlobalProduct API normally, please re-authorize your shops and switch the sub account page when authorizing.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=%2FtkqbH1OWRX5p%2BJqIXv4P%2F2jUkHtR4lAKGFg65Do2ok0Qw9rufVkAOU4Rg1bC%2BNpiFcgLReOQ7I%2B5WlGHNiiYA%3D%3D&image_type=png)

 

Please use your main account for authorization. Sub-accounts cannot finish the authorization. The account format of the main account is  ***.main

 

After the account is successfully logged in, you will see the Authorization page, first check the shop you want to authorize and then check Auth Merchant. If you do not check Auth Merchant, you will not be able to call the relevant Global Product API or to obtain the Merchant information. If some shops are not checked, the product cannot be published to the related shop through the API. So please make sure you check the Merchant and shop that you manage completely.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=4c9N1UeOHmOxZrOM9k9j74G56wAN%2BjJIq3QzJGaZctkPeFH0S%2B2rEl7qk5wMDRRenBwidiy2ByVpN69yXwh83A%3D%3D&image_type=png)

 

After the authorization is successful, the callback address will return the main_account_id instead of shop id. Main_account_id will be used to obtain AccessToken later.

 

Then please refresh the token according to this [_document_](<https://open.shopee.com/documents/v2/OpenAPI%202.0%20Overview?module=87&type=2>)

 

Through the GetAccesstoken API, you will get a list of all merchant ids and shop ids that have been successfully authorized at that time.

 

Note that the tokens for each merchant and each shop are independent and you need to store them separately. When you completing the authorization, the initial refresh token and access token you obtained can be shared by the currently authorized merchant id and shop id, and then you call the RefreshAccessToken API, and different merchant ids or different shop ids will return different refresh tokens and access token, so please keep their tokens separately.

 

If you want to obtain the relationship between the merchant id and the shop id, please call the [_get_shop_list_by_merchant_](<https://open.shopee.com/documents/v2/v2.merchant.get_shop_list_by_merchant?module=93&type=1>) API. You can get each merchant information by calling [_get_merchant_info_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>), and call [_get_shop_info_](<https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1>) to get each shop information.

# 3\. Summary

 

1）When you create an app, or use an existing app, please make sure that your app type can call the v2.0 GlobalProduct API.

2）The shop needs the seller's re-authorization to provide the seller with CNSC  product related API services.

3）It is necessary to ensure that the APP status is Online, so that seller users can use the CNSC API in the production environment. Clicking Go Live in the Open Platform [_Console_](<https://open.shopee.com/myconsole/management/app?from=header>) and submitting the information. APP will automatically be approved after 24 hours.

4）The seller needs to log in to CNSC and complete the relevant settings before the CNSC product upgrade is successful. Only when the product is successfully upgraded, can the Global Product API be called normally.

5）You can learn more CNSC API FAQ from here: [_API FAQ_](<https://open.shopee.com/faq?top=162&sub=181>)

###  If you have any technical connection problems that are not covered by this document, please contact Shopee Open Platform through the [_ticket system_](<https://open.shopee.com/myconsole/ticket-system/raise-ticket>).