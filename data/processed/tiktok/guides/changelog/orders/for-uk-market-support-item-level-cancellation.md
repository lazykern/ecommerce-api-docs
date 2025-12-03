# What is changing?
The UK market now supports item level cancellations. Sellers are not forced to cancel the entire order when a single item cannot be fulfilled, they can now cancel the single item that is unable to be fulfilled.
Please note that item level cancellation is only available when an item is out of stock. Single item cancellations under other scenarios or for other reasons is not supported.
As of this change, item level cancellations (fka partial cancellations) are now supported in US and UK.
# Which markets are affected?
This change extends support for partial cancellations to the UK market.
# Who is affected?
Any developer who handles shipping, fulfillment or returns and deals with cancellation requests can adopt these changes. It is applicable to both local and cross-border sellers.
# Which version is applicable?
This change is only for **v202309**. Legacy APIs will not have support for item level cancellations.
# What action is required?
Developers need to update the business logic for handling cancellations when calling [Cancel Order API](cancel-order) such that they can now provide `order_line_item_ids` in the request body as part of the `skus` array.
Failure to integrate partial cancellations would mean that sellers will be forced to cancel the entire order and lead to poor user experience for the seller and the buyer.