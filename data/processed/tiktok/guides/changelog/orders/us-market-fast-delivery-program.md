## Summary
To better support our 2024 Q4 rollout of *3 Day Delivery* through Fulfilled-by-TikTok (FBT), we're adding a merchant badge in Seller Center that more clearly indicates if a seller is offering *3 Day Delivery* for a specific order. We've updated some of our order management APIs to reflect this badge.
## Impact
|  |  |
| --- | --- |
| Impacted market(s) | United States (US) |
| Impacted version(s) | 202309 (and later) |
## Changes
### Order APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * [POST Get Order List](get-order-list) <br> * [GET Get Order Detail](get-order-detail) | * New response parameter: `fast_delivery_program`. <br> * Indicates whether the seller for an order participates in the fast delivery program. <br> * Currently, the only available value is: `3_DAY_DELIVERY` |