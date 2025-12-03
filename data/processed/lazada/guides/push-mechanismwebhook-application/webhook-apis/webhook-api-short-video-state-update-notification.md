Property | Value | Comment
---|---|---
msg_type | 7 | field to determine message type.
Retry times | 12 | Retry times when client failed to response
Retry Interval | 30 min | delay between two retries
Auth Required | true | This notification need authorization

Triggered when a short vdeio status is updated. 

Use this notification to track the video you uploaded for a product. 
    
    
    {
        "seller_id": "213",
        "message_type": 7,
        "data": {
            "state": "AUDIT_SUCCESS", //State Enumeration 
            "timestamp": 1626763154,
            "videoId": 30023210009
        },
        "timestamp": 1626763154,
        "site": "lazada_sg"
    }

State Enumeration :

READY_FOR_TRANSCODE,

TRANSCODING,

TRANSCODE_FAILED,

READY_FOR_AUDIT,

AUDIT_FAILED,

AUDIT_SUCCESS,

DELETED.