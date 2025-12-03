# Overall Introduction

 

（**Notice:****** After logging into the Open Console, check the Test Account function to determine whether it is a new sandbox. The new sandbox is Test Account-Sandbox v2.）

 

The sandbox environment is a testing environment provided by Open Platform to developers. It provides various types of test accounts and data. Developers can complete testing of most API scenarios in the sandbox environment. The sandbox provides basically the same functions as online, but only covers core scenarios, such as product management, order management, logistics and delivery, etc.

 

**Sandbox V2 support range:**

**Portal**| **Features**| **Remark**  
---|---|---  
**Console**|  Shop| Create test shop account|    
Order| Create test order|    
Push| Push test data|    
**Seller Center**|  Product| Create and manage the global SKU|    
Publish and manage the shop SKU|    
Order| Order|    
Ship Order| Printing of receipts is not supported at the moment, please use Open API to print.  
**Open API**|  Product| All APIs| Call through the API Test Tools in the Console, or call it yourself using the domain name https://openplatform.sandbox.test-stable.shopee.sg/ (for CN, please use https://openplatform.sandbox.test-stable.shopee.cn/)  
Global Product| All APIs  
Media Space| All APIs  
Order| All APIs  
Logistics| All APIs  
First Mile| All APIs  
Shop| All APIs  
Merchant| All APIs  
**Push**|  Supports receiving some push test data, see details 3.3  
  
(If you require additional sandbox support features, please submit a[ _ticket_](<https://open.shopee.com/console/raise-ticket>)with your specific use case and requirements.)

 

 

This document mainly introduces the process of creating test accounts, test orders and shipping in the Sandbox test environment.

# **1\. Create a test account**

 

Click Console>Select Test Account-Sandbox v2, the url is [_Create a test account_](<https://open.shopee.cn/console/tools/test-account>)

## **1.1 Local and cross-border test stores**

 Local and cross-border test stores differ in many aspects, such as store categories, available transportation channels, and other special logic.. It is recommended that developers create a test store corresponding to the service market.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=KtSWeex7pExDUSioe%2FVLXhIAkaHd9pxp0lnRkp5KympfHEebKWMnJdL0mAdNYRnW%2FqZBCcB5fEZqcLAg%2Bgvafw%3D%3D&image_type=png)

## **1.2 Merchant   **

For testing in China Seller Center (CNSC), developers can choose “**Merchant** "To create a test master account and bind merchants and stores.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=SIdzWjRn%2FkpyJRzU6DK0sv8%2BHKU9zkqnCr%2Bmp9xHBH8UxOWTZ30gV25zC5ewJSachuNBpj9Mf132slVj1274tg%3D%3D&image_type=png)

# **2.****Authorize the test account to the test Partner_id**

## 2.1**Preliminary steps:**

  1. Create APP:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=zLjqkfN6XwHX%2FVUgTiI3aw7QfXn74vluBXl7pS1A4sN1ogG%2FULCW1%2FrAhftGOp%2FMmTKZ7VF3PJ%2BwALrZD4KaqA%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=D%2BI5cRlL%2Bmg7mt9%2FJxC8Ym8pvbO%2FqT9GwJ%2B0L0i3qHR9aH9Rf7xvoTP0gMKwdxbyyr1Q2oszzeKTNAlPo%2BayzA%3D%3D&image_type=png)

  1. Create Sandbox Account:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=icgyodzJfMbJQE5hS2cEerIx%2BpoGfffuK3CoeGLDfJgYAA8AxyROYMAeUmT9Z0USxon%2B66dM7zBkityb487KRg%3D%3D&image_type=png)

You can choose the account type and create a shop or merchant type test account:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=NOO05UUX9ESG5dkQFWOgxLhP%2BH2ykRgzqlr283pnqiGh9engXIAuQp3ygM7cLQSxsCMPgrWELtU1j3JcNT0odw%3D%3D&image_type=png)

 

## **2.2 Shop authorization document**

 

**Authorization steps:**

 

