# Disconnecting TikTok shops
Once you've [stored one or more connections to a TikTok Shop](connecting-shops), it's important that your client application or connector have functionality to allow your customers to disconnect one or more TikTok Shop connections.
## Disconnect one or more shops
In this use case, your client application or connector disconnects your customer's TikTok shop. This can either be in response to your customer revoking authorization for you TikTok Shop App, or, if your customer requests the disconnection.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Developer_Guide/Integration%20Guides/disconnect_shops.png)
The call flow is:

1. Your customer requests a TikTok Shop be disconnected from their local account using your client application or connector user interface. Retrieve the data necessary for the deletion.
2. Delete the customer's `access_token`, `refresh_token`, and any other customer data as specified by your data retention policies.