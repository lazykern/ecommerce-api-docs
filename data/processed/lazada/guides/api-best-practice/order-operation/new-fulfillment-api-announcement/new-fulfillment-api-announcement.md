# Background

Because Current Fulfillment API got below issues:

  1. There is no a clear education Document to ISV developer;
  2. Current all API's?Request Parameters is trade order item id, except Repack, that is not align with Fulfillment system logic, need to change RTS, Print AWB and SOF API's Request Parameters to Fulfillment package ID;
  3. Too many back up logic for Open API, like RTS when no package in here, will auto trigger pack process, that is increasing fulfillment system and API?complexity; need to change to Pack at first and then request Print/ RTS based on Pack API?Response Parameters;
  4. Optimize Get shipment provider API, Response Parameters based on fulfillment system: 3PL list or default;
  5. Provide Tracking number checking;

We will Revamp Fulfillment API, and Provide Totally New Fulfillment to ERP Seller;

Old Fulfillment API will be offlined in **30th April 2023** ;

# Overview

**Note** :For a complete flow chart, please refer to：[New Fulfillment API Flow Chart](<https://www.yuque.com/docs/share/da1d477f-7f20-4acb-8217-082a5747106e#%20%E3%80%8ANew%20Fulfillment%20API%20Flow%20Chart%E3%80%8B>)

## 1.1 Order Status Flow Chart 

##  ![](https://tida.alicdn.com/oss_1670493120614_null_YRZTwq0m)

![](https://tida.alicdn.com/oss_1670397362524_null_9JvQBJ5Q)

![](https://id-live-02.slatic.net/p/a2c0b58f524e144cfba08deef772c3b0.jpg)

## 1.2 Order API Call Flow

![](https://tida.alicdn.com/oss_1683276528975_null_uFmHVZOn)

![](https://id-live-02.slatic.net/p/76eb613c4fe167218d0347c5aacc1a8b.jpg)

## 1.3 Scnarios List

![](https://id-live-02.slatic.net/p/176a81d137913b8a93960b88cb7c99bd.jpg)

**You may also be interested in the following topics:**

Click here to view [New Fulfillment API Details](<https://open.lazada.com/apps/doc/doc?nodeId=30765&docId=120984>)