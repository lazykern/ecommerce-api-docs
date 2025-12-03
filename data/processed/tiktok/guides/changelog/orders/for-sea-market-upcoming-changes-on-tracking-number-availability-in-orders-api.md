## What is changing?
In the past, the tracking_number field was automatically populated when you fetched order details using the [Get Order List](get-order-list) and [Get Order Detail](get-order-detail) APIs.
**Starting from March 25, 2024**, the tracking_number field will remain empty until the package is shipped.
## Which markets are affected?
This change applies to local shops and cross-border shops in TH, SG, MY, PH, VN markets, and local shops in the ID market.
## Who is affected?
Developers with apps that retrieve order information via Get Order List and Get Order Detail should take note of this change
## Which version is applicable?
This change applies to all versions of the Get Order List and Get Order Detail
## What action is required?
If your application relies on the tracking_number before the package is shipped, you'll need to update your code before **March 25, 2024**, to prevent any disruptions.
Moreover, for sellers using TikTok Shipping as their shipping method, it's not necessary to supply the tracking_number when calling the Ship Package API.