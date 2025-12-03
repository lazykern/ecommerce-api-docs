# Summary
Promotions API have been now expanded to allow sellers to create non-sellable gift products that can be added when a purchase is made, along with the ability to provide free samples. Virtual bundles can also be created by the API.
# API Changes
## Non-Sellable Gift With Purchase (NS-GWP)
### Creating NS-GWP
Create non-sellable products via API (connector), as integrators (developers) can mark a non-sellable product tag in connector. Then call the [Create Product API](create-product) and select `is_not_for_sale=true`. This creates a non-sellable product in TikTok Shop after synchronization.
### Getting NS-GWP
Seller creates non-sellable products in TikTok Shop Seller Center. Developers can get non-sellable products from Seller Center by calling the [Get Product API](get-product) and checking for `is_not_for_sale=true`. A mapping relationship with the seller's product in the partner platform is created.
### Change product type between sellable and non-sellable
In the case a seller chooses the incorrect type, and wants to change the product type from sellable to non-sellable or vice verse. TikTok shop policy requires products to be recreated when changing between sellable and non-sellable. It is up to the developer to decide whether the original product will be removed or deactivated.
### Shopify Considerations
In TikTok Shop [Get Order Detail API](get-order-detail), if it is a GWP (including GWP or NS-GWP) order, the `order_line` information for the gift is shown as follows:

* original_price, sale_price, platform_discount, seller_discount are all `0` , and the sku_type's `is_gift=true` (Please refer to the left picture)
* Item_line_type=normal (Please refer to the right picture)

![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/d1f74218ab934e3486359b64024bcf1f~tplv-10qhjjqwgv-image.image)
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/a53a885b508b4423bc8a01fefd14d589~tplv-10qhjjqwgv-image.image)
But when this type of order is passed into Shopify, the gift product's original price is still being displayed by Shopify , but the actual payment subtotal is 0, resulting in sellers reconciliation error (Total order value is not equal to customer paid). So as a Shopify connector, you need to add a 100% seller discount code for the gift in GWP order, to help sellers reconcile. (Please refer to the right picture)
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/52e2a4cf103f40e5925488c0ca4a91c6~tplv-10qhjjqwgv-image.image" width="850px" /></div>

Example payload with 100% discount to add for gift order_line.
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/ecdc96a64525419598021826b26884d6~tplv-10qhjjqwgv-image.image)
## Free Sample
### Recognizing Free Sample order
The following steps can explain how to recognize free samples

1. If `is_sample_order=true`
2. AND if `payment.original_total_product_price` is zero -> `order.payment` is null; `order.payment.original_total_product_price` is empty or "0"
   * With above two conditions, developers can recognize Free Sample order 'request from seller'
   * Adding 100% seller discount code for this type of order in Shopify.