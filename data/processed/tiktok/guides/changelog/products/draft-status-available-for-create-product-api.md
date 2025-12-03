# What is changing?
Draft products are products listed in Seller Center that can not be seen by customers. For sellers who don't have required product information, such as size charts or certifications, developers can use this feature to help sellers upload products as drafts first. Once uploaded, sellers can add the required information directly into Seller Center when they have it.
Developers on the legacy version (v202212) can use `Create Draft Product (V1)` API to upload products as draft.
Developers on the new version (v202309) don't have access to the above API, but instead can use [Create Product API](https://partner.tiktokshop.com/docv2/page/create-product) and pass `AS_DRAFT` to `save_mode` parameter in the request body.
# Which markets are affected?
This change is applicable to **all markets**.
# Who is affected?
**All sellers** can take advantage of this new feature.
# Which version is applicable?
This change is applicable to **v202309**.
# What action is required?
We recommend updating the logic when calling Create Product listing to allow creating a product as draft.
## Parameters
New parameter `save_mode` is available for developers. It is used to specify the mode in which the product is saved, and supports the following values:

* **AS_DRAFT**
* **LISTING**

**Note:**If you omit providing save_mode, the default value is "LISTING".
## Responses

* When `save_mode` is `LISTING`, the API will behave the same as before, listing the products.
* When `save_mode` is empty, the default value is LISTING.
* When `save_mode` is `AS_DRAFT`, the API will save the product information as draft in the Seller Center without listing.

## Error codes and messages
No changes to error codes or error messages.