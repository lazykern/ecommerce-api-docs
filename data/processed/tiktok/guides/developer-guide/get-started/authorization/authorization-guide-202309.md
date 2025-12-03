![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/d6fe2b8b66844b8096a70935498b11a1~tplv-10qhjjqwgv-image.image)
# Requirements
Before you begin, please ensure that you have completed the following steps:

1. [Register as a developer on Partner Center](developer-onboarding).
2. [Create an app](create-tts-app-oauth-client).
3. Verify that APIs are enabled for your app.

![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/92f31a8240f54e78a12d48b42f8d90b5~tplv-10qhjjqwgv-image.image)
# Development Shop authorization
For the purpose of testing API requests, it's recommended to get started by using a Seller Center test account through the Development Shops section of Partner Center. Seller Center tests accounts provide full Seller Center functionality, including authorization.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/244580c1b4af463d935265ce4a4e5fd0~tplv-10qhjjqwgv-image.image" width="1930px" /></div>

When authorizing an app using a test Seller Center account, you will be taken straight to the **seller authorization approval** step, allowing you to generate an access token without using an authorization link.
For more information on how to create a Seller Center test account, please visit our [Seller Center Development Shops User Guide](seller-center-development-shops).
# Step 1: Get authorization code
## Generating an authorization link
After creating an app, generate an authorization link by clicking **Copy authorization link** in the **Authorization** section of your app.
<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: If you cannot see the option to </span><span style="background-color: rgb(255, 245, 235)"><strong>Copy authorization link</strong></span><span style="background-color: rgb(255, 245, 235)">, check to see if you are still in draft mode. A custom app in draft mode will need to be published in order to generate an authorization link.</span>
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/364439f7a1214db69e7bc3bd6248734c~tplv-10qhjjqwgv-image.image)
<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: Be aware that the authorization link will differ between US and Non-US Partner Centers.</span>

**Authorization link example for US:**
```plaintext
https://services.us.tiktokshop.com/open/authorize?service_id=7172**********70150
```

**Authorization link example for Non-US:**
```plaintext
https://services.tiktokshop.com/open/authorize?service_id=7172*******70150
```