For the test Partner_id, see the figure below for the specific authorization process._Can be referenced_[ _Authorization related documents_](<https://open.shopee.com/developer-guide/20>) , or follow the steps below.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=WXQp4JLdYgN0RgyM6Bots1oIlJ5GV2o1nj7M0AEPpvdeYekdOd%2Brj12%2Bib71L3BShdDaXVGozOfnigXnA8JChA%3D%3D&image_type=png)

1\. Use the authorization link and fill in the corresponding**partner_id** :

[https://open.**sandbox.test-stable**.shopee.com/auth?auth_type=seller&partner_id=***&redirect_uri=https%3A%2F%2Fwww.baidu.com%2F&response_type=code](<https://open.sandbox.test-stable.shopee.com/auth?auth_type=seller&partner_id=***&redirect_uri=https%3A%2F%2Fwww.baidu.com%2F&response_type=code>)

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=GDqlDN3m5fQ5zmp3LunPH3QvdnwYgFUWMJ8z8Dk63KlTaivAmq1Qi0%2Ff4%2B73q1fmLoGIHohRvN5vf%2BB%2BDJoJxw%3D%3D&image_type=png)

Noti: Fixed authorization URL for sandbox environment (including https://account.**sandbox.test-stable.** shopee.com), please use **Sandbox Shop Account to m** ake a login, not a live account. Otherwise, the error "Account/Password Verification Failed" will be reported.

 

2\. Fill in the corresponding Sandbox Account and log in:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=sWrBHIe%2F8%2Ft6TBwFLUv2aoBlEHgwowPuyI1j45QicotW3gxSSVFnZfgouLTdY5Dj73FfmAE7qTIbARG6uClB4w%3D%3D&image_type=png)

3\. Click Authorization to jump to the success page:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Aa8juVrC%2Fa1hPZEEyjNx%2FlZfP%2BNGrA03mI64p7oJQl%2FH7tHE2jO8X82QB6eqnS4gRWTu9vhjIRdhKtM8e4RNhQ%3D%3D&image_type=png)

 

## **2.3 Merchant authorization document**

For the test Partner_id, see the figure below for the specific authorization process._Can be referenced_[ _Authorization related documents_](<https://open.shopee.com/developer-guide/20>) , or follow the steps below.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=PilgyQzAGDajfT5gGnL73MiDgidTJMtghUcmDn9Ch447xYX2djXRUPOTgMFpoykQoGeFe%2FaO5dpUduPjdTzfvg%3D%3D&image_type=png)

1\. Use the authorization link and fill in the corresponding **partner_id:**

https://open.**sandbox.test-stable**.shopee.cn/auth?auth_type=seller&partner_id=**&redirect_uri=https%3A%2F%2Fwww.baidu.com%2F&response_type=code

 

2.Click "main account" for merchant authorization:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=YBr7gULlsb7l%2Bbwv45rmOXLd9Qjg8h%2Ffcm1nEZqPJkqpjKoY2DzrPLUoNaD9iX1a7R9CYiWc7Ojevy8mJB483w%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Aa3cAfQXwo9RBCv4UKUKhf8aLDEmM24yV8puY51gNnO56sIjg1hv20AlBNZCE81H0bEFj%2FNoQNk8Wrj1UjCjbg%3D%3D&image_type=png)

Noti: Fixed authorization URL for sandbox environment (including https://account.**sandbox.test-stable.** shopee.com), please use**Sandbox Merchat Account** Make a login, not a live account. Otherwise, the error "Account/Password Verification Failed" will be reported.

3\. The verification code is “123456”

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Wq6vfTq3s4QRx%2FgWTu8aYeKJubxXwvPU4ckbauzt6QW%2Bf5jl1VrZaiara%2FLYUTagxyTWSOhiQxnBOMUn1wJyEw%3D%3D&image_type=png)

