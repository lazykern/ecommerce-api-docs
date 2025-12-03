# What is changing?
Effective today, we have extended the time limit for updating shipping information from 36 hours to 72 hours via the [Update Shipping Info](update-shipping-info) and [Update Package Shipping Info](update-package-shipping-info) APIs. This change provides sellers with more flexibility to accommodate scenarios that might require shipping information updates beyond 36 hours (such as making changes to the carrier or tracking number).


If you attempt to update the shipping information after 72 hours, the API returns the following error:

* **Error code:** 21011049
* **Error message:** Because of the platform rules limitations, updating the tracking number failed.

# Which markets are affected?
This change applies to cross-border and local sellers in the US market.
# Who is affected?
This change affects developers with applications that utilize the Update Shipping Info and Update Package Shipping APIs.
# What action is required?
You should adjust your time limit to accommodate the new 72-hour window if your application currently restricts shipping information updates to under 72 hours. Additionally, please ensure you inform sellers that they can only update shipping information within 72 hours post-shipment.