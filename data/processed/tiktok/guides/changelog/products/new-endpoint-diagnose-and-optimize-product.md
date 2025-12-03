## Summary
To improve product visibility, we are releasing a new endpoint called Diagnose and Optimize Product. It is not meant to be used for listing products, but rather for optimizing the product details and listing for existing products that are already live. This endpoint can help improve listing information, drive product traffic and increase conversions. The version for the [Diagnose and Optimize Product API](diagnose-and-optimize-product) is **v202411** and applies to all markets and all seller types.
*Please note that listing quality information is currently US-only. Other features of this endpoint, such as diagnosing issues with the current product details and the overall recommendations and auto-generated optimization suggestions targeted for specific product fields, including the title, are available in all markets and to all sellers.*
## What is changing
Previously, TikTok Shop had released a [Check Product Listing](check-product-listing) endpoint that helped identify any issues with product properties before submitting them for listing. This endpoint also diagnosed and optimized product information. We have now removed this logic from the API, and created this new endpoint called [Diagnose and Optimize Product API](diagnose-and-optimize-product) that hopes to provide insights on areas of improvement. This move lets us provide you with information on both products that are live in addition to new products that have not yet been listed.

* To diagnose a live product, provide the `product_id` and `category_id`, leaving all other fields blank.
* To diagnose a new product not yet listed, please *omit* the `product_id` and provide the rest of the necessary information.
* You can also provide an existing `product_id` and `category_id` along with any new information, so that you can check any updates that might be made to a product.

In addition, the Check Product Listing API will deprecate the `is_diagnosis_required` request parameter, along with `listing_quality` and `diagnoses` values in the response.
To diagnose multiple live products, please use the [Product Information Issue Diagnosis API](product-information-issue-diagnosis). To verify listing requirements, use [Check Product Listing](check-product-listing)
## What action is required
This is an optional API that can help boost GMV. We recommend adopting this API so that you can boost listing quality and improve the Product Details Page (PDP).
## What markets and version is affected
This change is applicable to **v202411** applies to all markets and all sellers.