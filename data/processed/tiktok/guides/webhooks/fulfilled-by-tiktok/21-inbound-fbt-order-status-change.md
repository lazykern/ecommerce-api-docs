## Trigger scenario
This webhook is triggered when the status of an FBT inbound order changes.
> Prerequisite: The **Fulfilled by TikTok(FBT) Info** API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).

## Data business parameters
| **Parameter Name** <!-- width:240px --> | **Data Type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | `21` | The ID of this webhook topic, which is 21. |
| tts_notification_id | string | `"7327112393057371910"` | The ID of this webhook notification. |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | The open_id of the seller. For more information, refer to [Authorization overview](authorization-overview-202407). |
| timestamp | int | `1644412885` | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ inbound_order_id | string | `"IBR577087614418520388"` | FBT inbound order ID. |
| └ order_status | string | `"CANCELLED"` | Inbound order status. Possible enumerations: <br>- TO_BE_RECEIVED <br>- ARRIVE_HUB, <br>- RECEIVING, <br>- PARTIALLY_RECEIVED, <br>- RECEIVED, <br>- CANCELLED |
| └ update_time | int | `1644412845` | The time when the change occurred. Unix timestamp. |
## Event example
```JSON
{
  "type": 21,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "inbound_order_id": "IBR577087614418520388",
    "order_status": "CANCELLED",
    "update_time": 1644412845
  }
}
```