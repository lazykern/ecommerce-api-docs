Property | Value | Comment
---|---|---
msg_type | 10 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30min | delay between two retries
Auth Required | true | This notification need authorization

 

Triggered when Reverse order status is updated
    
    
    {
        "seller_id": "12345",
        "message_type": 10,
        "data": {
            "reverse_order_id": 658960600102006,
            "reverse_status": "RTM_INIT",
            "trade_order_id": 416557324702006,
            "extraParams": {},
            "trade_order_line_id": 416557324802006,
            "buyer_id": 100112802006,
            "seller_id": 1000143772,
            "reverse_order_line_id": 663790000102006,
            "status_update_time": 1626767698
        },
        "timestamp": 1627889609,
        "site": "lazada_sg"
    }

"reverse_status" enumeration value

Please note that this push does not push all states of the reverse order. You will only receive a push of this type if the reverse order type and status meet the corresponding reverse-type and key.

For example, the REFUND_SUCCESS status will only be pushed if the reverse order is of type ONLY_REFUND, if your reverse order type is RTM, then you will not receive the REFUND_SUCCESS status.

reverse-type | key | title | content
---|---|---|---
CANCEL(Buyer Cancellation Trade Order) | CANCEL_INIT | Cancellation Initiated | Sorry this item didn't meet your expectations. Your request is being processed. You can track the status of your return request
CANCEL(Buyer Cancellation Trade Order) | CANCEL_SUCCESS | Cancellation Approved | Your refund of has been issued by the seller
CANCEL(Buyer Cancellation Trade Order) | CANCEL_REFUND_ISSUED | Cancellation Refund Issued | Your return request has been cancelled by our customer support team as another solution has been applied
RTM(Return to Merchant), MIX-RETURN | RTM_INIT | Return Initiated | Sorry this item didn't meet your expectations. Your request is being processed. You can track the status of your return request
RTM(Return to Merchant), MIX-RETURN | RTM_CANCELED | Return Request Cancelled | Your return was automatically cancelled. Please contact customer support if there is has been an issue
RTM(Return to Merchant) | RTM_SHIPPING_BACK | Return Collected | Our team have picked up your return item and are on their way back to our warehouse for inspection
RTM(Return to Merchant) | RTM_RECEIVE_ITEM | Return Processing | Your item has been received at seller and is being prepared for inspection
RTW(Return to Lazada Warehouse) | RTW_INIT | Return Initiated | Sorry this item didn't meet your expectations. Your request is being processed. You can track the status of your return request
RTW(Return to Lazada Warehouse) | RTW_CANCELED | Return Request Cancelled | Your return was automatically cancelled. Please contact customer support if there is has been an issue
RTW(Return to Lazada Warehouse), MIX-RETURN | RTW_SHIPPING_BACK | Return Collected | Our team have picked up your return item and are on their way back to our warehouse for inspection
RTW(Return to Lazada Warehouse), MIX-RETURN | RTW_REJECT | Return Processed | Sorry, your return goods did not pass inspection.
RTW(Return to Lazada Warehouse), MIX-RETURN | RTW_REFUND_PENDING | Return Processed | Your refund is on the way
ONLY_REFUND(Buyer initiated refund for Fresh Food or Redmart type orders) | REFUND_INIT | Refund Initiated | Sorry this item didn't meet your expectations. Your request is being processed. You can track the status of your return request
ONLY_REFUND(Buyer initiated refund for Fresh Food or Redmart type orders) | REFUND_PENDING | Refund Approved | Your refund of has been approved by our customer support team
ONLY_REFUND(Buyer initiated refund for Fresh Food or Redmart type orders) | REFUND_SUCCESS | Refund Issued | Your refund of has been issued
ONLY_REFUND(Buyer initiated refund for Fresh Food or Redmart type orders) | REFUND_REJECTED | Refund Rejected | Your refund has been rejected by our customer support team