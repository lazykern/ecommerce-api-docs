We're excited to share the upcoming changes to the TikTok Shop Open API, set for release in **December 2023 or Q1 2024**. These changes are designed to streamline operations and expand functionalities for our partners.
*Note: This document is a preview for developers. Actual release details, including API request workflows and property names, are subject to change. Use this information for planning application roadmaps and upcoming features.*
## [Get Order List](get-order-list) and [Get Order Detail](get-order-detail)
A new **On Hold** status will be added, allowing sellers to identify orders within the customer's 1-hour remorse window, reducing the risk of order cancellations after shipment.
**Applicable markets**: local and cross-border sellers in the US and UK markets
In addition to the modifications in the order status flow, the Orders resources will have the following enhancements:

* Adding `tax_rate` to the `line_items` component to express the tax rate of the item, enabling sellers to clearly express the tax rate for each item and ensuring accurate tax calculations.
* Adding new fields indicating the **estimated shipment** **time** range and **estimated delivery time** range set by sellers, to offer customers a more reliable view of shipping and delivery timelines.
* Adding new fields `shipped_time`, `delivered_time`, `cancelled_time`, `status_update_time` to capture key timestamps during significant order status changes.
* Adding`retail_delivery_fee`to comply with specific state regulations in the US.
* Adding new field `delivery_preference` to represent customers' delivery preferences, such as "leave the package in the mailbox."
* Adding `address_level` to the `district_info` component to indicate the administrative district level of the address. The new field improves address accuracy for shipping.

**Applicable markets**: local sellers in the US market

## Order cancellation workflow revamp
Under the current system, when an order has a cancellation request, sellers must first address this request (usually by rejecting it) before they can ship the package. The upcoming changes will simplify this process: sellers will be able to directly reject a cancellation request simply by shipping the package.
The revamp will bring changes to the Orders resources and Fulfillment APIs, as well as reduce the API integration workload.
**Applicable markets**: local sellers in the US market

## Item replacement workflow
When an item in a package is lost or missing, currently, customers only have the option of canceling the entire order and requesting a refund. With the introduction of the new 'item replacement' workflow, sellers will have the ability to send a replacement item instead of canceling and refunding the order.
This new workflow will bring changes to the Returns and Orders resources.
**Applicable markets**: local sellers in the US market

## [Create Product](create-product)
In a seller's shop, a product can have one of two statuses:

* Product Listing: This is an activated product stored in the Seller Center, visible to customers.
* Product Drafts: This refers to a product stored in the Seller Center which is not activated and, therefore, can not be found by customers.

For API version 202309, we are introducing a new functionality: 'listing fails and create draft'. Developers will have access to a new request parameter that allows them to pass an enumerated value to this API. This feature enables them to decide whether to move a 'product listing' to 'product drafts' in scenarios where the 'product listing' cannot be successfully created.
**Applicable markets**: local and cross-border sellers in all markets

## [Get Category Rules](get-category-rules)
We are adding a new property to the Get Category Rules to indicate if package length, width and height are required for the category. This new property can let developers know which categories require package dimensions to streamline the product listing and editing for sellers.
**Applicable markets**: local sellers in all markets

## [Check Listing Prerequisites](check-listing-prerequisites)
We are replacing the dynamic strings in the API response with fixed properties for easier integration.
**Applicable markets**: local and cross-border sellers in all markets

## New API to check product information
This new API allows developers to submit product information, such as the title, description, images, and attributes, for validation. The API checks if the information meets value validation criteria, such as a minimum length of one character for the product title, and compliance requirements, including ensuring the product description does not contain unsupported languages.
**Applicable markets**: local and cross-border sellers in all markets

## New API to import product reviews
New API endpoint to empower developers to import reviews from external systems on behalf of sellers. This functionality is designed to align with sellers' business needs, facilitating the import of existing reviews into their TikTok Shop.
**Applicable markets**: local sellers in the US market