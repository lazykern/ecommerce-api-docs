## Summary
To meet compliance requirements, TikTok Shop is making compliance-related attributes mandatory across various product categories.
Starting from **2025-08-30**, the Products API will require these compliance-related attributes to be provided.
## Impact
|  |  |
| --- | --- |
| Impacted market(s) | United States (US) - **Local sellers** |
| Impacted version(s) | 202309 (and later) |
## Changes
The following attributes in the specified categories will become mandatory.
| **Compliance scenario** | **Attributes affected** | **Categories affected** |
| --- | --- | --- |
| California proposition 65 | The following level 1 attributes will become mandatory: <br>  <br> * Attribute ID `101400` <br> * Attribute ID `101395` | The enforcement of these mandatory attributes apply to **all categories** containing them, except for pre-owned product categories (e.g. Pre-owned luxury footwear). |
| Choking hazard | Attribute ID `102291` will become mandatory. | Certain leaf categories under the following L1 categories: <br>  <br> * Toys & Hobbies <br> * Kids' Fashion <br> * Home Supplies <br> * Collectibles <br> * Baby & Maternity <br> * Fashion Accessories <br> * Jewelry Accessories & Derivatives <br>  <br> Refer to the full list [here](https://bytedance.sg.larkoffice.com/sheets/DXu8sWDtAhGBnKtyXlQlRaeHgAe?sheet=MCyFH4). |
| Dietary supplement disclaimers | Attribute ID `102482` will become mandatory. | Certain leaf categories under the L1 category "Health". Refer to the full list [here](https://bytedance.sg.larkoffice.com/sheets/DXu8sWDtAhGBnKtyXlQlRaeHgAe?sheet=MCyFH4). |
### Product APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| [Get Attributes](get-attributes) | The response body for attribute IDs `101400`, `101395`, `102291`, `102482` will now reflect the latest compliance rules (specifically in `is_required` and `requirement_conditions` fields). <br> Please call this endpoint to retrieve the latest rules and update your locally stored attribute list, if any. |
| [Check Product Listing](check-product-listing) <br> [Create Product](create-product) <br> [Edit Product](edit-product) <br> [Partial Edit Product](partial-edit-product) | If no values are provided for attribute IDs `101400`, `101395`, `102291`, `102482`, the API call will fail and the operation cannot proceed. |
## Next steps
Sellers will be unable to create or update products in the stated categories without providing the required compliance-related attributes. Use [Get Attributes](get-attributes) to identify the mandatory attributes and provide the appropriate values in [Check Product Listing](check-product-listing), [Create Product](create-product), [Edit Product](edit-product), and [Partial Edit Product](partial-edit-product) to help sellers fill in the attribute values.