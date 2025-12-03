# 1. Trigger scenario
The **upcoming authorization expiration** webhook is triggered 30 days before authorization automatically expires. This webhook continues to notify the seller once a day at 0:00 until re-authorization is completed.
# 2. Data business parameters
| **Parameter name** | **Sample** | **Description** |
| --- | --- | --- |
| type | 7 | The identification of each type of notification |
| shop_id | 123455 | The identification of the shop |
| timestamp | 1627587506 | The time when the notification is pushed, represented as a Unix timestamp (seconds). |
| data | "data": {"message": "Authorization of shop_id {xxx} is expiring in {} days. Please direct the merchant to re-authorize.", "expiration_time": "1627587506"} | The object contains business parameters related to the specific notification type. |
## Event example
```JSON
{
  "type": 7,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "message": "Authorization of shop_id {xxx} is expiring in {x} days. Please direct the merchant to re-authorize.",
    "expiration_time": "1627587506"
  }
}
```