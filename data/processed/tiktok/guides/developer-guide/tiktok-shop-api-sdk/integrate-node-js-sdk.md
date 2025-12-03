Follow the guide to install the Node.js SDK to your project and make your first API call using SDK. The commonly-used API [Search Products](search-products) is used as an example.
## Prerequisites
Before integrating TikTok Shop API SDK into your project and making your first API call with the SDK, you must [create a test seller account](create-test-seller-account).
After the account is created, go to your account, consent to share data with your test TikTok Shop App, and retrieve the **authorization code** in the return URL that you specified when you created your test TikTok Shop App. For guidance, refer to [Generate a test access token](generate-test-access-token).
## Environment
Ensure your project meets all of the following conditions:

* Node.js 16+

## Installation
Refer to the following steps to integrate the SDK into your project.

1. Add the unzipped folder to your project directory.
2. Configure dependencies in `package.json`:

```json
{
  "dependencies": {
    "request":"2.88.2"
  },
  "devDependencies": {
    "@types/request":"2.48.12",
    "@types/node": "16",
    "tslib":"2.6.2",
    "typescript": "^4.9.5",
  }
}
```


3. Add the following to your `tsconfig.json` file:

```json
{
    "esModuleInterop": true,
}
```


4. Install dependencies using your preferred package manager:

```shell
// npm
npm install
// yarn
yarn install
// pnpm
pnpm i
```

## Get Access Token
You can use the method included in the SDK to get Access Token:
```Javascript
const auth_code = "your_auth_code";
const { body } = await AccessTokenTool.getAccessToken(auth_code);
console.log('getAccessToken resp data := ', JSON.stringify(body, null, 2));
const access_token = body.data?.access_token;
if (!access_token) {
    throw new Error("Failed to get access token");
}
```

## Get Shop Cipher
`shop_cipher` is a parameter in the query of the API request of Search Products. You'll need to use this property to pass shop information when requesting to search for products.
To get `shop_cipher`, you'll need to call the API [Get Authorized Shops](get-authorized-shops) which is also included in the SDK as a method.
```Javascript
const contentType = 'application/json';
const { body: shopsGetBody } = await client.api.AuthorizationV202309Api.ShopsGet(access_token, contentType);
console.log('ShopsGet resp data := ', JSON.stringify(shopsGetBody, null, 2));
const shopList = shopsGetBody.data.shops || [];
if (shopList.length === 0) {
    throw new Error("No authorized shops found.");
}
shopList.forEach((shop, index) => {
    const shopId = shop.id;
    const shopCipher = shop.cipher;
    console.log(`shop_id: ${shopId}, shop_cipher: ${shopCipher}`);
});
```

## Search Products
With Access Token and Shop Cipher, you can call the API to retrieve a list of products that meet the specified conditions. Every time you make an API request, TikTok Shop sends you back a response. Access the response and handle possible errors.
```Javascript
const result = await client.api.ProductV202502Api.ProductsSearchPost(1,access_token,'application/json',undefined,undefined, shop_cipher);
console.log('resp data := ',JSON.stringify(result.body, null, 2));
```

## Code Demo
```Javascript
import { ClientConfiguration, TikTokShopNodeApiClient,AccessTokenTool } from ".";

ClientConfiguration.globalConfig.app_key = "XXXXXXXXX";
ClientConfiguration.globalConfig.app_secret =
  "XXXXXXXXX";
 
const access_token = "XXXXXXXXX"
const shop_cipher="XXXXXXXXX"

const client = new TikTokShopNodeApiClient({
  config: {
    sandbox: false,
  },
});

const main = async () => {
  // 1. get access token
  const auth_code = "your_auth_code";
  const { body } = await AccessTokenTool.getAccessToken(auth_code);
  console.log('getAccessToken resp data := ', JSON.stringify(body, null, 2));
  const access_token = body.data?.access_token;
  if (!access_token) {
    throw new Error("Failed to get access token");
  }
  
  // 2. get shop cipher
  const contentType = 'application/json';
  const { body: shopsGetBody } = await client.api.AuthorizationV202309Api.ShopsGet(access_token, contentType);
  console.log('ShopsGet resp data := ', JSON.stringify(shopsGetBody, null, 2));
  const shopList = shopsGetBody.data.shops || [];
  if (shopList.length === 0) {
    throw new Error("No authorized shops found.");
  }
  shopList.forEach((shop, index) => {
    const shopId = shop.id;
    const shopCipher = shop.cipher;
    console.log(`shop_id: ${shopId}, shop_cipher: ${shopCipher}`);
  });
  
  // 3. search products
  const result = await client.api.ProductV202502Api.ProductsSearchPost(1,access_token,'application/json',undefined,undefined, shop_cipher);
  console.log('resp data := ',JSON.stringify(result.body, null, 2));
};

main();  
```