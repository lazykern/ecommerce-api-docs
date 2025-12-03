Follow the guide to install the GoLang SDK to your project and make your first API call using SDK. The commonly-used API [Search Products](search-products) is used as an example.
## Prerequisites
Before integrating TikTok Shop API SDK into your project and making your first API call with the SDK, you must [create a test seller account](create-test-seller-account).
After the account is created, go to your account, consent to share data with your test TikTok Shop App, and retrieve the **authorization code** in the return URL that you specified when you created your test TikTok Shop App. For guidance, refer to [Generate a test access token](generate-test-access-token).
## Environment
Ensure your project meets all of the following conditions:

* GoLang 1.18+

## Installation

1. Unzip the downloaded package to get the source code folder.
2. Copy the source code folder to your project directory.
3. Download the dependencies in the SDK package. Run the following commands in the root directory of the project:

```go
go get github.com/stretchr/testify/assert
go get golang.org/x/net/context
```


4. Add TikTok Shop API SDK to the modules required in your project. Add the following content in go.mod:

```go
// replace 1.0.0 with the version number of the SDK you downloaded.
require tiktokshop/open/<name-of-the-SDK-folder> v1.0.0
replace tiktokshop/open/<name-of-the-SDK-folder> => ./sdk_golang
```


5. Compile the project using go build command.If there are no errors, the SDK import is successful.

## Initialize API Request Client
Import the corresponding module.
```go
import (
    "context"
    "fmt"
    "log"
    "testing"

    "github.com/luci/go-render/render"
    "tiktokshop/open/sdk_golang/apis"
    product_V202502 "tiktokshop/open/sdk_golang/models/product/v202502"
    "tiktokshop/open/sdk_golang/utils"
)
```

Set authorization information for the API request.
```go
var (
    appKey      = "wiwiow594"
    appSecret   = "825cahe7h404u04j49dj80wc3d777759c"
    authCode    = "ROW_H4MBwAAAAADRK3uVWpMjrRJUtbDmh3gbNvOKafk6rg6fdVSoyUv06rX4-JR5za8dkBt6gExeFADqILbGgIdLIaw2bop28KEqOPLELKlQZXYLVeneQSLyrYPLoPt2wTO6rp0REOwMmIk2MANjNOLVt3AthiUjAThaUTLBeL07gd8upAv5hSCgjA"
)
```

Create an API request client instance.
```go
configuration := apis.NewConfiguration()
configuration.AddAppInfo(appKey, appSecret)
apiClient := apis.NewAPIClient(configuration)
request := apiClient.ProductV202502API.Product202502ProductsSearchPost(context.Background())
request = request.ContentType("application/json")
request = request.XTtsAccessToken(token)
request = request.ShopCipher(cipher)
request = request.PageSize(1)
reqBody := product_v202502.Product202502SearchProductsRequestBody{
    Status: utils.PtrString("ALL"),
}
request = request.Product202502SearchProductsRequestBody(reqBody)
```

## Get Access Token
You can use the method included in the SDK to get Access Token:
```go
at := apis.NewAccessToken(appKey, appSecret)
resp, err := at.GetToken(authCode)
if err != nil {
   log.Printf("GetToken err:%v", err)
}
fmt.Printf("resp:%v", render.Render(resp))
if resp.Code != 0 {
   log.Printf("resp code:%v", resp.Code)
   return
}
fmt.Printf("AccessToken:%v", resp.Data.AccessToken)
fmt.Printf("RefreshToken:%v", resp.Data.RefreshToken)
accessToken := resp.Data.AccessToken
```

## Get Shop Cipher
`shop_cipher` is a parameter in the query of the API request of Search Products. You'll need to use this property to pass shop information when requesting to search for products.
To get `shop_cipher`, you'll need to call the API [Get Authorized Shops](get-authorized-shops) which is also included in the SDK as a method.
```go
shopsRequest := apiClient.AuthorizationV202309API.Authorization202309ShopsGet(ctx)
shopsRequest = shopsRequest.ContentType("application/json")
shopsRequest = shopsRequest.XTtsAccessToken(accessToken)
shopsResponse, httpRes, err := shopsRequest.Execute()
if err != nil || httpRes.StatusCode != 200 {
   fmt.Printf("productsRequest err:%v resbody:%s", err, httpRes.Body)
   return
}
if shopsResponse == nil {
   fmt.Printf("response is nil")
   return
}
if shopsResponse.GetCode() != 0 {
   fmt.Printf("response business is error! errorCode:%d errorMessage:%s", shopsResponse.GetCode(), shopsResponse.GetMessage())
   return
}
for _, shop := range shopsResponse.Data.Shops {
    fmt.Printf("ShopID: %s, ShopCipher: %s \n", *shop.Id, *shop.Cipher)
}
shopCipher := "{{Your Shop Cipher}}"
```

