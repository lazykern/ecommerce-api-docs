# Basic Data Type

 

  * uint8: 8 bit unsigned integer
  * uint16: 16 bit unsigned integer
  * int32: 32 bit signed integer
  * uint32: 32 bit unsigned integer
  * uint64: 64 bit unsigned integer
  * timestamp: uint32
  * country: ISO ALPHA-2 Code, string of 2 characters



# OrderStatus

 

  * UNPAID:Order is created, buyer has not paid yet.
  * READY_TO_SHIP:Seller can arrange shipment.
  * PROCESSED:Seller has arranged shipment online and got tracking number from 3PL.
  * RETRY_SHIP:3PL pickup parcel fail. Need to re arrange shipment. 
  * SHIPPED:The parcel has been drop to 3PL or picked up by 3PL.
  * TO_CONFIRM_RECEIVE:The order has been received by buyer.
  * IN_CANCEL:The order's cancelation is under processing.
  * CANCELLED:The order has been canceled.
  * TO_RETURN:The buyer requested to return the order and order's return is processing.
  * COMPLETED:The order has been completed.



# ReturnStatus

 

  * REQUESTED
  * ACCEPTED
  * CANCELLED
  * JUDGING
  * CLOSED
  * PROCESSING
  * SELLER_DISPUTE



# ReturnSolution

 

  * RETURN_REFUND
  * REFUND



# ReturnReason

 

  * NONRECEIPT
  * WRONG_ITEM
  * ITEM_DAMAGED
  * DIFF_DESC
  * MUITAL_AGREE
  * OTHER
  * USED
  * NO_REASON
  * ITEM_WRONGDAMAGED
  * CHANGE_MIND
  * ITEM_MISSING
  * EXPECTATION_FAILED
  * ITEM_FAKE
  * PHYSICAL_DMG
  * FUNCTIONAL_DMG
  * ITEM_NOT_FIT
  * SUSPICIOUS_PARCEL
  * EXPIRED_PRODUCT
  * WRONG_ORDER_INFO
  * WRONG_ADDRESS
  * CHANGE_OF_MIND
  * SELLER_SENT_WRONG_ITEM
  * SPILLED_CONTENTS
  * BROKEN_PRODUCTS
  * DAMAGED_PACKAGE
  * SCRATCHED
  * DAMAGED_OTHERS
  * SIZE_DEVIATION
  * LOOK_DEVIATION
  * DATE_DEVIATION
  * DIFFERENT_DESCRIPTION



# LogisticsStatus

 

  * LOGISTICS_NOT_START:Initial status, order not ready for fulfillment
  * LOGISTICS_PENDING_ARRANGE:order logistics pending arrangement
  * LOGISTICS_COD_REJECTED:Integrated logistics COD: Order rejected for COD
  * LOGISTICS_READY:order ready for fulfillment from payment perspective:non-COD: order paidCOD: order passed COD screening
  * LOGISTICS_REQUEST_CREATED:order arranged shipment
  * LOGISTICS_PICKUP_DONE:order handed over to 3PL
  * LOGISTICS_DELIVERY_DONE:order successfully delivered
  * LOGISTICS_INVALID:order cancelled when order at LOGISTICS_READY
  * LOGISTICS_REQUEST_CANCELED:order cancelled when order at LOGISTICS_REQUEST_CREATED
  * LOGISTICS_PICKUP_FAILED:order cancelled by 3PL due to failed pickup or picked up but not able to proceed with delivery
  * LOGISTICS_PICKUP_RETRY:order pending 3PL retry pickup
  * LOGISTICS_DELIVERY_FAILED:order cancelled due to 3PL delivery failed
  * LOGISTICS_LOST:order cancelled due to 3PL lost the order



