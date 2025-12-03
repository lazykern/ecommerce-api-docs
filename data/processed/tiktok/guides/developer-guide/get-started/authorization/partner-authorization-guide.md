# What does partner authorization do?
After creator authorization, the app can call **Affiliate Partner** APIs.
Right now, the partner authorization is built exclusively for "Affiliate Partner" APIs. They are only for the "Seller and Scalable Creator Match-Up"(aka. TAP) partner category.
For more information, please refer to the "Affiliate Partner" API reference.
# Requirements

1. If the app is still in development, the app can only accept authorization from the owner of the app. After the launch, the app can accept authorization from other partners.
2. The app must enable partner API scopes, which are the ones starting with "partner" in scope keys:

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/89d6471312e4450c984c3c90d10b520e~tplv-10qhjjqwgv-image.image" width="1496px" /></div>

## Authorization link
The basic authorization link can be obtained from the **Copy authorization link** button.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/711f991ebb054e20a80116ce84c99063~tplv-10qhjjqwgv-image.image" width="2302px" /></div>

If the app is in development, the developer needs to generate the authorization link manually using their app's `service_id`, which can be found here:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/c25844315b1d48d1b1220e9f0ab2f4b6~tplv-10qhjjqwgv-image.image" width="1280px" /></div>

<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: The authorization domain is different for US and non-US partners:</span>

1. <span style="background-color: rgb(255, 245, 235)">United States: </span>[https://partner.us.tiktokshop.com/open/authorize?service_id=](https://partner.us.tiktokshop.com/open/authorize?service_id=xxxx)<span style="background-color: rgb(255, 245, 235)">{service_id}</span>
2. <span style="background-color: rgb(255, 245, 235)">Rest of World (ROW): </span>[https://partner.tiktokshop.com/open/authorize?service_id=](https://partner.tiktokshop.com/open/authorize?service_id=xxxx)<span style="background-color: rgb(255, 245, 235)">{service_id}</span>

Adding a `state` parameter is encouraged, but not required for partner authorization. Please see the [OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect#createxsrftoken) documentation for an example of how to create and confirm a `state`.
## Partner requirements
A partner can authorize any business data to an app, but right now, TikTok Shop Partner Center only provides TAP related APIs.
The partner must have enrolled as "Seller and Scalable Creator Match-up" successfully:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/bebee5bfbae843a48b1a87ea6e4efbe6~tplv-10qhjjqwgv-image.image" width="2904px" /></div>

Make sure the user chooses "Seller and Scalable Creator Match-up" on the authorization page.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/e1790b6a344c4bbda8b59bec4053629a~tplv-10qhjjqwgv-image.image" width="2934px" /></div>

## Cancel authorization
The partner can cancel authorization from: **My account > My authorizations**
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/867b24102f314631be850afb478a5fa1~tplv-10qhjjqwgv-image.image" width="2932px" /></div>