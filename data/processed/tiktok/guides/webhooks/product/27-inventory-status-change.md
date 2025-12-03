# 1. Trigger scenario
This webhook will be triggered in either of the following situations:

* The `current_inventory_status` has dropped to LOW_STOCK / OUT_OF_STOCK.
* TikTok Shop predicts the `available_quantity` will drop to `0` in X days.

> Note: The value of X can be system-configured or manually set by the seller.
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | 27 | The ID of this webhook topic, which is 27. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| shop_id | string | "7494049642642441621" | The shop ID. |
| timestamp | int | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ product_id | string | "732357708734418520388" | The ID of the product. |
| └ sku_id | string | "73235770873441823254" | The ID of the SKU. |
| └ trigger_reason | object |  |  |
| └└ alert_type | string | "PREDICTION" | PREDICTION: TikTok Shop predicts the inventory will go out of stock in X days <br> REALTIME: The inventory has reached LOW_STOCK or OUT_OF_STOCK |
| └└ lead_days | int | 21 | When `alert_type == PREDICTION`, the value is the time slot between `update_time` and the predicted out-of-stock date. <br> When `alert_type == REALTIME`, the parameter is not returned. |
| └└ low_stock_threshold | int | 0 | When `alert_type == REALTIME`, the value is the low stock threshold met. <br> When `alert_type == PREDICTION`, the parameter is not returned. |
| └ current_inventory_status | string | "LOW_STOCK" | SUFFICIENT_STOCK: defined as having enough stocks. <br> LOW_STOCK: defined as available stock ≤ stock alert value <br> OUT_OF_STOCK: defined as having 0 available stock. |
| └ inventory_distribution | object |  |  |
| └└ total_quantity | int | 100 | The total quantity of the stock physically in the warehouses. `total_quantity`=`available_quantity` + `creator_reserved_quantity` + `campaign_reserved_quantity` + `committed_quantity`. |
| └└ available_quantity | int | 50 | The total number of SKUs available for ordering in the warehouses. |
| └└ creator_reserved_quantity | int | 20 | The total number of SKUs reserved for creators in the warehouses. |
| └└ campaign_reserved_quantity | int | 20 | The total number of SKUs reserved for campaigns in the warehouses. |
| └└ committed_quantity | int | 10 | The total number of SKUs reserved by existing customer orders in the warehouses. |
| └ update_time | int | 1627587600 | The time when the status changed, represented as a Unix timestamp (seconds). |
## Event example
```JSON
{
  "type": 27,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": "732357708734418520388"
    "sku_id": "73235770873441823254"
    "trigger_reason": {
        "alert_type": "PREDICTION",
        "lead_days": 21
    },
    "current_inventory_status": "LOW_STOCK",
    "inventory_distribution": {
        "total_quantity": 100,
        "available_quantity": 50,
        "creator_reserved_quantity": 20,
        "campaign_reserved_quantity": 20,
        "committed_quantity": 10
    },
    "update_time": 1627587600
  }
}
```