# Understanding how access scopes work
When you develop an app for TikTok Shop, it's essential to define the specific data you require access to. This is where access scopes come into play. Access scopes act as gatekeepers, restricting an app's access to certain data(specific APIs). They provide the means to precisely outline the type of access needed for your app.
Equally important is clarity these scopes offer to sellers who authorizes your app to access their data. Sellers need to know the extent of an app's capabilities and limitations concerning their data on Seller Center account. Upon authorizing an app access to their data, each scope delineates the endpoints the app can access. For example, an app may gain authorization to access order and product data within a shop.
| Type of access scopes | Description |
| --- | --- |
| Public | APIs categorized under public scopes are accessible to all developers. These APIs are fundamental for building app functionalities that support TikTok Shop sellers. Upon creating an app in Partner Center, you will by default get access to all public scope APIs. However, your app needs to be authorized by the seller before you can access specific shop-related data. |
| Custom | APIs categorized under custom scopes contain sensitive data. To access APIs within this scope, you can apply for access through Partner Center, by navigating to **Partner Console >> App & Service >> Manage >> Manage API.** Similar to public scope, your app requires seller authorization before accessing specific shop-related data. |
# List of available access scopes
The following table lists some examples of access scopes for TikTok Shop APIs.
📌 To view the full list of API access scopes available for your app, please go to the **Partner Console >> App & Service >> Manage >> Manage API**.
| Scope Name | Description | Type |
| --- | --- | --- |
| **Shop Authorized Information** | The Partner will have access to the seller's TikTok Shop shop ID(s). | Public |
| **Product** **Basic** | The Partner will be able to sync product information to seller's TikTok Shop(s). | Public |
| **Product Modify** | The Partner will be able to manage seller's product information, by having access to listing of products, to edit product attributes, to change product status and to sync product inventory, etc. | Public |
| **Product Delete & Recover** | The partner will be able to manage seller's products, delete and recover from the showcase. | Public |
| **Order Information** | The Partner will be able to have access to all of seller's order data in real-time via API. | Public |
| **Fulfillment Basic** | The Partner will be able to fulfil and manage orders on seller's behalf, and provide real-time updates on the status of seller's orders. | Public |
| **Package Split And Combine** | The Partner will be able to split and combine orders on seller's behalf. | Public |
| **Update Delivery Status** | The Partner will be able to push a package to delivered status for seller which has transport capacity (3PL shipping). | Public |
| **Logistics Basic** | The Partner will be able to get seller's logistics and warehouse information. | Public |
| **Return & Refund Basic** | The Partner will be able to manage seller's return and refund requests. | Public |
| **Finance Information** | The Partner will be able to have access to transaction and settlement amount information by order, and reconcile seller's settlements from TikTok Shop against the orders. | Public |
| **Promotion Information** | The Partner will be able to obtain seller's promotion list and promotion event details. | Public |
| **Promotion Modify** | The Partner will be able to create and manage seller's discounts and promotions on TikTok Shop. | Public |
| **Global Shop Information** | The Partner will be able to access seller's global shop information. | Public |
| **Global Product Information** | The Partner will be able to access seller's global product information. | Public |
| **Global Product Modify** | The Partner will be able to manage seller's global product information, etc. | Public |
| **Global Product Delete** | The Partner will be able to delete global products on seller's behalf. | Public |
| **Global Category Information** | The Partner will be able to access seller's global product category information. | Public |
| and more... <!-- colSpan:3 --> |  |  |