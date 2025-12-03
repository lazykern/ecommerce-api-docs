# Overview
Welcome to the Tokopedia & Shop Developer Guideline. Here you'll find guidance on how to:

1. Onboard as a developer partner in Tokopedia & Shop Partner Center.
2. Develop and publish your apps in Tokopedia & Shop Partner Center.
3. Implement new Tokopedia & Shop APIs and configure your Webhooks.
4. Use our developer tools provided in your Tokopedia & Shop Partner Center

# Integration Guide
**Onboarding process**
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image01.jpeg)
<br>

**High-level timeline**
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image02.jpeg)
## Definition and basic business introductions

* [Tokopedia & Shop Partner Center](https://partner.tiktokshop.com/): mainly builds related systems for two types of User Persona, partners and sellers, and finally realizes a complete B2B product process around partners' service/App release and platform sellers' order services. Compared with the B2C e-commerce scenario, the role of the partners is "service seller" and the role of the e-commerce seller is "service buyer".
* **Tokopedia & Shop App Store**:
   * **For partners**: The Public App will be published in the Tokopedia & Shop App Store. Sellers can browse and authorize the App(s) created by ISV or 3rd-party developers in the App Store.
   * **For sellers**: To help sellers boost business on Tokopedia & Shop and improve your operational efficiency, Tokopedia & Shop now offers an App Store where sellers can contact and authorize App(s) that suit sellers to improve productivity, and synchronize products.

| **Seller Market** | **App Store Portal** | **Tokopedia & Shop Seller Center - App Store** |
| --- | --- | --- |
| **Indonesia local seller** | [https://seller-id.tokopedia.com/appstore/id](https://seller-id.tokopedia.com/appstore/id) | [https://seller-id.tokopedia.com/services/market?shop_region=ID](https://seller-id.tokopedia.com/services/market?shop_region=ID) |
# Case 1: If you have integrated with「Tokopedia Open Platform」and「Tokopedia & Shop Partner Center」before
> Tokopedia Open Platform: https://developer.tokopedia.com/
> Tokopedia & Shop Partner Center: https://partner.tiktokshop.com/

## Step 1: Login「Tokopedia & Shop Partner Center」
> 📌 Access to Tokopedia & Shop website: **https://partner.tiktokshop.com/**

<br>

## Step 2: Bind「Tokopedia Open Platform」account and「Tokopedia & Shop Partner Center」account
### 2.1 Find the Organization ID in Tokopedia Open Platform <span id="case1_step2"></span> 

1. Go to [Tokopedia dev portal](https://developer.tokopedia.com/console). Once logged in, you will be directed to the main dashboard of the developer console.
2. Identify Organization ID: Look at the top left corner of the dashboard, below your company's name, you will see the Organization ID

<div style="text-align: center"><img src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image04.png" width="2852px" /></div>

### 2.2 Bind account
> 📌 By binding the accounts, you no longer need to create multiple applications. This not only saves your time and resources but also reduces complexity. In the future, you will be able to maintain merchants from both platforms under a single application, which will significantly streamline your shop operation.

Use the Organization ID from Tokopedia Open Platform and input it into the「Tokopedia & Shop Partner Center」.
| **#** <!-- width:70px --> | **Operation** | **Demo** <!-- width:250px --> |
| --- | --- | --- |
| Step 1 | 1. Click "[My Account - Link Tokopedia Account](https://partner.tiktokshop.com/approval/toko)" <br> 2. If you already have Tokopedia & Shop App, you can see the entrance in the App Management page <br>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image05.png) <br> ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image06.png) <br>  |
| Step 2 | Click "Link now" and enter Tokopedia organization ID and Registered email in Tokopedia Open Platform <br> 📌 One「Tokopedia & Shop Partner Center」account can only be bound to one 「Tokopedia Open Platform」account, establishing a 1:1 mapping relationship. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image07.png) <br>  |
<br>

