This table shows the calculation logic of some fields in GetPayoutStatus API and the fees covered.

  


**response key**| **value**  
---|---  
item_revenue| Item Price Credit  
other_revenue_total| Shipping Fee (Paid By Customer)Seller CreditSeller Credit ItemLost or Damaged - Sales Order ItemLost or Damaged - Product  
fees_total| Monthly SubscriptionPayment FeeFulfillment by Lazada Handling Fee - AutomaticHandling FeeCommissionOther FeeSeller Debit ItemShipping Fee (Charged by Lazada)Automatic Shipping FeeStorage FeeCancellation FeeReturn Delivery FeeReturned QC FeeReturn to Seller FeeDropshipping Delivery FeeRefund FeeLazada Shipping Service CostPick FeePack FeeDropshipping Delivery FeePromotional Charges BundlesPromotional Charges Vouchers  
refunds| Reversal Item Price  
fees_on_refunds_total| Reversal Item PriceReversal CommissionReversal Promotional Charges BundlesReversal Promotional Charges Vouchers  
shipment_fee| Shipping Fee (Charged by Lazada)  
shipment_fee_credit| Shipping Fee (Paid By Customer)  
subtotal1| item_revenue + other_revenue_total - fees_total  
subtotal2| subtotal1 - refunds