4\. After logging in, check the stores that require authorization:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=wpVOH7tlrO%2BTRX4os356YpD9oOB8uP07bFdunTJ%2BbwYICP6ag0%2FEw%2B41HP7xM5x7oBuPm5ue2cC%2FfyXFeYQqww%3D%3D&image_type=png)

5\. Click Authorization to jump to the success page:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=OeXjxmuUjt2E8PDqSSUfZbW9WjquENcbghazC5%2FJADW0WL7Htn5NrUrsAWf415YRsxxQ1h%2BbLlXBW54YEum1Nw%3D%3D&image_type=png)

# **3\. Sandbox testing process**

## **3.1 Shop account**

### **3.1.1 Log in to the Seller Center**

 

Click Console>Select[Test Account-Sandbox ](<https://open.shopee.cn/console/tools/test-account>)page, click Login Seller Center on the right side of the created test store to enter the Seller Center page.

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=VI3z5tCevHC5fEww1YgcMFi2LoXTLYXNqwdXrRcgevXx34uLMPSdeKfgxqSzi%2BTjZxg9eY6xRy3IWfOamdgjsw%3D%3D&image_type=png)

 

The Seller Center page is displayed as shown below:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=06tdHdB%2F%2FLtVu9OSrh8P%2BL%2FmZplkYhdQUgQqr54SI9nlprvupRwdlMdU9vVqcqvHKRKbrWH6v03knpoJZ7%2Bgfg%3D%3D&image_type=png)

_                              _

 

### **3.1.2 Create test products**

 

3.1.2.1 You can choose to create products from SellerCenter or through Open API.

The following are test products created through Seller Center:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=ikz4IWB%2Bw4co19jkfAbeOQXPVGOn4C27Xz5QxcFIuWEOjRjttu9OlhLmT3dQ0%2BVT4nPhx6sZfUMKA9IJElm28A%3D%3D&image_type=png)

 

Fill in all required information, select Save and Publish

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=9foJwO69nmlW5hBp4%2FIsFw0gm7h7aFL%2Fd0XZzk1viwdgNjt5ukGzwOFJSwz%2BZOyfbYC1DkoDhpWf5oC8HXhDLw%3D%3D&image_type=png)

 

3.1.2.2 After successfully creating the product, the seller center can view My Products (My Products)

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=ABBNsU0dl0Gz7u%2BI4Gqb5I4mygwiMRp86RK55pEC6IHJuII3F7h%2FcVh0n0sa3CWoqFwmzT%2FAyUgnWaSLd5zJuw%3D%3D&image_type=png)

### **3.1.3 Create test order**

 

3.1.3.1 Click Console>select the Test Order page, click "Create Test Order" to pop up the order creation pop-up window.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=L%2BVs00yD0kLAGjJK%2B4hCogZPlkvW8IkrqTyqkFFmn%2B%2FIrz4DD2F%2FIGOqKo0ujUnUKCe6FKFWiWW5B48%2BoaLA4A%3D%3D&image_type=png)

 

 Click the "Shop" drop-down box and select the shop you want to create

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=4kJHKjsbs4M5XaDxlNnBnFvr%2FnTRI35hbU3isxrZOHgMzulFjmb%2BvOsnxJLODj%2BAKGkeH4gKU9qemv%2FMIn9eFA%3D%3D&image_type=png)

 Click"Select Item" under Item(s), select the item that needs to be created, and click "Confirm"

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=MzwpdeE3iuKCsNTIDjZuq%2FQNSfAICztfKj63e4bLeIJakID9JIN%2FZnOrWKljftYnrF0Ew9c7UhpfeiwWmCh1DA%3D%3D&image_type=png)

Click the "Shipping Option" drop-down box to select the fulfillment channel, and click "Create" to complete the order creation

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=RI1xnk8ur7d7rCR8FDYs%2BxVqqMQVuPCxgSyAsKSl1b0Wyyn%2BYTSeX7hw4CKp4b8bvKUW7FZ9Q4M0aLH5VG1ahQ%3D%3D&image_type=png)

