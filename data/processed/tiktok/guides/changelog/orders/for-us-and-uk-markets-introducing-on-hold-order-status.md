# Summary
All changes are **effective December 13, 2023.**

---


<span style="background-color: rgb(255, 245, 235)">We strongly recommend updating to API v202309. "On Hold" status is at the store level. If a seller installs more than one application and if ANY ONE of the apps are not updated, you will not get the "On Hold" status. Refer to </span>[Required Actions](#Required Actions)<span style="background-color: rgb(255, 245, 235)"> section for details on how to support the new status. Learn more about how to upgrade to the v202309 version here: </span>[Upgrading to API version 202309](https://partner.tiktokshop.com/docv2/page/upgrading-to-api-version-202309)<span style="background-color: rgb(255, 245, 235)">.</span>

---


**If your apps have Orders API scope**, regardless of whether the apps use Orders API or not, they will be marked as "On Hold not supported". If your apps do not process orders for sellers, you can go to TikTok Shop Partner Center to complete the "On Hold Status Developer Declaration" without updating your integration.
On your App Detail page of TikTok Shop Partner Center, there will be a notification to inform you that the app does not support "On Hold" status. If you don't see the notification, it means the app is supported or doesn't need to support "On Hold" status. Learn more about the details from the "Required actions" action in this article.

* The `is_on_hold_order` property will only be given to apps that use the newer version. If you are on the legacy API, please update your integration to v202309. **All installed applications need to be on the newer version for the new status to be visible**.
* A new "On Hold" status is introduced for orders.
* A new key, `is_on_hold_order` is added to the Get Order List API and Get Order Detail API.
* When orders are in "On Hold" status, the values of `full_address`, `recipient_address` and `district_info` are empty.
* After you integrate the "On Hold" status, for certain shops' orders, the order status flow is still changing from "Unpaid to Awaiting Shipment". Depending on the shop's type, your app will receive both the **New** and **Existing** order status flows from different shops. This means that instead of cutting over implementation to support the new "On Hold" status flow, you also need to manage the two different order status flows in your app's order or shipping management functionality.
   * Refer to [important notes](#Important notes) for any pitfalls that might be relevant to your use case.

# Order Flow Diagram
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/e0abcc637b174093b51f24be96cdcb91~tplv-10qhjjqwgv-image.image)
# Upcoming Changes
**Effective December 13, 2023**, a new order status, "On Hold", will be added. This status will have a duration of 1 hour, during which buyers will have the ability to cancel their order without requiring seller approval. Within this 1-hour window, sellers will be unable to take action on the order (including activities such as printing shipping labels or arranging for shipment).
API changes include updates to both the *Get Order List API* and the *Get Order Detail API* responses, where a **new "On Hold" status** for orders is added.

* The status parameter allows filtering for "On Hold" orders.
* The response includes an "On Hold" status so developers can get and use the status for orders
* A new property, `is_on_hold_order` is added to the API response. The new property represents whether the order is marked as "ON HOLD" status after customer finishes payment.
* When an order is "On Hold", the values of `full_address`, `recipient_address`, and `district_info` properties will be empty.

# Affected APIs
The following APIs are updated to include the new "On Hold" status:
| **API v202309** |
| --- |
| [Get Order Split Attributes](get-order-split-attributes) |
| [Split Orders](split-orders) |
| [Search Combinable Packages](search-combinable-packages) |
| [Combine Package](combine-package) |
| [Search Package](search-package) |
| [Mark Package As Shipped](mark-package-as-shipped) |
| [Batch Ship Packages](batch-ship-packages) |
| [Update Shipping Info](update-shipping-info) |
### Error Codes
The APIs will return an error `Error Code: 21011044; Error Message: "Order status is on hold. Please process when order status update to awaiting shipment"` if that validation fails, since "On Hold" orders can not be fulfilled.
# Affected webhooks
Order status webhooks have been updated to include logic for the "On Hold" status. Developers will receive webhooks in the following situations:

* When an order's status changes from "Unpaid" to "On Hold"
* When an order's status changes from "On Hold" to "Cancelled"
* When an order's status changes from "On Hold" to "Awaiting Shipment"
* When an order's status changes from "Awaiting Shipment" to "Awaiting Collection"

# Affected markets
The changes apply to cross-border and local sellers in the US and UK markets.
# Affected developers
Developers with apps that have Orders API scope will be affected.
# Applicable versions
On Hold status will be added to all versions; but `is_on_hold_order` property will be only to v202309
We recommend developers to upgrade to v202309 of the APIs. Learn more about how to upgrade to the v202309 version from [Upgrading to API version 202309](upgrading-to-api-version-202309).
# Required Actions
## When should "On Hold" orders be supported?
Developers should integrate "On Hold" status and complete the "On Hold Status Developer Declaration" before **June 30, 2024**.
## Actions for public apps
"On Hold" is a significant order status change that all apps must adopt and should be used when building new integrations. When sellers install an app from App Store - App Detail page, a warning message will be shown to sellers to inform them that the app doesn't support "On Hold" status.
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/58fa6a6cab994dc2a5593cbe3036a450~tplv-10qhjjqwgv-image.image)
Here is a step by step guide on how to integrate "On Hold" order status, declare that your app supports "On Hold" status and remove the warning message.
### Step 1: App updates and testing

