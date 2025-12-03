# What is OMS

An order management system (OMS) is a digital way to manage the lifecycle of an order.¹ It tracks all the information and processes, including order entry, inventory management, fulfillment and after-sales service. An OMS offers visibility to both the business and the buyer. Organizations can have near real-time insight into inventories and customers can check when an order will arrive.

# Why I need build an OMS to integrate with Lazada

  * You have multiple stores in Lazada and other E-commerce platform
  * You want to link your own ERP with Lazadas stores.
  * Have development resources, and hope to meet the needs of the company requirements through customization



# A basic OMS architecture

## System architecture

![](https://tida.alicdn.com/oss_1671004718439_null_RPOSI3Pg)

## Tech architecture

![](https://tida.alicdn.com/oss_1671004755883_null_HR1F5axL)

# How to develop OMS with Lazada OpenAPI

## Precondition

You should grant your OMS have Lazada stores access permission and a lazada open platform account.

  * [Registration and Authorization process for newly registered ISVs](<https://open.lazada.com/apps/doc/doc?nodeId=38138&docId=121098>)
  * [Seller authorization introduction](<https://open.lazada.com/apps/doc/doc?spm=a1zq7z.man121098.site_detail.2.289f7c73NxrAyt&nodeId=10777&docId=108260>)
  * [Configure seller authorization](<https://open.lazada.com/apps/doc/doc?nodeId=10434&docId=108056>)



## Modules

### Product Management 

Features:

  * Add Product
  * Edit Product
  * Delete Product
  * Update Product Price only
  * Update Product stock only
  * Active/Deactive Product



#### Basic flow of create product

![](https://tida.alicdn.com/oss_1671004819496_null_FpRmoUP9)

  * [Get category attributes](<https://open.lazada.com/apps/doc/doc?nodeId=30717&docId=120946>)
  * [Image Upload](<https://open.lazada.com/apps/doc/doc?nodeId=30718&docId=120947>)
  * [Video Upload](<Video Upload>)
  * [Create a product](<https://open.lazada.com/apps/doc/doc?nodeId=30720&docId=120949>)



 

 

You can also accept the Lazada message to update your product info in OMS. 

OMS can monitor the product info from Lazada to check if the product info (such as price) is different between Lazada and your OMS.

 

### Order Management

Features

  * Pull Orders from Lazada
  * Cancel Order
  * RTS
  * Print AWB
  * Package Order
  * Get Reverse Reasons



#### Basic flow of order management

![](https://tida.alicdn.com/oss_1671004877060_null_fq5XxaFb)

 

#### Best Practice of use Lazada order OpenAPI

  * [Order Status Flow](<https://open.lazada.com/apps/doc/doc?nodeId=29484&docId=120167>)
  * [Order management and processing](<https://open.lazada.com/apps/doc/doc?nodeId=10548&docId=108143>)



 

You can also accept the Lazada message to update your orders Status in OMS. OMS monitor the orders status change in Lazada such as buyers cancel the order. 

# Other features that can improve efficiency

## Integrate chat with lazada buyer within your own CRM sys

## Basic chat flow

![](https://tida.alicdn.com/oss_1671004916280_null_GtPC9LtH)

[Lazada IM Open API](<https://www.yuque.com/barrieryouning/kb/oym4cz>)