3.1.3.2 Test order creation completed

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=hUp0dNWivfl%2F7F6%2FsJz1g9LhEIygggkW%2FmYhw4psP%2F2p2rqAKvfd1W4g1NLTgAPWKVMFqsyT92eGyCUgWWDncg%3D%3D&image_type=png)

 

 

### **3.1.4 View created orders**

 Enter the seller center and click "My Orders" to view the created orders

 _Note: After creating an order on the Console page, you need to wait for about 5 minutes before proceeding to the next step._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=NBexCChaFtrOvKM1fCiXXYi7R%2Fq6sV7Li%2BAQ%2BzJaDkvdgI6OGiNDivCXSkv3BRdtXTF4MnYp9DKCVPMFsCzMCQ%3D%3D&image_type=png)

### **3.1.5 Shipping**

 

Click Arrange shipment and select the shipping method (pickup/dropoff). A tracking number will be automatically generated. At this time, the order status is PROCESSED.

_Note: Please operate the shipment in the "To Ship" tab. The "All" tab may not be able to operate._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=IC4ZANYYrkJqIMcMPzEE%2BVfGcU%2Br7hfk3EhOvS2lYriX32GYMNfOSmJNVnGgtmjhny6JYx2W6Dy74awxaogypA%3D%3D&image_type=png)

_Note: The logistics channels selected for testing in different regions are different, and the order delivery methods will be different. Generally, only two delivery methods, drop off/pick up, are provided._

 

### **3.1.6 Print the form**

Currently, at the Seller Center**Printing of the form is not currently supported.** This operation. If you need to print a form, this can only be achieved through the API.

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=AxcWu6ssgJI8jUZ5ao8cwrplOsfgqW8dWebYCSj6DZ0lLQkjhYKbTA%2FCbQxJdqDLemfEHoNefo4j8OnKRZw0SQ%3D%3D&image_type=png)

_Note: The receipt can only be printed after the order is shipped successfully and before the order status reaches SHIPPED. There is no limit to the number of times it can be printed._

### **3.1.7 Order status transfer**

 

After completing the shipment in the test environment, you can enter the Console->Test Order page to operate the order flow status.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=dZFu65n8YO4NM9MafwitphAblCtert2v8Znhf0NNLFI7Ub2bAOcZ31yLhIikfPVqkz9x1RZmZTO7%2Bu2to%2Bhfzg%3D%3D&image_type=png)

3.1.7.1 Click "Pickup" and the order status will automatically change to "SHIPPED"

_Note: You need to complete Arrange Shipment in the seller center or call /api/v2/logistics/ship_order. You can click "Pickup" only when the order status is PROCESSED._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=UBTnQMW0MX1hq1QiW5GPPOUrFXFrLD%2FtXCC8XKgsywbqH7ifWFX9bTzbrlQK7gxzYEdI0jJpbLw8wbjxEF0NuQ%3D%3D&image_type=png)

3.1.7.2 Click“Deliver”When the order delivery is completed, it will change to "TO_CONFIRM_RECEIVE”

 _Note: The order needs to be in the "SHIPPED" status before you can click "_ Deliver _”_

 

 

## **3.2 Merchant account**

 

For testing of China Seller Center (CNSC), developers can choose "China Merchant" to create a main test account and bind merchants and stores.

