<span style="color: orange">📌 </span><span style="color: orange"><strong>Note</strong></span><span style="color: orange">: Both core function accounts and full function accounts can be used for customer messaging end-to-end testing.</span>


<span style="color: orange"><strong>Core account limitations</strong></span><span style="color: orange">:</span>

<span style="color: orange">Core function test accounts and their associated shops do not involve real transactions or purchases through a Buyer Test TikTok Account. As a result, any test cases that require actual orders, such as sending or receiving order cards, are not supported.</span>
# Apply for a development shop
Refer to our [Seller Center Development Shops User Guide](seller-center-development-shops) for a detailed breakdown on how to set up and use a development shop.
# Register and link TikTok accounts
<span style="color: orange">📌 </span><span style="color: orange"><strong>Note</strong></span><span style="color: orange">: Once linked, an official TikTok account cannot access shop products due to policy constraints. You must use another TikTok account as a test buyer account.</span>
Register two separate TikTok accounts using the TikTok app:

* One to link to your Seller Center test account (official TikTok account)
* One to link as a buyer test account

<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/register_tiktok_official.mp4?x-resource-account=public" type="video/mp4"></video>
## Link an official TikTok account to a development shop
<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/official_account_linking.mp4?x-resource-account=public" type="video/mp4"></video>
## Link a test buyer account to a development shop
<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/test_buyer_linking.mp4?x-resource-account=public" type="video/mp4"></video>
# List products in a development shop
<span style="color: orange">📌 </span><span style="color: orange"><strong>Note</strong></span><span style="color: orange">: Once a product listing has been submitted for review, it can take a couple of minutes for it to go live.</span>
For developer core function accounts, please use the following entry point to navigate to Seller Center:
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/core_account1.png?x-resource-account=public)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/core_account2.png?x-resource-account=public)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/core_account3.png?x-resource-account=public)
For developer full function accounts, please use the following entry point to navigate to Seller Center:
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/fullfunction_account1.png?x-resource-account=public)
# End-to-end testing flow
## [Seller] Create a product
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/create_product1.png?x-resource-account=public)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/create_product2.png?x-resource-account=public)
## [Buyer] Find your development shop
Log in to the linked test buyer account. Use the linked official TikTok account name to search for your development shop, which can be found under the **Shop** tab.
<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/find_dev_shop.mp4?x-resource-account=public" type="video/mp4"></video>
## [Buyer] Place a test order in the TikTok app
<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/place_test_order.mp4?x-resource-account=public" type="video/mp4"></video>
## [Buyer] Initiate a customer conversation in the TikTok app
<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/initiate_customer_convo.mp4?x-resource-account=public" type="video/mp4"></video>
## [Buyer] Send an order card
After placing a test order, when the buyer initiates a message, shortcuts will appear above the input box. Choose the order from the list and click the **Send** button to send an order card from the buyer to the seller.
<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/send_order_card.mp4?x-resource-account=public" type="video/mp4"></video>
## [Seller] Receive and reply to customer service messages in Seller Center
<video controls width="1000px"><source src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Developer_Guide/Customer%20Service%20End-to-end%20Testing%20Handbook/receive_and_reply.mp4?x-resource-account=public" type="video/mp4"></video>