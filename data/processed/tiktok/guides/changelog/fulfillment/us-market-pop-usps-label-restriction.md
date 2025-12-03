# Summary
Beginning **October 27th, 2025**, 3PL USPS labels will be restricted under our new shipping policy for POP sellers. If sellers want to use USPS labels, they will have to purchase them through TikTok Shipping, which will require all apps used by POP sellers to integrate with TikTok Shipping.
|  |  |
| --- | --- |
| Impacted market(s) | * United States (US) - Cross-border and ACCU |
| Impacted version(s) | * 202309 (and later) |
# What's new?
US cross-border merchants and ACCU merchants will **no longer be allowed to use USPS** as a shipping carrier when fulfilling orders. This change applies to the following API endpoints:
| **API** | **Affected Parameter** |
| --- | --- |
| [POST Ship Package](https://partner.tiktokshop.com/docv2/page/ship-package-202309) | `self_shipment.shipping_provider_id` |
| [POST Batch Ship Packages](https://partner.tiktokshop.com/docv2/page/batch-ship-packages-202309) | `self_shipment.shipping_provider_id` |
| [POST Mark Package as Shipped](https://partner.tiktokshop.com/docv2/page/mark-package-as-shipped-202309) | `shipping_provider_id` |
| [POST Create Packages](https://partner.tiktokshop.com/docv2/page/create-packages-202309) | `shipping_service_id` |