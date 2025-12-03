## Summary
When buying a shipping label through TikTok Shop, TikTok Shipping (4PL) will be updated to automatically allocate the best logistics service for each package. This label allocation feature will initially rollout to selected sellers, and will require apps to support some minor changes in fulfillment logic.
## Impact
|  |  |
| --- | --- |
| Impacted market(s) | * United States (US) |
| Impacted version(s) | * 202309 (or later) |
## Changes
For selected sellers with orders where `shipping_type=TIKTOK` (use [Get Order List](get-order-list) or [Get Order Detail](get-order-detail)):

* [Get Eligible Shipping Service](get-eligible-shipping-service) will return only one `shipping_services.id`.
* [Create Packages](create-packages) will ignore the request body parameter, `shipping_service_id`. Package labels will use the single `shipping_services.id` tied to the order.

## Next steps
Developers must upgrade their apps to support the new TikTok Shipping label allocation by **May 22nd, 2025**. For each package, use the Get Eligible Shipping Service endpoint to dynamically obtain the recommended available logistics service to support labels allocated by TikTok Shop.