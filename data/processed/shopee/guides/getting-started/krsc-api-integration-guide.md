# 1\. What is KRSC

 

The full name of KRSC is the Korean Seller Center. It is a seller center for Korean cross-border sellers. Sellers can manage the products, orders, and marketing of multiple shops through it. For the basic operation guide and introduction of KRSC, please click [_here_](<https://shopee.kr/edu/article/10732>).

 

Important: KRCB Sellers and KRCB shops managing ERP developers (ISVs) need to pay attention who upgrade to KRSC need to pay attention that the product API needs to replace other APIs. The APIs you need to be developed include [_Global Product API_](<https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1>) and [_Merchant API_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>). And make sure that you have used V2.0 shop authorization.

If KRSC API - Global Product API and Merchant APIs are not integrated, KRSC upgraded shops cannot use API calls for Product listing related modules.

 

FAQ:

Q:How to judge whether a shop has been upgraded to KRSC?

A:You can query the v2.shop.get_shop_info API and the api returns the parameter merchant_id, then query the v2.merchant.get_merchant_info,  merchant_region=KR, which means that the shop has been upgraded to KRSC.

 

Q:If my system does not have product-related functions, that is, it does not include product creation and product update functions, do I need to connect to do some adjustment?

A:No need, such as order-related API, there is no change for api call flow.

# 2\. How to integrate KRSC API

## 2.1 Register as a developer（If you already have a developer account, you can skip this step）

 

a. Click "Sign up" and read "Agreement", and register a Shopee Open Platform account by email. [_https://open.shopee.com/_](<https://open.shopee.com/>)

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=07DNyyfCiU9Ua3QSELO5rrCrGiGREHeTKPWY%2Fkw7%2FlgAhjfyQ4qbef0gTUCzmSJAUzOph5HMQ%2B5lz73IOs%2BZWQ%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=BVs0FCmQ%2B1zwxPsYrUatW6Pjzm5QEIdLUNMuB%2B2DPPjBEqyMNuLz4wZAFFvOC5dj3wzkRDJc1Fk43qX5QIdhhg%3D%3D&image_type=png)

 

b. You will receive a verification email, please verify your email and set a password.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=BAQ1eWOJR6mWBitGCpYucjrV4Gy32V6Mhrd6zFw4jNpw2SnjMfb2edrYAmqX6bFnmpsrdRTQ7jAFoCgLiNaMZg%3D%3D&image_type=png)

 

c. Login with your account.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=xkNBehrdYmvsiqY16RwrOvm%2FZYhmJ3Swg4Ev%2BH4kS6BofNHitA3OuUkDmB%2FmO6i47Rw4M5NX60gRPXiIjq4PXA%3D%3D&image_type=png)

## 2.2 Complete account information （If you already have an approved developer account, you can skip this step）

 

