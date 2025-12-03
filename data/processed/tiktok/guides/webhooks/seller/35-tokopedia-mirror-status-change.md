# 1. Trigger scenario
This webhook is triggered when the TikTok Shop to Tokopedia mirroring process is completed or rolled back. Applicable only for the **Indonesia** market.

**Prerequisite**: The shop is [active](get-active-shops), and the "**Shop Authorized Information**" API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | 35 | The ID of this webhook topic, which is 35. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| seller_open_id | string | "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw" | The open_id of the seller. For more information, refer to [Authorization overview](authorization-overview-202407). |
| timestamp | int | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ tts_shop_id | string | "7494049642642441621" | The shop ID in TikTok Shop. |
| └ update_time | int | 1627587600 | The time when the change occurred. Unix timestamp. |
| └ mirror_status | string | "MIRRORED" | The shop mirroring status: <br> - MIRRORED <br> - ROLLED_BACK <br> - CANCELED |
## Event example
```JSON
{
  "type": 35,
  "tts_notification_id" : "7327112393057371910",
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "timestamp": 1644412885,
  "data": {
    "tts_shop_id": "7494049642642441621",
    "mirror_status" : "MIRRORED",
    "update_time": 1627587600
  }
}
```