This tutorial will describe which APIs to call to cancel unshipped orders for seller reasons.

Note: Cancellation of orders for seller's reason will affect store rating, high cancellation rate may lead to daily order volume limit (ovl), please use with caution.

![](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1716883000837_BZFqxIWc)

# Step 1 Call the GetOrderItems API

Call the GetOrderItems API to get all order item ids for the order you need.

Lazada cancels orders not by order level, but by order item level.

# Step 2 Call the OrderCancelValidate API

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Freverse%2Fcancel%2Fvalidate>)

Before canceling an order, you also need to confirm whether the current order can be cancelled and what are the available reasons for cancellation, so you need to call the OrderCancelValidate API.

If the status of the order item you need to cancel is not Pending\Packed\ReadyToShip, then you cannot cancel the order item.

## Response Demo

{

  "data": {

    "tip_content": "SKU stock may be set to 0* after cancellation due to reasons: ‘out of stock’ or ‘incorrect pricing’, to prevent new orders while you adjust your stock/pricing. You can adjust your stock back up at any time. This adjustment will not impact existing orders. Note that cancellations can impact your ability to sell on Lazada if not managed carefully.\n\n*For more information, please view Seller Cancellation Policy page",

    "reason_options": [

      {

        "reason_name": "Sourcing Delay",

        "reason_id": "10000019"

      },

      {

        "reason_name": "Out of Stock",

        "reason_id": "10000021"

      },

      {

        "reason_name": "Wrong Price or Pricing Error",

        "reason_id": "10000023"

      }

    ],

    "tip_type": "warning"

  },

  "code": "0",

  "request_id": "2101069616872400092505868"

}

### Notes

  1. Not all orders can be cancelled. Orders that do not meet the criteria will report an error, and the specific reason will be displayed in the tip_content field.
  2. If you select "Out of Stock" or "Wrong Price or Pricing Error" as the reason for cancellation, the stock of the corresponding item will be adjusted to 0 to prevent further incorrect orders.
  3. The reason_id may be different for each country.
  4. Only order items with the Pending ~ Ready To Ship status can be cancelled.



# Step 3 Call the InitReverseOrderCancel API

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Freverse%2Fcancel%2Fcreate>)

Call this API and add the order id and order item id you need to cancel, as well as one of the reason_id in the second step of the response, so that it can be successfully cancelled.

## Response Demo

{

  "data": {

    "tip_content": "The order has been cancelled and SKU stock may have been set to 0. Please ensure you check your stock/pricing under “Manage Products”. Your customer has also been informed of the cancellation and will receive a customer experience survey.\nPlease reach out to your customer if you would like to provide service recovery.",

    "tip_type": "success"

  },

  "code": "0",

  "request_id": "2140c3e616872414077912824"

}

  1. Only order items with the Pending ~ Ready To Ship status can be cancelled.
  2. If the order is in pending status, then you can cancel any item in the order using the order item id without canceling the whole order.
  3. If the order is in the packaged state, other order items in the same package will also be cancelled when the order item is cancelled. So if you don't want this, please call the [RecreatePackage API](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fpackage%2Frepack>) to cancel the package first.