## Service address

Environment | Service address
---|---
Central: for all countries (SG/MY/TH/VN/ID/PH) | https://auth.lazada.com/rest

## Authorization steps

The figure below shows the authorization steps:

### 1\.  Concatenate authorization URL

**Sample link for authorization:**

https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=${app call back url}&client_id=${appkey}

Note that the “client_id” and “redirect_uri” should be replaced with the ones of your own application.

The following table lists the parameters and their description.![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误1_1728886354584__yXpG.jpg)

Parameter | Required? | Value | Parameter
---|---|---|---
client_id | Yes |  | The App Key of your application, assigned by Lazada Open Platform.
redirect_uri | Yes | The callback URL you provided when creating the application. | The “redirect_uri” is used for receiving the code when a seller completes the authorization. It must be the same with the callback URL you provided when creating the application on Lazada Open Platform.
response_type | Yes | code | The authorization type, with the value of “code”.
force_auth | No | true | Refresh the web browser cookie for a new authorization session.

### 2\. Guide sellers to authorize

Guide a seller to open the above authorization URL through the web browser. The following window with the login panel is displayed. The permissions to be granted to the application after the authorization are listed on the left. The seller selects the country, enters seller account and password, and clicks the “Sign in And Authorize” button to complete the authorization of the application.

  

Note:

For Cross Border sellers, you only need to authorize once for all the 6 ventures. Take the following steps to complete the authorization:

1\. Select Lazada Choice - xx” from the Country dropdown list.

2\. Authorize using the seller account and password.

3\. Use the code returned to the callback URL to get the access token. This access token can be used for authorized venture.

  

See the screen capture below.

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误2_1728886483245__DHVo.jpg)

### 3\. Retrieve authorization code

After the seller completes the authorization, Lazada Open Platform will return the authorization code to the callback URL address. Your application can retrieve the code and use it to get the Access Token. The sample authorization code is shown below.

![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_错误3_1728886529681__USEG.jpg)

Note: Note: The authorization code is valid for half an hour and can only be used once. Once it expires, it needs to be re-authorized

### 4\. Get the access_token

Use the **/auth/token/create** API to get the Access Token (access_token).

**Code sample:**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

LazopClient client = new LazopClient("https://auth.lazada.com/rest", "${appkey}", "${app_secret}");

LazopRequest request = new LazopRequest("/auth/token/create");

request.addApiParam("code", "0_100132_zQh27YbbE1AH32NY3xqxCAMQ10175");

LazopResponse response = client.execute(request);

System.out.println(response.getBody());

### 5\. Save the token

The access token will expire in a specific period (expires_in). Before it expires, the seller does not need to authorize the application again. You need to save the latest token properly.

### 6\. Sample of the token

**Notes:**

1\. The “access_token” and “refresh_token” in this sample are for reference only.

2\. For cross border sellers, the returned access token can be used for multiple sites. Therefore, the “country_user_info” section contains multiple country values.

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

{

"access_token": "50000201b01qj1ef00869sqCageT3NTwdoDuGVHQSIe3jwPENwVulOwDguQwgl",

"country": "my",

"refresh_token": "50001200701ak1d2fc8c3qMDuBlnnYOsahYGTCLP90qj7jBT7sRycHebI1SWyF",

"account_platform": "seller_center",

"refresh_expires_in": 4320000,

"country_user_info": [

{

"country": "my",

"user_id": "300253344022",

"seller_id": "300253344022",

"short_code": "MY4NBRIFM2"

}

],

"expires_in": 864000,

"account": "choice_virtual_testcbshop1803@gmail.com",

"code": "0",

"request_id": "212a6f1317090164028607735"

}

The following table lists the parameters in the token and their description.

Key | Type | Sample | Description
---|---|---|---
access_token | string | 50000601c30atpedfgu3LVvik87Ixlsvle3mSoB7701ceb156fPunYZ43GBg | Access token.
refresh_token | string | 500016000300bwa2WteaQyfwBMnPxurcA0mXGhQdTt18356663CfcDTYpWoi | Refresh token, used to refresh the token when “refresh_expires_in”>0.
expires_in | number | 25920 (expires in 25920 seconds) | The expiring time of the access token, in seconds. For APPs in "Test" status, the value is 7 days. For APPs in "Online" status, the value is 30 days.
refresh_expires_in | number | 25920 (expires in 25920 seconds) | The expiring time of the refresh token. For APPs in "Test" status, the value is 30 days. For APPs in "Online" status, the value is 180 days.
country | string | sg | The country ID (sg: Singapore, my: Malaysia, ph: Philippines, th: Thailand, id: Indonesia, vn: Vietnam).
account_id | string | 706388888 | User ID, which can be ignored when “account_platform” = “seller_center”.
account | string | xxx@126.com | User account.
account_platform | string | seller_center | User platform, supporting multiple platforms.

## Refresh authorization steps

### 1\. Use “/auth/token/refresh” to refresh the access token

See the following code sample.

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

LazopClient client = new LazopClient("https://auht.lazada.com/rest", "${appkey}", "${app_secret}");

LazopRequest request = new LazopRequest("/auth/token/refresh");

request.addApiParam("refresh_token", "50000601c30atpedfgu3LVvik87Ixlsvle3mSoB7701ceb156fPunYZ43GBg");

LazopResponse response = client.execute(request);

System.out.println(response.getBody());

The returned data structure by “/auth/token/refresh” is the same with that by getting the access token with authorization code. You will get new “access_token” and “refresh_token”. You must save the latest “refresh_token” for getting the new “access_token”. Note that the duration of the access token will be reset, but the duration of the refresh token will not be reset. After the refresh token expires, sellers need to re-authorize your application to generate new access token and refresh token.

**Usage notes**

1Sellers do not need to authorize again before the token expires.

2If “refresh_expires_in” = 0, the access token cannot be refreshed. Only when “refresh_expires_in” > 0, you can call the /auth/token/refresh API to refresh the access token.

3If token needs to be refreshed, it is recommended to refresh it 30 minutes before the token expires.