CNSC, the full name of China Seller Center, is a seller backend customized for Chinese cross-border sellers. Sellers can manage products, orders, marketing, etc. in multiple stores through it. For basic operating instructions and introduction to CNSC, please visit[ _here_](<https://shopee.cn/edu/home>)。

### **3.2.1 Basic settings**

 

After the Merchant test account is created, log in to the main account through "login Seller Center", complete the authorization of the main account and store, and set the exchange rate conversion and price adjustment percentage of each site to facilitate subsequent interface debugging smoothly. For detailed tutorials, please refer to the Seller Learning Center:[_Required basic settings_](<https://shopee.cn/edu/courseDetail/378?lessonId=1147>)

 

_Note: If you need to enter the verification code (OTP), please enter_ _"__**123456**_ _"._

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=oZ3hV0EZ7qpla3XgIbqKge9m4s5fMwwpc19SO0o%2F5D97Ko3Jr5PpvPslENeYE12Px1H%2BcuHXtmP9eN4aWazzPg%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=Ba4rXm8lF11N1Vzqcj26x1d%2B6ZE9693xcJU0Rh%2F3TJnRiIQevfnReMot4QTFpGAMYWwuoUdwmdIF3faiS9Iqbw%3D%3D&image_type=png)

(Log in to CNSC-->Select the desired**Platform base currency unit** \-->Complete pop-up window settings-->Click OK)

 

Set the platform base currency unit and market exchange rate:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=zXMDBiI6gTh%2F6BZRWt2GCikvcrSdHmGKMjp%2BtFp%2FyKfvv1KLCb2GWdvstlqqiPMUsALxXp1GQfIpY1iw4JDsTg%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=ZgUC9e4bjpbU0CW8%2Bkv4v8x8LmShVopzkXAS9f8vY4nefBrtNDaaw%2Bz%2F6RgRgDE0DpvPzd%2BRVNiC3kEumcmBcA%3D%3D&image_type=png)

(Set the market exchange rate of the platform currency-->fill in the specific exchange rate ratio-->click OK-->complete the setting and enter CNSC)

 

Global product and store product price settings:

After entering CNSC, click on the "Global Products" page, and a pop-up window will pop up to set the prices of global products and store products.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=NoSpCQAL2%2FRCCctbq60ycM1SEKyGkUbJQdR7al9ZDrXSQ9PJJw%2B8yRVNmuVvJsbMeKIMHEfD%2B0uu%2FuFUOV%2B3rg%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=gKv%2BPlSDwmF2kotYEUkRpaT7uorWi2MJZ43DTb4Us0TPm5RLGRzLq53y%2FDbD5ShVTPeBOnAhWaJwy8DWh5PCnA%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=AA32WGy5DgjQS7w4D8Hx%2B7HG1tYXigz9rVdLbazotOq10zajMBhaR9yumzv6HPsPwh5ayjP71rX%2F5Wy6Ry%2BRpA%3D%3D&image_type=png)

 

Fill in the site price adjustment ratio, event service rate and other parameters. It can be applied to multiple stores under Main Account through "one batch filling". After filling in, click "Start Upgrading Global Products" to complete the settings:

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=%2FURuZG2quNVlp%2BhxNnGA8Rym27jGes%2Bq9D2SEulFM4URCbfRTw85%2B1raOkyLiiV4VlxShNQWLhqF%2BhCS8N3PLw%3D%3D&image_type=png)

  
Global Item FM shipment warehouse settings

In Seller center, select Settings>Store Settings>Logistics Settings>Shipping Forecast Settings, and then you can ship your products according to the standard process after the settings are completed.  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=G2tAMn27UdWfUe%2BnwnMNNzhKbG84Jsj%2BOlq%2Fdr3OvY%2FTIrqwbhzPzGg3ftUpfQAShQ%2F5BEOEuNObAnGq63MD%2BA%3D%3D&image_type=png)

  
  
**3.2.2 Add global products**

 

3.2.2.1 Click Add Global Product in the sidebar or click Add Global Product on the Global Product Page

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=TACREf9yYFOzUqpCCakAyJgJETs4r4FIDernh7FwDewn%2BpbEwg2X3oI6Qb7A034XVLhDqOHG%2Fu%2F%2FxlwGMrXOyQ%3D%3D&image_type=png)

 

