Follow the guide to install the Java SDK to your project and make your first API call using SDK. The commonly-used API [Search Products](search-products) is used as an example.
## Prerequisites
Before integrating TikTok Shop API SDK into your project and making your first API call with the SDK, you must [create a test seller account](create-test-seller-account).
After the account is created, go to your account, consent to share data with your test TikTok Shop App, and retrieve the **authorization code** in the return URL that you specified when you created your test TikTok Shop App. For guidance, refer to [Generate a test access token](generate-test-access-token).
## Environment
Ensure your project meets all of the following conditions:
- Java 1.8+
- Maven (3.8.3+)/Gradle (7.2+)
## Installation
### For Maven Users
Follow the steps to install the SDK to your existing Java project:

1. Unzip the downloaded package to obtain the source code.
2. Compile the source code locally by executing mvn clean install. If there are no errors, the compilation is successful.
3. Add this dependency to your project's POM file and replace 1.0.0 with the version number of the SDK you downloaded.

```xml
<dependency>
  <groupId>com.tiktokshop</groupId>
  <artifactId>open-sdk-java</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```


4. Execute `mvn clean install` in your project to include the SDK dependency.

### For Gradle Users
Add the following dependency to your build.gradle and replace `1.0.0` with the version number of the SDK you downloaded.
```groovy
repositories {
    mavenCentral()     // Needed if the 'open-sdk-java' jar has been published to maven central.
    mavenLocal()       // Needed if the 'open-sdk-java' jar has been published to the local maven repo.
}

dependencies {
    implementation "com.tiktokshop:open-sdk-java:1.0.0"
}
```

### For Others
Generate the JAR by executing: `mvn clean package`.
Manually install the following JARs:

* `target/open-sdk-java-1.0.0.jar`
* `target/lib/*.jar`

Replace `1.0.0` with the version number of the SDK you downloaded.
### Get Access Token
Currently, the SDK does not implement a method to obtain an Access Token, and you must initiate a request yourself to acquire the Access Token. For details, refer to [Generate a Test Access Token](generate-test-access-token).
### Get Shop Cipher
`shop_cipher` is a parameter in the query of the API request of Search Products. You'll need to use this property to pass shop information when requesting to search for products.
To get `shop_cipher`, you'll need to call the API [Get Authorized Shops](get-authorized-shops) which is also included in the SDK as a function.
```java
AuthorizationV202309Api authAPIInstance = new AuthorizationV202309Api(defaultClient);
    try {
        GetAuthorizedShopsResponse shopsResponse = authAPIInstance.authorization202309ShopsGet(accessToken, contentType);
        System.out.println(shopsResponse);
        for (GetAuthorizedShopsResponseDataShops shop : shopsResponse.getData().getShops()) {
            System.out.println("shop_id: " + shop.getId() + ", shop_cipher: " + shop.getCipher());
        }
    } catch (ApiException e) {
        System.err.println("Exception when calling AuthorizationV202309Api#authorization202309ShopsGet");
        System.err.println("Status code: " + e.getCode());
        System.err.println("Reason: " + e.getResponseBody());
        System.err.println("Response headers: " + e.getResponseHeaders());
        e.printStackTrace();
    }
```

### Search Products
With Access Token and Shop Cipher, you can call the API to retrieve a list of products that meet the specified conditions. Every time you make an API request, TikTok Shop sends you back a response. Access the response and handle possible errors.
```java
String accessToken = "ROW_VHM8dXS3r90w3wd67339r84k59v873nd73nf73JF3JKcaY"; // String |
    String contentType = "application/json"; // String | Allowed type: application/json
    String shopCipher = "TTP_Pse393kj92728jv9";
    ApiClient defaultClient = Configuration.getDefaultApiClient()
        .setAppkey("wiwiow594")
        .setSecret("825cahe7h404u04j49dj80wc3d777759c")
        .setBasePath("https://open-api.tiktokglobalshop.com");
    ProductV202502Api apiInstance = new ProductV202502Api(defaultClient);
    SearchProductsRequestBody searchProductsRequestBody = new SearchProductsRequestBody();
    searchProductsRequestBody.setStatus("ALL");
    try {
        SearchProductsResponse result = apiInstance.product202502ProductsSearchPost(1, accessToken, contentType, null, shopCipher, searchProductsRequestBody);
        System.out.println(result);
    } catch (ApiException e) {
        System.err.println("Exception when calling ProductV202502Api#product202502ProductsSearchPost");
        System.err.println("Status code: " + e.getCode());
        System.err.println("Reason: " + e.getResponseBody());
        System.err.println("Response headers: " + e.getResponseHeaders());
        e.printStackTrace();
    }
```

