## US Market: Introducing Product LQT (Listing Quality Tiers)
### Summary
Listing quality impacts customer trust and influences purchasing decisions. To improve listing quality, Sellers will be able to see Listing Quality Tiers (LQT), a tier system for measuring listing quality (e.g., "Poor", "Fair", "Good"), and take action to address listing-quality issues. Information quality is a crucial factor for consumers when making purchasing decisions in online shopping. Therefore, improved product information quality directly influences customer satisfaction, trust, and conversion rates. **This change will be for the US market and will be live as of 9/29**
### API Changes
In the US market, the response of [Product Information Issue Diagnosis](product-information-issue-diagnosis) API will now include a `listing_quality` object which will include a listing quality indicator (e.g., "POOR", "FAIR", "GOOD", "EXCELLENT") along with recommendations on what changes to make to get it to the next level, if possible.
#### Product Information Issue Diagnosis (v202405)
Sellers and Developers managing Products through the API channel can use this API to obtain LQT-related data and optimization recommendations to improve listing quality of their products.

* You can now query up to 200 products
* In US, this endpoint will also return a `listing quality` object with the following properties:
   * current_tier (string)
   * remaining_recommendations (int)
   * *NOTE:* The response "NA" represents null. LQT can be null.
* The field enum has two new valid values
   * `ATTRIBUTE`
   * `SIZE_CHART`
* There are also additional error codes that will be added.
   * Please refer to the [API Reference](product-information-issue-diagnosis)

#### Search Products (v202312)
Developers can search a seller's catalog to retrieve a list of Product IDs based on filter conditions through this API. To obtain detailed information about a listing, you can use the Product ID response in the "Get Product" API.

* A new `listing_quality_tier` key can be provided in the request body
   * Values will be one of [`"POOR"`, `"FAIR"`, `"GOOD"` and `"EXCELLENT"`]
   * *NOTE:* The response "NA" represents null. LQT can be null.
* There are also additional error codes that will be added.
   * Please refer to the [API Reference](search-products)

#### Get Product (v202309)
Search a shop's catalog to retrieve a list of products based on filter conditions through this API. If you need to get detailed information about a product, use the product ID response in the "Get Product" API.

* The response will now include the `listing_quality_tier` of that product.
   * *NOTE:* The response "NA" represents null. LQT can be null.
* There are also additional error codes that will be added.
   * Please refer to the [API Reference](get-product)

#### Check Product Listing (v202309)
As you attempt to create new listings, you can use this API to check whether their listings can be published. During the process, you can check whether their listings meet LQT requirements.

* A new `listing_quality_tier` object is returned in the response
   * Values will be one of [`"POOR"`, `"FAIR"`, `"GOOD"` and `"EXCELLENT"`]
   * *NOTE:* The response "NA" represents null. LQT can be null.
* There are also additional error codes that will be added.
   * Please refer to the [API Reference](check-product-listing)

### Appendix

* [Product Information Quality Diagnosis Codes And Recommendations](listing-quality-diagnosis)