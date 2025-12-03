<span style="background-color: rgb(255, 245, 235)">[📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Retired: This API was retired on August 31, 2024 and is no longer available.]</strong></span>
# What is changing?
A new API endpoint is now added to return the field requirements for creating a product. By providing the leaf category ID, you can now obtain the field information and input methods for product creation requirements. **The endpoint is: Listing Schema**. Please refer to the API reference for detailed information.
# Which markets are affected?
This change applies to **all markets**.
# Who is affected?
This change applies to **all sellers**.
# Which version is applicable?
This change is applicable to **v202401**.
# What action is required?
We recommend adopting this API to cut down on the number of calls you have to make to get listing requirements. Previously, you had to make 3 API calls to get this information, now you can make just 1.
Once you have implemented this endpoint, you can call it to get listing requirements before calling the Create Product API.