If the API request succeeds, you will get a result which resembles the following content:
```json
{
  "code": 0,
  "data": {
    "next_page_token": "b2Zmc2V0PTAK",
    "products": [
      {
        "audit": {
          "status": "AUDITING"
        },
        "create_time": 1234567890,
        "id": "1729592969712207008",
        "integrated_platform_statuses": [
          {
            "platform": "TOKOPEDIA",
            "status": "PLATFORM_DEACTIVATED"
          }
        /* ... */
}
```

### Code Demo
```java
import tiktokshop.open.sdk_java.api.ProductV202502Api;  
import tiktokshop.open.sdk_java.invoke.ApiClient;  
import tiktokshop.open.sdk_java.invoke.ApiException;  
import tiktokshop.open.sdk_java.invoke.Configuration;  
import tiktokshop.open.sdk_java.model.Product.V202502.SearchProductsRequestBody;  
import tiktokshop.open.sdk_java.model.Product.V202502.SearchProductsResponse;  
  
public class Example {  
    public static void main(String[] args) throws Exception {
        String appKey = "6fki53g8uldu4";
        String appSecret = "7a6028ce703044dd798aa297333ad2b19dfb4e39";
        String accessToken = "ROW_yuz9UgAAAAA7n0AT3oGJiYa5j5m45lv_rWWk-KqNdcCNYaB0Q51Whbrh24aCYM1DbbONA6SGPZSky4eFJ1xrIx9UWf_C-HSjb2G3aQv-gyhE6QOG8JgP2ECcDQmTwuHdNQh5QjOF0eY";
    
        String contentType = "application/json";
        String shopCipher = "ROW_jKz9TQAAAABBmX6PM8wgVqtjkfVwkwvl";
    
        // 1. get access token
        AccessTokenAPI accessTokenAPI = new AccessTokenAPI(appKey, appSecret);
        ResponseInfo getTokenResponse = accessTokenAPI.getToken("ROW_8KPJXgAAAABl9RnFLTHz0mJlo-SXeRCklBr0FykbOOvxCFCMHe4TAAxY0xf5n3tLe-eoN6aCr1WWlLBw1pVAd1CET8ngjFHr4Pj6vMuzIE0bBX7UNFMmZlgH64y7nhuYM-frjWnnHxI");
        System.out.println("AccessTokenAPI getToken response: " + getTokenResponse);
        accessToken = getTokenResponse.getData().getAccessToken();
        
        // refresh token (needed when access token is expired)
        // ResponseInfo refreshTokenResponse = accessTokenAPI.refreshToken(getTokenResponse.getData().getRefreshToken());
        // System.out.println("AccessTokenAPI refreshToken response: " + refreshTokenResponse);
    
        // 2. get shop_cipher
        ApiClient defaultClient = Configuration.getDefaultApiClient()
                .setAppkey(appKey)
                .setSecret(appSecret)
                .setBasePath("https://open-api.tikTokglobalshop.com");
        AuthorizationV202309Api authAPIInstance = new AuthorizationV202309Api(defaultClient);
        try {
            GetAuthorizedShopsResponse shopsResponse = authAPIInstance.authorization202309ShopsGet(accessToken, contentType);
            System.out.println(shopsResponse);
            for (GetAuthorizedShopsResponseDataShops shop : shopsResponse.getData().getShops()) {
                System.out.println("shop_id: " + shop.getId() + ", shop_cipher: " + shop.getCipher());
            }
        } catch (ApiException e) {
            System.err.println("Exception when calling AuthorizationV202309Api#authorization202309ShopsGet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    
        // 3. search products
        ProductV202502Api apiInstance = new ProductV202502Api(defaultClient);
        SearchProductsRequestBody searchProductsRequestBody = new SearchProductsRequestBody();
        searchProductsRequestBody.setStatus("ALL");
        try {
            SearchProductsResponse result = apiInstance.product202502ProductsSearchPost(1, accessToken, contentType, null, shopCipher, searchProductsRequestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ProductV202502Api#product202502ProductsSearchPost");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```