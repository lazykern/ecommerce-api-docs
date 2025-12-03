## Summary
Previously, L2L sellers could only list a single image per product variant. We've introduced the ability to add multiple product variant images to better support our sellers.
## Affected markets and versions
This change applies to the following market(s):

* United States (US)

This change applies to the following API version(s):

* 202309 (and later)

## API changes
### Product APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * Create Product <br> * Edit Product <br> * Partial Edit Product <br> * Check Product Listing | * Added new body parameter: `supplementary_sku_images`. <br> * A list of supplementary images for each value (e.g. red) of the primary sales attribute (e.g. color) to provide multiple views or details of the product for that attribute value. These appear in the product options gallery on TikTok Shop. <br> * A maximum of 8 supplementary image URIs are allowed, and should be arranged in the order you wish for them to appear on TikTok Shop. |
| * Get Product <br>  <br>  | * Added new response parameter: `supplementary_sku_images`. |