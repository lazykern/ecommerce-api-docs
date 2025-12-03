# What is changing?
We added the `permission_statuses` response property to all versions of the [Recommend Category API](recommend-category). `Permission_statuses` indicates whether the seller has permission to use the recommended category for a product listing. The possible values are:

* `AVAILABLE`: You have permission for this category and can create products under this category.
* `INVITE_ONLY` : This category is an invitation category, and you can not use it to create products. Contact the account manager or TikTok Shop support team for permission to access this category or select another one.

# Which markets are affected?
Local and cross-border sellers in all markets can use the new `permission_statuses` property.
# Who is affected?
This change applies to developers with applications that use any version of the Recommend Category API.
# What action is required?
When you receive `permission_statuses` in the API response, adopt the new field in your integration. Clearly communicate the permission status to sellers so they know which recommended categories they can use for product listings. Guide sellers on how to request access to categories marked as `INVITE_ONLY` or `NON_MAIN_CATEGORY`.