# 1. Trigger scenario
The **product status change** webhook triggers when a product audit status changes or is completed:

* Product passes the first audit: `PRODUCT_FIRST_PASS_REVIEW`
* Product status changes by platform: `PRODUCT_STATUS_CHANGED`
* Product audit fails: `PRODUCT_AUDIT_FAILURE`

# 2. Data business parameters
| **Parameter name** | **Sample** | **Description** |
| --- | --- | --- |
| product_id | 1X2X3X4X5 | The identification of a TikTok Shop product |
| status | Live-On sell | Product audit status, with possible values: <br>  <br> * PRODUCT_FIRST_PASS_REVIEW <br> * PRODUCT_STATUS_CHANGED <br> * PRODUCT_AUDIT_FAILURE |
| suspended_reason | 1X2X3X4X5 | The reason a product audit was rejected or frozen |
| update_time | 1627587600 | The time when the status changed, represented as a Unix timestamp (seconds). |
## Event example
```JSON
{
  "type": 5,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "product_id": 576486316948490000,
    "status": "PRODUCT_FIRST_PASS_REVIEW",
    "suspended_reason": "",
    "update_time": 1644412885
  }
}
```