a. Please refer to this [_article_](<https://open.shopee.com/documents/v2/Introduction?module=87&type=2>) to find out what type of developer account you are. Login to Open Platform >> Console >> App List >> Select developer type >> Add

*Different types of developers will own different types of apps. For details, please refer to [_App management_](<https://open.shopee.com/developer-guide/14>) __ page.

 

b. Complete the appropriate profile according to the type of developer you choose. The information needs to be reviewed by the Shopee platform.

## 2.3 Create an app

 

To call Shopee OpenAPI, you need to create an App first. You can create apps after the developer profile is approved.

 

**Noted**

*Original APP type does not support V2.0 api, If your existing app is Original type, please complete the app upgrade according to this [_announcement._](<https://open.shopee.com/announcements/553>)

*For other types of app types, please check the API permission according to this [_article_](<https://open.shopee.com/documents/v2/Developer%20Types%20and%20APP%20Types?module=87&type=2>).

 

If you don't have an app, you can create one through this path

**Path：** Open Platform >> [_Console_](<https://open.shopee.com/myconsole/management/app?from=header>) >> App List >> \+ Create App >> Fill in the information >> Submit

## 2.4 Go live app

 

You must make sure your app status is online. Click "Go-Live" to request to use the Live environment API.

Open Platform >> [_Console_](<https://open.shopee.com/myconsole/management/app?from=header>) >> App List >> Select the APP to be launched >> Click Go live >> Fill in the information >> Submit

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=1bRneJcp7OTLdjQ82C7VENn4FpvXw2%2FiWNE%2BsGrbXbnENjzi1aGeSXZFjsZhzMiaDL6W%2Fjkc9Ih40BDl6OF3IQ%3D%3D&image_type=png)

 

APP will automatically complete the review after 24 hours and the APP status will change to the Online status, and the developer will obtain the Live Partner id and Partner Key of the Live environment.

## 2.5 Start API testing

 

a. Until KRSC Sandbox is ready, KRSC Devs can use CNSC Sandbox to test API since the function is similar to KRSC.

1) To start testing, you should create a China merchant on [_Console_](<https://open.shopee.com/myconsole/tools/test-account>)  

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=ZeLHVtU8WelqVJRdsbQqeuKEbyAhzLKxIPxqn9L5FfRwKNKhatrh1jYdi2NyZx%2FqvCH7qUQhBk9rNDSGsqOu5g%3D%3D&image_type=png)

 

2）Login [_https://seller.test-stable.shopee.cn_](<https://seller.test-stable.shopee.cn>). Please note that otp is 123456.

_** Note: Kindly use google translator to translate to English or Korean if needed._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Z%2FuyR1WrCBnGHeY3KSevD%2FZY%2BH2%2FLhsbp1HO%2BzDsq%2B%2B3QK0MP%2BidCH%2FJvp5g%2BY%2F9emVg4GHbCDcYkIjcWZO5tw%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=JvSqNkMgwzqnIzsM4REnYXr%2BCOCMIzw1XejYrJ1NIDDcU%2FJcapOHkEr0BEQY%2FFmyM4prk1EiAz%2B4a6IUtupjYA%3D%3D&image_type=png)

3)  Set the currency after login.

_** Note: When testing in the CNSC sandbox, only CNY currency is available. In the actual KRSC (Live environment), the currency options will be USD or KRW._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=8oXXnc6F8lniaGfCFYR7hNaHZyjalfZAEvc6vDRREH%2FVv3Qu7ejFENdvxVvyGo7ndSYuwfdxGhbFCE5gkTe52A%3D%3D&image_type=png)

 

4) Set the market rate. If you set the wrong number, we will prompt the correct range of the number as the screenshot shown.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=fh01dA9MXGyppU17dMjT7YdJc9qG1wR26fgseQwQgIqpM%2FZd7pzgorwcIcIUR34dNq6%2BWEmjqZOqauDatrq5Bg%3D%3D&image_type=png)

5) Then, you can set the Interface language in [_Merchant setting page_](<https://seller.test-stable.shopee.cn/portal/merchant/setting/basic>) to English.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=6qhJCHNH7nYqIV2wKsFRbMofALZdOYKnFweDBLDYNXz8Cp4QUDgSYiPeOEIdAutZGGXxdyHHL96mrpv4%2BAqcGA%3D%3D&image_type=png)

6) Check the [_Global SKU page_](<https://seller.test-stable.shopee.cn/portal/product/mtsku/list>). Please finish the setting and click the button “Start to upgrade to Global SKU”

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=okLn69TBiWNkRCHNG8OXHY1GUvbCFTFJkgfucjIIEznOD8BU3c3%2FRhr64aNoFptIc1W09SXD8KdYav0QEGigHw%3D%3D&image_type=png)

 

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=xNF2eZI3wGgvOdQTYFxS5WA3OklnuIIha8pBbbxCW%2BvMBkWB5CYycsNUbvaxW41tZNIxCj5I7olFIZSgJD1Qug%3D%3D&image_type=png)

 

