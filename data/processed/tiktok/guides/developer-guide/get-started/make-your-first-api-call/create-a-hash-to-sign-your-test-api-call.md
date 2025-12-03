Now that you've [created a test access token](generate-test-access-token), you're ready to generate the cryptographic hash required to sign your first API call.
There are six steps to generating the required cryptographic hash:
## Step 1: Sort query parameter names alphabetically
Sort the query parameter names and values alphabetically. For the Get Authorized shop API, there are two required query parameters: `app_key` and `timestamp`. You're already familiar with `app_key`, it's the TikTok Shop App key that was generated for your test TikTok Shop App when you created it. `timestamp` is the current date and time in Unix epoch format, which is the number of seconds that have passed since January 1, 1970.
If you don't have a way to generate this programmatically, you can perform a web search to find a [website that can produce this value for you](https://www.google.com/search?q=generate+timestamp+in+unix+format). As an example, let's assume your `app_key` is `123456` and the current `timestamp` is `1234567890`. To sort these parameters, we compare `app_key` to `timestamp`, and since the first letter of `app_key` is `a`, it comes before the `t` in `timestamp`. Therefore, our sorted query parameters are 1: `app_key`, 2: `timestamp`.
## Step 2: Concatenate the sorted parameters names and values
Concatenate the sorted query parameters and their values from step 1 into a single string. In the example from step 1, this string is `app_key123456timestamp1234567890`.
## Step 3: Append the string from step 2 to the API path
For our first API call, we don't need to perform a step to concatenate the request body to the string created in step 2. For the call to Get Authorized Shops, there is no request body.
Therefore, our next step is to append the string from step 2 to the API request path. For Get Authorized Shops, this is:
```text
/authorization/202309/shops
```

In the example from steps 1 and 2, the resulting string is:
```text
/authorization/202309/shops/app_key123456timestamp1234567890
```

## Step 4: Prepend and append TikTok Shop App client secret
Prepend and append your TikTok Shop App client secret to the string in step 3. In our example, let's assume that our client secret is `abc000def111`. The resulting string is now:
```text
abc000def111/authorization/202309/shops/app_key123456timestamp1234567890abc000def111
```

## Step 5: Encode the string using HMAC-SHA256
The HMAC-SHA256 algorithm takes two parameters: first, a shared secret between the encoder and the decoder, and second, the message to be encoded.
In our case, the shared secret is the TikTok Shop App client secret that was generated when you created your TikTok Shop App. You can easily find this value by navigating to the [TikTok Shop Partner Center Console](https://partner-sso.tiktok.com/account/login), selecting **App & Service** from the left hand navigation, clicking on your TikTok Shop App, then scrolling down to the **Developing** section. Your **App secret** is the value required here.
Next, you must encode the string in step 6 using HMAC-SHA256. This step can be performed manually if you search the web find a [website that can generate these hashes](https://www.google.com/search?q=generate+HMAC-SHA256+key).
If you prefer to use code to perform this step, you can find code samples in multiple language in the [sign your API request](sign-your-api-request) content.
## Next steps
Now that you've generated your cryptographic hash, you can make your first API call.