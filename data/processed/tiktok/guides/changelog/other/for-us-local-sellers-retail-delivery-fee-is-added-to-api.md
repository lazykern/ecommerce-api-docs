# What is changing?
The states of Colorado enacted a new retail delivery fee, with Minnesota introducing a similar policy effective July 2024.
To be compliant with these laws, TikTok Shop will collect retail delivery fees from CO & MN states' buyers and show retail delivery fees on the place order page and invoice. The estimated launch time will be beginning of October. The following APIs will reflect the change:
## Get Order List, Get Order Details
A new property, `retail_delivery_fee`is added to the API response.
## Search Cancellations
A new property `refund_retail_delivery_fee` (the retail delivery fee refunded to buyer) is added to the API response as part of the `refund_amount` and `cancel_line_items` object.
## Search Return
A new property `refund_retail_delivery_fee` (the retail delivery fee refunded to buyer) is added to the API response as part of the `refund_amount` and `return_line_items` object.
## Calculate Refund
A new property `refund_retail_delivery_fee` (the retail delivery fee refunded to buyer) is added to the API response, in the `order_refund_amount` object.
# Which markets are affected?
This change is only for the **US market.**
# Who is affected?
All **local** sellers in the US will be affected by this change.
# Which version is applicable?
This change is applicable to **v202309**.
# What action is required?
We recommend that all integrations that serve these markets and use the API version update the processing logic to include these changes.