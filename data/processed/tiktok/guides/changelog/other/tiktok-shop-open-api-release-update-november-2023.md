We're excited to share the latest enhancements to the TikTok Shop Open API, released since October 2023. These updates are designed to streamline operations and expand functionalities for our partners.
## [Get Order Detail](shortened-string-length-for-buyer-email-in-get-order-detail-api)
The `buyer_email` property's string value has been shortened to fewer than 45 characters to enhance compatibility with external systems, such as shipping software.
Applicable markets: local and cross-border sellers in all markets
## [Mark Package As Shipped](for-local-sellers-in-us-market-warning-information-added-to-mark-package-as-shipped-api)
A new `warning` component has been added to the [Mark Package As Shipped](mark-package-as-shipped) API. The new component includes the following fields:

* `message`: TikTok Shop validates the `tracking number` value and returns a warning message if it detects any issues, such as:
   * The value does not match any shipping provider.
   * The value matches multiple shipping providers.
   * The value matches a different `shipping_provider_id` than what you passed via the API parameter.

Applicable markets: local sellers in the US market
## [Recommend Category](new-property-added-to-recommend-category-api-to-indicate-whether-sellers-can-use-recommended-category)
We added the `permission_statuses` response property to all versions of the [Recommend Category API](recommend-category). `Permission_statuses` indicates whether the seller has permission to use the recommended category for a product listing. The possible values are:

* `AVAILABLE`: You have permission for this category and can create products under this category.
* `INVITE_ONLY` : This category is an invitation category, and you can not use it to create products. Contact the account manager or TikTok Shop support team for permission to access this category or select another one.

Applicable markets: local and cross-border sellers in all markets
## [Update Shipping Info](for-local-and-cross-border-sellers-in-us-market-shipping-information-update-time-window-extended-to-72-hours)and [Update Package Shipping](for-local-and-cross-border-sellers-in-us-market-shipping-information-update-time-window-extended-to-72-hours)
We have extended the time limit for updating shipping information from 36 hours to 72 hours via the [Update Shipping Info](update-shipping-info) and [Update Package Shipping Info](update-package-shipping-info) APIs. This change provides sellers with more flexibility to accommodate scenarios that might require shipping information updates beyond 36 hours (such as making changes to the carrier or tracking number).
Applicable markets: local and cross-border sellers in the US market
## [Get Package Shipping Document](new-shipping-label-format-launched-in-id-my-and-vn-markets) and [Get Shipping Document](new-shipping-label-format-launched-in-id-my-and-vn-markets)
The shipping label file and the shipping label with packing list file have been updated to have a new format and size for the content area.
Applicable markets: local sellers in the ID market, local and cross-border sellers in the MY and VN markets
## [Mark Package As Shipped](for-local-sellers-in-uk-market-introducing-item-level-order-split-shipping)
[Mark Package As Shipped](mark-package-as-shipped) has been released for local sellers in the UK market.
This API is designed for sellers who manage order fulfillment via their preferred logistics carriers. It facilitates the seamless uploading of valid package information directly to TikTok Shop. This feature applies to both individual orders and order line items.
Applicable markets: local sellers in the UK market
Best regards,
TikTok Shop Partner Product Team