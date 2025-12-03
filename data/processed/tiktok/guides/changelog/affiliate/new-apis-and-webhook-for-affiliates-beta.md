# Summary
With creators at the heart of TikTok as a platform and a proven resource to drive trust, awareness and purchases for brands, affiliate collaborations are the perfect blend between creator-driven video content and social commerce.
TikTok Shop has officially launched a new category of Affiliate APIs designed around **creator affiliate marketing**, enabling development partners to help drive new monetization avenues for TikTok Shop Creator Affiliates (hereinafter referred to as creators) and enhance workflows and growth opportunities for brands and sellers alike.
Development partners can integrate with the TikTok Shop Affiliate APIs to help TikTok Shop stakeholders **create, manage, matchmake, track, monetize, and collaborate across TikTok Shop Affiliate Collaborations and Partner Campaigns**. Listing an Affiliate API integrated app within the TikTok Shop App Store offers development partners numerous advantages:

* **Support for Existing Customers**: Satisfy and support your existing customers who are already on TikTok Shop or will be joining soon.
* **Increased Exposure**: Gain visibility among TikTok Shop sellers looking for affiliate solutions within the app store.
* **Marketing Opportunities**: Benefit from inclusion in marketing initiatives related to the TikTok Shop App Store.
* **Competitive Differentiation**: Stand out from competitors that are not integrated with TikTok Shop.
* **Enhanced Revenue Generation**: Provide a down-funnel, measurable solution that focuses on performance and revenue generation, beyond just top-of-funnel awareness and engagement marketing.

