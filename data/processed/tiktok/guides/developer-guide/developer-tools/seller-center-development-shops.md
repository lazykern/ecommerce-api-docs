# Seller Center Development Shops User Guide
# Introduction
Seller Center Development Shops offer developers the ability to easily and efficiently generate Test Seller Center accounts that can be used for testing and development of TikTok Shop APIs. These test accounts will replicate production Seller Center Accounts and provide access to all production features and functionalities. Seller Center Development Shops are created exclusively for each Partner Center account. The key difference between Seller Center Development Shops and Product TikTok Shop Seller Center accounts is that Development Shops can not be discovered by TikTok users in the regular TikTok Apps.
Below are some examples of actions that can be tested and developed against in Development Shops
## Examples of actions in Seller Development Shops

* Create products
* Place TikTok Shop orders
* Place orders within Seller Center Development Shops without payments
* Explore TikTok Shop and TikTok Product discoverability and buying experience through Test Buyer accounts
* Place order payments through Test Buyer accounts with real payments
* Fulfill orders
* Process returns and refunds
* Extract financial statements and settlements for the shop
* Enable customer messaging services

# Supported markets and seller types
Seller Development Shops are now available for **cross-border and local shops** in the JP, MY, PH, SG, TH, US, UK, and VN markets, and for local shops in the ID market.
# Terminology
Important terms that might be used in Seller Development Shops and its related documents.
| Term | Definition |
| --- | --- |
| Seller Center Development Account | In the real-world, a TikTok Shop seller must have a Seller Center account to manage their e-commerce business with TikTok Shop. Inside Seller Center Development Accounts, you can create Seller Center test accounts and operate shops for testing purposes. The shops in these test accounts will have the same functions as real-world shops, with the only difference being that Development Shops can not be discovered by TikTok users in the regular TikTok Apps. Events triggered in Seller Center test accounts will also not affect the production or real Seller Center Account once it's live. There are two different types of Development Account. |
| Core Function Account | Core test accounts do not require any actual <br> business information, TikTok account setup, or credit card information for developers to register and get started. Core function test accounts can only access Test Seller <br> Centers through a windowed view in the Partner Center, but will have access to all core <br> testing features related to <br> i) Products <br> ii) Orders, <br> iii) Fulfillment. <br> As core function test accounts and corresponding shops do not involve actual transactions and buying through a Buyer Test TikTok Account, functionalities related to finance APIs, account settlement, customer service etc will not be available. |
| Full Function Account | Full function accounts require Business and Know your Customer (KYC) information to be used for development and testing. Full function accounts support testing through the Core Account features and through linked Buyer Test TikTok accounts. Setup must be fully completed before orders can be placed with credit cards. Full function accounts can access the Seller Center and all related features through the link provided in the Partner Center. Full Accounts can be used for development for all TikTok Shop feature and APIs such as customer service, settlements etc. |
| TikTok Account | A term used to describe an account created in the TikTok app. A user can register a TikTok account with their email or phone number, and log into the app to watch short videos, live stream and browse online stores' products. |
| Official Test TikTok Account | In the real-world, a seller can link a TikTok account to a Seller Center shop to act as the shop's Official TikTok Account. When linked, the shop's information will be displayed in the TikTok account. Other TikTok users can search for the shop's information through this Official TikTok account in the TikTok app. <br> Similar to real-world accounts, test shops also need to be linked with a TikTok account. These TikTok accounts are created normally inside the TikTok app. After linking to a test shop, they will be converted into an Official Test TikTok Account. After linking and account conversion, shop functions can be tested directly in the TikTok app. |
| Buyer Test TikTok Account | In the real-world, TikTok users can shop for products and pay for orders in the TikTok app. <br> A buyer test account is a real TikTok account that has been converted into a test account. Seller Development Shops can convert real TikTok accounts into buyer test accounts after the developer links the account in the Partner Center. With a buyer test account, you can experience your TikTok Shop discoverability and PDP experience first hand. And also shop for products and pay for orders in your test shops. |
| Shop Type | --- |
| Onboarding Type | Onboarding type refers to the account entity type. In terms of functionality, there is no difference between individual and business Seller Center accounts. |
# Set up overview
In general, developers will need to create test data to validate an API integration. The majority of integration cases will require creating a product and creating an order. With these two types of data, a developer will be able to run through the majority of integration cases necessary to service a seller. In order to create this data, a developer will need access to the following assets.