3.2.2.2 Add global product details (please fill in and select each attribute according to your needs:[_Create global products_](<https://open.shopee.com/developer-guide/213>)）

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=TvriiqVM0RC5u%2FqCE1F7Xu%2FkbznmzQDeWzCABAOQgQOSeeBG4r%2FkGg1gpNwtxRw0C9DD6c%2FKEfL6pUOz3wj0lA%3D%3D&image_type=png)

### **3.2.3 Global products and store products**

 

3.2.3.1 Add and publish global products

Click Save and Publish

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=hWSOBBevZDtj1GKB07LxxeXeaxYWZ8u6DDJf%2BesA9ixP4WvZAraKGmTdlhKA1Hqy5HNHkVuNHNg%2Fh7w5BsP2RA%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=mUD4BEFgQMUD8stV1lp0cliV8M21ac0WuJ5GdJjzlem1rs3C5kXud1DUwWUoYQK5FjAcT0Yh3ALrBvMzJyDkHg%3D%3D&image_type=png)

 

3.2.3.2 Select publishing store

 

a. The picture below shows a store selected from the Singapore site (due to region restrictions, shop sites that cannot be published will be grayed out. Please select the appropriate global product information as needed)

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=cljuMvZnm9%2FQafP0KwF4%2BWK3ndhrG4ATCqZRWFdyoQfgwMCuwbdCiKW5jntXnylD0K99nU977gJymD2VGbKXhw%3D%3D&image_type=png)

 

b. Confirm the store product information and click Confirm to publish if it is correct.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=W%2BlmtKArHpx5chm8uINION5mKbmEfsyGU0sfmznOoSjRSCJbp3axeKKoKEycglbIl3QBgV%2BLNo%2BDSbJ9ue7pEA%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=MPYvMBxfHZ4cA4yoFiZsHgxs5OWlJcPZtHqPCUgUR%2Fq1jxIB3CAH2j3sUxAta5ywHhsn2kMMWPhML9hvdVNXpA%3D%3D&image_type=png)

 c.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=EzfQ5%2BtB3LfGfIQldeXhVGJv9aFBS7tTuCSJOoUqkULy9f2lscfLLIkmNjzXR1uVHESg09ciOPxt9UDt0g8nWA%3D%3D&image_type=png)

 

d. Select the store product to view the released product.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=XpE%2B7H%2FA00nxvc1YKlLQvYZAu%2Fhs0f6Vq1zfQVW29zkpxZ9eNQobx4l7rJdz3%2BeZ8cg7paR2xYj7LkhQNsXjgg%3D%3D&image_type=png)

 

e. Select to modify the inventory, price and other attributes of the item that can be updated (MPSKU)

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=9KvfrFOlPQodIL%2BGTl%2BBOkWx9umCRNkq50JIlEq1%2FJLYfg8fytShFYNfJM5QzNw7idSV1BHnkMK5h6R2wtR97A%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=%2BXLSDpiLDFLNnEtGpsSTH6VnKmesftujEPZk6XwhO%2BGSH7zWZgrmgghFOSPi9pWv%2FAh3ZAVcFO2pnDwwv3rV1Q%3D%3D&image_type=png)

 

3.2.3.3 MTSKU and MPSKU

 

Global product (MTSKU): MTSKU is equivalent to a parent product, a virtual product, which can be published to multiple regions and generate multiple product MPSKUs. 

Store item (MPSKU): item=store item. Real item visible to buyers.

 

_Note: MPSKUs will directly inherit the basic information of MTSKUs. The inventory information of MPSKUs and MTSKUs in multiple regions is the same. Sellers no longer need to manage some basic information of the same product in multiple regions. Sellers only need to modify the basic information of MTSKU, and the system can automatically modify all published MPSKUs simultaneously._

 

**3.2.5 Shipment of global orders**  
  
a. The order creation procedure is the same as Local Shop, you can refer to **3.1.3 Creating Test Orders and 3.1.4 Viewing Created Orders**.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=yZ4R3Vz6EA5RaqDPiIiqGPgNwJ%2Bc7olNpJcq7kg3hUDADueXGzTt2JD5wpHN%2FRhX3JDVbL7PtZXxaWgjSy7mBw%3D%3D&image_type=png)