# PackageFulfillmentStatus

  * LOGISTICS_NOT_START: Initial status, package not ready for fulfillment
  * LOGISTICS_READY: Package ready for fulfillment from payment perspective. For non-COD:  paid; forCOD: passed COD screening
  * LOGISTICS_REQUEST_CREATED: Package arranged shipment
  * LOGISTICS_PICKUP_DONE: Package handed over to 3PL
  * LOGISTICS_DELIVERY_DONE: Package successfully delivered
  * LOGISTICS_INVALID: Order cancelled when package at LOGISTICS_READY
  * LOGISTICS_REQUEST_CANCELED: Order cancelled when package at LOGISTICS_REQUEST_CREATED
  * LOGISTICS_PICKUP_FAILED: Order cancelled by 3PL due to failed pickup or picked up but not able to proceed with delivery
  * LOGISTICS_PICKUP_RETRY: Package pending 3PL retry pickup
  * LOGISTICS_DELIVERY_FAILED: Order cancelled due to 3PL delivery failed
  * LOGISTICS_LOST: Order cancelled due to 3PL lost the Package



# ReturnDisputeReasonId

 

  * "1": "I would like to reject the non-receipt claim"
  * "2": "I would like to reject the return request"
  * "3": "I agree with the return request, but I did not receive the product(s) which was/were supposed to be"
  * "4": "未收到退貨"
  * "5": "商品毀損/瑕疵"
  * "6": "商品缺件/不符"
  * "7": "非鑑賞期商品"
  * "8": "其他"
  * "9": "I have shipped the item(s) and have proof of shipment"
  * "10": "I shipped the correct item(s) as buyer ordered"
  * "11": "I shipped the item(s) in good working condition"
  * "12": "I agreed with the return request, but I have not received the item(s) that was/were supposed to be returned"
  * "13": "I agreed with the return request, but I received wrong/damaged item(s) from buyer"
  * "41": "I have shipped the item(s) and have proof of shipment"
  * "42": "I shipped the correct item(s) as buyer ordered"
  * "43": "I shipped the item(s) in good working condition"
  * "44": "Unable to come to an agreement with buyer"
  * "45": "Products are not in the appreciation period"
  * "46": "Did not receive the return product"
  * "47": "Received return products with physical damage"
  * "48": "Received incomplete return products (missing quantity/accessories)"
  * "49": "Received wrong return product"
  * "50": "Received return item(s), buyer's claim incorrect"
  * "51": "Unable to come to an agreement with seller"
  * "53": "Buyer’s claim is incorrect"
  * "54": "Buyer has been refunded wrong amount"
  * "55": "Buyer claim is correct, but I have other concerns"
  * "56": "Received return item(s), but item is used"
  * "81": "Did not receive the return product"
  * "82": "Received return products with physical damage"
  * "83": "Received incomplete return products (missing quantity/accessories)"
  * "84": "Received wrong return product"
  * "85": "Products are not in the appreciation period"
  * "86": "Received return item(s), buyer's claim incorrect"
  * "87": "The product(s) returned is excluded from buyer's statutory right of withdrawal"
  * "88": "Buyer was unresponsive in Seller Arrange Return"
  * "89": "Received return item(s), but item is used"



# AttributeType

 

  * INT_TYPE
  * STRING_TYPE
  * ENUM_TYPE
  * FLOAT_TYPE
  * DATE_TYPE
  * TIMESTAMP_TYPE



# AttributeInputTypeEdit

 

  * DROP_DOWN
  * TEXT_FILED
  * COMBO_BOX
  * MULTIPLE_SELECT
  * ﻿MULTIPLE_SELECT_COMBO_BOX



 