## Step 3: Bind Tokopedia App and "Tokopedia & Shop" App <span id="case1_step3"></span> 
> 📌 After binding the App key, you will be able to query valuable information. For example, you can find out how many Tokopedia merchants have migrated to TTS and how many merchants have completed App authorization. This data will be very useful for you to better understand the market situation and plan your business strategies accordingly.

### 3.1 Find App ID in Tokopedia Open Platform
Go back to the Tokopedia Developer Portal to locate the **App ID** for the application you have integrated
### 3.2 Bind App
| **#** <!-- width:70px --> | **Operation** | **Demo** <!-- width:250px --> |
| --- | --- | --- |
| Step 1 | When you finish the account binding, you will enter the App binding page automatically. <br> You can also click "[My Account - Link Tokopedia Account](https://partner.tiktokshop.com/approval/toko)" to bind the Tokopedia App and "Tokopedia & Shop" App. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image08.jpeg) <br> ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image09.png) <br>  |
| Step 2 | Choose "Tokopedia & Shop" App and Tokopedia App which you want to bind. <br>  <br> 📌Please note that: <br> 1. One "Tokopedia & Shop" Appkey can bind to multiple Tokopedia App IDs, but one Tokopedia App ID cannot be bound to multiple "Tokopedia & Shop" Appkeys. <br> 2. The status of "Tokopedia & Shop" App should be online | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image10.png) <br>  |
<br>

## Step 4: Integrate with Tokopedia & Shop API <span id="case1_step4"></span> 

* By integrating with the new API, only one merchant portal (Tokopedia & Shop Seller Center) and one set of Open APIs (TikTok Shop APIs) will be available
* Both user Apps — Tokopedia and Shop｜Tokopedia — will remain available
* Merchants can choose to sell products on one of these apps or both simultaneously. ISVs must use the Shop｜Tokopedia APIs to manage merchant operations on both apps. Once the merchant migration is complete, all newly generated data can only be accessed through the Shop｜Tokopedia APIs. Some historical data (such as merchant data) will be migrated to Shop｜Tokopedia, while other historical data (such as orders and bills) will remain in Tokopedia.

**Please** [click here to access to the API onepager](id-market-tokopedia-shop-open-api-integration-one-pager) **to view more about:**

1. **Data access via APIs**: What APIs to use to access new data and integrate historical data of merchants migrating from Tokopedia to "Tokopedia & Shop"?
2. **Changes to Shop｜Tokopedia APIs**: What changes are made in Shop｜Tokopedia APIs to suit the Indonesian market?
3. **Mapping of shops and products**: How will the new shops and products from "Tokopedia & Shop" be mapped to those from Tokopedia?

<br>

## Step 5: Test your App and Publish <span id="case1_step5"></span> 

1. Create a test account in Development Shop with "Target market: Indonesia"

<div style="text-align: center"><img src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image11.png" width="2932px" /></div>


2. Use this test account to authorize your app:

<div style="text-align: center"><img src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image12.png" width="2932px" /></div>


* After authorization, you should receive an "authorization_code", follow this instruction to get "access_token": https://partner.tiktokshop.com/docv2/page/678e3a3292b0f40314a92d75.
* Call [[Get Authorized Shops](get-authorized-shops)] to get "shop_cipher"
* Use "access_token" and "shop_cipher" for further API calls.
3. Start testing your app:
   * Test product listing
      * For product listing with API, please refer to [this document](products-api-overview).
      * If you wish to list products manually, please use [ModHeader](https://modheader.com/). Use the below profile:
      ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image13.png)
      Then click "Go to Seller Center" for product listing:
      <div style="text-align: center"><img src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image14.png" width="2932px" />      </div>


   * Test order placement and fulfillment
      Before order placement, please make sure you have successfully listed the products for this shop, then click "start testing".
      <div style="text-align: center"><img src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image15.png" width="2928px" />      </div>

      Click "Create test order" to mock order placement.
      <div style="text-align: center"><img src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image16.png" width="2920px" />      </div>


