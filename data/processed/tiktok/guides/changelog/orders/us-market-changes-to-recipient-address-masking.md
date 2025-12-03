## Summary
We'll be making some upcoming customer data desensitization changes, specifically which `recipient_address`-related parameters are masked in the API response for our [Get Order List](get-order-list) and [Get Order Detail](get-order-detail) endpoints.

For some additional context, our current address masking protocol is as follows:

* Seller Shipping (**3PL**, `shipping_type=SELLER`) orders return an unmasked `recipient_address`.
* TikTok Shipping (**4PL**, `shipping_type=TIKTOK`) orders return a masked `recipient_address`.
* Fulfilled-by-TikTok (**FBT**, `fulfillment_type=FULFILLMENT_BY_TIKTOK`) orders return a masked `recipient_address`.

### Why is this a breaking change?

* We're masking some previously unmasked fields, which may affect the expected information in the API response, and feature/app logic as a result.
* Some sellers have built fulfillment processes based on the unmasking/availability of an address. In these cases, we want to emphasize that sellers should use `order_status` to determine if an order should be shipped.
* Unmasking/masking changes should have no impact on a seller's current fulfillment process, specifically whether they use 3PL or 4PL to fulfill an order.

## Impact
|  |  |
| --- | --- |
| Impacted market(s) | * United States (US) - **Local** and **cross-border** |
| Impacted version(s) | * 202309 (and later) |
## Changes
### Seller Shipping (3PL) and TikTok Shipping (4PL)
Address masking is dependent on `order_status`. For **3PL** and **4PL** orders, most address parameters will be **unmasked**. The key **masked** fields are as follows:
| `order_status` | `recipient_address` |
| --- | --- |
| * `UNPAID` <br> * `ON_HOLD` <br> * `CANCELLED` <br> * **30 days after** `COMPLETED` | * `phone_number` <br> * `name` <br> * `address_detail` <br> * `address_line1` <br> * `address_line2` <br> * `delivery_preferences` <br> * `postal_code` <br> * `district_info.address_level` **if L3 or L4** |
### Fulfilled-by-TikTok (FBT)
For **FBT** orders, most address parameters will be **masked**. The following `recipient_address` parameters for **all** `order_status` are will be **unmasked**:

* `buyer_email`
* `district_info.address_level` **if L0, L1, or L2**

Additionally, `district_info.address_level=L3` will be **unmasked** for the following `order_status`:

* `AWAITING_SHIPMENT`
* `AWAITING_COLLECTION`
* `PARTIALLY_SHIPPING`
* `IN_TRANSIT`
* `DELIVERED`
* `COMPLETED`

## Next steps
We're planning to implement these changes by **July 21st, 2025**, so please make sure any necessary updates are made by then.