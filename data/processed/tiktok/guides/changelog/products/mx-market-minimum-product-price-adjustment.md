## Summary
Previously, the range of prices for MX market was 0.1 - 50,000 MXN. As of **Feb 14, 2025**, the range is now 1 - 50,000 MXN.
## What is changing?
Previously, the minimum price for MX market was 0.1 MXN to a maximum of 50,000 MXN. Starting from today, the minimum price has been updated to 1 MXN while the maximum remains 50,000.
This change affects all endpoints that handle product pricing, including:

* Check Product Listing
* Create Product
* Edit Product
* Partial Edit Product
* Update Price

## Which markets and sellers are affected
This update applies to local sellers in the MX market.
## Who is affected?
Developers building apps to manage products for sellers should take action on this update.
## Which version is applicable?
This change applies to all versions of the API.
## What action is required?
If your application includes product price validation based on the previous pricing limits, please update your validation rules to align with the new minimum price of 1.