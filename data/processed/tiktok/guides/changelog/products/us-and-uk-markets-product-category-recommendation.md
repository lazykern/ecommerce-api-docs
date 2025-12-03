# What is changing?
TikTok Shop is hoping to improve the accuracy of product categorization, and help sellers reduce the number of miscategorized products. To accomplish this, we are discouraging sellers from manually mapping categories between TikTok Shop and another platform, and encouraging developers to instead implement our [POST Recommended Category API](recommend-category).
# Which markets are affected?
This change is applicable to local and cross-border sellers in the US and UK markets.
# Who is affected?
This change is applicable to all developers who integrate with TikTok Shop API.
# Which version is applicable?
This change is applicable to version **202309**.
# What action is required?
Developers are incentivized to implement the [POST Recommended Category API](recommend-category) in order to map categories for seller products. This API **requires** you to provide a product title, description, and images, and will return a recommended category for the product.
<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: The current </span><span style="background-color: rgb(255, 245, 235)"><strong>202309</strong></span><span style="background-color: rgb(255, 245, 235)"> version of POST Recommended Category does not require a product description or product images; however, providing these parameters will greatly improve the quality of the product recommendation. Please ensure you provide both these parameters, as they will become required in a future version of the Recommended Category API.</span>