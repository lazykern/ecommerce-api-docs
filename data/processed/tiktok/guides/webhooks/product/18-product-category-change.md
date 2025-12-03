# 1. Trigger scenario
When the category of a product is changed, all apps authorized by the shop (using `shop_id`) receive this webhook. When you receive the webhook, you can get more detailed product information by using the [Get Product](get-product) API.
This webhook is triggered regardless of how a product category is changed. Categories can be changed by the seller, developer, or TikTok Shop.
# 2. Data business parameters
| **Parameter name** | **Data Type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | `18` | The ID of the webhook type. |
| tts_notification_id | string | `"7327112393057371910"` | The ID of the notification. |
| shop_id | string | `"7494049642642441621"` | The ID of the shop. |
| timestamp | int | `1644412885` | The time when this webhook was triggered, represented by Unix timestamp. |
| data | object |  |  |
| └product_id | string | `"789078671231"` | ID of the product promoted in the creator's video. |
| └previous_category_id | string | `"600001"` | The category ID of the product before the category update. |
| └current_category_id | string | `"600002"` | The category ID of the product after the category update. |
| └update_time | int | `1644412845` | The time when this category update happens, represented by Unix timestamp. |
## Event example
```JSON
{
  "type": 18,
  "shop_id": "7494049642642441621",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "product_id": "789078671231",
    "previous_category_id": "600001",
    "current_category_id": "600002",
    "update_time": 1644412845
  }
}
```