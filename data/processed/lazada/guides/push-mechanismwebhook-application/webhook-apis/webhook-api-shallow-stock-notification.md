## Notification

Triggered when warehouse sellable stock number below certain thresh hold(5 for now).

Property | Value | Comment
---|---|---
msg_type | 6 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

 
    
    
    {
        "seller_id": "1000008313", //sellerId
        "message_type": 6,  //message type
        "data": {
            "seller_sku":"test-Lazada-sku",//sku name
            "withhold_quantity": 0,  //withold quantity 
            "sku_id": 1173310888,  //skuId
            "real_quantity": 5,  //total quantity
            "warehouse": "dropshipping", //warehouse identifier
            "occupy_quantity": 5, //occupied quantity
            "pre_order_quantity": 0 //pre_order quantity
        },
        "timestamp": 1626164321,  //时间戳
        "site": "lazada_sg" //站点
    }

Sellable = real_quantity - withold_quantity - occupy_quantity.

## \---stock knowledage--

A example to help you understand real_quantity, withold_quantity and occupy_quantity

### Normal order flow

 | entity_id | sellable_qty | real_qty | withhold_qty | occupy_qty
---|---|---|---|---|---
init | 1 | 10 | 10 | 0 | 0
order_pending | 1 | 9 | 10 | 1 | 0
order_unpaid | 1 | 9 | 10 | 1 | 0
order_paid | 1 | 9 | 10 | 0 | 1
RTS | 1 | 9 | 9 | 0 | 0

 

### Order is paid and canceled

 | entity_id | sellable_qty | real_qty | withhold_qty | occupy_qty
---|---|---|---|---|---
init | 1 | 10 | 10 | 0 | 0
order_pending | 1 | 9 | 10 | 1 | 0
order_unpaid | 1 | 9 | 10 | 1 | 0
order_paid | 1 | 9 | 10 | 0 | 1
order_canceld | 1 | 10 | 10 | 0 | 0

 

### Order peding expired and repaid.

 | entity_id | sellable_qty | real_qty | withhold_qty | occupy_qty
---|---|---|---|---|---
init | 1 | 10 | 10 | 0 | 0
order_pending | 1 | 9 | 10 | 1 | 0
order_pending_expired | 1 | 10 | 10 | 0 | 0
order_unpaid | 1 | 9 | 10 | 1 | 0
order_paid | 1 | 9 | 10 | 0 | 1
RTS | 1 | 9 | 9 | 0 | 0