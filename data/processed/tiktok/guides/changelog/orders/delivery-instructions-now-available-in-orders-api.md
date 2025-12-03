# What is changing?
We've introduced a new `delivery_instruction` component to the Get Order Detail and Get Order List APIs. This component includes the `drop_off_location` property, which represents the customer's preferred package drop-off location specified at the time of order placement. For instance, it could be "front door / porch" or "back door".


This new property allows sellers to provide delivery instructions to the shipping provider, enabling the postman to deliver the package to the customer's preferred location.


To effectively implement the newly introduced `delivery_instruction` component, it's essential to adopt version 202309 of the APIs. Learn more about the prior significant updates on API paths and versioning methods from [Introducing API version 202309](introducing-api-version-202309).


The following are the new API paths:

* Get Order List: /order/202309/orders/search
   * For example:

```plaintext
https://open-api.tiktokglobalshop.com/order/202309/orders/search?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268
```


* Get Order Detail: /order/202309/orders
   * For example:

```plaintext
https://open-api.tiktokglobalshop.com/order/202309/orders?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&ids=ids=1234565,123555
```

# Which markets are affected?
The `delivery_instruction` component is available to local sellers and cross-border sellers in the US market.
# Who is affected?
This change only applies to developers with applications that use API version 202309 of the Get Order Detail and Get Order List API.
Learn more about [Upgrading to API version 202309](upgrading-to-api-version-202309).
# What action is required?
We strongly recommend developers integrate the new `delivery_instruction` component and prominently display the `drop_off_location` sellers and shipping providers for efficient and accurate deliveries.