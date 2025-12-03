# What is changing?
We've introduced a new `tax_rate` property for the Order resource. This `tax_rate` represents the item's tax rate within an order, calculated by TikTok Shop. Factors influencing this rate include US Sales Tax regulations and the product's category.
Developers can access the `tax_rate` in version 202309 of the Get Order List and Get Order Detail API. For example:

* API request path: `/order/202309/orders`
* API response:

```JSON
{
    "code": 0,
    "data": {
        "orders": [
            {
                "line_items": [
                    {
                        "display_status": "TO_SHIP",
                        "id": "577086512123755123",
                        "is_gift": false,
                        "item_tax": [
                            {
                                "tax_amount": "21.2",
                                "tax_type": "SALES_TAX",
                                "tax_rate": "0.03"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "message": "Success",
    "request_id": "202203070749000101890810281E8C70B7"
}
```

# Which markets are affected?
The new property is applicable to **local sellers** in the US markets.
# Who is affected?
Developers utilizing version 202309 of either the Get Order List API or the Get Order Detail API will benefit from this update, enabling enhanced functionality in their applications.
## Which version is applicable?
This `tax_rate` property is a feature exclusive to version 202309 of the Get Order List API or Get Order Detail API. To utilize it, ensure you're using the updated API path that includes the version number, as shown in the example: `/order/202309/orders`.
Learn more about [Upgrading to API version 202309](upgrading-to-api-version-202309).
# What action is required?
Developers who build order management features for sellers are required to integrate this new property and meet the tax reporting requirement of the sellers.