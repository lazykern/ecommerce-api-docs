# 1. Trigger scenario
This webhook is triggered when the status of an invoice upload changes after using the [POST Upload Invoice](upload-invoice) endpoint.
**Note**: The [POST Upload Invoice](upload-invoice) API is currently only applicable to the Brazil market.
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| shop_id | string | "7494049642642441621" | The TikTok Shop ID. |
| type | int64 | 36 | The ID of this webhook topic, which is 36. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| timestamp | int64 | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ package_id | string | "123456" | The ID of the package. |
| └ order_ids | []string | ["152523", "532123"] | List of order IDs in the corresponding `package_id`. |
| └ invoice_status | string | "SUCCESS" | The status of the invoice upload. Possible values: <br>  <br> * `SUCCESS` <br> * `PROCESSING` <br> * `FAILED` <br> * `INVALID` |
| └ invalid_reason | string | "NOT_FOUND" | The reason why `invoice_status = INVALID`. Possible values: <br>  <br> * `UNKNOWN`: Internal system error. Please try again later. <br> * `FAILED`: The NFe file or access key is invalid. Please check the XML file for correctness. <br> * `NOT_FOUND`: The NFe was not found. This may be due to data delay. Please try again later. <br> * `NOT_AUTHORIZED`: The NFe is not legally authorized. It may not have been issued or has been canceled. <br> * `ACCESS_KEY_DUPLICATE`: The access key already exists. You cannot upload an invoice with duplicate access key. |
## Event example
```json
{
    "type":36,
    "tts_notification_id": "7327112393057371910",
    "shop_id": "7494049642642441621",
    "timestamp": 1644412885,
    "data":{
        "package_id": "123456",
        "order_ids": ["152523", "532123"],
        "invoice_status": "INVALID",
        "invalid_reason": "NOT_FOUND"
    }
}
```