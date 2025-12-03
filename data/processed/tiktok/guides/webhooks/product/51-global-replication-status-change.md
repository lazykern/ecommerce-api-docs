# 1. Trigger scenario
This webhook is triggered when a product replication operation in another market is completed, regardless of success or failure. If the replication fails, the failure reason(s) will be included in the response.
**Applicable only for global sellers.**
**Prerequisite**: The "Product Basic" API scope is enabled in Partner Center. For more information, refer to [Access Scope](https://partner.tiktokshop.com/docv2/page/access-scope).
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | 51 | The ID of this webhook topic, which is 51. |
| tts_notification_id | string | "7327112393057371910" | The ID of this webhook notification. |
| shop_id | string | "7494049642642441621" | The shop ID. |
| timestamp | int | 1644412885 | The time when this webhook is triggered. Unix timestamp. |
| data | object |  |  |
| └ source_product_id | string | "764c6e87eedcea90399a0dafcd572b71" | The ID of the product that's being replicated to other markets. |
| └ replicated_product | object |  | The product that was replicated from the source product. |
| └ └ product_id | string | "576486316948490000" | The ID of the product created through replication. <br> Pass this ID to the [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) endpoint for more details about the product. |
| └ └ region | string | "GB" | The market where the product has been replicated. |
| └ └ result | string | "SUCCESS" | The result of replicating the product. <br> Possible values: <br>  <br> * SUCCESS: The product was successfully replicated to the local shop, submitted for listing, and is now under review. <br> * DRAFT: The product was successfully replicated to the local shop but saved as a draft local product due to validation errors. You need to call [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) to obtain the original submitted data, pass that data to [POST Check Product Listing](https://partner.tiktokshop.com/docv2/page/check-product-listing-202309) to identify the errors, then call [PUT Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202309) to rectify the errors and send for review. <br> * FAILED: Replication of the product to the local shop was unsuccessful. |
| └ └ fail_reasons | []object |  | The list of reasons for why the replication failed. |
| └ └ └ message | string |  | The reason for why the replication failed. |

---


## Event example
```JSON
{
    "type": 51,
    "shop_id": "7494049642642441621",
    "tts_notification_id": "7327112393057371910",
    "timestamp": 1644412885,
    "data": {
        "source_product_id": "764c6e87eedcea90399a0dafcd572b71",
        "replicated_product": {
            "product_id": "576486316948490000",
            "region": "GB",
            "result": "SUCCESS",            
            "fail_reasons": {
                "message": ""
                }
            }
        }
    }
}
```