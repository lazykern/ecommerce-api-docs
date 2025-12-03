This tutorial will explain lazada's inventory calculation logic so that you can better manage your inventory using the API.

# Stock types

Inventory name | Order Status | Description
---|---|---
WithholdQuantity | Unpaid | The quantity of inventory that is locked when a buyer submits an order but has not yet paid for it. Seller Center does not show. This quantity will move from SellableQuantity to WithholdQuantity when the order is submitted. When the payment is made, the stock will be moved to OccupyQuantity. After the order remains unpaid for 30 minutes, the inventory will be moved to SellableQuantity. Sellers cannot manually modify.
OccupyQuantity | Pending ~ Packed | When an order is cancelled, the inventory will be moved from OccupyQuantity to SellableQuantity. Seller Center does not show. When the order is updated to RTS status, the inventory will be moved out of OccupyQuantity. Sellers cannot manually modify.
SellableQuantity | N/A | The quantity of stock that can be purchased by buyers. Seller Central shows this inventory This inventory quantity includes the inventory locked by the campaign. The inventory cannot be modified with less than the inventory locked by the campaign. This inventory can be modified using the following API: AdjustSellableQuantity UpdateProduct UpdateSellableQuantity
totalQuantity | N/A | Combination of the above inventory. Seller Center does not show. The inventory cannot be less than WithholdQuantity+OccupyQuantity+channelInventories when the inventory is modified. This inventory can be modified using the following API: UpdatePriceQuantity
channelInventories | N/A | The amount of inventory locked by the campaign after participating in the campaign . This inventory will be removed at the end of the event and will become a modifiable SellableQuantity.

 

# Flow chart of inventory change after placing an order

![](https://tida.alicdn.com/oss_1680155071963_null_8k3WK14U)

# Multi-warehouse

Usually a seller can only configure one Warehouse Address, which is a single-warehouse seller. However, by applying to the seller's customer service, the seller can set up multiple Warehouse Addresses, which is a multi-warehouse seller.

## Impact of multiple warehouses on products

When a multi-warehouse seller creates multiple warehouses, a new warehouse inventory setting will be added for all items in that store. The inventory of different warehouses is independent.

### Seller Center Demo

![](https://tida.alicdn.com/oss_1680155098705_null_S1BhwlVz)

### GetProducts/GetProductItem API Demo
    
    
    {
        "data": {
            "skus": [
                {
                    ......
                    "multiWarehouseInventories": [
                        {
                            "occupyQuantity": 0,
                            "quantity": 100,
                            "totalQuantity": 100,
                            "withholdQuantity": 0,
                            "warehouseCode": "dropshipping",
                            "sellableQuantity": 100
                        },
                        {
                            "occupyQuantity": 0,
                            "quantity": 1,
                            "totalQuantity": 1,
                            "withholdQuantity": 0,
                            "warehouseCode": "MY10RV7-WH-10002",
                            "sellableQuantity": 1
                        },
                        .......
                    ]
                }
            ],
            ......
        },
        "code": "0",
        "request_id": "2141276616801444715421373"
    }

#### Note

  * The inventory locked by channelInventories is not warehouse dependent, as long as the remaining available inventory for the SKU is an integer greater than or equal to the inventory locked by channelInventories.
  * The multiWarehouseInventories field cannot be used to determine if a seller is a multiwarehouse seller because the field does not respond to information from other warehouses when those warehouses are not in stock.

## How to determine if a seller is a multi-warehouse seller

### Determine in seller center

Please open “My Account - Settings - Warehouse” in Seller Central to check the Warehouse Address section.

If the Warehouse Address field has a warehouse address other than dropshipping, then this is a multi-warehouse seller.

![](https://tida.alicdn.com/oss_1680155121095_null_dGg9rEhj)

### Determine by API

You need to call the [GetMultiWarehouseBySeller API](<https://open.lazada.com/apps/doc/api?path=%2Fseller%2Fwarehouse%2Fget>) to get the warehouse information of the corresponding seller. If the GetMultiWarehouseBySeller API responds with an array of modules with more than 1 elements, then this means that it is a multiwarehouse seller.
    
    
    {
        "result": {
            "success": true,
            "module": [
                {
                    "code": "dropshipping",
                    "name": "MultiWH",
                    "detailAddress": "20230308 test0011",
                    "needToUpdate": false,
                    "defaultAddress": true,
                    "status": "ACTIVE"
                },
                {
                    "code": "MY10RV7-WH-10002",
                    "name": "ceshis ",
                    "detailAddress": "Kp. Bojong Se.............ndung",
                    "needToUpdate": false,
                    "defaultAddress": false,
                    "status": "ACTIVE"
                }
            ],
            "error_code": {}
        },
        "code": "0",
        "request_id": "2101069616800787642261910"
    }

#### Note

When calling the GetMultiWarehouseBySeller API, please make sure the addressTypes field is filled with "["warehouse"]", this is a required field and failure to fill in this field may result in inaccurate results.