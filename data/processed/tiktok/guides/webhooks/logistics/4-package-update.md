# 1. Trigger scenario
The **package update** webhook is triggered when package updates such as combine, split, cancel the combine package operation, etc. occur.
# 2. Data business parameters
| **Parameter name** | **Sample** | **Description** |
| --- | --- | --- |
| sc_type | COMBINE | Type of the event trigger, with possible values: <br>  <br> * COMBINE <br> * CANCEL_COMBINE <br> * SPLIT <br> * CANCEL_SPLIT <br> * ADDRESS_UPDATE_SPLIT <br> * CANCEL_FULFILL_SPLIT <br> * FULFILL_UNCOMBINE <br> * PARTLY_CANCEL_SPLIT <br> * SPLIT_BY_SKU_CANCEL |
| role_type | ROLE_USER | Operator of the event trigger, with possible values: <br>  <br> * ROLE_USER <br> * ROLE_SELLER <br> * ROLE_OPERATOR <br> * ROLE_SYSTEM |
| package_list | []object | Package list updated by the event trigger |
| └ package_id | "123456" | The identification of a package |
| └ order_id_list | ["152523", "532123"] | List of order IDs in a given package |
| update_time | 1627587600 | The time when the package was updated, represented as a Unix timestamp (seconds). |
## Event example
```JSON
{
  "type": 4,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "sc_type": "COMBINE",
    "role_type": "ROLE_USER",
    "package_list": [
      {
        "package_id": "123456",
        "order_id_list": [
          "152523",
          "532123"
        ]
      }
    ],
    "update_time": 1644412885
  }
}
```