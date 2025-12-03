# What is changing?
To comply with GDPR ruling, there are changes coming to the app installation and authorization workflow. When creating an application, developers are now required to select API scopes their application will need to function as expected. Sellers are then shown the same list of scopes when installing the application, and are given the option to reject the authorization request. This is a major change from the previous flow where apps were implicitly granted all scopes and the seller was shown all options with no obvious way to reject the authorization request.
# Which markets are affected?
This change is for all markets.
# Who is affected?
This change affects all sellers (both local and cross border).
# Which version is applicable?
This change is for the Access Token endpoint, which is applicable for all versions.
# What action is required?
Applications that are already authorized will continue to work until the authorization expires.
Applications that are new or have expired authorization:

1. The scopes for the app need to be selected in Partner Center.
2. The API request to get the access token must include the scopes in the request
3. The response will contain the scopes that were granted
4. Existing sellers who have authorized the application will need to renew their authorization before the scopes can take effect.
   1. When they do this, only the scopes that have been selected by the developer will be shown during the flow.
5. Redirect URL will contain the code if everything is working well
   1. In case of an error, there will be `error=access_denied` added to the redirect URL query parameters.

Any APIs that are called without scopes associated with the access token will fail with a 401 status code.
## Get Access Token API Changes
### Parameters
No changes
### Responses
A new array of strings titled `granted_permissions` will be present in the response body. These strings represent the scopes the user has authorized to access and are in upper snake case (ex ["MANAGE_GLOBAL_PRODUCTS", "LIVEROOM_INFO"]).
## Seller App Authorization Flow Changes
Sellers will see the scopes that the developer has chosen when installing an application. Before this change, the seller had no choice to reject the connection and was forced to install the application. Now there is a new "Discard" button that they can click which will cancel the installation process. In this situation, the system will redirect to the URL specified by the application and will include `error=access_denied&code=null` as query parameters.
### Change Summary
| Description | Scope Changes | Actions Required |
| --- | --- | --- |
| Existing apps with all API scopes | Existing apps have all the Public API scopes. <br> No extra configuration needed. | After the change, sellers still authorize all the Public API scopes to their existing apps. <br> **Good to know** for developers, no extra action needed |
| New apps with all API scopes | Developers choose all Public API scopes. | After the change, sellers still authorize all the Public API scopes to their existing apps. <br> **Good to know** for developers, no extra action needed |
| New apps with **selected API scopes** | Developers choose only **certain Public API scopes.** | * When developers don't need new scopes for the app, no extra action is needed <br> * When developers need new scopes for building new features for the app, they need **turn on the needed scope** from Partner Center to have permission to call the related APIs and also: <br> * Existing sellers will not give their shops authorization with new scopes by default, need guide them to **renew the authorization in order to grant new scopes to the App** <br> * Newly installed sellers will give their shop authorization with new scopes to the App <br>  |