**📌 Please note: we only support test order placement from TikTok right now.**
You should be able to get the order data from Orders API, then proceed to fulfillment API calls.
# Case 2: If you only integrate with Tokopedia Open Platform, and not yet integrated with Tokopedia & Shop Partner Center
> Tokopedia Open Platform: https://developer.tokopedia.com/
> Tokopedia & Shop Partner Center: https://partner.tiktokshop.com/

<br>

## Step 1: Create an account on Tokopedia & Shop Partner Center
> 📌 Access to Tokopedia & Shop Partner Center: **https://partner.tiktokshop.com/**

Set up an account on Partner Center. Provide your email address and, optionally, your phone number. Ensure your email address on Partner Center is current, as it is essential for receiving crucial updates from the Partner Center platform.
<br>

## Step 2: Register as an App developer (ISV or Seller developer)
### If you are ISV
| **#** <!-- width:70px --> | **Description** | **Screenshot** <!-- width:250px --> |
| --- | --- | --- |
| 1 | After creating an account, you'll find a business guide tailored to different partner types. Pick App developer as your partner type from this guide, click on 'Start Business,' and it will lead you to the 'Get Started' page to initiate your application for your selected category. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image17.png) |
| 2 | Click on "Get started" to start your partner application. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image18.png) |
| 3 | As a first step, Tokopedia & Shop needs to know what type of Apps you plan to build for sellers. **Please choose the target App category and target seller market**. <br> For example, you can choose "Enterprise Resource Planning" as the target category and "Indonesia" as the target market. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image19.png) |
| 4 | You can click "Get app key now" and complete your registration later. But you must come back and pass the certification review before the App published. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image20.png) |
| 5 | You'll need to complete the necessary fields based on the category you've selected, including business license related information. Be sure to have your business license and related documents prepared in advance. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image21.png) <br> ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image22.png) <br>  |
<br>

### If you are the seller developer
| **#** <!-- width:70px --> | **Description** | **Screenshot** <!-- width:250px --> |
| --- | --- | --- |
| 1 | After creating an account, you'll find a business guide tailored to different partner types. Pick App developer as your partner type from this guide, click on 'Start Business,' and it will lead you to the 'Get Started' page to initiate your application for your selected category. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image17.png) |
| 2 | Click on "Get started" to start your partner application. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image18.png) |
| 3 | **Please choose the target App category and target seller market**. <br> 📌 Please choose 「TikTok Shop Seller」as the business category | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image23.jpeg) |
| 4 | Please verify your seller account with login and password (email or phone number). <br> [Tokopedia & Shop Partner Center](https://partner.tiktokshop.com/) will verify the account automatically. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image24.png) |
| 5 | When you are verified, you will see the tag of "Tokopedia & Shop Seller" under My Account page. <br> 📌 You should have a Tokopedia & Shop seller account first, no matter which market this account belongs to <br>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image25.png) <br>  |
<br>

