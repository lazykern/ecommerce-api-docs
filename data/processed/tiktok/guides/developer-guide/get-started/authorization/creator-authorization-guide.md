# What does creator authorization do?
After creator authorization, the app can call **Affiliate Creator** APIs.
# Requirements
Currently, creator authorization is a beta feature. Only allowlisted apps can obtain creator authorization.
Only MVP participants can be added to the allowlist, please contact @Danny Hsiung to be added to the allowlist. Please provide your app key.
The app **must** enable specific creator API scopes. Look for scope keys that begin with **creator**.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/84b991d8c4cd4a8e82c1226b2e0e5770~tplv-10qhjjqwgv-image.image" width="1506px" /></div>

# Authorization link
The basic authorization link can be obtained from the **Copy authorization link** button.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/83d326b9f47e46d18ecf82cfd38822b0~tplv-10qhjjqwgv-image.image" width="2932px" /></div>

For creator authorization links, you are **required to manually** add a `state` parameter for extra security. The `state` is an unguessable random string that can help protect cross-site request forgery attacks, and is **not automatically included** in the basic authorization link.
Please see the [OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect#createxsrftoken) documentation for an example of how to create and confirm a `state`. When encoding a state, remove leading and trailing white spaces.
Additionally, you may manually concatenate the entire authorization link by using your `app_key` and `state`.
The final authorization link should resemble:
```plaintext
https://shop.tiktok.com/alliance/creator/auth?app_key={your_app_key}&state={state_id}
```

# Creator requirements
The creator **must** be a TikTok Shop creator, not any TikTok account. The creator can enroll as a TikTok Shop creator by following the guides for the respective countries:

* [Indonesia](https://seller-id.tokopedia.com/university/essay?identity=1&role=2&knowledge_id=6837812658128641&from=feature_guide)
* [Ireland](https://seller-ie.tiktok.com/university/essay?identity=1&role=1&knowledge_id=8607911547799328)
* [Malaysia](https://seller-my.tiktok.com/university/essay?identity=1&role=2&knowledge_id=6837863837042434&from=feature_guide)
* [Philippines](https://seller-ph.tiktok.com/university/course?identity=1&role=2&learning_id=1295010259994369&from=course&content_id=3904538843121410)
* [Singapore](https://seller-sg.tiktok.com/university/essay?identity=1&role=2&knowledge_id=7996132844111617&from=feature_guide)
* [Thailand](https://seller-th.tiktok.com/university/essay?identity=1&role=2&knowledge_id=6837882170361601&from=feature_guide)
* [United Kingdom](https://business.tiktokshop.com/uk/creator)
* [United States](https://business.tiktokshop.com/us/creator)
* [Vietnam](https://seller-vn.tiktok.com/university/essay?knowledge_id=6837838528808705&role=2&course_type=1&from=search&identity=1)


The creator's selection region must be one of the app's target markets:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/c18c4e8fa9224470ab65902e3c04d9a0~tplv-10qhjjqwgv-image.image" width="2932px" /></div>

If your app is in development, please contact your App Store Manager for a Creator testing account. Creator test accounts are only available to members of our beta phase today.
# Partial authorization
Creators can opt in or out what scope to authorize.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/39b06e0cf95e4201a650d3c97065e5f9~tplv-10qhjjqwgv-image.image" width="2932px" /></div>

After calling [Get Access Token], please check the `granted_scopes` array in the response, and make sure the creator has authorized all necessary scopes.
The scope keys definition is on the **Manage API** page:
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/702659a6c6ed4d328b2e8426c9d1c538~tplv-10qhjjqwgv-image.image" width="1502px" /></div>

If the authorized scopes are not sufficient for your business, please ask the creator to "remove all access" and re-authorize again.
# Provide an entrance in the app for users to deauthorize
For creator authorization, the app MUST provide an entrance for creator to deauthorize the app.
The app should reuse the authorization link. When a creator re-visits this link, they can toggle on or off the scopes they authorized previously. Additionally, they can "remove all access."
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/4397fd35abac4034b47cd9b9a14849ac~tplv-10qhjjqwgv-image.image" width="2928px" /></div>

After the creator toggled off the scope, the API under this scope will return error:
`{105005 you should apply auth pkg for this api }`
If the creator removes all access, the access_token will expire, the API call will return error:
`{105001 access token is invalid; detail:your token has been deauthorized }`
<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: There is no expiration time for creator authorization.</span>