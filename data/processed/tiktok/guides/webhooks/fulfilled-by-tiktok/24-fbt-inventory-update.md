## Trigger scenario
This webhook is triggered when the FBT inventory updates.
> Prerequisite: The **Fulfilled by TikTok(FBT) Info** API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).

## Data business parameters
| Parameter Name <!-- width:240px --> | Data Type | Sample | Description |
| --- | --- | --- | --- |
| type | int | `24` | The ID of this webhook topic, which is 24. |
| tts_notification_id | string | `"7327112393057371910"` | The ID of this webhook notification. |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | The open_id of the seller. For more information, refer to [Authorization overview](authorization-overview-202407). |
| timestamp | int | `1644412885` | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ goods_id | string | `"732357708734418520388"` | FBT goods ID. |
| └ sku_id | string | `"123513234"` | TikTok Shop SKU ID. |
| └ fbt_warehouse_inventory | []object |  | Inventory in different FBT warehouses. |
| └└ fbt_warehouse_id | string | `"73823232239293999999"` | ID of the FBT warehouse. |
| └└ on_hand_detail | object |  | The number of units physically in the warehouse, excluding those in transit or damaged. |
| └└└ total_quantity | int | `7` | The total number of units. |
| └└└ reserved_quantity | int | `5` | The number of units reserved for confirmed orders and yet to be outbound. |
| └└└ available_quantity | int | `2` | The number of units available for sale. This does not include reserved units. |
| └ update_time | int | `1644412845` | The time when the action occurred. Unix timestamp. |
## Event example
```JSON
{
  "type": 24,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "goods_id": "732357708734418520388",
    "sku_id": "123513234",
    "fbt_warehouse_inventory": [
        {
            "fbt_warehouse_id": "73823232239293999999",
            "on_hand_detail": {
                "total_quantity": 7,
                "reserved_quantity": 5,
                "available_quantity": 2
            }
        }
    ],
    "update_time": 1644412845
  }
}
```