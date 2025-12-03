# What is changing?
[Check Listing Prerequisites](check-listing-prerequisites) has a new version of v202312, updated from v202309. With this change, fields in the response body are now static. We hope this change improves developer experience and productivity.
# What are the affected markets?
This change is applicable to all markets.
# Who is affected?
All seller types can benefit from this change.
# Which version are these changes for?
This change is only for v202312, which is available for the Check Listing Prerequisite API. Upgrade to v202312 to benefit from a better development experience from a more RESTful API.
# Required Actions
We recommend adopting this new version and updating your code with the refactored fields. Static fields simplifies logic on API response parsing, which will lead to a smaller number of issues that would otherwise happen if the response has dynamic fields. [API Reference](check-listing-prerequisites).