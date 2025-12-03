For developers who have integrated with Quality Engine, when there are some incidents, developers need to sync incident reason by reason code of the list. It can help the system to identify risk order and A-LOC order with higher accuracy and then we can provide more efficient suggestions for sellers/developers to resolve the issues. And it also is very helpful to improve our system performance.
To sync reason code, developers need:

1. Syncing enumeration of reason code on the list via Quality Engine data exchanging API.
2. Using codes on the list, any codes out of the list will be forbidden to sync by Quality Engine.
3. Using correct code, developers need to pay attention to the description of code and sync the most reasonable code for the specific incident.
4. Using the code which is suitable for the rule, every reason code has its suitable rules, developers need to follow the mapping relationship on the list.

Reason Code List:

1. Reason codes for incident that there is no related order in DTC channel. (Orphan order)

| Reason Category | Suitable for Rules | Reason Code | Orphan Reason Desc |
| --- | --- | --- | --- |
| Orphan Order | R1/R2/A1 | **SELLER_TIKTOKSHOP_AUTHORIZATION_REVOKED** | Seller revoked TikTok shop authorization for the App |
| Orphan Order | R1/R2/A1 | **SELLER_UNINSTALLED_DTC_APP** | Seller uninstalled the App from the Channel platform |
| Orphan Order | R1/R2/A1 | **SELLER_NOT_GRANT_DTC_PERMISSION** | Seller did not grant corresponding APIs permission of the Channel platform for App |
| Orphan Order | R1/R2/A1 | **SELLER_DTC_STORE_UNAVAILABLE** | Seller's Channel store is unavailable |
| Orphan Order | R1/R2/A1 | **SELLER_TIKTOKSHOP_STORE_INACTIVE** | Seller's TikTok shop store is inactive |
| Orphan Order | R1/R2/A1 | **SELLER_DTC_NO_SKU** | No corresponding SKU found for seller's Channel products |
| Orphan Order | R1/R2/A1 | **SELLER_DTC_ABNORMAL_PRODUCT_STATUS** | Abnormal product status on seller's Channel platform |
| Orphan Order | R1/R2/A1 | **SELLER_DTC_PRODUCT_OUT_OF_STOCK** | Products on seller's Channel platform are out of stock |
| Orphan Order | R1/R2/A1 | **SELLER_TIKTOKSHOP_ORDER_AMOUNT_ZERO** | Order amount in seller's TikTok shop orders is 0 |
| Orphan Order | R1/R2/A1 | **SELLER_APP_OWE_FEE** | Seller used the App but did not renew or out of quota |
| Orphan Order | R1/R2/A1 | **SELLER_ABANDON_SYNC_TIKTOKSHOP_ORDER** | Seller opted not to synchronize TikTok shop orders |
| Orphan Order | R1/R2/A1 | **APP_MISSED_WEBHOOK** | App missed TikTok shop order webhooks |
| Orphan Order | R1/R2/A1 | **APP_ORDER_RETRIEVE_API_FAILED** | App failed to retrieve orders by calling TikTok shop API |
| Orphan Order | R1/R2/A1 | **APP_ORDER_RETRIEVE_API_NOT_MATCH_DTC_FIELD** | The order information retrieved by the App through the TikTok shop API is incomplete |
| Orphan Order | R1/R2/A1 | **APP_CALL_DTC_CREATE_ORDER_API_FAILED** | App failed to create orders by calling Channel API |
| Orphan Order | R1/R2/A1 | **OTHER** | Other |

2. Reason code for incident that order is shipped in DTC channel but not shipped in TikTok Shop.

| Reason Category | Suitable for Rules | Reason Code | Pre-RTS Desc |
| --- | --- | --- | --- |
| Pre-RTS | A3/R5/R6 | **INVALID_TRACKING_NUMBER** | Invalid Tracking Number entered in DTC: <br> - tracking number has extra spaces or tabs <br> - tracking number is incorrect but accepted by DTC <br> TTS rejects this fulfillment |
| Pre-RTS | A3/R5/R6 | **UNSUPPORTED_CARRIER_TRACKING_NUMBER** | Supported carrier by DTC but unsupported carrier in TTS <br> TTS rejects this fulfillment |
| Pre-RTS | A3/R5/R6 | **ORDER_NOT_ELIGIBLE_FOR_FULFILLMENT** | Package shipped in DTC but not TTS because TTS has a <br> cancellation or refund request for that order. <br> TTS rejects this fulfillment |
| Pre-RTS | A3/R5/R6 | **FULFILL_UNIT_OR_ORDER_NUMBER_NOT_COMBINED_CORRECTLY** | Package or Order fulfillment call to TTS failed because <br> the tracking number has been used in another order without <br> combining orders. |
| Pre-RTS | A3/R5/R6 | **FULFILL_UNIT_OR_ORDER_NUMBER_NOT_FOUND** | Package or Order fulfillment call to TTS failed because seller <br> combined or split order in TTS or the DTC before fulfillment. <br> TTS rejects this fulfillment |
| Pre-RTS | A3/R5/R6 | **FULFILLMENT_FAILURE_DUE_TO_RATE_LIMIT** | Package or Order fulfillment call to TTS failed because app <br> rate limit was exceeded and there was no retry |
| Pre-RTS | A3/R5/R6 | **FULFILLMENT_FAILURE_DUE_TO_NO_RETRY_LOGIC** | order fulfillment call was made for this order from the connector app <br> but TTS system was down and threw an internal error. Order fulfillment <br> was not retried by the connector app |
| Pre-RTS | A3/R5/R6 | **FULFILLMENT_FAILURE_DUE_TO_NO_API_CALL** | No order fulfillment call was made for this order from the connector |