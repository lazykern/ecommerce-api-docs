## Summary
New properties added to the statement-related Finance API endpoints for more detailed finance statements. Please refer to the **Required Actions** section for more information on the new properties.
## Affected Markets and Sellers
This change applies to local sellers in the US and UK markets.
## Applicable API Versions
This change applies to the v202309 API version.
## Required Actions
Developers who integrate with the following Finance APIs should apply these changes:

* [Get Order Statement Transactions](get-transactions-by-order)
* [Get Statement Transactions](get-transactions-by-statement)
* [Get Statements](get-statements)

Refer to the following table for the properties added to each endpoint:
| New properties | Description | Affected API(s) |
| --- | --- | --- |
| `net_sales_amount` | The total revenue with any applicable seller discounts deducted. Used for US, UK L2L sellers only. `net_sales_amount = gross_sales_amount + gross_sales_refund_amount + seller_discount_amount + seller_discount_refund_amount` | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) <br> * [Get Statements](get-statements) |
| `gross_sales_amount` | The total revenue before any discounts from the seller or TikTok Shop has been deducted. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |
| `gross_sales_refund_amount` | The amount of gross sales refunded to customers. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |
| `seller_discount_amount` | Seller discounts are the total amount of discounts funded by the seller. These include: <br>  <br> 1. Discounts funded by the seller through the seller's promotions (Product Discount, Flash Deal, Buy More Save More, Voucher and Bundle Deal) <br> 2. Seller's portion of a co-funded voucher discount during the seller's participation in co-funding campaigns <br> 3. Discounts funded by the seller during a campaign. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |
| `seller_discount_refund_amount` | Discounts refunded to the seller. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |
| `shipping_cost_amount` | Only for UK and US Local Sellers, represent the total fees related to shipping. Equates to `fbm_shipping_cost_amount + fbt_shipping_cost_amount + signature_confirmation_fee_amount + customer_paid_shipping_fee_amount + customer_paid_shipping_fee_refund_amount + shipping_cost_discount_amount + refund_shipping_cost_discount_amount + shipping_fee_subsidy_amount + return_shipping_fee_amount + shipping_insurance_amount` | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) <br> * [Get Statements](get-statements) |
| `customer_paid_shipping_fee_amount` | The shipping fee incurred by the customer based on the product weight you uploaded. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |
| `customer_paid_shipping_fee_refund_amount` | The refunded amount of customer-paid shipping fees deducted from your account. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |
| `shipping_fee_subsidy_amount` | The shipping fee subsidy provided by TikTok Shop for orders fulfilled by seller themselves. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |
| `return_shipping_fee_amount` | The shipping fee paid by the seller for the delivery of returns. | * [Get Order Statement Transactions](get-transactions-by-order) <br> * [Get Statement Transactions](get-transactions-by-statement) |

Additionally, the `settlement_amount` is returned from the same three endpoints:

* [Get Order Statement Transactions](get-transactions-by-order)
* [Get Statement Transactions](get-transactions-by-statement)
* [Get Statements](get-statements)

For orders created after 2024-01-01, the calculation for `settlement_amount` is adjusted as `settlement_amount = net_sales_amount + shipping_cost_amount + fee_amount + adjustment_amount`.