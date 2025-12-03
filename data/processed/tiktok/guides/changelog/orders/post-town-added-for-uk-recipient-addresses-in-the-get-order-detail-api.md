# Summary
Addresses in the United Kingdom (UK) require a [Post Town](https://en.wikipedia.org/wiki/Post_town), so we've added a data field for UK buyers to include their Post Town information.
## What's changed?
To support this, we've added a new property `post_town` to the `recipient_addresses` object in the [Get Order Detail API](get-order-detail).
## Which markets are affected?
This change affects the UK market only.
## Who is affected?
Developers with applications that use the Get Order Detail API to manage orders for sellers are affected.
## What action is required?
Applications that include an integration with the [Get Order Detail API](get-order-detail) should be updated to include support for `post_town` field in the `recipient_addresses` object.