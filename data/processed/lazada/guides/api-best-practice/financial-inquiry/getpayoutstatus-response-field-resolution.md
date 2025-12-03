This table shows the calculation logic of some fields in GetPayoutStatus API and the fees covered.

  

response key | value
---|---
item_revenue | Item Price Credit
other_revenue_total | Shipping Fee (Paid By Customer) Seller Credit Seller Credit Item Lost or Damaged - Sales Order Item Lost or Damaged - Product
fees_total | Monthly Subscription Payment Fee Fulfillment by Lazada Handling Fee - Automatic Handling Fee Commission Other Fee Seller Debit Item Shipping Fee (Charged by Lazada) Automatic Shipping Fee Storage Fee Cancellation Fee Return Delivery Fee Returned QC Fee Return to Seller Fee Dropshipping Delivery Fee Refund Fee Lazada Shipping Service Cost Pick Fee Pack Fee Dropshipping Delivery Fee Promotional Charges Bundles Promotional Charges Vouchers
refunds | Reversal Item Price
fees_on_refunds_total | Reversal Item Price Reversal Commission R eversal Promotional Charges Bundles Reversal Promotional Charges Vouchers
shipment_fee | Shipping Fee (Charged by Lazada)
shipment_fee_credit | Shipping Fee (Paid By Customer)
subtotal1 | item_revenue + other_revenue_total - fees_total
subtotal2 | subtotal1 - refunds