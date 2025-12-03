# What is changing?
We've introduced a new component, `package_dimension` , to version 202309 of the [Get Category Rules](get-category-rules) API response, including the following property:

* `is_required`: Indicate whether the package dimension is mandatory when creating or editing a product. For example:

```JSON
{
  "code": 0,
  "data": {
    "cod": {
      "is_supported": true
    },
    "package_dimension": {
        "is_required": true // newly added property
    },
    "product_certifications": [
      {
        "id": "602362",
        "is_required": true,
        "name": "SNI Certificate",
        "sample_image_url": "https://p-boei18n.byted.org/tos-boei18n-i-jvtte31kaf/80b32f2896829eeb69d4b278c4f3aa75.jpg~tplv-jvtte31kaf-origin-jpeg.jpeg"
      }
    ],
    "size_chart": {
      "is_required": true,
      "is_supported": true
    }
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

# Which markets are affected?
The new property is added for **local sellers** in all markets.
# Who is affected?
Developers who use version 202309 of the "Get Category Rules API" in their applications can now leverage this update for enhanced functionality.
# Which version is applicable?
This new property will be exclusively added into version 202309 of the Get Category Rules API. To access it, you need to use the updated path, specifying the version in the path parameter. As in the following example: `/product/202309/categories/{category_id}/rules`.
Learn more about [Upgrading to API version 202309](upgrading-to-api-version-202309).
# What action is required?
To ensure seamless integration with this update, developers should:

1. Integrate the `is_required` property into their applications.
2. Implement validation to inform sellers about the requirement of package dimensions, which varies based on the product category.
3. Enable input fields for sellers to provide package dimension details when required.

## Note for UK market applications
We have revised the requirement for product package dimensions, making them optional for [59 categories](https://bytedance.larkoffice.com/sheets/ZoGosN8pmh358dtXQK0cHdd7nbb) (second-level) in the UK market. Developers managing product listings for UK sellers should **integrate and utilize** the `is_required` property in the [Get Category Rule](get-category-rules) API to adapt their application's functionality. This includes modifying the implementation to treat package dimensions as optional for categories where this information is not mandatory.
## Note for applications that work with cross-border sellers
The product package dimension information is mandatory for cross-border sellers across all markets. Please be aware that the '`is_required`' property will not be returned in the response from the Get Category Rules API for cross-border sellers.