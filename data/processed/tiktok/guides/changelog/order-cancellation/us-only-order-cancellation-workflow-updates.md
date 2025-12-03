# What is changing?
Sellers can reject the buyer's cancel requests by shipping the packages. Previously, when the seller tried to ship the package, the following APIs would return an error: [Ship Package](https://partner.tiktokshop.com/docv2/page/ship-package), [Batch Ship Package](https://partner.tiktokshop.com/docv2/page/batch-ship-packages), [Mark Package As Shipped](https://partner.tiktokshop.com/docv2/page/mark-package-as-shipped) with the message `{"fail_code":21011007,"fail_reason":"Package item has after-sale request"}`. The parameters and responses of these APIs are not changed. See [below](#API Changes) for the endpoints that have changed.
After this change:

1. When there is a customer cancellation request pending process, we allow sellers to ship the package instead of previously returning API errors.
2. When sellers successfully ship the package, the cancellation request will be rejected automatically by TikTok Shop. Previously, sellers had to go to Seller Center to reject the cancellation request manually.

## API Changes
### Get Order List
| **Type** | **Changes** | **Notes** |
| --- | --- | --- |
| Request Body | Added `is_buyer_request_cancel` parameter | Set this to `TRUE` to retrieve orders that have a buyer cancel request. |
| Response | New property `is_buyer_request_cancel` | Returns `TRUE` if buyer has requested cancellation |
|  | New property `request_cancel_time` | The time when buyer requested cancellation |
### Get Order Detail
| **Type** | **Changes** | **Notes** |
| --- | --- | --- |
| Response | New property `is_buyer_request_cancel` | Returns `TRUE` if buyer has requested cancellation |
|  | New property `request_cancel_time` | The time when buyer requested cancellation |
# Which markets are affected?
This backend logic change is only for the US Market.
# Who is affected?
Local and cross-border sellers in the US Market are affected.
# Which version is applicable?
These changes are only for **v202309**.
# What action is required?
## Integration suggestions

1. Let sellers know they can reject the buyer's cancel requests by shipping the packages
2. Show sellers the orders that are attached with cancel requests
   * Use `is_buyer_request_cancel` in Orders API to let sellers know which orders have pending cancel requests from buyers (the Search Cancellation API also works in this case)
3. Use fulfillment APIs to ship packages and reject cancel requests
4. Stop using the Reject Cancellation endpoint before **March 31, 2024**.