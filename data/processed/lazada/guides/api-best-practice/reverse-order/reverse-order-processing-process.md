![2.png](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1690765962788_rDNMgmCm)

# Auto Pass Feature Introduction for Open APl:

Auto Pass is belonging Reverse Bot, Which is A Reverse Tool Lazada Providing to Seller, Help Seller Handle Reverse Order Automatically and Improve Reverse Efficiency;

## Auto Pass Function:

Auto Pass Help Seller Automatical Review and Approve Return Requests or/and Quality Check(QC) Process, Including:

Auto Approved New Return Requests, Which is Auto Review and Approve New Return Requests to Return or Refund;

Auto Approved Quality Check(QC) process, Which is Auto Review and Approve QC Process to Refund.

## Seller Control & Automated Activation Rules:

Sellers can manually enable or disable this feature.

Note: The feature maybe automatically activated if the seller triggers the following scenarios

i. Return Request Approve: Automatically enabled if all return request approve breached SLA in the past 30 days.

ii. Return QC Approve: Automatically enabled if all return QC approve breached SLA in the past 30 days.

Violation Handling

i. Sellers may manually disable the feature after automatic activation for the first three violations.

ii. After the third violation, the feature remains active for 30 days before manual disablement is available.

# **Type of return**

## **Step 1 Call API to get reverse order information**

**request_type** : RETURN

You need to call the _[GetReverseOrderDetail API](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Freverse%2Freturn%2Fdetail%2Flist>)_ or the _GetReverseOrdersForSeller API_ to get the list of returned orders along with the details and to pick out the ones that are in the REQUEST_INITIATE state.

## **Step 2 Calling the API to Process Reverse Orders**

**Available Actions** :instantRefund、agreeReturn、refuesReturn

![image.png](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1690765963144_PhkGgOsw)

Orders that are normally in the REQUEST_INITIATE state have three options for the seller to actively choose how to handle them within the SLA timeframe.

You need to call the ReverseOrderReturnUpdate API to manipulate this option. To do so, enter "instantRefund", "agreeReturn" or "refuesReturn" in the action field. These three first choices correspond to the "Refund Only", "Return & refund" and "Reject" options in the screenshot.

When you use "instantRefund" or "agreeReturn", you only need to enter the action, reverse_order_id and reverse_order_item_ids fields.

But if you want to use "refuseReturn", then you have to call GetReverseOrderReasonList API first to get the available reasion ids to be entered in the reason-id field, and the comment and fields as well mandatory.

If you select refuseReturn, the process will end at this step.

## **Step 3 Confirm receipt of item(s)**

**Available Actions** : confirmDelivery

When the seller chooses agreeReturn(Return & refund) in the second step, the buyer needs to choose the transportation method and send out the goods, after the seller receives the goods, he needs to call ReverseOrderReturnUpdate API to input "confirmDelivery" to confirm.

![image.png](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1690765963464_kNnVzxbr)

## **![image.png](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1690765963838_P2BxzuFo)Step 4 Decide whether or not to make a refund after inspecting the items**

**Available Actions** : agreeRefund、refuseRefund

![image.png](https://wirelsee-weex-tasp-public-oss.oss-cn-hangzhou.aliyuncs.com/oss_1690765964133_Sc1kOf8Q)

When the seller confirms the receipt of the goods, they need to check the goods within the SLA time limit and call the API or select "Process Refund" or "Reject the Request" in the seller center to confirm whether to refund or not.

Corresponds to the "agreeRefund" and "refuseRefund" enumerations in the action field of the ReverseOrderReturnUpdate API. When you use the "refuseRefund" enumeration "reason_id", "comment" and " image_info" fields are required.

# **Type of refund only**

**Note** : This type of reverse order is limited to specific categories can apply, specific categories, please consult the local national customer service.

## **Step 1 Call API to get reverse order information**

**request_type** : ONLY_ REFUND

You need to call the _[GetReverseOrderDetail API](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Freverse%2Freturn%2Fdetail%2Flist>)_ or the _GetReverseOrdersForSeller API_ to get the list of returned orders along with the details and to pick out the ones that are in the REQUEST_INITIATE state.

## **Step 2 Calling the[ReverseOrderOnlyRefundDecide API](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Freverse%2Fonlyrefund%2Fseller%2Fdecide>) to Process Reverse Orders**

**Available Actions** : agreeRefund, startDispute

Upon receipt of this type of reverse order, you will need to confirm weather your agreement to the refund within the SLA timeframe.

If you agree, you need to enter "agreeRefund".

When you use the "startDispute" enumeration,then "comment" and " image_info" fields are required.