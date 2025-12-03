# Mapping
## Path mapping
| **CS API v1.0 (old)** | **CS API v2.0 (new)** |
| --- | --- |
| [POST]/api/seller/im/send_message | [POST]/customer_service/202309/conversations/:conversation_id/messages |
| [GET]/api/seller/im/customer_service/status | [GET]/customer_service/202309/agents/settings |
| [POST]/api/seller/im/customer_service/status/update | [PUT]/customer_service/202309/agents/settings |
| [POST]/api/seller/im/list_conversations | [GET]/customer_service/202309/conversations |
| [POST]/api/seller/im/get_conversation_messages | [GET]/customer_service/202309/conversations/:conversation_id/messages |
| [POST]/api/seller/im/img/upload | [POST]/customer_service/202309/images/upload |
| [POST]/api/seller/im/mark_read | [POST]/customer_service/202309/conversations/:conversation_id/messages/read |
| [POST]/api/seller/im/create_conversation | [POST]/customer_service/202309/conversations |
## Field mapping
### [POST]/api/seller/im/send_message
New path: [POST]/customer_service/202309/conversations/:conversation_id/messages
#### Request param
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| conv_short_id | string | conversation_id | string | Move to path variable |
| msg_type | string | type | string(enum) | Enum mapping: <br> text->TEXT <br> file_image->IMAGE <br> goods_card->PRODUCT_CARD <br> order_card->ORDER_CARD |
| content | string | content | string | **text**: <br> old: <br> { <br> "content": "simple text" <br> } <br>  <br> new: <br> { <br> "content": "simple text" <br> } <br>  <br> **file_image**: <br> old: <br> { <br> "imageHeight": "290", <br> "imageUrl": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "imageWidth": "304" <br> } <br>  <br> new: <br> { <br> "height": 290, <br> "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "width": 304 <br> } <br>  <br> **goods_card**: <br> old: <br> { <br> "goods_id": "7494560109732334267" <br> } <br>  <br> new: <br> { <br> "product_id": "7494560109732334267" <br> } <br>  <br> **order_card**: <br> old: <br> { <br> "order_id": "7494560109732334267" <br> } <br>  <br> new: <br> { <br> "order_id": "7494560109732334267" <br> } |
#### Response
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| msg_id | string | message_id | string |  |
### [GET]/api/seller/im/customer_service/status
New path: [GET]/customer_service/202309/agents/settings
#### Request param
none
#### Response
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| status | int | can_accept_chat | bool | Value mapping: <br> 1->true <br> 0->false <br> 2->false <br>  <br> The old values 0 and 2 mean the customer service agent won't accept any chats. |
### [POST]/api/seller/im/customer_service/status/update
New path: [PUT]/customer_service/202309/agents/settings
#### Request param
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| status | int | can_accept_chat | bool | Value mapping: <br> 1->true <br> 0->false |
#### Response
None
### [POST]/api/seller/im/list_conversations
New path: [GET]/customer_service/202309/conversations
#### Request
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| cursor | string | page_token | string |  |
| limit | int | page_size | int |  |
| language | string | locale | string |  |
#### Response
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| next_cursor | string | next_page_token | string | 2 old fields are mixed to 1 new field. <br> An empty `page_token` means `has_more` is `false`. |
| has_more | bool |  |  |  |
| conv_with_last_msg | Object[] | conversations | Object[] |  |
| conv_with_last_msg[].conv_info.conv_short_id | string | conversations[].id | string |  |
| conv_with_last_msg[].conv_info.app_id | int | **Deleted** |  |  |
| conv_with_last_msg[].conv_info.member_count | int | conversations[].participant_count | int |  |
| conv_with_last_msg[].conv_info.can_send_message | bool | conversations[].can_send_message | bool |  |
| conv_with_last_msg[].conv_info.unread_count | int | conversations[].unread_count | int |  |
| conv_with_last_msg[].conv_info.participants | Object[] | conversations[].participants | Object[] |  |
| conv_with_last_msg[].conv_info.participants[].participant_id | string | conversations[].participants[].im_user_id | string |  |
| conv_with_last_msg[].conv_info.participants[].role | int | conversations[].participants[].role | string(enum) | Enum mapping: <br> 1->BUYER <br> 2->SHOP <br> 3->CUSTOMER_SERVICE |
| conv_with_last_msg[].conv_info.participants[].nick | string | conversations[].participants[].nickname | string |  |
| conv_with_last_msg[].conv_info.participants[].avatar | string | conversations[].participants[].avatar | string |  |
| conv_with_last_msg[].conv_info.participants[].outer_id | string | conversations[].participants[].user_id | string |  |
| conv_with_last_msg[].latest_msg | Object | conversations[].latest_message | Object |  |
| conv_with_last_msg[].latest_msg.conv_short_id | string | **Deleted** |  |  |
| conv_with_last_msg[].latest_msg.msg_id | string | conversations[].latest_message.id | string |  |
| **Newly added** |  | conversations[].latest_message.sender | Object |  |
| conv_with_last_msg[].latest_msg.sender_id | string | conversations[].latest_message.sender.im_user_id | string |  |
| conv_with_last_msg[].latest_msg.sender_role | int | **Deleted** |  |  |
| conv_with_last_msg[].latest_msg.sender_role_v2 | int | conversations[].latest_message.sender.role | string(enum) | Enum mapping: <br> 1->BUYER <br> 2->SHOP <br> 3->CUSTOMER_SERVICE <br> 4(deprecated) <br> 5->SYSTEM <br> 6->ROBOT |
| conv_with_last_msg[].latest_msg.sender_nick | string | conversations[].latest_message.sender.nickname | string |  |
| conv_with_last_msg[].latest_msg.sender_avatar | string | conversations[].latest_message.sender.avatar | string |  |
| conv_with_last_msg[].latest_msg.ref_msg_info | Object | **Deleted** |  |  |
| conv_with_last_msg[].latest_msg.msg_type | string(enum) | conversations[].latest_message.type | string(enum) | Enum mapping: <br> text->TEXT <br> file_image->IMAGE <br> allocated_service->ALLOCATED_SERVICE <br> notification->NOTIFICATION <br> use_enter_from_transfer->BUYER_ENTER_FROM_TRANSFER <br> user_enter_from_goods->BUYER_ENTER_FROM_PRODUCT <br> user_enter_from_order->BUYER_ENTER_FROM_ORDER <br> goods_card->PRODUCT_CARD <br> order_card->ORDER_CARD <br> emoticons->EMOTICONS <br> video->VIDEO <br> other->OTHER |
| conv_with_last_msg[].latest_msg.content | string | conversations[].latest_message.content | string | **text, allocated_service, notification, user_enter_from_transfer**: <br> old: <br> { <br> "content": "simple text" <br> } <br>  <br> new: <br> { <br> "content": "simple text" <br> } <br>  <br> **file_image**: <br> old: <br> { <br> "imageHeight": "290", <br> "imageUrl": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "imageWidth": "304" <br> } <br>  <br> new: <br> { <br> "height": 290, <br> "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "width": 304 <br> } <br>  <br> **goods_card, user_enter_from_goods**: <br> old: <br> { <br> "goods_id": "7494560109732334274" <br> } <br>  <br> new: <br> { <br> "product_id": "7494560109732334274" <br> } <br>  <br> **order_card, user_enter_from_orders**: <br> old: <br> { <br> "order_id": "7494560109732336829" <br> } <br>  <br> new: <br> { <br> "order_id": "7494560109732336829" <br> } <br>  <br> **video**: <br> old: <br> { <br> "video_info": "{"videoUrl":"https://v16m-default.akamaized.net/f4d97c4ca9018602e423366c40e9ccec/660fc8a9/video/tos/alisg/tos-alisg-v-2ea863-sg/okIEwc9EIW4OAJyZTiBOc6iIoB4xf3YEoQA2Po","coverUrl":"https://p16-oec-sg.ibyteimg.com/tos-alisg-v-2ea863-sg/oA29Bf4OciNoIyOEIAywiAToE6oBYbIZzAl4WF~tplv-aphluv4xwc-origin-jpeg.jpeg?from=3431008404","videoWidth":1920,"videoHeight":960,"videoDuration":127.254,"vid":"v10394g5000ccnk3m7fog65o44qog4cg","videoExpireTime":1712310441,"videoFormat":"mp4","videoSize":9309252,"videoBitRate":585239,"videoQuality":"original","codecType":"h264","nonOriginal":""}" <br> } <br>  <br> new: <br> { <br> "url": "https://v16m-default.akamaized.net/f4d97c4ca9018602e423366c40e9ccec/660fc8a9/video/tos/alisg/tos-alisg-v-2ea863-sg/okIEwc9EIW4OAJyZTiBOc6iIoB4xf3YEoQA2Po", <br> "width": 1920, <br> "height": 960, <br> "duration": "127.254", <br> "vid": "v10394g5000ccnk3m7fog65o44qog4cg", <br> "expire_time": 1712310441, <br> "format": "mp4", <br> "size": 9309252, <br> "bit_rate": 585239, <br> "quality": "original", <br> "codec_type": "h264" <br> } |
| conv_with_last_msg[].latest_msg.index_in_conversation | string | **Deleted** |  |  |
| conv_with_last_msg[].latest_msg.is_visible | bool | conversations[].latest_message.is_visible | bool |  |
| conv_with_last_msg[].latest_msg.create_time | int | conversations[].latest_message.create_time | int |  |
### [POST]/api/seller/im/get_conversation_messages
New path: [GET]/customer_service/202309/conversations/:conversation_id/messages
#### Request param
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| conv_short_id | string | conversation_id | string | Move to path variable |
| pull_direction | int | sort_order | string(enum) | Enum mapping: <br> 0->ASC <br> 1->DESC <br>  <br> In the old API, messages will always be sorted from oldest to latest. <br> In the new API, messages will be sorted from oldest to latest if the "sort_order" is "ASC", while they will be sorted from latest to oldest if "sort_order" is "DESC". |
| **Newly added** |  | sort_field | string | Sort messages by <br> Available value: <br> create_time (default) |
| cursor | string | page_token | string |  |
| limit | int | page_size | int |  |
| language | string | locale | string |  |
#### Response
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| next_cursor | string | next_page_token | string | 2 old fields are mixed to 1 new field. <br> An empty `page_token` means `has_more` is `false`. |
| has_more | bool |  |  |  |
| unsupport_msg_tips | string | unsupported_msg_tips | string |  |
| msgs | Object[] | messages | Object[] |  |
| msgs[].conv_short_id | string | **Deleted** |  |  |
| msgs[].msg_id | string | messages[].id | string |  |
| **Newly added** |  | messages[].sender | Object |  |
| msgs[].sender_id | string | messages[].sender.im_user_id | string |  |
| msgs[].sender_role | int | **Deleted** |  |  |
| msgs[].sender_role_v2 | int | messages[].sender.role | string(enum) | Enum mapping: <br> 1->BUYER <br> 2->SHOP <br> 3->CUSTOMER_SERVICE <br> 4(deprecated) <br> 5->SYSTEM <br> 6->ROBOT |
| msgs[].sender_nick | string | messages[].sender.nickname | string |  |
| msgs[].sender_avatar | string | messages[].sender.avatar | string |  |
| msgs[].ref_msg_info | Object | **Deleted** |  |  |
| msgs[].msg_type | string(enum) | messages[].type | string(enum) | Enum mapping: <br> text->TEXT <br> file_image->IMAGE <br> allocated_service->ALLOCATED_SERVICE <br> notification->NOTIFICATION <br> use_enter_from_transfer->BUYER_ENTER_FROM_TRANSFER <br> user_enter_from_goods->BUYER_ENTER_FROM_PRODUCT <br> user_enter_from_order->BUYER_ENTER_FROM_ORDER <br> goods_card->PRODUCT_CARD <br> order_card->ORDER_CARD <br> emoticons->EMOTICONS <br> video->VIDEO <br> other->OTHER |
| msgs[].content | string | messages[].content | string | **text, allocated_service, notification, user_enter_from_transfer**: <br> old: <br> { <br> "content": "simple text" <br> } <br>  <br> new: <br> { <br> "content": "simple text" <br> } <br>  <br> **file_image**: <br> old: <br> { <br> "imageHeight": "290", <br> "imageUrl": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "imageWidth": "304" <br> } <br>  <br> new: <br> { <br> "height": 290, <br> "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "width": 304 <br> } <br>  <br> **goods_card, user_enter_from_goods**: <br> old: <br> { <br> "goods_id": "7494560175032334583" <br> } <br>  <br> new: <br> { <br> "product_id": "7494560175032334583" <br> } <br>  <br> **order_card, user_enter_from_orders**: <br> old: <br> { <br> "order_id": "7494560109732337395" <br> } <br>  <br> new: <br> { <br> "order_id": "7494560109732337395" <br> } <br>  <br> **video**: <br> old: <br> { <br> "video_info": "{"videoUrl":"https://v16m-default.akamaized.net/f4d97c4ca9018602e423366c40e9ccec/660fc8a9/video/tos/alisg/tos-alisg-v-2ea863-sg/okIEwc9EIW4OAJyZTiBOc6iIoB4xf3YEoQA2Po","coverUrl":"https://p16-oec-sg.ibyteimg.com/tos-alisg-v-2ea863-sg/oA29Bf4OciNoIyOEIAywiAToE6oBYbIZzAl4WF~tplv-aphluv4xwc-origin-jpeg.jpeg?from=3431008404","videoWidth":1920,"videoHeight":960,"videoDuration":127.254,"vid":"v10394g5000ccnk3m7fog65o44qog4cg","videoExpireTime":1712310441,"videoFormat":"mp4","videoSize":9309252,"videoBitRate":585239,"videoQuality":"original","codecType":"h264","nonOriginal":""}" <br> } <br>  <br> new: <br> { <br> "url": "https://v16m-default.akamaized.net/f4d97c4ca9018602e423366c40e9ccec/660fc8a9/video/tos/alisg/tos-alisg-v-2ea863-sg/okIEwc9EIW4OAJyZTiBOc6iIoB4xf3YEoQA2Po", <br> "width": 1920, <br> "height": 960, <br> "duration": "127.254", <br> "vid": "v10394g5000ccnk3m7fog65o44qog4cg", <br> "expire_time": 1712310441, <br> "format": "mp4", <br> "size": 9309252, <br> "bit_rate": 585239, <br> "quality": "original", <br> "codec_type": "h264" <br> } |
| msgs[].index_in_conversation | string | **Deleted** |  |  |
| msgs[].is_visible | bool | messages[].is_visible | bool |  |
| msgs[].create_time | int | messages[].create_time | int |  |
### [POST]/api/seller/im/img/upload
New path: [POST]/customer_service/202309/images/upload
#### Request param
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| data | string | data | binary | In the old API, you should encode your image into BASE64 string, then put it in to a JSON request body. <br>  <br> In the new API, you should put your image binary data into the request body, with "Content-Type=multipart/form-data" and a form key named "data". |
#### Response
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| url | string | url | string |  |
| width | int | width | int |  |
| height | int | height | int |  |
### [POST]/api/seller/im/mark_read
New path: [POST]/customer_service/202309/conversations/:conversation_id/messages/read
#### Request param
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| conv_short_id | string | conversation_id | string | Move to path variable. |
#### Response
None
### [POST]/api/seller/im/create_conversation
New path: [POST]/customer_service/202309/conversations
#### Request param
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| buyer_id | string | buyer_user_id | string |  |
#### Response
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| conv_short_id | string | conversation_id | string |  |
## Webhook
### Type mapping
| **Event** | **Old type** | **New type** |
| --- | --- | --- |
| New conversation | 8 | 13 |
| New messages | 9 | 14 |
### Field mapping
#### New Conversation
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| conv_short_id | string | conversation_id | string |  |
| create_time | int | create_time | int |  |
#### New Messages
| **Old** | **Old type** | **New** | **New type** | **Description** |
| --- | --- | --- | --- | --- |
| message_id | string | message_id | string |  |
| conv_short_id | string | conversation_id | string |  |
| content | string | content | string | **text, allocated_service, notification, user_enter_from_transfer**: <br> old: <br> { <br> "content": "simple text" <br> } <br>  <br> new: <br> { <br> "content": "simple text" <br> } <br>  <br> **file_image**: <br> old: <br> { <br> "imageHeight": "290", <br> "imageUrl": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "imageWidth": "304" <br> } <br>  <br> new: <br> { <br> "height": 290, <br> "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290", <br> "width": 304 <br> } <br>  <br> **goods_card, user_enter_from_goods**: <br> old: <br> { <br> "goods_id": "7494560175032334583" <br> } <br>  <br> new: <br> { <br> "product_id": "7494560175032334583" <br> } <br>  <br> **order_card, user_enter_from_orders**: <br> old: <br> { <br> "order_id": "7494560109732337395" <br> } <br>  <br> new: <br> { <br> "order_id": "7494560109732337395" <br> } <br>  <br> **video**: <br> old: <br> { <br> "video_info": "{"videoUrl":"https://v16m-default.akamaized.net/f4d97c4ca9018602e423366c40e9ccec/660fc8a9/video/tos/alisg/tos-alisg-v-2ea863-sg/okIEwc9EIW4OAJyZTiBOc6iIoB4xf3YEoQA2Po","coverUrl":"https://p16-oec-sg.ibyteimg.com/tos-alisg-v-2ea863-sg/oA29Bf4OciNoIyOEIAywiAToE6oBYbIZzAl4WF~tplv-aphluv4xwc-origin-jpeg.jpeg?from=3431008404","videoWidth":1920,"videoHeight":960,"videoDuration":127.254,"vid":"v10394g5000ccnk3m7fog65o44qog4cg","videoExpireTime":1712310441,"videoFormat":"mp4","videoSize":9309252,"videoBitRate":585239,"videoQuality":"original","codecType":"h264","nonOriginal":""}" <br> } <br>  <br> new: <br> { <br> "url": "https://v16m-default.akamaized.net/f4d97c4ca9018602e423366c40e9ccec/660fc8a9/video/tos/alisg/tos-alisg-v-2ea863-sg/okIEwc9EIW4OAJyZTiBOc6iIoB4xf3YEoQA2Po", <br> "width": 1920, <br> "height": 960, <br> "duration": "127.254", <br> "vid": "v10394g5000ccnk3m7fog65o44qog4cg", <br> "expire_time": 1712310441, <br> "format": "mp4", <br> "size": 9309252, <br> "bit_rate": 585239, <br> "quality": "original", <br> "codec_type": "h264" <br> } |
| is_visible | bool | is_visible | bool |  |
| msg_type | string | type | string(enum) | Enum mapping: <br> text->TEXT <br> file_image->IMAGE <br> allocated_service->ALLOCATED_SERVICE <br> notification->NOTIFICATION <br> use_enter_from_transfer->BUYER_ENTER_FROM_TRANSFER <br> user_enter_from_goods->BUYER_ENTER_FROM_PRODUCT <br> user_enter_from_order->BUYER_ENTER_FROM_ORDER <br> goods_card->PRODUCT_CARD <br> order_card->ORDER_CARD <br> emoticons->EMOTICONS <br> video->VIDEO <br> other->OTHER |
| **Newly added** |  | sender | Object |  |
| sender_id | string | sender.im_user_id | string |  |
| sender_role | int | **Deleted** |  |  |
| sender_role_v2 | int | sender.role | string(enum) | Enum mapping: <br> 1->BUYER <br> 2->SHOP <br> 3->CUSTOMER_SERVICE <br> 4(deprecated) <br> 5->SYSTEM <br> 6->ROBOT |
| create_time | int | create_time | int |  |