## Step 3: Create an App
| **#** <!-- width:70px --> | **Description** | **Screenshot** <!-- width:250px --> |
| --- | --- | --- |
| 1 | **Determine what type of App to build** <br> There are two types of Apps you can build with Tokopedia & Shop APIs: public and custom. Each App type has its own workflows and requirements. <br>  <br> * **Public App:** This type of App is publicly listed on the [Tokopedia & Shop App Store](https://seller-id.tokopedia.com/appstore/id) and is discoverable by sellers. Sellers will authorize the App to connect their Tokopedia & Shop account. To list this App on [Tokopedia & Shop App Store](https://seller-id.tokopedia.com/appstore/id), the App must pass Tokopedia & Shop's App review process. <br> * **Custom App:** This type of App is typically developed for a particular seller. It is tailored to meet the specific business needs, requirements, or preferences of a seller. The App is not listed on Tokopedia & Shop App Store. You can distribute this App to individual sellers by sharing the App's authorization link. <br>  <br> 📌 **Note:** Partner Center supports the ability to convert/upgrade a custom App to a public app. Refer to [Publishing a custom App](publish-custom-app) for more information on how to convert your published custom App. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image26.png) |
| 2 | **Create your App** <br>  <br> 1. Select **App & Service** from the navigation panel. The Partner Center displays the 「App & service」 page. <br> 2. Click the **Create app & service** button in the top right corner of the page. The Partner Center displays the「Create app & service」page. <br> 3. Select either **Public** or **Custom**, based on the type of App you wish to create. <br> 4. Select the **Service category** and set the **default name** of your App. Optionally, upload a logo for your App. <br> 📌 Please note that you can only choose the category you chose in「Step2 Register as an App developer」 <br> 5. Select the **Market** and set the **seller type** for your App. <br> 📌 You can choose multiple seller market and seller type. <br> 6. Toggle the **Enable API** switch on and complete the following fields. Otherwise, skip to the next step. <br> &nbsp;&nbsp;&nbsp;&nbsp;- **Redirect URL** Enter the URL at which to receive your authorization code. After the seller authorize the App, it will jump to this URL (it can be the URL of your system's web page) and transmit the `auth_code`, which you can use to get the `access_token`. <br> &nbsp;&nbsp;&nbsp;&nbsp;- **Webhook URL** Optionally, enter the URL to receive [push notifications](configuration-guide) (it can be the URL of your system). <br> 7. Click **Create** to complete the process. <br> After you create your App, Partner Center displays the App and service detail page. Here you can access your App's unique App key and secret, which allow you to complete [seller authorization](seller-authorization-guide) and [API calls](make-your-first-api-call-overview). <br> &nbsp;&nbsp;&nbsp;&nbsp;- **App Key** - The unique identification of the service. <br> &nbsp;&nbsp;&nbsp;&nbsp;- **App Secret** - The application key generated by the platform when you create an App. You can use this secret to obtain the API access token. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image27.png) |
<br>

## Step 4: Bind「Tokopedia Open Platform」account and「Tokopedia & Shop Partner Center」account
Same as[Case 1 - Step 2](#case1_step2)
## Step 5: Bind「Tokopedia Open Platform」App and「Tokopedia & Shop Partner Center」App
Same as [Case 1 - Step 3](#case1_step3)
## Step 6: Integrate with Tokopedia & Shop API
Same as [Case 1 - Step 4](#case1_step4)
## Step 7: Test your App
Same as [Case 1 - Step 5](#case1_step5)
<br>

## Step 8: Ready to launch
### For Public App
> 📌 **Checklist:** Once you're ready to launch your public App, you must go through review requirements before you can make your App live:


1. Pass the registration review
2. Complete and submit your language listing form for review.
3. Initiate and complete your App review.
4. If required by your case, ensure you've passed the compliance and legal review you initiated during onboarding.

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image28.png)
<br>

**Initiate and complete the App review form (Only for public App)**
Fill out the App Review form to initiate the app review process. To access the App Review form scroll down to the App Review section of the app and service detail page and click **Submission materials for review**. Alternatively, you can hover over **Publish** on the app and service detail page and click **Modify**.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image29.gif)

Complete the following steps to submit the form:

1. In the **API Scope Information** section, ensure the APIs integrated with your app are listed correctly. Modify the APIs as necessary.
2. In the **Product testing** section, provide the information necessary for us to test and review your product. Enter the information that identifies your app, such as the URL of your product, the account you used for testing, and any testing instructions.
3. In the **Product screenshots** section, provide a brief explanation of what features your app has, what it can do, and who it serves. Include screenshots and, optionally, videos of your app as necessary.
4. In the **Required Product Design** section, provide the design document you used to plan out the design of your app.
5. Click **Submit** to initiate the app review process.

**Note:** Once you submit the form, you can't edit it during the review process. You are able to edit the app review form and resubmit if we reject your app.
<br>

**Fill in the listing information and initiate listing review (Only for public App)**
> 📌 Please fill in carefully. The listing information that will be shown on the [Tokopedia & Shop App Store](https://seller-id.tokopedia.com/appstore/id) for sellers.

You must complete a language listing form to set the language of your app listing according to the target market. The specific market(s) in which your app is accessible necessitates distinct language requirements for its listing. The table below describes the language listing requirements based on market and seller type.
| **Target market** | **Seller Type** | **Language required for listing** |
| --- | --- | --- |
| Indonesia(ID) | Local | Bahasa Indonesia |

Completing and submitting the language listing form initiates a review for the market in which you're listing your app. You must complete a language listing form for each market your app targets.
To access the language listing form, click the market name under the Target Sellers section of the app and service detail page and then click **Edit**. Alternatively, you can click **Edit** next to the **Publish** button.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image31.gif)
**Notes:**

* If you have already finished a language listing form for another market, you can use the **translate and import from** feature to auto-fill the listing form. Refer to the Translate and import your listing section below for more information.
* You can click **Save** at the top of the form to save your progress.

<br>

Complete the following steps for each market in which you wish to list your App:

1. In the **Service overview** section, provide an overview of your app, including:
   * The name of your App. A concise name helps to attract more sellers. It's the first thing sellers will see when browsing the App Store.
   * The logo for your App. If your logo contains any text, please ensure that the text is in the same language as the App.
   * A short introductory description of your App.
   * Media (images or video) that highlights your app's functionality and benefits. You should choose at least one image or one video to describe your service. We highly recommend providing a video rather than an image.

| **Field Name** <!-- width:90px --> | **Type** | **Field Description** | **Requirements** <!-- width:150px --> | **Screenshot** <!-- width:100px --> | **Seller-side Demo** <!-- width:150px --> |
| --- | --- | --- | --- | --- | --- |
| App or service name | Mandatory | Please provide an app name. <br> 💡A concise name will help you to attract more sellers. It's the first thing sellers will see when browsing the **App & Service Store.** | Format: Text, less than 100 characters. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image32.png) | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image33.png) |
| App or service logo | Mandatory | Please upload a logo to help sellers recognize your app and brand. <br>  <br> 📌 If your logo contains any text, please ensure that the text is in the same language as the app. | A logo to help sellers recognize your service and brand. <br> Size: < 10MB <br> Ratio: 1:1 <br> Dimensions: 150 * 150 <br> Format: jpg, jpeg, png | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image32.png) | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image34.png) |
| App or service language | Mandatory | In order to enable local businesses to better understand your services, please fill out the service information according to the specified **target market service language.** <br>  <br> To facilitate a clear understanding of your app among sellers, kindly complete the service listing information in accordance with the specified target market service language. |  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image35.png) |  |
| App or service short description | Mandatory | Give a short description to introduce your service | Format : Text, less than 200 characters | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image36.png) <br>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image37.png) |
| Video or main image | Mandatory | Upload a video or image that highlights the impact of your app. This is a visible way to demonstrate to sellers the benefits of your app. You need choose at least 1 image or 1 video to describe your service. <br>  <br> 💡It's better to provide a video rather than an image. | **Video** <br> Format: mp4, mov, flv <br> Size: < 200MB <br>  <br> **Image** <br> Size: <= 10MB <br> Ratio: 5:3 <br> Format: jpg, jpeg, png | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image38.png) <br> ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image39.png) <br>  <br>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image40.png) |

