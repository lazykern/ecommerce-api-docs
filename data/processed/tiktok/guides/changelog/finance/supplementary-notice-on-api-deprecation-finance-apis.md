Following the announcement of **V1 API deprecation** by the TikTok Shop Open Platform, we are issuing an additional clarification regarding the deprecation plan for the following two Finance category APIs:

* [Get Transactions by Order](get-transactions-by-order);
* [Get Transactions by Statement](get-transactions-by-statement).

## Action Required
In addition to the deprecation of all V1 APIs (version number < 202309), the **202309 versions** of the above two APIs will also be included in the deprecation plan. These endpoints will no longer be supported after the official sunset date. You must migrate to the latest V2 versions as soon as possible.
## 🔍 Scope of Impact
| API Name | Deprecated Version | Replacement |
| --- | --- | --- |
| [Get Transactions by Order](get-transactions-by-order) | 202309 | 202501 |
| [Get Transactions by Statement](get-transactions-by-statement) | 202309 | 202501 |
## Deprecation Timeline

* **From July 1, 2025**: Gradual deprecation begins. You will start encountering stricter request limits and errors as part of the deprecation process. To avoid disruptions, please migrate to the new version promptly.
* **By December 31, 2025**: The 202309 version of these APIs will be fully sunset, and all requests will be blocked.

## Reference
Please refer to:

* Full deprecation policy: [Deprecating TikTok Shop API V1](deprecating-tts-api-v1);
* Finance API official upgrade announcement: [New version (v202501) for Statement Transactions and Order Statement Transactions](new-version-v202501-for-statement-transactions-and-order-statement-transactions).

## Next Steps for Developers

* Review your system to identify whether the above APIs in **202309 version** are still being used;
* Upgrade to the corresponding latest **V2 API versions** as soon as possible;
* A detailed **migration guide** will be published soon. Please stay tuned for further updates.


---


Thank you for your continued support and cooperation.


Regards,


TikTok Shop Open Platform Team