The `service_id` is the unique identity of your registered online application (client). You can obtain your `service_id` in the app details, as shown in the following image:
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/ea4e878dee024e3f865b9c89608cdab9~tplv-10qhjjqwgv-image.image)
Additionally, a `state` parameter can be added to your authorization link for extra security. The `state` is an unguessable random string that can help protect against cross-site request forgery attacks.
Please see the [OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect#createxsrftoken) documentation for an example of how to create and confirm a `state`. When encoding a `state`, remove leading and trailing white spaces.
**Authorization link with** **`state` parameter example:**
```plaintext
https://services.us.tiktokshop.com/open/authorize?service_id=7172**********70150
&state=xaoegsefowuf
```

## Seller authorization approval
After a seller opens your authorization link, they will be presented with the following authorization prompt:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/877d19da8a0e47689b2867f9a348855b~tplv-10qhjjqwgv-image.image" width="500px" /></div>

After clicking **Next** under the correct region, the seller will be required to log in to their account (or create a seller account if they do not currently have one). If there is already a seller center account that's signed in, this step will be skipped and the seller will be taken directly to the next step:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/5515b522d7e948eaa8eb580cc57d4476~tplv-10qhjjqwgv-image.image" width="500px" /></div>

After logging in, the seller will be presented with the following form:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/072e9b2f9b1c4a51abcc85a4aa126300~tplv-10qhjjqwgv-image.image" width="500px" /></div>

After entering and confirming the required information, the seller will be able to authorize your app:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/5b8265f070864f45aa3feb85d6f27ca8~tplv-10qhjjqwgv-image.image" width="500px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/07a5a6af50b14cafaf3c451072601a5e~tplv-10qhjjqwgv-image.image" width="500px" /></div>

<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: After successful authorization approval, the seller will be redirected to the </span><span style="background-color: rgb(255, 235, 235)"><strong>Redirect URL</strong></span><span style="background-color: rgb(255, 235, 235)"> you provided in your app. This URL contains critical information for the following step(s).</span>

## Receiving an authorization code
Once the seller approves authorization of the app in the TikTok Seller Center account through the service authorization link, they will be redirected to the **Redirect URL** entered during app creation. The **Redirect URL** will contain a temporary `auth_code` as a query parameter.

<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: The auth_code expires in </span><span style="background-color: rgb(255, 235, 235)"><strong>30 minutes</strong></span><span style="background-color: rgb(255, 235, 235)"> and can only be used </span><span style="background-color: rgb(255, 235, 235)"><strong>once</strong></span><span style="background-color: rgb(255, 235, 235)">.</span>

**Redirect URL and** **`auth_code` example:**
```plaintext
{redirect_url}?code=FeBoANmHP3yqdoUI9fZOCw&state={state}
```

# Step 2: Request access token and refresh token
Ensure you have a valid `auth_code` before requesting an access token. Please refer to **Step 1: Get authorization code** on how to obtain an `auth_code`.
To request an `access_token` and `refresh_token`, make a **GET** request to the following endpoint:
```plaintext
auth.tiktok-shops.com/api/v2/token/get
```

| **Parameter** | **Type** | **Required?** | **Description** | **Sample** |
| --- | --- | --- | --- | --- |
| `app_key` | string | Yes | App key in Partner Center app page | 123abc |
| `app_secret` | string | Yes | App secret in Partner Center app page | 15abf8a4972afd1f275d5b19bfa9a17e0d142aa7 |
| `auth_code` | string | Yes | Authorization code obtained in **Step 1: Get authorization code** | TTP_FeBoANmHP3yqdoUI9fZOCw |
| `grant_type` | string | Yes | Grant token type. Only `authorized_code` is accepted as a value | authorized_code |

Your request should resemble the following:
```plaintext
auth.tiktok-shops.com/api/v2/token/get?app_key=123abcd
&app_secret=15abf8a4972afd1f275d5b19bfa9a17e0d142aa7
&auth_code=TTP_FeBoANmHP3yqdoUI9fZOCw
&grant_type=authorized_code
```

If all the parameters entered in the **GET** request are valid, the response will contain the following parameters:
| **Parameter** | **Type** | **Description** | **Sample** |
| --- | --- | --- | --- |
| `access_token` | string | User access token needed to make calls to TikTok Shop Open API endpoints. Pass this value in the `x-tts-access-token` header of an API request to authorize the request. | TTP_RLM6CIADWF606TZGFO5XGA |
| `access_token_expire_in` | Unix timestamp | Expiration timestamp for access token, with default expiration time set to **seven days**. The Unix timestamp represents the date and time the access token will expire. | 1630401330 |
| `refresh_token` | string | A token to refresh the access token | TTP_C2XWDN63ON-FOHJSMR0WSG |
| `refresh_token_expire_in` | Unix timestamp | Expiration timestamp for refresh token. The Unix timestamp represents the date and time the refresh token will expire. | 1630401510 |
| `open_id` | string | An ID used to identify the user who has authorized the retrieval of their data in API calls | ephr6QAAAADhos3OBMztFEwRCWQGzDmfXm_7O2OTJyaYKA15pIaiEg |
| `seller_name` | string | The name of the seller you are authorizing for your app | Test Name |
| `seller_base_region` | string | The region where the seller is based | US |
| `user_type` | int | Type of user, with possible values: <br>  <br> * 0: Seller <br> * 1: Creator <br> * 3: Partner | 1 |
| `request_id` | string | ID to track the API request | 2022080809462301024509910319695C45 |
```plaintext
{    
"code":0,    
"message":"success",    
"data":{    
        "access_token":"TTP_Fw8rBwAAAAAkW03FYd09DG-9INtpw361hWthei8S3fHX8iPJ5AUv99fLSCYD9-UucaqxTgNRzKZxi5-tfFMtdWqglEt5_iCk",    
        "access_token_expire_in":1660556783,    
        "refresh_token":"TTP_NTUxZTNhYTQ2ZDk2YmRmZWNmYWY2YWY2YzkxNGYwNjQ3YjkzYTllYjA0YmNlMw",    
        "refresh_token_expire_in":1691487031,    
        "open_id":"7010736057180325637",    
        "seller_name":"Jjj test shop",    
        "seller_base_region":"ID",    
        "user_type":0    
    },    
"request_id":"2022080809462301024509910319695C45"    
}
```

# Step 3: Refresh access token
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/b926e4d8ac244551914301eac05992d0~tplv-10qhjjqwgv-image.image)
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/365966fefa794d7aafa11a7d7f4bc18f~tplv-10qhjjqwgv-image.image)
Once an app is authorized by a TikTok Shop seller account, it obtains an `access_token`, which is essential for authenticating and making calls to TikTok Shop APIs.