b. After the order creation step is completed, find your test account under Test Account-Sandbox v2> China Merchant and CB Shops and press the button "Login Seller Center".  
After successfully logging in, go to the "My Order" page and select the site and shop for the order you created.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=zdbevtpb3mhbV%2FUgUbBPfvNOB8AAkqpN6XvJlEsKq2gg9z7raWPS5VyRXuZh9EIQxNvknsDaHAKJ0f6GtJet8w%3D%3D&image_type=png)

  
c. After switching to the corresponding shop, you can see the corresponding order, the order status flow to "To Ship" can be operated after the shipment (before shipment, please make sure that the first kilometer of the global goods shipment warehouse setup is complete).  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=s1gbYcKtBEAg8W5SirGsP5kG8plU%2FtXls8qrmIZdnx2c8BnyGtTUS8Nx9EYKR9UATlSOWXdIs0IQDrk7QjZ%2BoA%3D%3D&image_type=png)

  
  
d. Select your order and click "Arrange Shipment".

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=XuZhCqlQ5P9IoAzT7v9DKLezxT84m01oufHjRa7rx8I4dPEtJP0%2FsrX%2Fkx%2B42fbc5Fo8cbNrSGxxz%2FmyGkD5Yg%3D%3D&image_type=png)

e. Select your order, click "Arrange Shipment", select the Drop-off method, and click "Confirm" to ship your order. (CB channel only supports Drop-off method at this time)  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=crh%2BzbTN1xDjWCWUymx6xQS89FYoaqXxWf3tqT%2Fo%2B1glCdx7jkjh0tb1QYLIsRrx%2BWvjE2O561I9njYcjK2pXA%3D%3D&image_type=png)

f. After shipment, the order generates a TN as well as an AWB, which the developer can obtain as appropriate (currently only the API is supported for obtaining the AWB).  
 

![Image to View](https://open.shopee.com/opservice/api/v1/image/download/?image_id=OtYTzRk2N1m%2BwKHCNAVrnrLEpz7XBket8giWZCpGodmOurTGr9VDk%2BXK13Ntp3WhFJ9VyEMmWrhAUhw1munqvA%3D%3D&image_type=png)

  
g. Finally, return to the Test Order page and complete the simulation by clicking "Pickup" and "Deliver" to complete the subsequent fulfillment.  
After clicking "Pickup", the order will flow to "SHIPPED" status.

After clicking "Deliver", the order will flow to "TO_CONFIRM_RECEIVE" status.  
 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=mHusMAeEXgiyp6ZFJaKw73jaHXuNpCe2%2BhIz2tslCqvsQ%2FUXI9Q9rpGYzUlaINJVquR%2F%2Ba1HaEY%2BhzsriBrgKw%3D%3D&image_type=png)

h. After the fulfillment is completed, the order does not need to be operated by you, and will flow to the status of "COMPLETED" after a certain period of time, so that the fulfillment is completed.  
 

### **3.2.5 CNSC testable interface**

 

The interfaces that CNSC focuses on are related to commodity management, and testable interfaces include[ _Merchant_](<https://open.shopee.com/documents/v2/v2.merchant.get_merchant_info?module=93&type=1>) [ _GlobalProduct_](<https://open.shopee.com/documents/v2/v2.global_product.get_category?module=90&type=1>) and[ _MediaSpace_](<https://open.shopee.com/documents?module=91&type=1&id=660&version=2>)All interfaces are downloaded, and other tests are no different from ordinary stores.

## **3.3 Push Mechanism**

Click Console>select the Push Mechaniam page, select the APP with the status of Developing, and enter Set Push.

 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=40UvCQAQ0ybE4QoFRRc21avXtNglh200rWRao4Xb3LUycnqJbdNT%2FlBw%2BLN0YJEY6eQSyand9AFJleHutSnmaA%3D%3D&image_type=png)

 

The Push Mechanism in the Sandbox environment is different from the production environment. It is no longer necessary to use related operations to trigger the push. Enter the Test Call Back URL and click "Verify and Save" to complete the verification. Just click "Push Test Data" after the corresponding Push Mechaniam to receive the test data.