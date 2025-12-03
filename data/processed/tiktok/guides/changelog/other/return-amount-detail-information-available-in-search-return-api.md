# What is changing?
The [Search Return API](https://partner.tiktokshop.com/docv2/page/search-returns) will now return the granular data fields (such as discount returned and shipping fee returned) regarding the return amount. These fields can be used by any seller that has a strong data analytics team.
## Search Returns
### Parameters
No change
### Responses
Adding `discount_amount` and `return_shipping_fee_amount` property, which includes the following fields:

* `discount_amount:`
   * `currency`
   * `product_platform_discount`: The refund amount of product platform discount.
   * `product_seller_discount`: The refund amount of product seller discount.
   * `shipping_fee_platform_discount`: The refund amount of shipping fee platform discount.
   * `shipping_fee_seller_discount`: The refund amount of shipping fee seller discount
* `return_shipping_fee_amount`:
   * `currency`
   * `seller_paid_return_shipping_fee_amount`: The amount of return shipping fee seller paid.
   * `buyer_paid_return_shipping_fee_amount`: The amount of return shipping fee buyer paid.
   * `platform_paid_return_shipping_fee_amount`: The amount of return shipping fee platform paid.

```JSON
{
  "code": 0,
  "data": {
    "next_page_token": "aDU2dHIzMlFhME5CUzJKUDhDdVJhTDM1WmJkeFVTVW9LTkRaSnNaZCtuWjJXVU5CSDhlaA==",
    "return_orders": [
      {
        "arbitration_status": "IN_PROGRESS",
        "refund_amount": {
          "currency": "USD",
          "refund_shipping_fee": "0.2",
          "refund_subtotal": "1",
          "refund_tax": "0.03",
          "refund_total": "1.23"
        },
        "discount_amount":{
          "currency": "USD",
          "product_platform_discount":"12",
          "product_seller_discount":"12",
          "shipping_fee_platform_discount":"12",
          "shipping_fee_seller_discount":"12"
        },
        "return_shipping_fee_amount":{
          "currency": "USD",
          "seller_paid_return_shipping_fee":"12",
          "buyer_paid_return_shipping_fee":"12",
          "platform_paid_return_shipping_fee":"12"
       },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

Calculation logic: `refund_total` = `refund_subtotal` + `refund_shipping_fee` + `refund_tax`
# Which markets are affected?
This change is rolled out to all markets.
# Who is affected?
This change can be integrated by all sellers.
# Which version is applicable?
This change is applicable only to **v202309**.
# What action is required?
Any seller that wants to do advanced data analytics on the return amounts can integrate the new data points.