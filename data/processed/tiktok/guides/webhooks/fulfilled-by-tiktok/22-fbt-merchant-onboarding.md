## Trigger scenario
This webhook is triggered when the TikTok Shop seller onboards FBT platform to enable FBT service.
> Prerequisite: The **Fulfilled by TikTok(FBT) Info** API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).

## Data business parameters
| **Parameter Name** <!-- width:240px --> | **Data Type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | `22` | The ID of this webhook topic, which is 22. |
| tts_notification_id | string | `"7327112393057371910"` | The ID of this webhook notification. |
| seller_open_id | string | `"VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw"` | The open_id of the seller. For more information, refer to [Authorization overview](authorization-overview-202407). |
| timestamp | int | `1644412885` | The UNIX timestamp when the FBT onboarding status is updated. |
| data | object |  |  |
| └ onboarded_regions | []object |  | All onboarded FBT regions. |
| └└ region_code | string | `"GB"` | Onboarded FBT region code. |
| └ update_time | int | `1644412845` | The latest update time. Unix timestamp. |
## Event example
```JSON
{
  "type": 22,
  "seller_open_id": "VIyStQAAAADCBQ40s4TzOSSOEIW-bM5O9cod3vK8OytW8m-bnBYlXw",
  "tts_notification_id" : "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "onboarded_regions": [
      {
        "region_code": "GB"
      }
    ],
    "update_time": 1644412845
  }
}
```