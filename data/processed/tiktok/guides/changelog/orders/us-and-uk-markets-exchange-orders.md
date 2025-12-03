## Summary
To provide a smoother after-sales experience, we've added a couple of response parameters that should help sellers keep track of their exchange orders.
## Affected markets and versions
This change applies to the following market(s):

* United States (US)
* United Kingdom (UK)

This change applies to the following API version(s):

* 202309 (and later)

## What's changing?
### Order APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * [Get Order List](get-order-list) <br> * [Get Order Detail](get-order-detail) | New response parameters: <br>  <br> * `is_exchange_order`: Indicates an exchange order when **TRUE**. <br> * `exchange_order_source_id`: If `is_exchange_order=TRUE`, returns the ID of the original order. |