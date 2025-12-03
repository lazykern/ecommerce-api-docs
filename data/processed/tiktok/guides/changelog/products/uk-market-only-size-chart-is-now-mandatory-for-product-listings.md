# What is changing?
**Beginning April 19, 2024, the** **`size_chart` parameter is mandatory for UK local sellers** when creating and editing products. This parameter already exists in all versions of the [Create Product API](create-product), [Edit Product API](edit-product) and [Partial Edit Product API](partial-edit-product). It is currently optional, but starting April 19, 2024 it will be mandatory. Developers can pass the image URI to TikTok Shop to render the size chart image for the product under the required categories.
# Which markets are affected?
This change is for the UK market only.
# Who is affected?
Local sellers in UK market who develop connector and multichannel applications are affected by this change.
# Which version is applicable?
This change is implemented across all API versions.
# What action is required?
There are two ways developers can implement this change and ensure size_chart parameter is passed when creating and editing products:
## Option 1 - Upload A Size Chart Image

1. Call [Get Category Rules](get-category-rules) and check if `size_chart.is_required` is set to `true`
   1. If yes, then that category requires a size chart image
2. Call [Upload Product Image](upload-product-image), set the `use_case` to `SIZE_CHART_IMAGE`
   1. This will upload the image
   2. Parse the image URI from the API response.
3. When calling [Create Product](create-product), [Edit Product](edit-product), [Partial Edit Product](partial-edit-product), pass the image URI from step 2 as value for `size_chart.image.uri` parameter.

## Option 2 - Provide A Size Chart ID

1. Call [Get Category Rules](get-category-rules) and check if `size_chart.is_required` is set to `true`
   1. If yes, then that category requires a size chart image
2. Ask the seller to login to the Seller Center
3. Create a size chart using the Size Chart Tool
   1. This tool can be found by navigating to **Manage Products - Bulk Action - Batch manage size charts**
4. Get the size chart ID
5. When using [Create Product](create-product), [Edit Product](edit-product), [Partial Edit Product](partial-edit-product), pass the size chart ID to the `size_chart.template.id` parameter.
6. When calling [Create Product](create-product), [Edit Product](edit-product), [Partial Edit Product](partial-edit-product), pass the size chart ID to the `size_chart.template.id` parameter.

# Appendix
## List of Categories Impacted
Please refer to [this link](https://bytedance.sg.larkoffice.com/sheets/JfgTsLMZYhxTjjtVuk5lDMMvgWP?sheet=d882bd) for a complete list of categories that are impacted.
## Screenshots of Size Chart Tool
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/41b35d731c8641b2a01e3d7e477b4941~tplv-10qhjjqwgv-image.image)
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/5f429002bfc6465a896b6dc5cb5cd929~tplv-10qhjjqwgv-image.image)