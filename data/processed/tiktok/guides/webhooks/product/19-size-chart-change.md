# 1. Trigger scenario
This webhook is triggered when a product size chart is created, edited, or deleted.
**Prerequisite**: The "Product Basic" API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).
# 2. Data business parameters
| **Parameter Name** <!-- width:240px --> | **Data Type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | `19` | The ID of this webhook topic, which is 19. |
| tts_notification_id | string | `"7327112393057371910"` | The ID of this webhook notification. |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | The open_id of the seller. For more information, refer to [Authorization overview](authorization-overview-202407). |
| timestamp | int | `1644412885` | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ size_chart_template_id | string | `"789078671231"` | The ID of the size chart template that's being changed. |
| └ size_chart_template_name | string | `"600001"` | The name of the size chart template that's being changed. |
| └ event_type | string | `"EDIT"` | The change that occurred for the size chart. Possible values: <br> - `CREATE`: A new size chart is created <br> - `EDIT`: The size chart is edited <br> - `DELETE`: The size chart is deleted |
| └ update_time | int | `1644412845` | The time when the change occurred. Unix timestamp. |
## Event example
```JSON
{
  "type": 19,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "size_chart_template_id": "789078671231",
    "size_chart_template_name": "600001",
    "event_type": "EDIT",
    "update_time": 1644412845
  }
}
```