Then you can start to test open api. More details you can check [_Sandbox Testing_](<https://open.shopee.com/developer-guide/8>) article.

 

b. When the seller logs in to KRSC and completes the upgrade for each shops’ products, [_v2.shop.get_shop_info_](<https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1>) will return mtsku_upgraded_status:UPGRADED

c.Test [_Global Product API_](<https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1>) and [_Merchant API_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>). You can check the API call flow from [_here_](<https://open.shopee.com/documents/v2/API%20Call%20Flows?module=87&type=2>)

##  2.6 Merchant & Shop Authorization

Because after the shop account is upgraded to KRSC, multiple shops will belong to merchants, you can learn more about the relationship between Merchant and shop through this [_FAQ_](<https://open.shopee.com/faq?top=162&sub=181&page=1&faq=222>). Therefore, in order for you to call the GlobalProduct API normally, please re-authorize your shops and switch the sub account page when authorizing.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=3yR0asw1jvtA3%2F9oYcUWNIji3AdXQqe5t14vyZGkRaB9GmdCLhUT4NJEMGmPyyaGVI4Kr2cJZLRLMlFg2EQKBg%3D%3D&image_type=png)

Please use your main account for authorization. Sub-accounts cannot finish the authorization. The account format of the main account is  ***.main

 

After the account is successfully logged in, you will see the Authorization page, first check the shop you want to authorize and then check Auth Merchant. If you do not check Auth Merchant, you will not be able to call the relevant Global Product API or to obtain the Merchant information. If some shops are not checked, the product cannot be published to the related shop through the API. So please make sure you check the Merchant and shop that you manage completely.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Tl0U8usumC9hZgPO94%2FG9W5Gs4WGeeCddgO9c31Re0ftxnprH8jSRzVOPCB%2Bw%2F%2B5Tztu9Tnqcpn2JCSCHIucfA%3D%3D&image_type=png)

 

After the authorization is successful, the callback address will return the main_account_id instead of shop id. Main_account_id will be used to obtain AccessToken later.

 

Then please refresh the token according to this [_document_](<https://open.shopee.com/documents/v2/OpenAPI%202.0%20Overview?module=87&type=2>)

 

Through the GetAccesstoken API, you will get a list of all merchant ids and shop ids that have been successfully authorized at that time.

 

Note that the tokens for each merchant and each shop are independent and you need to store them separately. When you completing the authorization, the initial refresh token and access token you obtained can be shared by the currently authorized merchant id and shop id, and then you call the RefreshAccessToken API, and different merchant ids or different shop ids will return different refresh tokens and access token, so please keep their tokens separately.

 

If you want to obtain the relationship between the merchant id and the shop id, please call the [_get_shop_list_by_merchant_](<https://open.shopee.com/documents/v2/v2.merchant.get_shop_list_by_merchant?module=93&type=1>) API. You can get each merchant information by calling [_get_merchant_info_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>), and call [_get_shop_info_](<https://open.shopee.com/documents/v2/v2.shop.get_shop_info?module=92&type=1>) to get each shop information.

# 3\. Summary

 

1）When you create an app, or use an existing app, please make sure that your app type can call the v2.0 GlobalProduct API.

2）The shop needs the seller's re-authorization to provide the seller with KRSC product related API services.

3）It is necessary to ensure that the APP status is Online, so that seller users can use the KRSC API in the production environment. Clicking Go Live in the Open Platform [_Console_](<https://open.shopee.com/myconsole/management/app?from=header>) and submitting the information. APP will automatically be approved after 24 hours.

4）The seller needs to log in to KRSC and complete the relevant settings before the KRSC product upgrade is successful. Only when the product is successfully upgraded, can the Global Product API be called normally.

5）You can learn more KRSC API FAQ from here: [_KRSC API FAQ_](<https://open.shopee.com/faq?top=162&sub=181>)

 

### If you have any technical connection problems that are not covered by this document, please contact Shopee Open Platform through the [_ticket system_](<https://open.shopee.com/myconsole/ticket-system/raise-ticket>).