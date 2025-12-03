## What is changing?
Previously, TikTok Shop sellers had to apply for the necessary permission(s) in Seller Center to list products under invite-only categories. We've updated this workflow to allow sellers to first list such products, then apply for permission(s).



Now, when a seller lists a product under an invite-only category they do not have permission for, the product will be in the `PENDING` status and unavailable to buyers. Similarly, the product audit status will be `PRE_APPROVED` if it has passed product audit but the seller still does not have the required permission(s).



**Note**: In Seller Center, **invite-only** categories may also be displayed as **restricted**.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/Invite-only%20products/Screenshot%202025-04-01%20at%2011.57.04%E2%80%AFAM.png)
## Affected markets and versions
This change applies to the following market(s):

* US (local sellers)

This change applies to the following API version(s):

* All versions

## API changes
### Get Category Rules
Previously, when a seller did not have the necessary permission(s) for an invite-only category, inputting a `category_id` would return an error. This has been updated to always return the category rules regardless of permission(s).
### Create Product, Edit Product
Similar to the Get Category Rules endpoint, inputting the `category_id` will allow the seller to create a new product listing, or modify the product category, regardless of whether they have the necessary permission(s) for the category.



These products will remain in the `PENDING` status and `PRE_APPROVED` audit status (if product audit has been passed), and will be unavailable to buyers until the seller has acquired the necessary permission(s) through the Qualification Center in the TikTok Shop Seller Center.
### Get Product
The `audit.status` response parameter now has a new possible value:

* `PRE_APPROVED`: The product has passed the audit but is not yet listed due to pending prerequisites. Refer to `pre_approved_reasons` for the prerequisites.

The `audit.pre_approved_reasons` response parameter has been added and is applicable only if `audit.status=PRE_APPROVED`, otherwise it returns an empty array.



For a product listed under an invite-only category that a seller does not have permission(s) for, but has passed audit, the `audit.status` will be `PRE_APPROVED` and the `audit.pre_approved_reasons` will be `RESTRICTED_CATEGORY_PENDING`.
### New webhook: product audit status change
The [product audit status change](37-product-audit-status-change) webhook has been launched. When the product audit status changes, developers will receive this webhook. With this webhook, developers can easily get the audit status information of a product instead of calling Get Product API. To receive this webhook, you must ensure the Product Basic API scope is enabled in Partner Center.



In this webhook, the invite-only category related fields are the same as the new properties added for the Get Product API: `audit.status` and `audit.pre_approved_reasons`.
## What action is required?

1. Developers should notify sellers when they list a product under an invite-only category they do not have permission(s) for, and prompt sellers to apply in the [Seller Center Qualification Center](https://seller-us.tiktok.com/qualification?tab=category).

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/Invite-only%20products/Screenshot%202025-04-01%20at%2012.22.37%E2%80%AFPM.png)

2. Developers should integrate with the `audit.status` and `audit.pre_approved_reasons` parameters, as well as the new product audit status change webhook, to display the correct statuses on their app's interface.