# 1. Trigger scenario
This webhook is triggered when a combined listing is created, updated (the list of products in the combined listing changes), or deleted.
**Prerequisite**: The "Product Basic" API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | 42 | The ID of this webhook topic, which is 42. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| shop_id | string | "7494049642642441621" | The shop ID. |
| timestamp | int | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ combined_listing_id | string | "123456789" | The combined listing ID. |
| └ products | []object |  | The current list of products in this combined listing after the change. |
| └└ id | string | "987654321" | The product id. |
| └ status | string | "LIVE" | The status of the combined listing. <br> Possible values: <br>  <br> * LIVE <br> * SYSTEM_DEACTIVATED <br> * SELLER_DEACTIVATED <br> * DELETED <br>  <br> Note: Only products in LIVE combined listings will appear on the product display page. |
| └ change_type | string | "UPDATE" | The type of change made to this combined listing. <br> Possible values: <br>  <br> * CREATE: The combined listing was created. <br> * UPDATE: The combined listing was updated to add or remove products. <br> * DELETE: The combined listing was deleted. |
| └ added_product_ids | []string | ["987654321"] | The list of products that were newly added to the combined listing. |
| └ removed_product_ids | []string | ["987654322"] | The list of products that were removed from the combined listing. |
## Event example
```JSON
{
  "type": 42,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "combined_listing_id": "123456789",
    "products": [
      {
        "id": "987654321"
      },
      {
        "id": "987654322"
      }
    ],
    "status": "LIVE",
    "change_type": "UPDATE",
    "added_product_ids": ["987654321"],
    "removed_product_ids": ["987654333"]    
  }
}
```