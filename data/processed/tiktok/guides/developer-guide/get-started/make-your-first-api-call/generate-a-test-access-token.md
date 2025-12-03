Now that you've [created a test TikTok Seller account](create-test-seller-account), you're ready to generate a test access token.
A test access token is an OAuth 2.0 credential that you present to the TikTok Shop API resource server to access the data of the TikTok Shop test Seller that consented to sharing their data with your TikTok Shop App.
In order to generate a test access token, you'll first need to go to your test Seller account, consent to share data with your test TikTok Shop App, and retrieve the **authorization code** in the return URL that you specified when you created your test TikTok Shop App. You'll then pass the authorization code to the TikTok Shop Authorization Server to retrieve an **access token** and a **refresh token**.
To generate a test access token, begin by navigating to the [TikTok Shop Partner Center Console](https://partner-sso.tiktok.com/account/login).

1. Click on Development Kits -> Development Shops.
2. Click on the test account. In the right hand pane, under **Start Testing**, click on the **Authorize App** button.
3. In the **Authorize a service** dialog box, enable the radio button for your TikTok Shop App.
4. You'll be redirected to the TikTok Shop Seller center for your test Seller account. Select the duration, enter a contact email though it's not used, and finally click the **Confirm to install** button.
5. You'll be redirected to the **Authorize** dialog box. Select the checkbox next to the acknowledgement, and click the **Authorize** button.
6. You'll be redirect to the **redirect URL** that you specified for your TikTok Shop App when you created it. If you don't have a service at the redirect URL to receive the authorization code, the URL address in your browser will contain your callback URL, so copy and paste the URL to a text document. Select the value that the `code` parameter is set to, this is your **authorization code**.
7. Your authorization code is valid for 30 minutes only, so you'll need to move quickly on the next step. You'll be making an HTTP call to the TikTok Shop authorization server. You can use your favorite way to call HTTP services for this step, including just formatting a URL and pasting it into your browser's address bar. The server address is `https://auth.tiktok-shops.com/api/v2/token/get` and there are four required query parameters:
   1. `app_key`: Your TikTok Shop App application key that was generated for you when you created your TikTok Shop App.
   2. `app_secret`: Your TikTok Shop App secret that was generated for you when you created your TikTok Shop App.
   3. `auth_code`: The `code` parameter from step 6.
   4. `grant_type`: This is a string that must always be set to `authorized_code`.
8. The response body for the call in step 7 includes a JSON object named `data`. For the purposes of making your first API call, we'll focus on four properties in this object:
   1. `access_token`: This is the **access token** necessary to make your first API call.
   2. `access_token_expire_in`: This the expiration date and time for the `access_token`. It's in Unix epoch time.
   3. `refresh_token`: This is the **refresh token** you'll use to generate a new `access_token` once the current date is greater than `access_token_expire_in`.
   4. `refresh_token_expire_in`: This is the expiration date and time of the refresh token in Unix epoch format. Once this date and time has been reached, you must re-authorize your TikTok Shop App starting at step 2 above.

## Example call flow
For step 7 above, you can create the URL to paste into your browser by copying the string and substituting the parameter values for those associated with your test TikTok Shop App:
```plaintext
https://auth.tiktok-shops.com/api/v2/token/get?app_key=123abcd
&app_secret=15abf8a4972afd1f275d5b19bfa9a17e0d142aa7
&auth_code=TTP_FeBoANmHP3yqdoUI9fZOCw
&grant_type=authorized_code
```

If all the parameter values are valid, your browser window will display the response in JSON text format. For example:
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
        "user_type":0,
        "granted_scopes": [
            "seller.affiliate_collaboration.read",
            "seller.affiliate_collaboration.write"
        ]
    },    
"request_id":"2022080809462301024509910319695C45"    
}
```

The fields in the response are defined as follows:
| **Parameter** | **Type** | **Description** | **Sample** |
| --- | --- | --- | --- |
| code | int | A machine-readable response code that represents the request result. `0` indicates success. For more information about failure codes, refer to [Common error codes](common-errors). | 0 |
| message | string | A human-readable message that describes the success or failure of the API request. | success |
| request_id | string | ID to track the API request. | 2022080809462301024509910319695C45 |
| data | object | The response data payload. |  |
| └ access_token | string | User access token needed to make calls to TikTok Shop Open API endpoints. Pass this value in the `x-tts-access-token` header of an API request to authorize the request. | TTP_RLM6CIADWF606TZGFO5XGA |
| └ access_token_expire_in | Unix timestamp | Expiration timestamp for access token, with default expiration time set to **seven days**. The unix timestamp represents the date and time the access token will expire. | 1630401330 |
| └ refresh_token | string | A token to refresh the access token. | TTP_C2XWDN63ON-FOHJSMR0WSG |
| └ refresh_token_expire_in | Unix timestamp | Expiration timestamp for refresh token. The unix timestamp represents the date and time the refresh token will expire. | 1630401510 |
| └ open_id | string | An ID used to identify the user who has authorized the retrieval of their data in API calls. | ephr6QAAAADhos3OBMztFEwRCWQGzDmfXm_7O2OTJyaYKA15pIaiEg |
| └ seller_name | string | The name of the seller you are authorizing for your app. | Test Name |
| └ seller_base_region | string | The region where the seller is based. | US |
| └ user_type | int | Type of user, with possible values: 0: Seller; 1: Creator, 3: Partner | 1 |
| └ granted_scopes | []string | The authorized API scopes for the app. This field includes the **Scope Key** value of the authorized API scopes. ![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/a28585cf3cec42c2846c13f2cfaec033~tplv-10qhjjqwgv-image.image) <br>  | ["seller.affiliate_collaboration.read","seller.affiliate_collaboration.write"] |
## Next steps
To continue on the journey to making your first API call, make note of your **access_token** value. You will make use of the **refresh token** in advanced topics, but we don't need to make note of it at this time.
Your next step is to create a [cryptographic hash to sign your API call](create-hash-to-sign-your-test-api-call).