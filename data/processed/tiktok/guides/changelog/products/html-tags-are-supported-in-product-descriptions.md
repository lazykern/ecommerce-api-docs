## Summary
TikTok Shop has enhanced product descriptions to support a wider range of HTML tags, allowing richer content to sync and render seamlessly from original product sources. For example, the `<table>` tag can be synced and rendered properly to TikTok Shop Product Detail Page. **All tags that conform with proper HTML syntax will be accepted by the API. You don't need filter out any HTML tags before sending them to TikTok Shop API.**
## What is changing
When using the above endpoints and passing HTML tags to the description parameter, a wider range of HTML tags will be rendered properly at the customer facing product detail page. Please note that though all HTML tags will be accepted by the API, TikTok Shop system will process each tag according to their best rendering effect on the native page of TikTok App.
For example, the `<table>` tag will be transferred to an image showing on the product detail page. When product description is edited in "source of truth", apps should retrieve the full HTML of edited product description, pass them all to TikTok Shop (via the description field of TTS API).
## Endpoints that have been optimized

1. Recommend Category
2. Check Product Listing
3. Recommend Global Categories
4. Create Global Product
5. Edit Global Product
6. Create Product
7. Partial Edit Product
8. Edit Product

## What action is required?
When using Products API (the endpoints stated above) to manage products for sellers, don't implement the logic of filtering out specific tags, and pass all HTML tags to the description field of the endpoints.
If a seller has not made any edits to a product synced but HTML tags are missing from TikTok Shop, you need to update the product description by retrieving and copying the full HTML from the original product description. To do this, we suggest following seller workflow from your app:

1. Fetch all HTML tags from the original product description
2. Use the in-app UI prompt or other channels to ask for sellers confirmation on updating the product description
3. Pass all the HTML tags to the description field using the Partial Edit Product endpoint.