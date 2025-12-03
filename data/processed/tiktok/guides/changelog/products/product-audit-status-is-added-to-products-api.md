## Summary
This change exposes the audit status of a particular product when calling GET Product Details, POST Edit Product and POST Partial Edit Product in the response under the `audit` object. It also lets you call the POST Search Products and filter by `audit_status`. This change is applicable to versions **v202309** and **v202312**, and applies to all markets and sellers.
## What is changing
Prior to this change, audit status was returned in a webhook when a merchant makes a change to a product. The developer was responsible for integrating this into their system. To streamline this logic by adding another avenue to access this data, TikTok is releasing these changes directly into the API itself.
## What action is required
Please ingest these values so merchants are aware of the current audit status of the product. This will improve user experience and provide sellers into more insight about the status of a product.
## What markets and version is affected
This change is applicable to versions **v202309** and **v202312**, and applies to all markets and sellers.