2. In the **Detail introduction** section, provide the functional details of your App, including:
   * Three key benefits of your App. We recommend that you use this space to address the requirements of sellers, focusing on their needs, rather than how a particular feature works.
   * Additional images of your App to attract sellers. We recommend providing at least three images that introduce your App's featured functions, images of staff, or success stories.
   * A detailed and comprehensive description of your App's key features and what sellers can do with your app.
   * A list of platforms/services with which your App can integrate. This information allows sellers to quickly determine whether your App is compatible with the platform(s) they are using.

| **Field Name** <!-- width:90px --> | **Type** | **Field Description** | **Requirements** <!-- width:150px --> | **Screenshot** <!-- width:100px --> | **Seller-side Demo** <!-- width:150px --> |
| --- | --- | --- | --- | --- | --- |
| Key benefits | Mandatory | Provide three key highlights of your app. Each highlight must include a title and description. <br>  <br> Leverage this space to address the requirements of sellers, focusing on their needs, rather than how a particular feature works. <br>  <br> 📌 All 3 sets are required. | Format: Text <br> Title (50 characters or less) & Description (150 characters or less) | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image41.png) <br>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image42.png) |
| Image | Mandatory | You can add additional images to prove your abilities and attract sellers. Recommend 3-6 pictures to introduce the service. For example, screenshots of your featured functions, images of staff or success stories. | jpg, jpeg and png only. <br> Ratio of length to width:5:3, within 10MB <br>  <br> *Please provide at least one Featured Image, but it is better to have 3-6 images | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image43.png) | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image44.png) <br>  |
| App or service detail description | Mandatory | Please provide a more detailed and comprehensive product introduction in this part. <br> Explain your service's key features in detail. Sellers want to know what your service can do for their shop. <br>  <br>  <br> * Don't use special characters or emojis in your description. <br> * Don't include testimonials in the detailed description. <br> * Don't use any personal information without written consent. | Format: Text and URL links <br> 2000 characters or less allowed, 500 or less recommended | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image45.png) | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image46.png) <br>  |
| Integrations | Mandatory | List any platforms that your app integrates with. <br> Sellers can quickly determine whether your app is compatible with the platform they are using and quickly make a decision on installing your app. | For example, Shopify, WooCommerce, Magento, BigCommerce, Amazon... | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image47.png) | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image48.png) |

