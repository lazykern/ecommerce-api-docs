If your application needs to access Lazada sellers’ business data, your application needs to get the authorization from sellers, and you need to guide them to complete the flow of “using Lazada seller account to log in and authorize”.

## Authorization strategy

Lazada Open Platform uses OAuth 2.0 protocol for user authentication and provides different authorization strategies for different application categories, which are pre-defined for the application category that your application belongs to. You can view the detailed authorization strategy for your application on the top section of the **Auth Management** page, including the following information:

  * Authorized Policy: The overall strategy for your application
  * Access Token Duration: The validity duration of the access token for your application
  * Refresh Token Duration: The validity duration of the refresh token (for details, refer to the [OAuth Documentation](<https://auth0.com/learn/refresh-tokens/>))
  * Authorized Page: Whether the authorization page is displayed (Show Auth Page by default)
  * Authorized Agreement: The OAuth2.0 authorization type
  * Authorized User Limit: The maximum number of sellers who can authorize the application

  

**Important**  
The following 3 kinds of authorization policy are applied to different APP categories:

  * **Allow subscribers to authorize** : This authorization policy applies to the “ERP Syetem” 、 “ERP IM Chat” and some other commercial categories. For this policy, you need to first release your app to the Lazada Service MarketPlace, and sellers need to order before authorization. The authorization duration will be the same as the subscription duration. For example, if the seller orders for one month, the authorization duration is one month.
  * **Allow binding user to authorize** : This authorization policy applies to the “Seller In-house APP” 、 “In-house IM Chat” categories. For this policy, only sellers who have been configured in the “Authorized Seller Whitelist” field can authorize your application. Refer to the section below for details.The number of authorized users is limited to 30.
  * **Allow login users to authorize** : This authorization policy applies to other categories such as “Lazrive”. For this policy, any Lazada sellers can authorize your application, so you do not need to configure the seller whitelist. You can just send your authorization URL to your sellers for authorization.

## Specify seller whitelist

If you develop an application for specific sellers, you can limit the authorization scope by specifying the seller whitelist on Lazada Open Platform, then only these sellers can authorize your application to access their business data in Lazada marketplace. After your application is deployed online, you need to provide the authorization URL to the sellers. When the sellers log in your application for the first time, they will be prompted to complete the authorization process.

Take the following steps to specify the short code of sellers who can authorize your application to access their business data.  
1\. Open the **APP Console** and click **App Management** -> **Auth Management.**  
2\. In the **Authorization Information** section, view the description of the authorization strategy for your application.  
3\. In the **Authorized Seller Whitelist** section, enter the seller account in the authorization field. Multiple seller accounts can be separated by semicolons.  
4\. Click **Submit**.

Note: If you are a third party developer and your application is open to all Lazada sellers, you only need to provide the URL of your application to the sellers when the application is deployed online. The sellers can follow the URL to complete the authorization process.

### Next step

Follow the instructions in this documentation to complete seller authorization: [Seller Authorization Introduction](<https://open.lazada.com/apps/doc/doc?nodeId=10777&docId=108260>).