<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: The access_token </span><span style="background-color: rgb(255, 235, 235)"><strong>must be refreshed every 7 days</strong></span><span style="background-color: rgb(255, 235, 235)"> using a refresh_token. Failure to refresh before its expiration will result in authentication failure when attempting to request data through TikTok Shop APIs.</span>

<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: The refresh_token_expire_in is equivalent to the authorization duration provided when the seller initially authorized app access.</span>

The `access_token` remains valid until the `refresh_expire_date`, which is returned in the response.
To refresh your `access_token`, make a **GET** request to the following endpoint:
```plaintext
auth.tiktok-shops.com/api/v2/token/refresh
```

| **Parameter** | **Type** | **Required?** | **Description** | **Sample** |
| --- | --- | --- | --- | --- |
| `app_key` | string | Yes | App key in the TikTok Shop Partner Center app page | 65t60877bfejb |
| `app_secret` | string | Yes | App secret in the Tiktok Shop Partner Center app page | 15abf8a4972afd1f275d5b19bfa9a17e0d142aa7 |
| `refresh_token` | string | Yes | A token to refresh the access token | TTP_C2XWDN63ON-FOHJSMR0WSG |
| `grant_type` | string | Yes | Grant token type. Only `refresh_token` is accepted. | refresh_token |

Your request should resemble the following:
```plaintext
https://auth.tiktok-shops.com/api/v2/token/refresh?app_key=65t6a8e8bfejb
&app_secret=f4c770e4b45aa62e
&refresh_token=TTP_EB9rlwAAAADXbnMESTWAZSxIcC-XUA5AyeEOdmGBKY2FiKFYKqON6jco
&grant_type=refresh_token
```

If all the parameters entered in the **GET** request are valid, the response will contain the following parameters:
| **Parameter** | **Type** | **Description** | **Sample** |
| --- | --- | --- | --- |
| `access_token` | string | User access token needed to make calls to TikTok Shop Open API endpoints. Pass this value in the `x-tts-access-token` header of an API request to authorize the request. | TTP_RLM6CIADWF606TZGFO5XGA |
| `access_token_expire_in` | Unix timestamp | Expiration timestamp for access token, with default expiration time set to **seven days**. The Unix timestamp represents the date and time the access token will expire. | 1630401330 |
| `refresh_token` | string | A token to refresh the access token | TTP_C2XWDN63ON-FOHJSMR0WSG |
| `refresh_token_expire_in` | Unix timestamp | Expiration timestamp for refresh token. The Unix timestamp represents the date and time the refresh token will expire. | 1630401510 |
| `open_id` | string | An ID used to identify the user who has authorized the retrieval of their data in API calls | jKlhBwAAAADxnvrRWZm0h5wx9isdVlL5tdIEOrGL_EZjSlhzJbuXt7_AZssO6oXnuIHC1NyR_ruluQnSaXetBDLjt_Y8d1JG |
| `seller_name` | string | The name of the seller you are authorizing for your app | Test Seller |
| `seller_base_region` | string | The region where the seller is based | US |
| `user_type` | int | Type of user, with possible values: <br>  <br> * 0: Seller <br> * 1: Creator | 1 |
| `request_id` | string | ID to track the API request | 2022080809462301024509910319695C45 |
```plaintext
{    
"code":0,    
"message":"success",    
"data":{    
        "access_token":"TTP_Fw8rBwAAAAAkW03FYd09DG-9INtpw361hWthei8S3fHX8iPJ5AUv99fLSCYD9-UucaqxTgNRzKZxi5-tfFMtdWqglEt5_iCk",    
        "access_token_expire_in":1660556783,    
        "refresh_token":"TTP_NTUxZTNhYTQ2ZDk2YmRmZWNmYWY2YWY2YzkxNGYwNjQ3YjkzYTllYjA0YmNlMw",    
        "refresh_token_expire_in":1691487031,    
        "open_id":"7010736057180325637",    
        "seller_name":"Jjj test shop",    
        "seller_base_region":"ID",    
        "user_type":0    
    },    
"request_id":"2022080809462301024509910319695C45"    
}
```