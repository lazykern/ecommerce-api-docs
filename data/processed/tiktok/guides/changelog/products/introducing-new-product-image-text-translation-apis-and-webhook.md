# Summary
In the EU marketplace, TikTok Sellers are required to translate all text information associated with a product, including image text. We've made this easier for our Sellers with a new a set of APIs to programmatically translate product image text to German, Irish English, Spanish, French, and Italian.
## What is changing?
We've released a new asynchronous API to [create a translation task](create-image-translation-tasks) for product image translations, a new [translation status API](get-image-translation-tasks) to query the task status and retrieve completed tasks, and a [webhook](46-image-translation-completed) to push image translation notifications to your application.
## What action is required?
To add image translation to your application, integrate the two new APIs into your application, and add a webhook listener for the image translation completion webhook.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/Image%20translation%20APIs/image-translation-apis.png)
The first step is to upload your product image to the TikTok Shop CDN using the [upload product image API](upload-product-image) and pass the returned `uri` values to the [create image translation task API](create-image-translation-tasks) in the `image_uri` field and specify the translation languages. Then, poll the [image translation status API](get-image-translation-tasks) to retrieve the status of the task or wait for the completion notification from the [image translation completion webhook](46-image-translation-completed).
## Notes

1. Image translation APIs are designed to support local sellers to local market listings.
2. Global APIs do not support market specific image uploads.
3. Main images of products published from Global Products cannot be modified.