3. In the **Contact & support** section, provide contact information and help resources to support sellers using your app, including:
   * A valid email address and, optionally, a phone number.
   * Optionally, links to your official website and app FAQs, user guide, etc.

| **Field Name** <!-- width:90px --> | **Type** | **Field Description** | **Screenshot** <!-- width:100px --> | **Seller-side Demo** <!-- width:150px --> |
| --- | --- | --- | --- | --- |
| Phone | Optional | Leave your phone number for sellers to contact you <br> 📌 Local phone number is recommended. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image49.png) <br>  | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image50.png) |
| Email address | Mandatory | Provide your email to help the seller contact you |  |  |
| Website | Optional | If there is an official website, you can fill in a valid official website address here. | ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image51.png) |  |
| App Userguide or FAQ | Optional | If you have the user guidebook or some common product questions and answers, please provide the URL link. |  |  |

4. Click **Next listing** to submit your App listing for review and move to the next listing (if applicable).

**Note:** Once you submit the form, you can't edit it during the review process. You are able to edit the language listing form and resubmit if we reject your listing.
<br>

### For Custom App (seller developer's App also included)
> 📌 **Checklist:** Once you're ready to launch your custom App, you must go through **registration review** before you can make your App live

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image52.png)
<br>

## Step 9: Publish App

* For Public Apps: Public App will be published in the [Tokopedia & Shop App Store](https://seller-id.tokopedia.com/appstore/id). Sellers can browse and authorize the App(s) in the App Store.
* For Custom Apps: Custom App is typically developed for a particular seller. It is tailored to meet the specific business needs, requirements, or preferences of a seller. The App is not listed on Tokopedia & Shop App Store. You can distribute this App to individual sellers by sharing the App's authorization link.

### For Public App
After you complete and submit the app review and language listing forms, and ensure you've passed the compliance review, you have finished all the steps necessary to publish and list your public app.
You can check the publishing status of your app on the app and service detail page.

* If Tokopedia & Shop approves your app, we will automatically make it available on the App and Service Store for sellers to authorize. In addition, we will provide you with an "Authorize link" you can copy and share with sellers individually.
* If Tokopedia & Shop rejects your app, click **Edit** to view our reasoning, make adjustments, and resubmit your app for further review.

### For Custom App
After you complete registration and integration, you have finished all the steps necessary to publish your custom app. Please click 「Publish」and then the App will be published automatically.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image53.png)
<br>

