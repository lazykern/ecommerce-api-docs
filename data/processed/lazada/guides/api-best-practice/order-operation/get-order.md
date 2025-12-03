This tutorial will introduce the API and fields related to getting orders.

# **Get order list**

Once a new store has authorized your app, you can call the GetOrders API to get all the orders for the open store.

## **API used**

[GetOrders API](<https://open.lazada.com/apps/doc/api?path=%2Forders%2Fget>)

## **1.Request parameter setting**

Parameter Name| Parameter Type| Value| Field Description  
---|---|---|---  
created_after| String| 2018-02-10T16:00:00+08:00| The time condition for querying orders, if you neet to get all orders in the store you can set this time to the store creation time or the time when the first order is generated.  
status| String| all| Filter orders by order status, fill all will get all status of orders.  
limit| String| 100| Number of orders that can be responded to per request.Maximum value: 100  
offset| String| 0| The number of skipped data. If limit is set to 100, then offset should be set to 0/100/200/300 ......Maximum value: 5000  
The rest of the parameters can be configured according to your needs  
  
Common Parameters will not be introduced

## **2\. Recurring request and get order information**

Based on the request in the first step, the value of offset is cyclically increased to get more orders.

You can use the countTotal field to determine how many orders there were in total during the time period you requested.

You can determine how many orders there were in total during the time period you requested based on the countTotal field in the GetOrders API response.

When offest is set to the maximum value, if you need to get subsequent orders. Please set the time of create_at to the creation time of the last order you fetched and set offset to 0 to continue the loop call.

## **3.Get new orders**

After getting old orders from the store, you need to get new orders, in this case we don't recommend you to keep calling GetOrders API in a loop to monitor new order generation, because it will lead to waste of resources and unstable service, so we may disable your app when we monitor a large number of exception calls.

### **Order push**

Lazada Open Platform has a push mechanism. If you complete the verification of the push URL and subscribe to the order push, you will receive a push when the order is generated or the status is updated. Then you can get the order information and status update according to the order id and order item id in the push by [GetOrder API](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fget>).

[Lazada Push Mechanism](<Lazada Push Mechanism>)

[Webhook API Trade Order Notifications](<https://open.lazada.com/apps/doc/doc?nodeId=29538&docId=120196>)

## **4.GetOrder/GetOrders API field analysis**

### **order_id**

The identification number of the order, unique to the current store only.

If a buyer buys products from both stores, then both stores will generate orders with the same order id.

### **address_shipping**

This field is the shipping address, where the address consists of address1~5.

address1 Detailed address

address2 Not used for now

address3 State name

address4 city

address5 Post Code

### **shipping_fee**

The actual shipping cost paid by the seller, including the shipping fee discount.

### **statuses**

Lazada has no order status, each item in the order has a separate status. So this field is a collection that will show the status of the order items that the order currently contains. The same status is displayed only once.

### **price**

Total order price (excluding product discounts and order discounts)

If you want to use the GetOrder/GetOrders API to calculate the actual amount paid for an order, please refer to this formula：buyer paid price = price - voucher + shipping_fee.

## **5.Get order item details**

To get order details, you need to call [GetOrderItems](<https://open.lazada.com/apps/doc/api?path=%2Forder%2Fitems%2Fget>)/[GetMultipleOrderItems](<https://open.lazada.com/apps/doc/api?path=%2Forders%2Fitems%2Fget>) API, please check if the order id exists in the requested store before calling.

When getting the order item details, please note that lazada does not count the number of items in the order, but rather responds to the order items as separate objects. If an order is placed for two identical items, it will still be responded to as two different objects with unique order item ids.