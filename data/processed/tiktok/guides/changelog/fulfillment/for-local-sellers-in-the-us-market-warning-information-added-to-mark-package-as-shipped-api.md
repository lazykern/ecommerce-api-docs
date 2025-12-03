# What is changing?
We added a new `warning` component to the [Mark Package As Shipped](mark-package-as-shipped) API. The new component includes the following field:

* `message`: TikTok Shop validates the `tracking number` value and returns a warning message if it detects any issues, such as:
   * The value does not match any shipping provider.
   * The value matches multiple shipping providers.
   * The value matches a different `shipping_provider_id` than what you passed via the API parameter.

The `message` field might contain the following warning messages:
| Message |
| --- |
| Verifying order tracking number timeout. Please ensure your tracking number and logistics provider is correct. |
| No logistics provider could be found for this tracking number. Check the tracking number and try again. |
| The tracking number you entered matches multiple logistics providers. Ensure you select the correct logistics provider. |
| No logistics provider or service could be found for this tracking number. Check the tracking number and try again. |
| The tracking number you entered does not match your selected logistics provider. Check the tracking number and logistics provider. Did you mean to select {{inferred_provider_name}}? |
## Code Sample
```JSON
{
  "code": 0,
  "data": 
  {
    "package_id": "31241234123131",
    "detail":
    {
        "order_id": "32213123",
        "Order_line_item_id": "231242313412234"
    }
    "warning":
    {
        "message": "The tracking number can not match logistics provider, please check the tracking number and shipping provider id."
    }
  },
  "message": "Success",
  "request_id": "202203070749000101890810281E8C70B7"
}
```

# Which markets are affected?
The `warning` component is available to local sellers in the US market.
# Who is affected?
This change only applies to developers with applications that use API version 202309 and the Mark Package As Shipped API to ship seller packages.
# What action is required?
When the `warning` component appears in the API response, be sure to clearly display the message to sellers and advise them to verify the accuracy of the tracking number and shipping provider information.