## Summary
TikTok Shop is implementing new Mandatory Certifications for categories in Beauty & Personal Care and Health.
Starting from 2025-04-19, Products API will be updated to require 510(k) PreMarket Notification for Class 2 Consumer Medical Products and Establishment Registration & Device Listing Account (FURLS) for Class 1, 2, and 3 Consumer Medical Products.
## Which markets and versions are affected?
This change applies to all versions and local sellers in the US market.
## API Changes
Developers with applications that use Create Product, Edit Product, and Partial Edit Product
There is no parameter or property changed for the Products API. When the Ops team configures the API to be effective, the TTS system will validate if the required Product Certifications are submitted via APIs. Without the required attributes and Product Certifications, API calls will return failure.
## Required Actions
Without mandatory product certifications, sellers will not be able to create and update products within specific categories
Use the Get Category Rule to check what product certifications are required for which categories, and pass the product certification files via the Create Product, Edit Product, and Partial Edit Product to help sellers submit product certification.