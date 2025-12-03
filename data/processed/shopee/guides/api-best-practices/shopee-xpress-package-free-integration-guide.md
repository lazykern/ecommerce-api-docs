## 1.Terminology

  * Shopee Xpress - Package-free: logistics channel ID 30029
  * Unpackage sku id: Unique item identifier used for this logistics channel.
  * Unpackage sku id label: The label that is used for attached on the item when shipping with this logistics channel.
  * TO label: The label that is used for attached on the shipping carton when shipping with this logistics channel.
  * Sorting group: The value that is used for sellers to pack the item together when shipping with this logistics channel.



## 2.Business Operation Logic

2.1 Automatic Order Splitting

For orders with logistics channel 30029, when the order status becomes "READY_TO_SHIP", the system will automatically split the order into multiple packages based on the quantity of each item (Quantity Level).

For example, if an order contains 3 bottles of milk tea and 2 bottles of black tea, the system will automatically split it into 5 packages, each containing 1 quantity.

 

2.2 Arrange Shipment Process

When using logistics channel 30029 to ship items, sellers no longer need to pack by order level. The steps are:

1) Attach the Unpackaged SKU ID Label to each item

2) Pack items together in a shipping carton by sorting_group and attach the TO Label on the shipping carton

 

Please refer to the Seller Education Hub article for more detail: [_【蝦皮店到店-環保無包裝】出貨流程教學_](<https://seller.shopee.tw/edu/article/24913>)

## 3.Query item’s Unpackaged SKU ID

The Unpackaged SKU ID is the unique identifier for the item under this logistics channel. You can obtain the information through the following API when item enabled logistic channel 30029:

  * [v2.product.search_unpackaged_model_list](<https://open.shopee.com/documents/v2/v2.product.search_unpackaged_model_list?module=89&type=1>)



 

## 4.Obtain order information and detail

Note: The logistics channel 30029 automatically splits orders. Be sure to get package level information while using the following APIs to avoid missing details.

  * [v2.order.search_package_list](<https://open.shopee.com/documents/v2/v2.order.search_package_list?module=94&type=1>)：To query the package list.
  * [v2.order.get_package_detail](<https://open.shopee.com/documents/v2/v2.order.get_package_detail?module=94&type=1>)：To query the package information.
  * [v2.order.get_order_detail](<https://open.shopee.com/documents/v2/v2.order.get_order_detail?module=94&type=1>)：To query the order information, please ensure “package_list” is included in the request parameter “response_optional_fields”.



 

*When the PackageFulfillmentStatus of packages with this logistics channel changes to “LOGISTICS_REQUEST_CREATED” (after arrange shipment), you can obtain the value in the “sorting_group” field.

## 5.Basic Shipping Logic

**5.1 Shipment API Call Flow**

Note: The logistics channel 30029 automatically splits orders, please ensure “package_number” is included in the request parameter for following APIs.

  1. **Obtain shipping parameter:** Call “[v2.logistics.get_shipping_parameter](<https://open.shopee.com/documents/v2/v2.logistics.get_shipping_parameter?module=95&type=1>)” or “[v2.logistics.get_mass_shipping_parameter](<https://open.shopee.com/documents/v2/v2.logistics.get_mass_shipping_parameter?module=95&type=1>)” API
  2. **Arrange Shipment:** Call “[v2.logistics.ship_order](<https://open.shopee.com/documents/v2/v2.logistics.ship_order?module=95&type=1>)” or “[v2.logistics.mass_ship_order](<https://open.shopee.com/documents/v2/v2.logistics.mass_ship_order?module=95&type=1>)” API
  3. **Obtain tracking number:** Call “[v2.logistics.get_tracking_number](<https://open.shopee.com/documents/v2/v2.logistics.get_tracking_number?module=95&type=1>)” API



 

**5.2 Obtain Unpackage sku id label call flow**

Call the following APIs in sequence to obtain the Unpackage sku id label corresponding to the package:

  1. [v2.logistics.get_shipping_document_parameter](<https://open.shopee.com/documents/v2/v2.logistics.get_shipping_document_parameter?module=95&type=1>)
  2. [v2.logistics.create_shipping_document](<https://open.shopee.com/documents/v2/v2.logistics.create_shipping_document?module=95&type=1>)
  3. [v2.logistics.get_shipping_document_result](<https://open.shopee.com/documents/v2/v2.logistics.get_shipping_document_result?module=95&type=1>)
  4. [v2.logistics.download_shipping_document](<https://open.shopee.com/documents/v2/v2.logistics.download_shipping_document?module=95&type=1>)



The order for this logistics channel only supports "THERMAL_UNPACKAGED_LABEL" as the "shipping_document_type".

 

**5.3 Obtain TO label call flow**

After completing the packing according to the sorting group, you can obtain the TO label file through the following API:

  * [v2.logistics.download_to_label](<https://open.shopee.com/documents/v2/v2.logistics.download_to_label?module=95&type=1>)



Please note that each TO label is unique. Ensure that each TO label is obtained by independently calling this API, as duplicate packing lists will affect the drop-off process.

## 6.Other Process

**6.1 Pre-printing Unpackaged SKU ID Label before order creation**

We support pre-printing Unpackaged SKU ID Label for items even before order creation, for advanced labeling and preparation

You can obtain the file by calling the following APIs in sequence:

  1. [v2.logistics.create_shipping_document_job](<https://open.shopee.com/documents/v2/v2.logistics.create_shipping_document_job?module=95&type=1>): Create a print job
  2. [v2.logistics.get_shipping_document_job_status](<https://open.shopee.com/documents/v2/v2.logistics.get_shipping_document_job_status?module=95&type=1>): Get the job status
  3. [v2.logistics.download_shipping_document_job](<https://open.shopee.com/documents/v2/v2.logistics.download_shipping_document_job?module=95&type=1>): Download the label files



Please note that the item must have logistics channel 30029 enabled to use this process for calling the API.

 

**6.2 Self-Design Unpackaged SKU ID Label**

In this logistics option, we recommend that you design the Unpackaged SKU ID Label according to sellers’ preferences. You can refer to the "custom fields" section specifications in the [FAQ](<https://open.shopee.com/faq/279>) attachment to create labels tailored to each seller's needs.

  * [v2.logistics.get_shipping_document_data_info](<https://open.shopee.com/documents/v2/v2.logistics.get_shipping_document_data_info?module=95&type=1>): For orders using B2C logistics, you can obtain the "unpackaged_sku_id" and "unpackaged_sku_id_qrcode" fields through this API.
  * Guidelines (for reference only, the official specifications are in the [FAQ](<https://open.shopee.com/faq/279>) on the Open Platform website)
    * QR Code Generation Rules:
      * ECI mode is not allowed.
      * Avoid embedding UTF-8 or other encoding declarations in the QR code.
    * Custom Area Display Rules:
      * Font size and line-break restrictions have been removed.
      * Ensure that custom areas do not affect the display or layout of non-custom areas.



## 7.Recommended API Call Flow

7.1 Printing Unpackaged SKU ID Label after order creation

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=gmp8Yaf%2BAd0cUw8hjvSD6ka4IJ7KHtGtlvUbmv5tQ3dAgOYw70brmf13MwIYphkB6D%2BqGP65L9SVOfmCZvFeYw%3D%3D&image_type=jpg)

7.2 Pre-printing Unpackaged SKU ID Label before order creation

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=VFVDZrjdvG26scOfRf9Miw23YTBsjwvb4txaTPFlBuIDcrpYvIpJw2vfSGSNHppPppImWDY9G5GqCbCmQXcfKw%3D%3D&image_type=jpg)

## 8.FAQ

Q: For orders under this logistics channel with multiple packages, when the logistics statuses of the packages differ, how will the order status be displayed?

 

A: Please to this FAQ for detail: [_https://open.shopee.com/faq/510_](<https://open.shopee.com/faq/510>)

 

—-—-—-—-—-—-

 

Q: Why is the "shipping_carrier" field at the outer level empty when I retrieve order details through the "v2.order.get_order_detail" API?

 

A: Orders under this logistics channel will be automatically split, and the "shipping_carrier" field at the outer level of the "v2.order.get_order_detail" API will not display a value. Please retrieve the "shipping_carrier" field from each package in the "package_list."

 

—-—-—-—-—-—-

 

Q: Why does the system return an error message when I call the Shipment or Unpackaged SKU ID Label API?

 

A: This logistics channel will automatically split orders. Please ensure that the "package_number" field parameter is included in the request when calling logistics-related APIs.

 

# 9.Data Definition

Please refer to the [V2.0 Data Definition](<https://open.shopee.com/developer-guide/31>) page.