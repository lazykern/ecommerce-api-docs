## Summary
TikTok Shop is rolling out **Co-Funded Free Shipping** in the US Market. New fields are added to both v202309 and v202212.
## API Changes
New fields to be added in 202309 ver. API:

* Customer shipping fee offset
* FBT fulfillment fee
* Promo Sign up shipping incentive

New fields to be added in 202212 ver. API:

* Limited-time Sign up incentive
* Limited-time Sign up incentive refund

## Detailed Changes
### Get Statement Transactions v202309

* Change 1: Three new properties added as per the table below:

| Property | Details |
| --- | --- |
| `customer_shipping_fee_offset_amount` | This billing item is currently applicable to US sellers only. Although included on FBT invoices, it will not lead to any net charges for sellers. Any shipping fees paid by the customer or the platform will be debited and forwarded to TikTok Shop. |
| `fbt_fulfillment_fee_amount` | The shipping fee incurred by sellers for orders fulfilled by TikTok. |
| `promo_shipping_incentive_amount` | From Aug 26, 2024 to Dec 31, 2024, TikTok shop will provide additional logistics incentives for sellers that have registered for the co-funded free shipping program. Negative amounts mean a clawback of the incentives given. |

* Change 2: The value existing field `shipping_cost_amount` is the sum of the three properties above.

There are no changes to the API parameters or error codes.
### Get Order Statement Transactions v202309

* Change 1: Three new properties added as per the table below:

| Property | Details |
| --- | --- |
| `customer_shipping_fee_offset_amount` | This billing item is currently applicable to US sellers only. Although included on FBT invoices, it will not lead to any net charges for sellers. Any shipping fees paid by the customer or the platform will be debited and forwarded to TikTok Shop. |
| `fbt_fulfillment_fee_amount` | The shipping fee incurred by sellers for orders fulfilled by TikTok. |
| `promo_shipping_incentive_amount` | From Aug 26, 2024 to Dec 31, 2024, TikTok shop will provide additional logistics incentives for sellers that have registered for the co-funded free shipping program. Negative amounts mean a clawback of the incentives given. |

* Change 2: The value existing field `shipping_cost_amount` is the sum of the three properties above.

There are no changes to the API parameters or error codes.
### Get Settlements v202212

* Change 1: Two new properties added as per the table below:

| Property | Details |
| --- | --- |
| `promo_shipping_incentive_amount` | For seller who signed up Co-funded free shipping program or joined FBT since 8/26, they will be eligible for an additional shipping incentives for orders if meet platform policy requirement. Incentives will ended up at 2024/12/31. |
| `promo_shipping_incentive_refund_amount` | Refund of promo_shipping_incentive_amount. |
There are no changes to the API parameters or error codes.
### Get Order Settlements v202212

* Change 1: Two new properties added as per the table below:

| Property | Details |
| --- | --- |
| `promo_shipping_incentive_amount` | For seller who signed up Co-funded free shipping program or joined FBT since 8/26, they will be eligible for an additional shipping incentives for orders if meet platform policy requirement. Incentives will ended up at 2024/12/31. |
| `promo_shipping_incentive_refund_amount` | Refund of promo_shipping_incentive_amount. |
There are no changes to the API parameters or error codes.