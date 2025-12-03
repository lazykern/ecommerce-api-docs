## Summary
A new webhook will be sent when products are created. This allows partners to now create products on other platforms when they are added to TikTok Shop.
A message will be sent to developer when a product is created via any channel (API, Seller Center, App, Excel). Once the product_id is generated, before sending the product to audit, the message will be sent.
## Affected Markets and Sellers
This change is for all markets and for all sellers.
## Applicable API Versions
Since this a webhook change, it is not directly tied to any version changes.
## Required Actions
Partners who develop connectors and multi-channel applications are recommended to integrate this webhook. Subscribe to this webhook and process them like any other webhook. Here is an example of a webhook:
```JSON
{  
  "type": 16,  
  "tts_notification_id": "7327112393057371910",  
  "shop_id": "7494049642642441621",  
  "timestamp": 1644412885,  
  "data": {  
    "product_id": "576486316948490000",  
    "product_type": ["GPR_PRODUCT"],  
    "update_time": 1644412885  
  }  
}
```