For more details, please check: [_https://open.shopee.com/faq?top=162 &sub=166&page=1&faq=195_](<https://open.shopee.com/faq?top=162&sub=166&page=1&faq=195>)

# CancelReason（Seller）

 

  * OUT_OF_STOCK
  * UNDELIVERABLE_AREA (only for TW and MY)



# FeeType

 

  * SIZE_SELECTION
  * SIZE_INPUT
  * FIXED_DEFAULT_PRICE
  * CUSTOM_PRICE
  * SELLER_LOGISTICS



# PaymentMethod

 

  * Cybersource [ID, VN, TW, SG, MY, TH, PH]
  * Nicepay Credit Card [ID]
  * IPay88 Credit Card [MY]
  * Airpay Credit Card [PH]
  * Stripe CC [PH]
  * Airpay Credit Card [ID, VN, TW, TH]
  * Bank Transfer [ID]
  * Bank BCA (Manual Transfer) [ID]
  * Bank Mandiri (Manual Transfer) [ID]
  * Bank BNI (Manual Transfer) [ID]
  * Bank BRI (Manual Transfer) [ID]
  * Bank CIMB Niaga (Manual Transfer) [ID]
  * Bank Transfer [VN]
  * Fubon Bank Transfer [TW]
  * Esun Bank Transfer [TW]
  * Bank Transfer [TW]
  * Esun CB Bank Transfer [TW]
  * Bank Transfer [SG]
  * Bank Transfer [MY]
  * ATM Payment [TH]
  * ATM Payment (BBL) [TH]
  * Bank Transfer [TH]
  * ATM Payment (KBANK) [TH]
  * ATM Payment (KTB) [TH]
  * ATM Payment (SCB) [TH]
  * ATM Payment (BAY) [TH]
  * Online Payment (KBANK) [TH]
  * Online Payment (BAY) [TH]
  * Bank Transfer [PH]
  * Cash on Delivery [ID, VN, SG, MY, TH, PH]
  * 現付 [TW]
  * Shopee Seller Wallet [ID]
  * Shopee Wallet [ID, VN, TW, SG, MY, TH, PH]
  * Indomaret [ID]
  * Bank BRI (Virtual Account) [ID]
  * Bank BCA (Virtual Account) [ID]
  * Bank Mandiri (Virtual Account) [ID]
  * Bank BNI (Virtual Account) [ID]
  * Virtual Account Parent [ID]
  * Android Pay [SG]
  * MOLPay [MY]
  * iPay 88 [MY]
  * iBanking Payment [TH]
  * iBanking Payment (BBL) [TH]
  * iBanking Payment (KTB) [TH]
  * iBanking Payment (SCB) [TH]
  * Dragonpay - Remittance Center [PH]
  * Dragonpay - OTC [PH]
  * Dragonpay - Online Payment [PH]
  * Buyer-Seller Self Arrange [ID, VN, TW, SG, MY, TH, PH]
  * Kredivo [ID]
  * Kredivo - BNPL [ID]
  * Kredivo - 3 Months Installment [ID]
  * Kredivo - 6 Months Installment [ID]
  * Kredivo - 12 Months Installment [ID]
  * Nicepay Credit Card Installment [ID]
  * BCA One Klik [ID]
  * Akulaku [ID]
  * Free [Vn, TW, SG, MY, TH, PH]
  * iPay88 CC Installment [MY]
  * Ebanx Credit Card [BR]
  * Ebanx Credit Card Installment [BR]
  * Ebanx Credit Card Installment 1x installment plan [BR]
  * Ebanx Credit Card Installment 2x installment plan [BR]
  * Ebanx Credit Card Installment 3x installment plan [BR]
  * Ebanx Credit Card Installment 4x installment plan [BR]
  * Ebanx Credit Card Installment 5x installment plan [BR]
  * Ebanx Credit Card Installment 6x installment plan [BR]
  * Ebanx Boleto [BR]



# CancelReason

 

  * Out of Stock
  * Buyer Request to Cancel
  * Undeliverable Area
  * COD Unsupported
  * Parcel is Lost
  * Game Completed
  * Unpaid Order
  * Underpaid Order
  * Unsuccessful / Rejected Payment
  * Logistics Request is Cancelled
  * 3PL pickup Fail
  * Failed Delivery
  * COD Rejected
  * Seller did not Ship
  * Transit Warehouse Cancelled
  * Other
  * Inactive Seller
  * Auto Cancel
  * Logistic Issue
  * Your approver did not approve order on time.
  * You are unable to place order at the moment.
  * TBC



# ShippingDocumentType

 

  * NORMAL_AIR_WAYBILL
  * THERMAL_AIR_WAYBILL
  * NORMAL_JOB_AIR_WAYBILL
  * THERMAL_JOB_AIR_WAYBILL



# ItemStatus

 

  * NORMAL
  * BANNED
  * UNLIST
  * REVIEWING
  * SELLER_DELETE
  * SHOPEE_DELETE



# StockType

 

  * 1: Shopee Warehouse Stock
  * 2: Seller Stock



# Language

 

  * zh-hans
  * zh-hant
  * ms-my
  * en-my
  * en
  * id
  * vi
  * th
  * pt-br
  * es-mx
  * pl
  * es-CO
  * es-CL
  * es-ES
  * es-ar



# PromotionType

 

  * Campaign
  * Discount Promotions
  * Flash Sale
  * Whole Sale
  * Group Buy
  * Bundle Deal
  * Welcome Package
  * Add-on Discount
  * Brand Sale
  * In ShopFlash Sale
  * Gift with purchase
  * ﻿Exclusive Price
  * Platform Streaming
  * Seller Streaming



# BuyerCancelReason

 

  * Seller is not Responsive to buyer's Inquires
  * Seller ask Buyer to Cancel
  * Modify Existing Order
  * Product has Bad Reviews
  * Seller Takes too Long to Ship The Order
  * Seller is Untrustworthy
  * Others
  * Forgot to Input Voucher Code
  * Need to change delivery address
  * Need to Change Delivery Address
  * Need to input / Change Voucher Code
  * Need to Modify Order
  * Payment Procedure too Troublesome
  * Found Cheaper Elsewhere
  * Don't Want to Buy Anymore
  * Your approver rejected the order.
  * You are unable to place order at the moment.
  * Need to change delivery address
  * Too long delivery time
  * Modify existing order (color, size, voucher, etc)
  * Change of mind / others



# TrackingLogisticsStatus

 

  * INITIAL
  * ORDER_INIT
  * ORDER_SUBMITTED
  * ORDER_FINALIZED
  * ORDER_CREATED
  * PICKUP_REQUESTED
  * PICKUP_PENDING
  * PICKED_UP
  * DELIVERY_PENDING
  * DELIVERED
  * PICKUP_RETRY
  * TIMEOUT
  * LOST
  * UPDATE
  * UPDATE_SUBMITTED
  * UPDATE_CREATED
  * RETURN_STARTED
  * RETURNED
  * RETURN_PENDING
  * RETURN_INITIATED
  * EXPIRED
  * CANCEL
  * CANCEL_CREATED
  * CANCELED
  * FAILED_ORDER_INIT
  * FAILED_ORDER_SUBMITTED
  * FAILED_ORDER_CREATED
  * FAILED_PICKUP_REQUESTED
  * FAILED_PICKED_UP
  * FAILED_DELIVERED
  * FAILED_UPDATE_SUBMITTED
  * FAILED_UPDATE_CREATED
  * FAILED_RETURN_STARTED
  * FAILED_RETURNED
  * FAILED_CANCEL_CREATED
  * FAILED_CANCELED



# SellerProofStatus

 

  * NOT_NEEDED
  * PENDING
  * UPLOADED
  * OVERDUE



# TransactionType

 

  * ESCROW_VERIFIED_ADD = 101;  // Escrow has been verified and paid to seller.    
  * ESCROW_VERIFIED_MINUS = 102; // Escrow has been verified and charged from seller as escrow amount is negative.    
  * WITHDRAWAL_CREATED = 201; // The seller has created a withdrawal, so it’s deducted from balance.      
  * WITHDRAWAL_COMPLETED = 202; // The withdrawal has been completed, so the ongoing amount decreases.        
  * WITHDRAWAL_CANCELLED = 203; // The withdrawal has been canceled, so the amount is added back to the seller balance. Ongoing amount decreases as well. 
  * REFUND_VERIFIED_ADD = 301; //  Normal Order Refund.
  * AUTO_REFUND_ADD=302; // Normal Order Auto Refund.   
  * ADJUSTMENT_ADD = 401; // One adjustment item has been paid to seller.     
  * ADJUSTMENT_MINUS = 402; // One adjustment item has been charged from seller.     
  * FBS_ADJUSTMENT_ADD = 404; //One adjustment item related to Shopee fulfillment order is added to seller.      
  * FBS_ADJUSTMENT_MINUS = 405; // One adjustment item related to Shopee fulfillment order is deducted from seller.      
  * ADJUSTMENT_CENTER_ADD = 406; // One adjustment item has been added to seller wallet.     
  * ADJUSTMENT_CENTER_DEDUCT = 407; // One adjustment item has been deducted from seller wallet.     
  * ESCROW_ADJUSTMENT_FOR_FD_DEDUCT = 408; // FSF cost passing for canceled/invalid orders.    
  * PERCEPTION_VAT_TAX_DEDUCT = 409; // Extra charge for perception regime VAT tax (Argentina). 
  * ADJUSTMENT_FOR_RR_AFTER_ESCROW_VERIFIED = 411;// RR adjustment after escrow verified (seller received the parcels), deduct.
  * AFFILIATE_COMMISSION_FEE_ADD = 412; // To credit Seller affiliate commission into seller wallet.
  * CROSS_MERCHANT_ADJUSTMENT_ADD = 413;// Automated positive wallet adjustment to FBS/B2C wallets based on the escrow amount owned by the FBS/B2C shop in a specific cross listed order.
  * CROSS_MERCHANT_ADJUSTMENT_DEDUCT = 414; // Automated negative wallet adjustment to FBS/B2C wallets based on the escrow amount owned by the FBS/B2C shop in a specific cross listed order.
  * SELLER_COMPENSATE_ADD = 415; // In the new RR flow, buyers will get the benefit of auto and accelerated refunds, where Shopee can accept the refunds without the seller. Subsequently, sellers can raise a compensation request if needed.This txn type is to compensate such sellers.
  * CAMPAIGN_PACKAGE_ADD = 416; // To refund sellers who have been overcharged for their campaign fees, only for ID.
  * CAMPAIGN_PACKAGE_MINUS = 417;// To further deduct from sellers who have been undercharged for their campaign fees, only for ID.
  * PAID_ADS_CHARGE = 450; // Paid ads are charged from seller.     
  * PAID_ADS_REFUND = 451; // Paid ads are refunded to seller.     
  * FAST_ESCROW_DISBURSE = 452; // ADD. // The first disbursement of fast escrow has been paid to seller.     
  * AFFILIATE_ADS_SELLER_FEE = 455; // DEDUCT // Affiliate ads seller fee is charged from seller.     
  * AFFILIATE_ADS_SELLER_FEE_REFUND = 456; // ADD // Affiliate ads seller fee is refunded to seller.
  * FAST_ESCROW_DEDUCT = 458; // Fast escrow is deducted from seller balance in the event of return and refund. 
  * FAST_ESCROW_DISBURSE_REMAIN = 459; // The second disbursement of fast escrow has been paid to seller.     
  * AFFILIATE_FEE_DEDUCT = 460; // Affiliate MKT fee is charged from seller for using affiliate MKT services.
  * SHOPEE_WALLET_PAY = 501;// Local SIP, deduct from seller wallet.
  * SPM_DEDUCT = 502;// SPM charge seller wallet as payment.
  * APM_DEDUCT = 503;// APM charge seller wallet as payment.
  * SPM_REFUND_ADD = 504; // Normal Order Refund.
  * APM_REFUND_ADD = 505; // Normal Order Refund.
  * DP_REFUND_VERIFIED_ADD = 701; // Digital product purchase refund verified and paid to seller.
  * SPM_DEDUCT_DIRECT = 801; // Shopee Credit Sellerloan Repayment, eg: provision channel id. 8008601
  * SPM_DISBURSE_ADD = 802; // Sellerloan pay out to seller wallet.



# SellerCompensationStatus

 

  * COMPENSATION_NOT_APPLICABLE
  * COMPENSATION_INITIAL_STAGE
  * COMPENSATION_PENDING_REQUEST
  * COMPENSATION_NOT_REQUIRED
  * COMPENSATION_REQUESTED
  * COMPENSATION_APPROVED
  * COMPENSATION_REJECTED
  * COMPENSATION_CANCELLED
  * COMPENSATION_NOT_ELIGIBLE



# NegotiationStatus

 

  * PENDING_RESPOND
  * PENDING_BUYER_RESPOND
  * TERMINATED



# **Return Refund Request Type**

 

  * 0:  Normal RR（RR is raised by the buyer after they have received the parcel, based on estimated delivery date /delivery done ）
  * 1: In-Transit RR (RR is raised by the buyer while item is still in-transit to buyer)
  * 2: Return-on-the-Spot (RR is raised by the driver after buyer rejected parcel at delivery)



# **Validation Type**

 

  * seller_validation: For Return & Refund requests with return parcel that will be delivered to the seller for validation and decision whether to refund buyer or to raise dispute
  * warehouse_validation: For Return & Refund requests with return parcel that will be delivered to warehouse for validation and decision whether to refund buyer or to raise dispute



# **Reverse Logistics Status**

## **[Normal Return]**

 

  * LOGISTICS_PENDING_ARRANGE: Return is now pending user to select shipping option. Same for both integrated logistics and non-integrated logistics. 
  * LOGISTICS_READY: User has selected shipping option, and pending system to create logistics request. Tracking number is not yet available. Same for both integrated logistics and non-integrated logistics. 
  * LOGISTICS_REQUEST_CREATED: Means that the logistics request has been created successfully. Tracking number should be available
  * LOGISTICS_PICKUP_RETRY: Third party logistics provider will make another attempt to pick up parcel from buyer. Only available for integrated logistics since this is updated by third party logistics provider back to Shopee. 
  * LOGISTICS_PICKUP_FAILED: Third party logistics provider has failed to pickup parcel from buyer. Only available for integrated logistics since this is updated by third party logistics provider back to Shopee. 
  * LOGISTICS_PICKUP_DONE: For integrated logistics, this means the parcel has been picked up by a third party logistics provider. For non-integrated logistics, this means the user has entered shipping proof. 
  * LOGISTICS_DELIVERY_FAILED: Parcel delivery to seller has failed. Only available for integrated logistics since this is updated by third party logistics provider back to Shopee. 
  * LOGISTICS_LOST: Parcel has been marked as lost. Only available for integrated logistics since this is updated by third party logistics provider back to Shopee. 
  * LOGISTICS_DELIVERY_DONE: Parcel has been successfully delivered to seller. Only available for integrated logistics since this is updated by third party logistics provider back to Shopee. 



## **[In-transit RR]**

 

  * Preparing
  * Delivered  
  * Delivery Failed  
  * Lost



## **[Return-on-the-Spot]**

 

  * Preparing
  * Delivered  
  * Delivery Failed  
  * Lost



# **Post Return Logistics Status**

 

Note this is only applicable to return parcels sent from warehouse back to seller

  * POST_RETURN_LOGISTICS_REQUEST_CREATED: Logistics request generated successfully with tracking number.
  * POST_RETURN_LOGISTICS_REQUEST_CANCELED: ​​Logistics request cancelled by warehouse team
  * POST_RETURN_LOGISTICS_PICKUP_FAILED: Failed to pickup parcel
  * POST_RETURN_LOGISTICS_PICKUP_RETRY: Subsequent attempt to pickup parcel.
  * POST_RETURN_LOGISTICS_PICKUP_DONE: Successful pickup; on the way to destination. 
  * POST_RETURN_LOGISTICS_DELIVERY_FAILED: Failed delivery of parcel. Driver will return parcel back to warehouse.
  * POST_RETURN_LOGISTICS_DELIVERY_DONE: Successful delivery of parcel
  * POST_RETURN_LOGISTICS_LOST: Parcel marked as Lost