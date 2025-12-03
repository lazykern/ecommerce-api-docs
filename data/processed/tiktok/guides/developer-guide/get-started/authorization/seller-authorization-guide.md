# Authorization from seller app store
<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: Authorizing via the Seller Center App Store only applies to </span><span style="background-color: rgb(255, 235, 235)"><strong>public</strong></span><span style="background-color: rgb(255, 235, 235)"> apps. Public apps must meet specific criteria and pass TikTok Shop's app review process. For more information on developing a public app, please visit our </span>[app development overview](https://partner.tiktokshop.com/docv2/page/app-development-overview)<span style="background-color: rgb(255, 235, 235)">.</span>

If your app is public and published, sellers may authorize data access directly from the Seller Center app store.
The seller should use the left-hand menu to navigate to **Growth** **> App store**. Here they will find a full list of apps they can install and authorize:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/44ad262b6c0642bb9ff8100cc480ea94~tplv-10qhjjqwgv-image.image" width="800px" /></div>

After finding your app to install, the seller will be prompted with the following:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/37a6d7a0cc55488ca4c6274858f15de4~tplv-10qhjjqwgv-image.image" width="600px" /></div>

After entering the required information, the seller will be presented with the step to authorize:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/1bc687c3991d4e769d9a2fb97e687581~tplv-10qhjjqwgv-image.image" width="600px" /></div>

Finally, the seller will be redirected to your **Redirect URL**, and will be required to log in to your app to finish the authorization process:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/cb5fb52fab074f9981331bda16a22001~tplv-10qhjjqwgv-image.image" width="600px" /></div>

**Note**: There will not be `state` passed to the Redirect URL from authorization in the App Store.
# Authorization link
After a seller opens your authorization link, they will be presented with the following authorization prompt:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/28000c23170c4021a5e264970fc7496c~tplv-10qhjjqwgv-image.image" width="600px" /></div>

After clicking **Next** under the correct region, the seller will be required to log in to their account (or create a seller account if they do not currently have one):
<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: If there is already a Seller Center account that's signed in, or you are using a Seller Center test account, this step will be skipped.</span>
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/898b707e46a047f59345f5aba7da95fc~tplv-10qhjjqwgv-image.image" width="600px" /></div>

After logging in, the seller will be presented with the following form:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/7bdeaa5ffda24c089f6b0427affd6eea~tplv-10qhjjqwgv-image.image" width="600px" /></div>

After entering and confirming the required information, the seller will be able to authorize your app:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/13d3c13e24fa4d66a1d6a3db9128a32e~tplv-10qhjjqwgv-image.image" width="600px" /></div>

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/176b3bdf014140a3ac4f73669796780b~tplv-10qhjjqwgv-image.image" width="600px" /></div>

<span style="background-color: rgb(255, 235, 235)">❗ </span><span style="background-color: rgb(255, 235, 235)"><strong>Important</strong></span><span style="background-color: rgb(255, 235, 235)">: After successful authorization approval, the seller will be redirected to the </span><span style="background-color: rgb(255, 235, 235)"><strong>Redirect URL</strong></span><span style="background-color: rgb(255, 235, 235)"> you provided in your app. This URL contains critical information for the following step(s).</span>

# Renew authorization
30 days before the authorization expires, an [Upcoming authorization expiration] webhook will be triggered. The developer can ask the seller to renew the authorization by:

* Visiting the authorization link again
* Navigating to **TikTok Shop Seller Center > App Store > My apps and incidents**

<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/f6ed2df39f19439899fdcec3f7aa6e11~tplv-10qhjjqwgv-image.image" width="800px" /></div>

# Cancel authorization
The seller may cancel authorization by navigating to **TikTok Shop Seller Center -> App Store -> My apps and incidents**. This will trigger a [Seller deauthorization] webhook.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/1dcf6bdd98f9431bbd27deff5a1dc27c~tplv-10qhjjqwgv-image.image" width="800px" /></div>

# Authorization in development stage
If an app is still in development, it can't be authorized by online sellers.
For the purpose of testing API requests, it's recommended to get started by using a Seller Center test account through the Development Shops section of Partner Center. Seller Center tests accounts provide full Seller Center functionality, including authorization.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/6f9eae64e51c49349d67f151e7e77f25~tplv-10qhjjqwgv-image.image" width="800px" /></div>

When authorizing an app using a test Seller Center account, you will be taken straight to the **seller authorization approval** step, allowing you to generate an access token without using an authorization link.
For more information on how to create a Seller Center test account, please visit our [Seller Center Development Shops User Guide](seller-center-development-shops).