## Step 10: Authorized by seller
### For Public App
There are two ways for sellers to authorize your App.

1. Sellers browse and authorize the App in the App Store

Sellers can go to [[Seller Center] > [Apps store]](https://seller-id.tokopedia.com/services/market) and finish the authorization.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image54.png)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image55.png)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image56.png)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image57.png)

2. Sellers authorize the App by the authorization link directly

Alternatively, you can send the authorization link to target sellers. Sellers can open the authorization link directly and authorize shops. This link serves as a means for sellers to authorize your application in a more personalized and targeted manner.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image58.png)
### For Custom App
> 📌 Sellers can only authorize the App by the authorization link

Alternatively, you can send the authorization link to target sellers. Sellers can open the authorization link directly and authorize shops. This link serves as a means for sellers to authorize your application in a more personalized and targeted manner.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image58.png)
<br>

# FAQ
## 1. Can I convert my custom app to a public app
If you determine that your published custom app can offer value to sellers outside your app's original seller scope, Partner Center offers the ability to convert your custom app to a public app. This allows you to make your app available on the [Tokopedia & Shop App Store](https://seller-id.tokopedia.com/appstore/id).
For a published custom app, you can click **Upgrade to Public Service** to convert your app from custom to public. Please note this is a beta feature on a gray test, and you may not see the button if you are not on the test invite list.
**Important:**

* You can't upgrade a custom App to public if you have not published the app yet.
* You can't change the target sellers (i.e. the market and seller type) when converting the app type from custom to public.
* You'll need to fill in all language listings before you can submit the custom app for upgrade review.
* The app type will remain custom until the app passes the upgrade review and reviews for all selected markets.

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image59.png)
<br>

## 2. What APIs can I integrate with?
**Please** [click here to access to the API onepager](id-market-tokopedia-shop-open-api-integration-one-pager) **to view more about:**

1. **Data access via APIs**: What APIs to use to access new data and integrate historical data of merchants migrating from Tokopedia to "Tokopedia & Shop"?
2. **Changes to "Tokopedia & Shop" APIs**: What changes are made in "Tokopedia & Shop" APIs to suit the Indonesian market?
3. **Mapping of shops and products**: How will the new shops and products from "Tokopedia & Shop" be mapped to those from Tokopedia?

<br>

## 3. Can I unbind「Tokopedia Open Platform」and「Tokopedia & Shop Partner Center」account?
Yes. After the binding is successful, developers are allowed to perform the [Unbind] or [Rebind after Unbinding] operation.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image60.png)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image61.png)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image62.png)
After unbinding, developers are allowed to bind again: Initiating the binding process again is consistent with the first binding process, and information input and email verification need to be completed.
<br>

## 4. Can I unbind Tokopedia App and Tokopedia & Shop App?
No. Appkey does not support rebinding or unbinding
<br>

## 5. If I have questions, where can I contact Tokopedia & Shop?
Please access the Help Center https://partner.tiktokshop.com/ticket/landing
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image63.png)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image64.png)
<br>

## 6. How to test API / Can I use the test shop?
There is the Sandbox (test tool) in [Tokopedia & Shop Partner Center - Development Kits](https://partner.tiktokshop.com/v2_sandbox/guide?region=ID).
Refer to [Step 5: Test your App and Publish](#case1_step5) for detailed steps.
<br>

## 7. I have API questions, how to solve it?
Please access the Help Center https://partner.tiktokshop.com/ticket/landing
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image63.png)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Get_Started/ISV_Onboardling_Toko/image64.png)