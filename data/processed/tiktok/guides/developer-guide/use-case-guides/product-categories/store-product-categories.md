# Get and store product categories
A core scenario for TikTok Shop API developers is to synchronize customer product data in their service with product data in TiKTok Shop.
## Retrieve and store all TikTok Shop product categories
A requirement for synchronizing your product data with TikTok Shop product data is to index your application or service's product categories with TikTok Shop Product categories. When your sellers create a new product, the category they select for your application or service will have a corresponding category in TikTok Shop.
The first step is to retrieve and store all TikTok Shop Product categories. This is because the category list is very large, and we recommend that you call the API once and store the list locally in your database. Then, implement a scheduled job to periodically retrieve the list, determine the differences, and update your local data.
Product categories in TikTok shop are hierarchical, and the full set of categories forms a category tree. It's unlikely that your product category metadata can be mapped to the same product category hierarchy in TikTok Shop, so we recommend that you simply map individual categories to one another. This way, you can maintain a link between categories without having to also attempt to map the relationship between categories in each system.
TikTok Shop categories are retrieved using the `GET product categories` API. This API takes no parameters and returns a list of JSON category objects.
> The `GET product categories` API returns a list of categories based on the `access_token` associated with the Seller account. In this use case, we just want the list of category objects, so you can use any valid TikTok Shop Seller account to retrieve them.

Each JSON category object includes the following properties:
| Property | Type | Description |
| --- | --- | --- |
| `id` | string | The identifier for the category. |
| `parent_id` | string | The `parent_id` property is the identifier of the parent category's `id` property. |
| `local_name` | string | The name of the category. |
| `is_leaf` | boolean | Set to `false` if the category is a container for other categories and cannot be applied to a product, otherwise it's set to `true` |
> Note that the JSON category object also includes a list of `permission_statuses` that represents the Seller's permissions to add a product to this category. As discussed earlier, it's not necessary to store these values for this use case because you must retrieve and check these permissions each time your seller creates a new product and synchronizes it in your application or service.

![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Integration%20Guides/cat-map-prod-1.png)
The call flow to download the entire TikTok shop product category list is:

1. Make an initial call to the `GET product categories` API. This API takes no parameters.
2. Receive the initial list of TikTok Shop product categories.
3. Iterate the list of categories, and store the metadata for each individual category in your local database.

## Retrieve and update TikTok Shop product categories
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Integration%20Guides/cat-map-prod-2.png)
This call flow assumes that you have a scheduled job that triggers this function. The call flow to retrieve and update your locally stored TikTok Shop product categories is:

1. When triggered, call the `GET product categories` API.
2. Receive the most recent list of TikTok Shop product categories.
3. Retrieve your locally stored list of TikTok Shop product categories that you created in the **retrieve and store all TikTok Shop product categories** use case above.
4. Iterate the locally stored list you created in step 3, and compare each property value.
5. If a property value is different, update your locally stored property value.
6. When the iteration started in step 4 is complete, end.

## Next steps
Now that you've downloaded the TikTok Shop product category list, stored it locally, and implemented logic to keep it up to date, learn how to [select the TikTok Shop product categories for your seller's products](map-product-categories).