# Summary
We've updated our Order APIs to support the rollout of item protection for TikTok Shop orders.
# Impact
|  |  |
| --- | --- |
| Impacted market(s) | * United States (US) - Local and cross-border |
| Impacted version(s) | * 202309 (and later) |
# What's new?
Since TikTok Shop buyers can now purchase item protection for their order(s), we wanted to ensure our APIs reflected that as well.
## POST Get Order List and GET Order Detail
For both [POST Get Order List](https://partner.tiktokshop.com/docv2/page/get-order-list-202309) and [GET Order Detail](https://partner.tiktokshop.com/docv2/page/get-order-detail-202507), we've expanded the response parameter `orders.payment.item_insurance_fee` to additionally be available in the US market (previously exclusive to the Indonesian market). This parameter indicates the amount the buyer paid for item protection.