* Seller Center Core Function Account or Full Function Account
* Official Test TikTok Account for Full Accounts
* Buyer Test TikTok Account for Full Accounts

After completing setup, the developer will be able to use Seller Development Shops to manage these assets and use them to create test data (products and orders and subsequent data such as finance data).
# Core Function Account
## Core Function Account features for Developers

* Core Function Accounts are easier to onboard for development since they require minimal business information to set-up and enable
* Core Function Accounts do not require creation of Test TikTok Official and Test Tiktok Buyer Accounts to create data for orders and fulfillment integrations
* Core Function Accounts do not require any payments or credit card information for data generation and integration testing
* Core Function Accounts cannot be used to test integrations outside of Product listing, order updates, and fulfillment


**IMPORTANT NOTE**: In **Core Account** mode, the sandbox provides built-in tools that allow you to directly advance the forward and reverse order status. As a result, some real production flows may be **inconsistent with** or **not fully aligned with** the online environment. We recommend using this mode **only for core functionality testing**. For any scenario that requires full-flow or detail-level verification, please use **Full Account** mode instead.

## Setting up a Seller Center Core Function Account

1. In Partner Center Console, go to **Development Kits > Sandbox**, click **Create test account**

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/f5694cc8562a4f5fb276ace3c84a4e79~tplv-10qhjjqwgv-image.image" width="476px" /></div>


2. Select **"Core Function"**
3. Select "**Shop Type"** "Local" for the targeting sellers in the local market
4. Provide an **"Account Nickname"**
5. **"Onboarding type"** can be individual or business (no difference in functionality)

Wait for Seller Center Test Account to finish setting up.
# Using Core Function Account to test your app
## Steps for entering test shops and authorizing apps with your test shops

1. From TikTok Shop Partner Center, go to **Development Kits** Sandbox, click Seller test accounts
2. In **Development Kits** -> **Sandbox -> Manage Account** Seller test account section, click **'Authorize app'** to install and test your app with the test shop

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/ddc3c178c3794713971308ced8711b56~tplv-10qhjjqwgv-image.image" width="434px" /></div>

## Adding and Managing Products
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/540262dee1f142a0ab01a40fecb999cc~tplv-10qhjjqwgv-image.image" width="464px" /></div>

Create your first product in the Core Test account by entering any and all required TikTok Shop product information. Once done hit **"Submit for review"**
Or alternatively developers can start using the [Create API endpoint](create-product) to create Products for this Development Shop
Developers can make, manage and verify changes to products through the "**Products**" tab inside the Core Account Seller Center.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/d8d0cd9058954e328f0242ed34b3d234~tplv-10qhjjqwgv-image.image" width="472px" /></div>

Under **Products** developers can manage and view all product information such as:

* Product Statuses
* Product titles and descriptions
* Product Images
* Product SKUs
* Product inventory
* Product Prices

**Note:** Please wait for products to be approved through TikTok Shop review processes before orders can be placed through the Buyer View for the order.
## Add Shipping Templates for Seller Shipping
**Note: The below images and instructions are for the US. Menu options for the UK will be different.**
For developers and partners looking to build API integrations which involve shipping and creating labels outside of the TikTok Shop Platform, it's recommended to explore and select the right shipping settings through the **"Orders"** tab on the Core Function Account.

1. Click on **Orders -> Shipping Options** in side Core Function Accounts
2. Select TikTok Shipping or Seller Shipping

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/03d3c5bdbcfa40aba97b66344a3df25d~tplv-10qhjjqwgv-image.image" width="400px" /></div>


3. If Seller Shipping is selected, click on **Orders->Shipping Templates** and set-up a shipping template that includes all buyer regions in the US/UK

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/f0e3889e1c1e47efb5dc27bb1ad95e55~tplv-10qhjjqwgv-image.image" width="310px" /></div>