Refer to [Affiliate API Overview](affiliate-seller-api-overview) for more information on the concepts related to TikTok Shop Affiliate Collaborations and Partner Campaigns.
<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: Affiliate APIs are currently available to a select group of beta partners, with GA in late Q3. The beta partner access is CLOSED. If you strongly feel you have value as a partner and are 100% committed to rapidly developing in this beta period, please fill in this form: </span>[TikTok Shop Affiliate API Beta Access Request Form](https://bytedance.us.larkoffice.com/share/base/form/shruswQ5pfMwqPKCzEvDlkGbs7c)
<span style="background-color: rgb(255, 245, 235)">Note that the beta program is only recommended for highly motivated partners with product and development resources.</span>

# New APIs and Webhook
We launched the following types of API to support the management and facilitation of TikTok Shop Affiliate Collaborations and Partner Campaigns.
## [Affiliate Seller APIs](affiliate-seller-api-overview)
Development partners can leverage the Affiliate Seller API suite to help sellers maximize product visibility through open and target collaborations with TikTok Shop Creator Affiliates, facilitate seamless product promotion, and track the overall conversions from their affiliate marketing efforts.
<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: Seller authorization is required to use these APIs.</span>
| **API** | **API description** |
| --- | --- |
| [Create Open Collaboration](create-open-collaboration) | This API allows the seller to create an open collaboration. You create an open collaboration by selecting products and setting a commission rate. |
| [Create Target Collaboration](create-target-collaboration) | This API is used to create a target collaboration. <br> A target collaboration is a collaboration between a seller selected set of products (including a commission payout) and a set of creators the seller has added (invited) to the collaboration. Target collaborations are private and not visible in the Creator Marketplace to all creators; they are only visible to those that have been added to the collaboration. |
| [Edit Open Collaboration Settings](edit-open-collaboration-settings) | This API is used to edit a Seller's open collaboration settings. It allows you to enroll your existing product catalog and all future products into an open collaboration plan. It also allows you to turn this setting off at any point. By default, this option is turned off for all Sellers. |
| [Remove Create Affiliate from Collaboration](remove-creator-from-open-collaboration) | This API is used to remove creators from open collaboration. Please note, due to current platform design, creators can still rejoin an open collaboration after removal. Partners/Sellers can call this API again to remove the creator again. |
| [Seller Search Affiliate Open Collaboration Product](seller-search-affiliate-open-collaboration-product) | This API is used to search the information of products with open collaboration by category, commission rate, and keywords. It will return all products on the TikTok Shop Affiliate Product Marketplace that are in an open collaboration. <br> Sellers can only search for open collaboration within the regions they are registered to sell in. |
| [Search Seller Affiliate Orders](search-seller-affiliate-orders) | This API allows the partner to retrieve a list of affiliate orders (orders which are affiliate-commission eligible) generated by a seller, returning the order ID and the product ID. Using this, the partner can track their affiliate-conversions on behalf of a seller, using the order ID. |
| [Seller Search Creator on Marketplace](seller-search-creator-on-marketplace) | This API is used by Sellers to search for Creators in the Creator Marketplace. Sellers can search based on filters such as GMV, keywords, and Creator follower demographics. All the data returned is for the last 30 days. |
| [Get Marketplace Creator Performance](get-marketplace-creator-performance) | Get the Creator Affiliate's Marketplace information and performance metrics in the last 30 days. |
| [Generate Affiliate Product Promotion Link](generate-affiliate-product-promotion-link) | The user of this API is a development partner, on behalf of Sellers. <br> This API is used to generate affiliate exclusive product link based on all open collaboration products available within the TikTok Shop Affiliate Product Marketplace. <br> This API generates a link, at the product ID level (which belongs to a Seller). This link, can be distributed to creators, by the development partner (the user of this API). The creator adds this product to the creators' showcase through this url. <br> This link, represents an affiliate partner's ability to bring higher matchmaking effectiveness on behalf of a seller. If a creator does indeed add the product to showcase through this link, then the downstream consumer purchases will be able to be attributed to this partner due to the link generation capabilities. |
### [Affiliate Creator APIs](affiliate-creator-api-overview)
Development partners can leverage the Affiliate Creator API suite to help TikTok Shop Creator Affiliates manage their collaborations and product showcases on TikTok Shop, while also tracking the conversion from their marketing efforts.
<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: Creator authorization is required to use these APIs.</span>
| **API** | **API description** |
| --- | --- |
| [Get Creator Profile](get-creator-profile) | This API gets the creator profile information. |
| [Get Showcase Products](get-showcase-products) | This API lists the products in the creator's showcase, paginated by specified page size and iterated through pages by page token for up to 2000 products in the showcase. This API is generally used when a creator would like to view the products in the showcase. The platform will return the product details in the showcase, as well as the products in the live room if the creator is live streaming. |
| [Add Showcase Products](add-showcase-products) | This API adds the products to the creator's showcase. The platform will return the add status of the products, and error code and error message if the deletion fails. <br> Products must be in a showcase for a Creator to add a link to content to turn it into a shoppable content. |
| [Search Creator Affiliate Orders](search-creator-affiliate-orders) | This API allows the partner to retrieve a list of affiliate orders generated by a creator, returning the order ID and the product ID. Using this, the partner can track their affiliate-conversions on behalf of a creator, using the order ID. |
| [Search Creator Target Collaborations](search-creator-target-collaborations) | This API is used to search for creator's target collaborations and the products within these target collaborations. |
| [Creator Search Open Collaboration Product](creator-search-open-collaboration-product) | This API is used to search the information of products with open collaboration by category, commission rate, and keywords. It will return all products on the TikTok Shop Affiliate Product Marketplace that are in an open collaboration. <br> Creators can only search for open collaboration within the regions they are registered in the affiliate. |
## [Affiliate Partner APIs](affiliate-partner-api-overview)
Development partners can leverage the Affiliate Partner API suite to help TikTok Shop Affiliate Partners (TAPs) effectively manage campaigns that match-make sellers with TikTok Shop Creator Affiliates, optimizing product promotion for sellers while offering enhanced monetization opportunities for TikTok Shop Creator Affiliates.
<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: Partner authorization is required to use these APIs.</span>
| **API** | **API description** |
| --- | --- |
| [Create Affiliate Partner Campaign](create-affiliate-partner-campaign) | This API offers the ability to create a campaign for targeted sellers/public sellers, including campaign period, campaign registration period and commission requirements. Note: The campaign will not be displayed to sellers after creation |
| [Publish Affiliate Partner Campaign](publish-affiliate-partner-campaign) | This API offers the ability to publish an Affiliate Partner campaign. The campaign will be displayed to sellers after publishing. |
| [Edit Affiliate Partner Campaign](edit-affiliate-partner-campaign) | This API offers the ability to edit an Affiliate Partner campaign. No editing after the campaign is closed. |
| [Get Affiliate Partner Campaign List](get-affiliate-partner-campaign-list) | This API offers the ability to list campaigns created by the Affiliate Partner. |
| [Get Affiliate Partner Campaign Detail](get-affiliate-partner-campaign-detail) | This API offers the ability to get affiliate campaign details. |
| [Get Affiliate Partner Campaign Product List](get-affiliate-partner-campaign-product-list) | This API offers the ability to list products submitted by sellers in an Affiliate Partner campaign. |
| [Review Affiliate Partner Campaign Product](review-affiliate-partner-campaign-product) | This API offers the ability for the TikTok Affiliate Partner to review the products submitted by the sellers. |
| [Generate Affiliate Partner Campaign Product Link](generate-affiliate-partner-campaign-product-link) | This API offers the ability to generate campaign product promotion links |
## Webhook
| **Webhook** | **Webhook description** |
| --- | --- |
| [Shoppable Content Posting](17-shoppable-content-posting) | The shoppable content posting webhook is triggered when the creator adds, updates, or removes a product link in a video or livestream. <br> This webhook will only be triggered after the creator has authorized the `Read Creator Affiliate Collaborations` scope. |
# Getting Started for Beta Partners
If you are a beta partner and have not registered as a TikTok Shop partner, please follow these procedures to get started.
## Set up your partner account

1. Refer to [Register as a service partner](tsp-onboarding) to register yourself, taking note to select the following values during registration.
   * **Business Guide**: For app developers (ISV)
   * **Category**: App developer > Customer Engagement > Affiliate
      ![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/fe7863ef6eb44c7f82b4ed65f5d41a83~tplv-10qhjjqwgv-image.image)
2. Go to **Apps & service** and create the following apps:
   * Affiliate (public): The official app to launch on TikTok App Store
   * Affiliate (custom): For testing purposes
   * Connector (custom): For gaining the necessary access to non-affiliate APIs.
3. Initiate a compliance review for the **Affiliate (public)** app by referring to [Publish and list a Public App](publish-and-list-public-app).
4. Provide **App Keys** (a 14 char long key, not the App ID or Partner ID) to your partner manager so that we can list you for creator authorization. Creator authorization is necessary for accessing Creator APIs.
5. Begin development of integration once API accessibility is granted.

## Obtain the required authorizations
Refer to [Authorization Guide](authorization-overview-202407) to obtain the required authorizations for the Affiliate Seller, Affiliate Creator, and Affiliate Partner APIs.