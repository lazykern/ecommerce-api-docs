# 1. Trigger scenario
The **seller deauthorization** webhook is triggered after a seller is deauthorized. This is important to prevent developers from assuming there is an issue with the platform authorization function.
# 2. Data business parameters
| **Parameter name** | **Sample** | **Description** |
| --- | --- | --- |
| type | 6 | The identification of each type of notification |
| shop_id | 123455 | The identification of the shop |
| timestamp | 1627587506 | The time when the notification is pushed, represented as a Unix timestamp (seconds). |
| data | "data": {"message": "Shop_id {xxx} is deauthorized from your APP by merchant."} | The object contains business parameters related to the specific notification type |
## Event example
```JSON
{
  "type": 6,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "message": "Shop_id {xxx} is deauthorized from your APP by merchant."
  }
}
```