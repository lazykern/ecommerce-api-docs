## Summary
A new API version is released for two APIs, [GET Statement Transactions](get-transactions-by-statement) and [GET Order Statement Transactions](get-transactions-by-order).
<span style="background-color: rgb(255, 245, 235)">📌 Starting from </span><span style="background-color: rgb(255, 245, 235)"><strong>2025-07-01</strong></span><span style="background-color: rgb(255, 245, 235)">, </span><span style="background-color: rgb(255, 245, 235)"><strong>v202309</strong></span><span style="background-color: rgb(255, 245, 235)"> for Get Statement Transactions and Get Order Statement Transactions endpoints will be retired.</span>
## What markets and versions are affected
This change is being made in an effort to unify the schema across multiple regions and is applicable to all regions.
## What is changing
### GET Statement Transactions

* **v2020309** has been upgraded to **v202501**.
* The root contains fields that provide aggregated financial details, such as the following:
   * `total_reserve_amount`
   * `total_settlement_amount`
   * `total_settlement_breakdown`
      * `total_revenue_amount`
      * `total_shipping_cost_amount`
      * `total_fee_tax_amount`
      * `total_adjustment_amount`
* The main data object is the `transactions` field, which contains detailed records of each transaction.
   * **Revenue Component**
      * Single `revenue_amount` field
      * A breakdown object with details on the breakdown of the revenue amount.
   * **Shipping Cost Component**
      * Single `shipping_cost_amount` field
      * A breakdown object with details on the breakdown of the shipping cost.
      * `customer_paid_shipping_fee_amount` and `customer_paid_shipping_fee_refund_amount` have been combined into a single field `customer_paid_shipping_fee_amount`.
      * NOTE: This object also has a `supplementary_component` object further breaking down things like platform/promotion/incentive amounts.
   * **Fee Tax Component**
      * Single `fee_tax_amount` field
      * A breakdown object with details on the breakdown of the fees and taxes, split into fee and tax objects.
   * Supplementary Component
      * Includes various information like sales tax, retail delivery, platform discounts, and other incentives that do not directly contribute to the settlement amount.

### GET Order Statement Transactions

* **v2020309** has been upgraded to **v202501**.
* The root now has the following keys:
   * `revenue_amount`
   * `fee_and_tax_amount`
   * `shipping_cost_amount`
   * `settlement_amount`
   * `statement_transactions` and `adjustment_amount` has been removed
   * `sku_statement_transactions` is now `sku_transactions`
* The main data object is the `sku_transactions` field, which contains detailed records of each SKU transaction.
   * **Revenue Component**
      * Single `revenue_amount` field
      * A breakdown object with details on the breakdown of the revenue amount.
   * **Shipping Cost Component**
      * Single `shipping_cost_amount` field
      * A breakdown object with details on the breakdown of the shipping cost.
      * `customer_paid_shipping_fee_amount` and `customer_paid_shipping_fee_refund_amount` have been combined into a single field `customer_paid_shipping_fee_amount`.
      * NOTE: This object also has a `supplementary_component` object further breaking down things like platform/promotion/incentive amounts.
   * **Fee Tax Component**
      * Single `fee_tax_amount` field
      * A breakdown object with details on the breakdown of the fees and taxes, split into fee and tax objects.

## What action is required
Developers with apps integrated with the Get Statement Transactions and Get Order Statement Transactions endpoints must upgrade to v202501 before **2025-07-01**. If you are integrating with the following two endpoints and support sellers across SEA + US/UK, we recommend you migrate to this version.