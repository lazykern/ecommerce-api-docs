# What is changing?
In the past, the tracking_number field was automatically populated when you fetched package information from APIs.
On January 25, 2024, we announced an update for the tracking_number field remaining empty before package shipping. Learn more about this announcement from our [changelog](for-sea-market-upcoming-changes-on-tracking-number-availability-in-orders-api). This is the second time announcement for this upcoming API change.
Starting from **May 31, 2024**, when retrieving package information from [Get Package Detail](get-package-detail), [Get Order Detail](get-order-detail) and [Get Order List](get-order-list), the tracking_number field will remain empty until the package is shipped or shipping label is printed.
# Which markets are affected?
This change applies to local shops and cross-border shops in TH, SG, MY, PH, VN markets, and local shops in the ID market.
# Who is affected?
Developers with apps that retrieve order and package information should take note of this change.
# Which version is applicable?
This change applies to all versions of the [Get Package Detail](get-package-detail), [Get Order Detail](get-order-detail) and [Get Order List](get-order-list).
# What action is required?
If your application relies on the tracking_number before the package is shipped or shipping label is created, you'll need to update your code before **May 31, 2024**, to prevent any disruptions.
Moreover, for sellers using TikTok Shipping as their shipping method, it's not necessary to supply the tracking_number when calling the Ship Package API.