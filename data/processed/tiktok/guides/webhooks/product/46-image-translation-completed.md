# 1. Trigger scenario
This webhook is triggered when an image translation is completed or failed.


Applicable only for sellers that sell across EU.
**Prerequisite**: The "Product Basic" API scope is enabled in Partner Center. For more information, refer to [Access Scope](access-scope).
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | 46 | The ID of this webhook topic, which is 46. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| shop_id | string | "7494049642642441621" | The shop ID. |
| timestamp | int | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ translation_task | object |  | The image translation task and the corresponding results. Each task corresponds to the translation of 1 image into 1 target language. |
| └ └ id | string | 764c6e87eedcea90399a0dafcd572b71 | The ID to identify the image translation task. |
| └ └ status | string | COMPLETED | The translation status. <br> Possible values: <br> - PROCESSING: Translation is underway and has not yet completed. <br> - COMPLETED: Translation has completed and results are ready. <br> - FAILED: Translation did not complete due to an error. |
| └ └ fail_reason | string |  | The reason why the translation task failed. |
| └ └ target_language | string | it-IT | The target language to translate the image into. <br> Possible values: <br> - de-DE <br> - en-IE <br> - es-ES <br> - fr-FR <br> - it-IT |
| └ └ original_image | string |  | The original image to be translated. |
| └ └ └ uri | string | tos-useast2a-i-tulkllf4y5-euttp/748e39ecff38453ab8396a36a53dbb92 | The URI of the original image. |
| └ └ └ url | string | https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xyz-sg/sample.jpeg | The URL of the original image. |
| └ └ translated_image | object |  | The translated image. |
| └ └ └ uri | string | tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d | The URI of the translated image. |
| └ └ └ url | string | https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg | The URL of the translated image. |

---


## Event example
```JSON
{
    "type": 46,
    "shop_id": "7494049642642441621",
    "tts_notification_id": "7327112393057371910",
    "timestamp": 1644412885,
    "data": {
        "translation_task": {
            "id": "764c6e87eedcea90399a0dafcd572b71",
            "status": "COMPLETED",
            "fail_reason": "",            
            "target_lang": "it-IT",
            "original_image": {
                "uri": "tos-useast2a-i-tulkllf4y5-euttp/748e39ecff38453ab8396a36a53dbb92",
                "url": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xyz-sg/sample.jpeg"
            },
            "translated_image": {
                "uri": "tos-maliva-i-o3syd03w52-us/53b55d6e8cdf1f315affa7e70b45707d",
                "url": "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/sample.jpeg"
            }
        }
    }
}
```