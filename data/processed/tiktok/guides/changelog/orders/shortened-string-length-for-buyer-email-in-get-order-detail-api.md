# What is changing?
In August, we added a new property called `buyer_email` to the [Get Order Detail](get-order-detail) API.


As of today, we've shortened the string value of the buyer_email property to less than 45 characters. This change improves compatibility with external systems like shipping software.
# Which markets are affected?
The shortened buyer_email string is available in these markets and for these seller types:

* US and ID markets for local sellers
* MY, PH, VN, TH, SG, UK markets for local and cross-border sellers

# Who is affected?
Developers with applications that use the Get Order Detail API to manage orders for sellers are affected.
# What action is required?
The length of the existing property buyer_email in the Get Order Detail API response has been shortened.


If your application syncs TikTok Shop orders to external systems like shipping software, you can use the shortened buyer_email value and make sure relevant customer information is still correctly synced back to those external systems.