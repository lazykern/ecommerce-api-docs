# 1. Trigger scenario
This webhook will be triggered when the strikethrough pricing verification information expires, 90 days after submission.
Prerequisite: The "Strikethrough Price" API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | 38 | The ID of this webhook topic, which is 38. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| shop_id | string | "7494049642642441621" | The shop ID. |
| timestamp | int | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ product_id | string | "732357708734418520388" | The TikTok Shop product ID. |
| └ sku_id | string | "73235770873441823254" | The TikTok Shop SKU ID. |
## Event example
```JSON
{
  "type": 38,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": "732357708734418520388",
    "sku_id": "73235770873441823254"
  }
}
```