## Search Products
With Access Token and Shop Cipher, you can call the API to retrieve a list of products that meet the specified conditions. Every time you make an API request, TikTok Shop sends you back a response. Access the response and handle possible errors.
```go
productsRequest := apiClient.ProductV202502API.Product202502ProductsSearchPost(ctx)
productsRequest = productsRequest.ContentType("application/json")
productsRequest = productsRequest.XTtsAccessToken(accessToken)
productsRequest = productsRequest.ShopCipher(shopCipher)
productsRequest = productsRequest.PageSize(1)
reqBody := product_V202502.Product202502SearchProductsRequestBody{
   Status: utils.PtrString("ALL"),
}
productsRequest = productsRequest.Product202502SearchProductsRequestBody(reqBody)
searchProductsResponse, httpRes, err := productsRequest.Execute()
if err != nil || httpRes.StatusCode != 200 {
   fmt.Printf("productsRequest err:%v resbody:%s", err, httpRes.Body)
   return
}
if searchProductsResponse == nil {
   fmt.Printf("response is nil")
   return
}
if searchProductsResponse.GetCode() != 0 {
   fmt.Printf("response business is error! errorCode:%d errorMessage:%s", searchProductsResponse.GetCode(), searchProductsResponse.GetMessage())
   return
}
fmt.Println("searchProductsResponse data := ", render.Render(searchProductsResponse.GetData()))
```

## Code Demo
```go
package main

import (
    "context"
    "fmt"
    "log"
    "testing"

    "github.com/luci/go-render/render"
    "tiktokshop/open/sdk_golang/apis"
    product_V202502 "tiktokshop/open/sdk_golang/models/product/v202502"
    "tiktokshop/open/sdk_golang/utils"
)

var (
    appKey      = "wiwiow594"
    appSecret   = "825cahe7h404u04j49dj80wc3d777759c"
    authCode    = "ROW_H4MBwAAAAADRK3uVWpMjrRJUtbDmh3gbNvOKafk6rg6fdVSoyUv06rX4-JR5za8dkBt6gExeFADqILbGgIdLIaw2bop28KEqOPLELKlQZXYLVeneQSLyrYPLoPt2wTO6rp0REOwMmIk2MANjNOLVt3AthiUjAThaUTLBeL07gd8upAv5hSCgjA"
)

// TestProduct202309ProductsSearchPost test Product202309ProductsSearchPost
func TestProduct202309ProductsSearchPost(t *testing.T) {
    ctx := context.Background()

    configuration := apis.NewConfiguration()
    configuration.AddAppInfo(appKey, appSecret)
    apiClient := apis.NewAPIClient(configuration)

    // 1. get access_token
    at := apis.NewAccessToken(appKey, appSecret)
    resp, err := at.GetToken(authCode)
    if err != nil {
       log.Printf("GetToken err:%v", err)
    }
    fmt.Printf("resp:%v", render.Render(resp))
    if resp.Code != 0 {
       log.Printf("resp code:%v", resp.Code)
       return
    }
    fmt.Printf("AccessToken:%v", resp.Data.AccessToken)
    fmt.Printf("RefreshToken:%v", resp.Data.RefreshToken)
    accessToken := resp.Data.AccessToken

    // 2. get shop_cipher
    shopsRequest := apiClient.AuthorizationV202309API.Authorization202309ShopsGet(ctx)
    shopsRequest = shopsRequest.ContentType("application/json")
    shopsRequest = shopsRequest.XTtsAccessToken(accessToken)
    shopsResponse, httpRes, err := shopsRequest.Execute()
    if err != nil || httpRes.StatusCode != 200 {
       fmt.Printf("productsRequest err:%v resbody:%s", err, httpRes.Body)
       return
    }
    if shopsResponse == nil {
       fmt.Printf("response is nil")
       return
    }
    if shopsResponse.GetCode() != 0 {
       fmt.Printf("response business is error! errorCode:%d errorMessage:%s", shopsResponse.GetCode(), shopsResponse.GetMessage())
       return
    }
    for _, shop := range shopsResponse.Data.Shops {
        fmt.Printf("ShopID: %s, ShopCipher: %s \n", *shop.Id, *shop.Cipher)
    }
    shopCipher := "{{Your Shop Cipher}}"
    
    // 3. search products
    productsRequest := apiClient.ProductV202502API.Product202502ProductsSearchPost(ctx)
    productsRequest = productsRequest.ContentType("application/json")
    productsRequest = productsRequest.XTtsAccessToken(accessToken)
    productsRequest = productsRequest.ShopCipher(shopCipher)
    productsRequest = productsRequest.PageSize(1)
    reqBody := product_V202502.Product202502SearchProductsRequestBody{
       Status: utils.PtrString("ALL"),
    }
    productsRequest = productsRequest.Product202502SearchProductsRequestBody(reqBody)
    searchProductsResponse, httpRes, err := productsRequest.Execute()
    if err != nil || httpRes.StatusCode != 200 {
       fmt.Printf("productsRequest err:%v resbody:%s", err, httpRes.Body)
       return
    }
    if searchProductsResponse == nil {
       fmt.Printf("response is nil")
       return
    }
    if searchProductsResponse.GetCode() != 0 {
       fmt.Printf("response business is error! errorCode:%d errorMessage:%s", searchProductsResponse.GetCode(), searchProductsResponse.GetMessage())
       return
    }
    fmt.Println("searchProductsResponse data := ", render.Render(searchProductsResponse.GetData()))
}
```