1. Adjust the features of the app to properly adopt the "On Hold" status. Take reference from the [Order Integration Solution Guide](https://bytedance.us.larkoffice.com/docx/T8HXdaOH2oJXdtxMkk9u5Sh1sCb#doxus5FdivUoNU8ksqrx1t7QYah).
2. By default, shops which have installed your app will not receive any order marked with "On Hold" status. All orders in the Sandbox 2.0 shops will have the "On Hold" status. You can utilize [Sandbox 2.0](seller-center-development-shops)and test integration with orders that have "On Hold" status.

### Step 2: App declaration

1. Once you have fully tested your app and are ready to implement the changes for production shops. Go to **TikTok Shop Partner Center - App & Service - App Detail** page, find the "**On Hold Status Developer Declaration**" banner, and click the "**Declare**" button.

![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/28674ac1423f4dc1a9022b98d682217e~tplv-10qhjjqwgv-image.image)

2. Once you have followed the instruction and confirmed the declaration of supporting "On Hold" status, your app will be marked as supporting "On Hold" status.
3. After your app is marked as supporting "On Hold" status, when sellers install the app from **App Store - App Detail** page, **they will not see a warning message** informing that the app doesn't support "On Hold" status.

## Actions for custom apps and seller developed apps
When sellers install an app from the installation link, a warning message will be shown to sellers to inform them that the app doesn't support "On Hold" status.
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/bc33c2fe646c44048657035f42ed9e3b~tplv-10qhjjqwgv-image.image)
### Step 1: App updates and testing

1. Adjust the features of the app to properly adopt the "On Hold" status. Take reference from the [Order Integration Solution Guide](https://bytedance.us.larkoffice.com/docx/T8HXdaOH2oJXdtxMkk9u5Sh1sCb#doxus5FdivUoNU8ksqrx1t7QYah).
2. By default, shops which have installed your app will not receive any order marked with "On Hold" status. All orders in the Sandbox 2.0 shops will have the "On Hold" status. You can utilize [Sandbox 2.0](seller-center-development-shops)and test integration with orders that have "On Hold" status.

### Step 2: App declaration

1. Once you have fully tested your app and are ready to implement the changes for production shops. Go to **TikTok Shop Partner Center - App & Service - App Detail** page, find the "**On Hold Status Developer Declaration**" banner, and click the "**Declare**" button.

![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/80416fbafcb14b19839675b77d85e9ef~tplv-10qhjjqwgv-image.image)

2. Once you have followed the instruction and confirmed the declaration of supporting "On Hold" status, your app will be marked as supporting "On Hold" status.
3. After your app is marked as supporting "On Hold" status, when sellers install the app from **App Store - App Detail** page, **they will not see a warning message** informing that the app doesn't support "On Hold" status.

# Important notes
There will be two order data flows after the release of "On Hold" status:

1. **New**: Changing from "Unpaid" to "On Hold", then to "Awaiting Shipment"
2. **Existing**: Changing from "Unpaid" to "Awaiting Shipment" (without "On Hold" status)

After you integrate the "On Hold" status, for certain shops' orders, the order status flow is still changing from "Unpaid to Awaiting Shipment". Depending on the shop's type, your app will receive both the **New** and **Existing** order status flows from different shops.
This means that instead of cutting over implementation to support the new "On Hold" status flow, you also need to manage the two different order status flows in your app's order or shipping management functionality.
You can utilize the new property `is_on_hold_order` in the v202309 of the Get Order List and Get Order to process orders in the correct manner:
**Scenario 1**: The value you retrieve from `is_on_hold_order` = "true". This means the order has undergone "On Hold" status (representing the **New** order status flow) and can be shipped without holding it for 1 hour.
**Scenario 2**: The value you retrieve from `is_on_hold_order` = "false". This means the order has gone from "Unpaid" to "Awaiting Shipment" where the 1 hour customer remorse window still exists (representing the **Existing** order status flow). You need to hold the order for 1 hour before shipping.
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/a1dba316f96f4a52aaa75ebb25a6fd81~tplv-10qhjjqwgv-image.image)
## How to test orders that do not have "On Hold" status

1. **Test "On Hold" status integration**

Create a new Sandbox 2.0 shop and a new draft app (with new app_key), then authorize the app to the shop.
For most product categories created from this Sandbox 2.0 shop, the order status flow of these categories will be changing from "Unpaid" to "On Hold". You can create products from Sandbox 2.0 shops and place orders for those products.

2. **Test orders that do not have "On Hold" status**

You can find and use the following product categories from Sandbox 2.0 shops to test orders that do not have "On Hold" status. This kind of order status flow represents the existing changing from "Unpaid" to "Awaiting Shipment" where customer 1 hour remorse window still exists.
|  | Level 1 Category | Level 2 Category | Level 3 Category |
| --- | --- | --- | --- |
| Name | Collectibles | Trading Cards & Accessories | Sports Trading Cards |
| ID | 951432 | 810000 | 937864 |