For more information about TikTok Shipping settings and Seller Shipping settings, please visit our Seller Academy [link](https://seller-us.tiktok.com/university/essay?knowledge_id=2921116620719915&role=1&course_type=1&from=search&identity=1)
## Buyer View
The Buyer View allows developers to trigger test orders and test order data to develop against in their Core Function Account.
### Create Orders

1. To create test orders and test data in the Buyer view click on **"Create test order"**

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/2e5db6712b1a4679a372d5dd498f2dad~tplv-10qhjjqwgv-image.image" width="348px" /></div>


2. Select the products for the test order. Only **3 products** can be included in a test order

**Note: Only 'Active'** status products in the Core Function account will be available to use in test orders

3. Select the Shipping Option for the order. For more information about TikTok Shipping settings and Seller Shipping settings, please visit our Seller Academy [link](https://seller-us.tiktok.com/university/essay?knowledge_id=2921116620719915&role=1&course_type=1&from=search&identity=1)

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/35099eed96d945b28b14b3e01bbc8e7d~tplv-10qhjjqwgv-image.image" width="404px" /></div>


4. Once the test order is successfully placed, it will show up in the Buyer view with status **"On Hold"**. For more information about TikTok Order Statuses, please visit our API documentation or Seller Center Academy

### Cancel Orders
Similar to creating test orders, developers can also trigger order cancellations on behalf of the buyer through the "**Cancel order"** functionality within Buyer view. For a test order to be available for cancellation, the order must be in status "On Hold" or "Awaiting Shipment"**.**

1. Find the test order in buyer view that is available for cancellation under the Action section

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/dca1211f2b2f40c19995d7e636512fcb~tplv-10qhjjqwgv-image.image" width="398px" /></div>


2. Provide cancellation reason to confirm test order as cancelled.

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/9474d29c6d7d46aa9f254e4a9a80d2b9~tplv-10qhjjqwgv-image.image" width="436px" /></div>


3. Once cancelled in the buyer view, the order will show un as Cancelled in the Seller view for the Core Function Account as well

### Request Refund
Developers can also trigger order refunds and returns on behalf of the buyer through the "**Request Refund"** functionality within Buyer view. For a test order to be available for refund, the order must be in status "Awaiting Collection"**, "**In Transit", "Delivered".

1. Find the test order in buyer view that is available for returns under the Action section
2. Provide return reason to send a return request to the Core Function Account

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/f9949afb14f644f089b517847c9fba62~tplv-10qhjjqwgv-image.image" width="458px" /></div>


3. Developers can respond to the Return Request from the Buyer through either API call or through the Core Function "**Orders" -> "Manage Returns"** section

## Orders
Developers can make, manage and verify changes to test orders through the "Orders" tab inside the Core Account Seller Center.
### Manage Orders
Developers can use the **"Manage Orders"** tab to:

* Check and verify Order details and information
* Fulfill test orders for both TikTok Shipping and Seller Shipping
* Validate changes to test orders through the API for both TikTok Shipping and Seller Shipping
* Trigger seller cancellations for test orders and test different cancellation reasons
* Split test orders (through the API or Interface)
* Combine test orders (through the API or Interface)

etc.
For more information on TikTok manages orders, please visit our Seller Academy [link.](https://seller-us.tiktok.com/university/essay?knowledge_id=7774796412471041&role=1&course_type=1&from=search&identity=1)
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/c9dde19c54d942d5881b3e844de6b914~tplv-10qhjjqwgv-image.image" width="454px" /></div>

### Manage Returns
Developers can use the **"Manage Returns"** tab to:

* Check and verify return details and information
* Respond to return requests through both the API or Interface
* Process the order return through both the API or interface

etc.
For more information on how TikTok manages returns, please visit our Seller Academy [link.](https://seller-us.tiktok.com/university/essay?knowledge_id=6837901778454274&role=1&course_type=1&from=search&identity=1)
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/9ad112da52614d0e900cd6c8963ad892~tplv-10qhjjqwgv-image.image" width="462px" /></div>

# Full Function Account
## Full Function Account features for Developers

* Full Function Accounts include all features of Core Accounts but require valid and correct business information for set-up and enablement
* Full Function Accounts will require complete TikTok Shop Seller Center set-up
* Full Function Accounts can be linked to Test TikTok Official and Test Tiktok Buyer Accounts to understand TikTok Shop and Product discoverability and buying experience
* Full Accounts can be linked to Test TikTok Official and Test Tiktok Buyer Accounts to create data for orders and fulfillment integrations with real payments and credit cards as buyers would do
* Full Accounts provide a stand-alone tab or window access to Test Seller Center Accounts
* Full Function Accounts can be used to develop and test all TikTok Shop API integrations

## Full Account: Buyer Experience and Product Discovery on TikTok Shop
Since all Full Account Seller Center test accounts mimic production accounts, the developer must follow all production and real seller center set-up steps when interacting with the assets in their Full Account Seller Center Development Shop.
**The only difference between the Full Account Seller Center Development Shop and Real TikTok Shop Seller Center account is that Development Shop can not be discovered by TikTok users in the regular TikTok Apps. The Full Account Seller Center Development Shop**
In the normal production environment on TikTok Shop, a seller manages their products within their shop through Seller Center. To make these products visible on the TikTok app, the shop needs to be associated with an official TikTok account. The seller is required to provide a TikTok account and establish this link within Seller Center. Once linked, the TikTok account becomes the shop's official account, and a new tab associated with this account appears when users search for it on TikTok. All available products will automatically be displayed under this tab, allowing buyers to browse and make purchases, resulting in the generation of orders.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/6155fb3fe3a34ab590c3e542fdb72338~tplv-10qhjjqwgv-image.image" width="485px" /></div>

## Requirements for Full Function Accounts
Before getting started with Full function accounts, please ensure the following steps are completed:

* Create an app with API enabled in TikTok Shop Partner Center.
* Depending on your Partner Center partner type, you may need to provide your business information when creating a Seller Center Full Function Account. The information provided must be real.
* For developers that have not previously linked their Seller Center account in Partner Center, you must provide your business information when creating a Full Function test account. This is required by TikTok Shop's payment service provider Paypal and Stripe (for payment and payout functionalities). The payment accounts you created for Paypal or Stripe will not affect other business or personal accounts you're using.
* Register at least two new TikTok accounts for testing purposes. As mentioned earlier, one will serve as the Official TikTok Account, and the other as the buyer test account. If you need to link multiple TikTok accounts, you'll need to create additional accounts for testing purposes.
* If you are unable to provide the required information or create a Full Function Account for testing, please consider using Core Function Accounts instead

## Creating and setting up assets for Full Function Account
**Test assets setup flow**
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/1555c5551a7a4e70a59dd7d4c2a70787~tplv-10qhjjqwgv-image.image" width="725px" /></div>

### Setting up a Seller Center Full Function Account

1. In Partner Center Console, go to **Development Kits > Sandbox**, click **Create test account**

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/e301bf0f1f4144cfafd82fdc7bd2a89b~tplv-10qhjjqwgv-image.image" width="504px" /></div>


2. Select **"Full Function"**
3. Select "**Shop Type"** "Local" for the targeting sellers in the local market
4. Provide an **"Account Nickname"**
5. Click "**Go to Seller Center"** and complete [Seller Center onboarding](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10013682&role=1&identity=1) (If you are a seller developer and already have a TikTok Shop linked to your Partner Center account, you will not see this step)

You need to provide business information to complete the onboarding. If some of the information provided fails to pass the review, we will notify you in both the Seller Center and the Full Function Account page in Partner Center. You'll need modify and resubmit the required information.
For US and UK Seller Center test accounts, the following information must be submitted if you need to make full use of the functionality:

* US: In order to publish new products in your test shop, you'll need to provide required tax information in the Seller Center.
* UK: In order to receive payouts from TikTok Shop, you'll need to fill out the tax information for your Seller Center test accounts.
* After creating test shops, default pickup warehouses will be set automatically. You will need to set shipping templates for the test shops. Learn more about how to [Set up shipping](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10012875&role=1&identity=1) in Seller Center.
* Provide and submit your tax information in Seller Center (US only). This step is required in order to publish products.

### Setting up an Official Test TikTok Account

1. Create a new TikTok account in the TikTok app. We recommend using an email address to create this account. Do not use any production TikTok accounts as your Official Test TikTok Account.
2. Link a TikTok account as your test shop's Official TikTok Account. Learn more about [how to link TikTok Shop Official Account](https://shop-academy-us.tiktok.com/university/essay?knowledge_id=10012412&role=1&identity=1). Note: TikTok accounts can also be linked as Marketing Accounts in your test shop. For testing your apps, we don't recommend linking TikTok accounts as Marketing Accounts. There are more restrictions on Marketing Accounts regarding merchandise and shop visibility.

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/c56f9cbcb98c4eeba815f2c76456cf28~tplv-10qhjjqwgv-image.image" width="446px" /></div>

Note:

* When creating the TikTok account, your physical location must be the same as the test account (shop) you created (i.e. You're physically located in the US and you're using a US test shop). Otherwise, when attempting to link the account, Seller Center will block you from linking. The TikTok account must be in the same region as the shop.
* If you cannot physically be in the same location as the shop, please remove the sim card from your device and use a VPN to change your IP to the location of the test shop you created before creating the TikTok account.

⚠️ **Warning:**
Once a TikTok account is linked in the Full Function Test Seller Center Account, it will be converted to a test account. This action is permanent and cannot be reversed. This account can not be used in the TikTok app or TikTok Shop production environment. It is "separated" from the real-world.
The conversion will happen when the TikTok account is linked to your test shop's "Official TikTok Account" or when it is linked as a buyer test account in your Partner Center account.
This will affect you in the following two cases:

1. If you have a TikTok account that has many followers and publishes video content, and you link the account to a test shop as the shop's Official TikTok Account, TikTok users will not see the TikTok account in the production environment.
2. If you use your personal email address to create a TikTok account and link the account in sandbox, this account will no longer be able to search for TikTok accounts or store products in the production environment.

We strongly suggest using testing email addresses when registering TikTok test accounts for Full Function use.
### Setting up a Buyer Test Account (TikTok Account)
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/533a24b1d59b47d5b8b2546c489812cd~tplv-10qhjjqwgv-image.image" width="456px" /></div>


1. Create a new TikTok account in the TikTok app. We recommend using an email address to create this account. Do not use any production TikTok accounts as your Buyer Test Account.
2. Link a second TikTok account as a buyer test account.
   1. Log into the TikTok app with the newly created TikTok account you want to use as the buyer test account.
   2. In TikTok Shop Partner Center, go to Development kits > Sandbox > Buyer test accounts, click **Link account**.
   3. Use the TikTok app to scan the QR code on the "Link TikTok account as buyer account" page and follow the "Authorize TikTok Partner Center" process on the TikTok app.
   4. Click **Link the account** on "Link TikTok account as buyer account" page

Note:

* This is a separate account from the one you just created to be used as your Official Test TikTok Account.
* When creating the TikTok account, your physical location must be the same as the test account (shop) you created (i.e. You're physically located in the US and you're using a US test shop). Otherwise, when attempting to link the account, Partner Center will block you from linking. The TikTok account must be in the same region as the shop.
* If you cannot physically be in the same location as the shop, please remove the sim card from your device and use a VPN to change your IP to the location of the test shop you created before creating the TikTok account.

Once a TikTok account is linked in the sandbox, it will be converted to a test account. This action is permanent and cannot be reversed. This account can not be used in the TikTok app or TikTok Shop production environment. It is "separated" from the real-world.
The conversion will happen when the TikTok account is linked to your test shop's "Official TikTok Account" or when it is linked as a buyer test account in your Partner Center account.
This will affect you in the following two cases:

1. If you have a TikTok account that has many followers and publishes video content, and you link the account to a test shop as the shop's Official TikTok Account, TikTok users will not see the TikTok account in the production environment.
2. If you use your personal email address to create a TikTok account and link the account in sandbox, this account will no longer be able to search for TikTok accounts or store products in the production environment.

We strongly suggest using testing email addresses when registering TikTok test accounts for sandbox use.
# Using Full Function Account to test your app
Test shops created as Full Function Account have the same functionalities as shops in the production TikTok Shop environment. We list the most common shop operations for testing apps and its feature guide article from the [TikTok Shop Academy](https://shop-academy-us.tiktok.com/university/home).
## Steps for entering test shops and authorizing apps with your test shops

1. From TikTok Shop Partner Center, go to **Development Kits** Sandbox, click Seller test accounts
2. In **Development Kits** **Sandbox**, Seller test account section, click "Authorize an app" to install and test your app with the test shop

## Adding and Managing Products
### Add and Publish Products
Add and publish products. In order for products to be published in the US, you must have submitted your tax info during the Seller Center test account setup stage.
Note:

* Please follow production rules when creating products. Do not add 'test' or random characters, or keywords that will get flagged by the system when creating products. Use real product names.

### Finding Products in TikTok
After products are published, you can check the product by using the Buyer Test Account in TikTok and search for the Official Test Account. The products tab should display the products you've published. You will only be able to use the accounts you linked in TikTok to search for these products. Using any other accounts will not work.
**Note:**

* If you are not seeing your product after searching in TikTok, please make sure to first check to see if your published products have any un-allowed key words in the product's title. The product could have been flagged even if it shows published in Seller Center.
* Make sure you're in the same physical location as the shop when searching. If you cannot be in the same physical location, remove the sim card from your device and use a VPN to change your device IP.

## Creating and Managing Orders
### Create Orders
By default, your newly created test shops will not have any orders. If your app provides product management and order & fulfillment synchronization to sellers, you can follow the below steps:
You need add a payment method to the Buyer Test Account (TikTok account) and pay for the test products with real money. Please set a very low price ($0.01) for test products.

1. Log into the Buyer Test Account in the TikTok app, find the test shop's Official TikTok Account by using the search function
2. In the TikTok app, from the Official TikTok Account's profile page, click **Shop** and enter the store page
3. From the store page, find the products you want to place orders with
4. Follow the TikTok app's purchasing process to complete the payment

Note:

* If you are getting any type of errors when trying to place an order (i.e. Something went wrong), please make sure you're in the same physical location as the shop when placing the order. If you cannot be in the same physical location, remove the sim card from your device and use a VPN to change your device IP.

### Manage Orders
Once the order is paid, the order can be managed by going to **Seller Center - Orders - Manage orders**. You can fulfill the orders via API according to your app's test cases. For more details regarding order management, please check the TikTok Shop Academy articles below.

* [Manage orders](https://seller-us.tiktok.com/university/essay?knowledge_id=7774796412471041&identity=1)
* [Manage seller arranged shipping](https://seller-us.tiktok.com/university/essay?knowledge_id=6837882170099457&identity=1)
* [Manage TikTok Shop logistics shipping](https://seller-us.tiktok.com/university/essay?knowledge_id=8706274700117762&identity=1)

<span style="background-color: rgba(255, 233, 40, 0.96)">Note:</span>

* If you need to test order settlement, revenue sharing, and other functions, please make sure to use a **Full Function Account**.

# Limitations

1. You can create up to 10 Seller Center **Full Function and Core Function Accounts**. That means you can concurrently use 10 test shops for different test cases. Furthermore, you are only required to submit your necessary business information for Full Function Accounts once. You won't be required to resubmit the same business information when generating additional Full Function Accounts.
2. Seller Center Development shops expire in 180 days but can be reactivated on Partner Center.
3. You can link up to 10 TikTok accounts as "buyer test accounts" to one Partner Center account. Buyer test accounts linked to the Partner Center account can be used with any of the test shops you create in Sandbox.
4. You need at least two real TikTok accounts - one for the Official TikTok account and another for the buyer test account in Seller Center Development Shops. Please note that you cannot simultaneously use the same TikTok account as both the Official TikTok Account for the test shop and as the buyer test account.