# Methods
TikTok Shop APIs support four common RESTful HTTP methods:

* **GET**: access resources that are located at the specified URL on the server
* **POST**: send data to the server
* **PUT**: update existing resources on the server
* **DELETE**: remove the resource

# Endpoints
TikTok Shop API endpoints are organized by resource type and follow the pattern:
**https://{domain}/{category}/{version}/{resource}**
We have one environment for **{domain}**:
| **Environment** | **URI** | **Use case** |
| --- | --- | --- |
| Production | `https://open-api.tiktokglobalshop.com` | The request address used by developer to call the interface after creating an application. Please use the HTTPS protocol. |

The **/{category}/{version}/{resource}** segment can be found in the corresponding reference doc for any TikTok Shop API.
For example, to call [Get Authorized Shops](get-authorized-shops), the endpoint would be:
```plaintext
https://open-api.tiktokglobalshop.com/authorization/202309/shops
```