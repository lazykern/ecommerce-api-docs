## Trigger scenario
When a creator completely removes the App's access to his/her data.
## Data business parameters
| Parameter name | Data Type | Sample | Description |
| --- | --- | --- | --- |
| type | int | `20` | Webhook type, fixed to `20` for this webhook. |
| tts_notification_id | string | `"7327112393057371910"` | The ID of the notification. |
| creator_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | The open_id of the creator. To get the value, see [Authorization overview](authorization-overview-202407). |
| timestamp | int | `1644412885` | The UNIX timestamp when this webhook was triggered. |
| data | object |  |  |
| └ cancel_time | string | `"1644412885"` | The UNIX timestamp when this event happened. |
## Event example
```JSON
{
  "type": 20,
  "creator_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "cancel_time": 1644412885
  }
}
```