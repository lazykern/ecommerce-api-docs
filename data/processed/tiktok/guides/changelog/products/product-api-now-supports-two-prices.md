## Summary
Previously, developers could only sync a single price to TikTok Shop, limiting merchants who use multiple pricing structures (e.g., Shopify's "Compare at Price" and "Sale Price"). Starting at the end of February, TTS will support syncing two prices — **List Price** and **Retail Price** — via the API, enabling better discount management and pricing consistency. After the end of February, TikTok Shop will also introduce a new private API called **External Verification API** that will allow approved developers to verify the authenticity of the original listing price.
## Change Details
The following endpoints will be updated to support two product prices:

* Check Product Listing
* Create Product
* Edit Product
* Partial Edit Product
* Update Price
* Get Product Details
* Search Product

### Payload Changes
#### Public APIs
The **request parameters** has each object in the `skus` array modified to contain both `price` (the **Retail Price**) and `list_price` (the **List Price**) as shown below:
```json
{
  "skus": [
    {
      "price": {
        "currency": "USD",
        "amount": "1.21"
      },
      "list_price": {
        "amount": "2.00",
        "currency": "USD"
      },
      "external_list_prices": [
        {
          "source": "shopify_compare_at_price",
          "amount": "2.00",
          "currency": "USD"
        }
      ],
      "seller_sku": "Color-Red-XM001"
    }
  ]
}
```

The **response** will also contain a similarly modified array of objects, with each object having both a `price` and `list_price`.
#### Private API: External Price Verification
Approved developers can use this API to send an external verification price (the highest sold price on a DTC website) to validate the List Price, enabling it to be displayed as a Strikethrough price on TTS.
## Required Actions
If you have sellers wishing to display discounted pricing, this new way will be a lot easier than managing promotions individually. We highly recommend that you adopt this feature.
## Markets and Versions
This change applies to all markets and all versions.