# 1. Trigger scenario
The **new message** webhook is triggered when a new message is sent in a customer service conversation.
# 2. Data business parameters
| **Parameter name** | **Data type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| message_id | string | 7494560109732334263 | The identification of the message |
| index | string | 7494560109732334274 | The message index that can be used to sort messages. <br> Newer messages have a larger index. |
| conversation_id | string | 576486316948490001 | The identification of the conversation |
| type | string(enum) | TEXT | Message type, with possible values: <br> * TEXT <br> * IMAGE <br> * ALLOCATED_SERVICE <br> * NOTIFICATION <br> * BUYER_ENTER_FROM_TRANSFER <br> * BUYER_ENTER_FROM_PRODUCT <br> * BUYER_ENTER_FROM_ORDER <br> * PRODUCT_CARD <br> * ORDER_CARD <br> * EMOTICONS <br> * VIDEO <br> * COUPON_CARD <br> * OTHER |
| content | string | {"content": "simple text message"} | Message content, in JSON serialized string. <br> Examples: <br>  <br> * TEXT: <br> {"content": "simple text"} <br>  <br> * IMAGE: <br> {  <br>      "height": "290",  <br>      "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290",  <br>      "width": "304"  <br>  }  <br>  <br> * PRODUCT_CARD, BUYER_ENTER_FROM_PRODUCT: <br>  {"product_id": "12345"}  <br>  <br> * ORDER_CARD, BUYER_ENTER_FROM_ORDER : <br>  {"order_id": "12345"}  <br>  <br> * VIDEO: <br>  {  <br>      "url": "https://video-boei18n.byted.org/storage/v1/tos-boei18n-v-c72c01/e8240f35244646428df9c3244d1a7408?x-tos-algorithm=v2&x-tos-authkey=5bf25627da095a5cba28ace592de46cc&x-tos-expires=1681980481&x-tos-signature=r_bRxtrvGhXAuZgMmNhlZ_Upqzg",  <br>      "cover": "https://p-boei18n.byted.org/tos-boei18n-v-c72c01/o8keEOhzTcNCcJyAbkWZwpLIyTfkJxcGbRBvLP~tplv-jvtte31kaf-origin-jpeg.jpeg?",  <br>      "width": 640,  <br>      "height": 360,  <br>      "duration": "20.504",  <br>      "vid": "v0e30cg700f7cgcmu8jc77u9e2bdp95g",  <br>      "expire_time": "1681980481",  <br>      "format": "mp4",  <br>      "size": 400000,  <br>      "bit_rate": 156067,  <br>      "quality": "original",  <br>      "codec_type": "h264"  <br>  }  <br>  <br> * COUPON_CARD: <br>  {"coupon_id": "7262992004278206762"} <br>  <br>  <br> Note: Use Get Coupon for the details of the coupon. <br>  <br> * ALLOCATED_SERVICE, NOTIFICATION, BUYER_ENTER_FROM_TRANSFER, OTHER: <br> {"content": "simple text"} |
| create_time | int | 1691411573 | Message creation time, represented as a Unix timestamp (seconds). |
| is_visible | bool | true | Whether this message should be displayed to customer service. |
| sender | Object |  | The message sender. <br> For system and robot roles, the shop is the sender. |
| ^im_user_id | string | 7494560109732334261 | Sender's ID <br> These are IM IDs, and can not be used to query orders. |
| ^role | string(enum) | BUYER | Sender's role, with possible values: <br> * BUYER <br> * SHOP <br> * CUSTOMER_SERVICE <br> * SYSTEM <br> * ROBOT |
## Event example
```JSON
{
  "type": 14,
  "tts_notification_id": "7327112393057371910",
  "shop_id": "7494049642642441621",
  "timestamp": 1644412885,
  "data": {
    "content": "{\"content\":\"444\"}",
    "conversation_id": "710688832392260838",
    "create_time": 1681790246,
    "is_visible": true,
    "message_id": "722323407926368819",
    "index": "7494560109732334274",
    "type": "TEXT",
    "sender": {
      "im_user_id": "707885565181165594",
      "role": "BUYER"
    }
  }
}
```