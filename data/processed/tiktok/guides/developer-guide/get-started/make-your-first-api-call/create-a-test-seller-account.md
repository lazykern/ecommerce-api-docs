Now that you've [created your TikTok Shop App](create-tts-app-oauth-client), you're ready to create a test Seller account that you can use to generate test access tokens to make your first call to the TikTok Shop API.
Because you're on the journey of making your first API call, you will most likely not have Sellers or Creators that can consent to sharing their data with you. To solve this problem, we've created a Development Shop Sandbox in which you can create a test TikTok Shop Seller account that you can use to generate authorization codes, access codes, and refresh codes.
Test Seller accounts include many features to assist you with testing. There are two types of accounts: a **core function account** and a **full function account**.
Core function accounts are easier to onboard for development since they require minimal business information to set-up and enable. Core Function Accounts also don't require you to create Test TikTok Official and Test Tiktok Buyer Accounts to create data for orders and fulfillment integrations. Finally, core function accounts do not require any payments or credit card information for data generation and integration testing.
Core Function Accounts can be used to test APIs that return data for product listings, order updates, and fulfillment, so this is a good choice for getting started.
To set up your core function account, follow these steps:

1. In Partner Center Console, select **Development Kits** from the navigation pane. Then select **Development Shops** from the list of options.
2. Click the **create test account** button on the **Seller Center Development Shops** panel.
3. Select **"Core Function"**.
4. Select "**Shop Type"** "Local" for the targeting sellers in the local market.
5. Provide an **"Account Nickname"**. This is the name that will be displayed in the user interface once the account is created, so you should name this something that you'll easily recognize in the future.
6. For **"Onboarding type"**, select **individual**.
7. Click the **create** button.

You're now ready to move on to the next step in making your first API call, but if you want to learn more about test Seller accounts and the test functionality you can use such as creating products and simulating sales and shipping, see [Seller Center development shops](seller-center-development-shops).
## Next steps
Now that you've got a test Seller account, you can [generate a test access token](generate-test-access-token).