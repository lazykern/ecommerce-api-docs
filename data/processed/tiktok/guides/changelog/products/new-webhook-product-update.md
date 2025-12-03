# What is changing?
TikTok Shop will now provide a [new webhook](15-product-information-change) for product update events. These webhooks are triggered when there are changes to title, description, attributes and main images.
When this change is implemented, sellers can change things like product titles, descriptions, attributes and images in TikTok Shop Seller Center and have a notification be sent to connector applications.
This alleviates an issue where product changes made to TikTok Shop Seller Center are overridden when connector apps push product updates back to TikTok Shop Seller Center.
# Which markets are affected?
This change is applicable to all markets.
# Who is affected?
This change is applicable to all developers who integrate with TikTok Shop API.
# Which version is applicable?
Since this is a webhook, it is not a change to API specifications. It is a new push notification that will be sent to the connector application's webhook URL.
# What action is required?
It is recommended that you incorporate this webhook so that sellers who use your integration can benefit from the new 2-way sync that can be unlocked after implementation.
For more information about the webhook schema, please refer to the Product Update Webhook API Reference.