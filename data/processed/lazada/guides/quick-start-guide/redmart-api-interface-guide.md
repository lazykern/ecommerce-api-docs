This document will guide Redmart developers on how to use the Open Platform to request the new version of the Redmart API.

# Register for an open platform account

## Registration link

<https://open.lazada.com/apps/user/register>

## Registered Email and Password Conditions

a. The password needs English+number+symbol, and the symbol cannot use "!" "<" 、">"；

b. The registered mailbox should not have a "+".

![image](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1710829696683_h0V2ygpP)

#### After registration, you need to fill in profile information first, and wait for review after submission

![image](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1710829697497_Ut6bMBAs)

**After completing the profile submission according to your actual situation, your profile will be reviewed and completed within 1~3 working days, and the registration process of the open platform will be finished after the review.**

# Redmart APP Creation

Before calling the API you need to create the Redmart APP.

  1. Select the Redmart category and click "Apply".
  2. Fill in the reason for your application.
  3. Wait for the application to be approved (this will usually be done within 1 to 3 business days).
  4. Click "Create APP".
  5. Fill in the app information to complete the creation of the app.



![](https://tida.alicdn.com/oss_1710830814052_null_SCp6DiKD)

## APP Parameter Introduction

![](https://tida.alicdn.com/oss_1711691072531_null_3x869hU8)

  1. It is used for the developer's system to receive the authorization code after the seller's authorization, and the detailed process of the seller's authorization will be introduced in the next section;
  2. Each app has a unique APPKEY, which is a necessary parameter when sending requests to the Open api, and is used to distinguish the accounts to which different requests belong;
  3. Used to generate a signature to ensure the security of the request parameters, the specific use will be introduced in the "Call Open API" section;
  4. The current status of the app is categorized into "Testing", "Onlice" and "Offline". The testing status will limit the number of sellers that can be authorized by the app, the access token validity and the daily API call traffic. If your app has completed the test, you can click "Apply Online" in the upper right corner to apply for online.
  5. The maximum number of API calls each app can make in a 24-hour period, beyond which all requests will be blocked until the total number of calls in a 24-hour period is reduced to within the maximum number;
  6. APP's authorization method, Redmart category authorization method is "AAllow login users to authorize", This means that sellers can log in for authorization directly from the document in the "Seller Authorization" section.
  7. The validity time of the Access token (the Access token needs to receive an authorization code using the callback address in point 1, and then use the authorization code to redeem it for an Access token);
  8. The validity time of Refresh token. When the Access token expires, but the Refresh token is still valid, the developer can call the API to use the Refresh token to get a new Access token.The Refresh token itself can not be refreshed, when the Refresh token expires, you can only re-authorize to get a new Refresh Refresh token cannot be refreshed by itself.
  9. There is a limit to the number of sellers that can be authorized for each app, and different categories have different quantity limits;
  10. Categories of APIs that can be called by the current APP, APIs outside of the categories cannot be called;



# Seller Authorization

## Service endpoint

**Environment** |  **Service address**  
---|---  
Central: for all countries (SG/MY/TH/VN/ID/PH) |  <https://auth.lazada.com/rest>  
  
## Authorization steps

![image](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1710829699165_2gVeOnF8)

[Detailed authorization steps](<https://open.lazada.com/apps/doc/doc?nodeId=10777&docId=108260>)

# Call Open API

## Service endpoint

**Region** |  **Service address**  
---|---  
Singapore |  <https://api.lazada.sg/rest>  
  
The Open API needs to be linked via an HTTP request, requiring a TLS version of no less than 1.1 or it may not be requested.

## Call API with official SDK

The open platform provides SDKs for some programming languages, which developers can download from APP Console - Development - Testing Toos - SDK Download section.

![image](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1710829699544_bgdtmHHE)

### Environment requirements

  * JAVA SDK requires Java SE/EE 1.5 or newer version
  * .Net SDK requires .NET Framework 2.0 or newer version (Windows Phone platform not supported）
  * PHP SDK requires PHP 5 or newer version
  * Python requires Python 3.0 or newer version
  * For Ruby, you can install it directly [here](<http://www.rubydoc.info/gems/lazop_api_client/1.1.0?spm=a1zq7z.man108064.site_detail.1.4cce7c73cojift&file=1.1.0>).



### [SDK sample codes](<https://open.lazada.com/apps/doc/doc?nodeId=10541&docId=108137>)

## Call API with HTTP requests

Before initiating an HTTP request, you need to understand the Open Platform's signature parameters as well as the signature algorithm so that your request can pass the Open Platform's checksum.

### sign method

sha256

### [signature algorithm](<https://open.lazada.com/apps/doc/doc?nodeId=10450&docId=108068>)

### [HTTP request sample](<https://open.lazada.com/apps/doc/doc?nodeId=10451&docId=108069>)

# How to get store id

1, Login to Seller Center

2, Switch Store page will show all your Store IDs

![](https://tida.alicdn.com/oss_1716365607750_null_n4ppcCLD)

# Old Redmart API Migration Guide

Old Redmart API |  API Path |  New Redmart API |  API Path  
---|---|---|---  
Get all Products |  /v1/products |  [RssGetProducts](<https://open.lazada.com/apps/doc/api?path=/rss/products/get>) |  /rss/products/get  
Get one Product |  /v1/products/{productId} |  [RssGetProduct](<https://open.lazada.com/apps/doc/api?path=%2Frss%2Fproduct%2Fget>) |  /rss/product/get  
Get all Pickup Locations |  /v1/pickup-locations |  [RssGetPickupLocations](<RssGetPickupLocations>) |  /rss/pickupLocations/get  
Get one Pickup Location |  /v1/pickup-locations/{pickupLocationId} |  [RssGetPickUpLocation](<https://open.lazada.com/apps/doc/api?path=%2Frss%2FpickupLocation%2Fget>) |  /rss/pickupLocation/get  
Get all Stock Lots |  /v1/products/{productId}/pickup-locations/{pickupLocationId}/stock-lots |  [RssGetStockLots](<https://open.lazada.com/apps/doc/api?path=%2Frss%2FstockLots%2Fget>) |  /rss/stockLots/get  
Get one Stock Lot |  /v1/products/{productId}/pickup-locations/{pickupLocationId}/stock-lots/0 |  [RssGetStockLot](<https://open.lazada.com/apps/doc/api?path=%2Frss%2FstockLot%2Fget>) |  /rss/stockLot/get  
Update one Stock Lot |  /v1/products/{productId}/pickup-locations/{pickupLocationId}/stock-lots/0 |  [RssUpdateStockLot](<https://open.lazada.com/apps/doc/api?path=%2Frss%2FstockLot%2Fupdate>) |  /rss/stockLot/update  
Get Pickup Jobs  |  /v1/pickup-jobs |  [RssGetPickupJobs](<https://open.lazada.com/apps/doc/api?path=%2Frss%2Fpickup-jobs%2Fget>) |  /rss/pickup-jobs/get  
Get Pickup Job   | /v1/pickup-jobs/{pickupJobId} | [RssGetOnePickupJob](<https://open.lazada.com/apps/doc/api?path=%2Frss%2Fpickup-job%2Fget>) | /rss/pickup-job/get