# 1、GetProductItemupgrade

PATH: /product/item/get

## 1.1 Request Parameters

No change

## 1.2 Response Parameters

### 1.2.1 Explain

Level1 | Level2 | Level3 | Level4 | Description  
---|---|---|---|---  
data | variation | Variation1 | name | Sales attribute names, such as color family, size, etc.Form a ref relationship with "color_family" in the sku below.  
|  |  | hasImage | Sales attribute image settings, Only Variation1 Can set hasImage to true  
|  |  | customize | Whether to customize sales attributes  
|  |  | options | List of sales attribute value names  
|  | Variation2 | name |   
|  |  | hasImage |   
|  |  | customize |   
|  |  | options |   
  
|   
| Variation3 | name | Very few cases will set this property. This attribute is not available for most categories  
  
|   
|   
| hasImage |   
  
  
|   
|   
| customize |   
  
  
|   
|   
| options |   
  
  
|   
| Variation4 | name | Very few cases will set this property. This attribute is not available for most categories  
  
|   
|   
| hasImage |   
  
  
|   
|   
| customize |   
  
  
|   
|   
| options |   
  
  
  


### 1.2.2 DEMO

#### CASE1

Custom sales attributes (1) + Standard sales attributes (1) + SKU pictures
    
    
    {
      "data": {
        "created_time": "1626242071000",
        "updated_time": "1626763060000",
        "images": [
          "https://sg-live-02.slatic.net/p/0ef9e15ad696adfc43333c646eec2ec4.jpg"
        ],
        "skus": [
          {
            "Status": "active",
            "quantity": 1,
            "Images": [
              "https://sg-live-02.slatic.net/p/42447e6aea05ea21f49f4f608b20b656.jpg"
            ],
            "SellerSku": "1884392091-1626242071365-0",
            "ShopSku": "1884392091_SGAMZ-10044238042",
            "Url": "https://www.lazada.sg/-i1884392091-s10044238042.html",
            "multiWarehouseInventories": [
              {
                "occupyQuantity": 0,
                "quantity": 1,
                "totalQuantity": 1,
                "withholdQuantity": 0,
                "warehouseCode": "dropshipping",
                "sellableQuantity": 1
              }
            ],
            "package_width": "1.00",
            "saleProp":{
              "color_family": "Maroon"
            },
            "package_height": "1.00",
            "fblWarehouseInventories": [],
            "special_price": 0.0,
            "price": 1000.0,
            "package_length": "1.00",
            "EditableQuantity": 1,
            "package_weight": "1",
            "Available": 1,
            "SkuId": 10044238042,
            "CustomProp1": "CustomOption1"
          },
          {
            "Status": "active",
            "quantity": 1,
            "Images": [
              "https://sg-live-02.slatic.net/p/0ef9e15ad696adfc43333c646eec2ec4.jpg"
            ],
            "SellerSku": "1884392091-1626242071365-1",
            "ShopSku": "1884392091_SGAMZ-10044238043",
            "Url": "https://www.lazada.sg/-i1884392091-s10044238043.html",
            "multiWarehouseInventories": [
              {
                "occupyQuantity": 0,
                "quantity": 1,
                "totalQuantity": 1,
                "withholdQuantity": 0,
                "warehouseCode": "dropshipping",
                "sellableQuantity": 1
              }
            ],
            "package_width": "1.00",
            "saleProp":{
              "color_family": "Maroon"
            },
            "package_height": "1.00",
            "fblWarehouseInventories": [],
            "special_price": 0.0,
            "price": 1000.0,
            "package_length": "1.00",
            "EditableQuantity": 1,
            "package_weight": "1",
            "Available": 1,
            "SkuId": 10044238043,
            "CustomProp1": "CustomOption2"
          }
        ],
        "item_id": 1884392091,
        "primary_category": 6583,
        "attributes": {
          "name": "Test Api Self Define Attributes By Boyan 0714001",
          "description": "<p style=\"margin: 0;\"><span style=\"font-family: none;\"></span></p>",
          "brand": "No Brand",
          "source": "asc",
          "delivery_option_sof": "0"
        },
        "variation": {
          "Variation1": {
            "name": "CustomProp1",
            "label": "CustomProp1",
            "hasImage": true,
            "customize": true,
            "options": [
              "CustomOption2",
              "CustomOption1"
            ]
          },
          "Variation2": {
            "name": "color_family",
            "label": "Color Family",
            "hasImage": false,
            "customize": false,
            "options": [
              "Maroon"
            ]
          }
        }
      },
      "code": "0",
      "request_id": "0be6f58116276233235264430"
    }

  


#### CASE2

All standard sales attributes (2)
    
    
    {
      "data": {
        "created_time": "1626764445000",
        "updated_time": "1626869157000",
        "images": [
          "https://sg-live.slatic.net/p/42447e6aea05ea21f49f4f608b20b656.jpg"
        ],
        "skus": [
          {
            "Status": "active",
            "quantity": 1,
            "Images": [],
            "SellerSku": "1901875545-1626764445757-0",
            "ShopSku": "1901875545_SGAMZ-10164106501",
            "Url": "https://www.lazada.sg/-i1901875545-s10164106501.html",
            "multiWarehouseInventories": [
              {
                "occupyQuantity": 0,
                "quantity": 1,
                "totalQuantity": 1,
                "withholdQuantity": 0,
                "warehouseCode": "dropshipping",
                "sellableQuantity": 1
              }
            ],
            "package_width": "1.00",
            "saleProp":{
              "size": "34",
              "color_family": "red"
            },
            "package_height": "1.00",
            "fblWarehouseInventories": [],
            "special_price": 0.0,
            "price": 1000.0,
            "package_length": "1.00",
            "EditableQuantity": 1,
            "package_weight": "1",
            "Available": 1,
            "SkuId": 10164106501
          },
          {
            "Status": "active",
            "quantity": 2,
            "Images": [],
            "SellerSku": "1901875545-1626764445757-2",
            "ShopSku": "1901875545_SGAMZ-10164106503",
            "Url": "https://www.lazada.sg/-i1901875545-s10164106503.html",
            "multiWarehouseInventories": [
              {
                "occupyQuantity": 0,
                "quantity": 2,
                "totalQuantity": 2,
                "withholdQuantity": 0,
                "warehouseCode": "dropshipping",
                "sellableQuantity": 2
              }
            ],
            "package_width": "1.00",
            "saleProp":{
              "size": "34",
              "color_family": "Blue"
            },
            "package_height": "1.00",
            "fblWarehouseInventories": [],
            "special_price": 0.0,
            "price": 1000.0,
            "package_length": "1.00",
            "EditableQuantity": 2,
            "package_weight": "1",
            "Available": 2,
            "SkuId": 10164106503
          },
          {
            "Status": "active",
            "quantity": 1,
            "Images": [],
            "SellerSku": "1901875545-1626764445757-1",
            "ShopSku": "1901875545_SGAMZ-10164106502",
            "Url": "https://www.lazada.sg/-i1901875545-s10164106502.html",
            "multiWarehouseInventories": [
              {
                "occupyQuantity": 0,
                "quantity": 1,
                "totalQuantity": 1,
                "withholdQuantity": 0,
                "warehouseCode": "dropshipping",
                "sellableQuantity": 1
              }
            ],
            "package_width": "1.00",
            "saleProp":{
              "size": "38",
              "color_family": "Red"
            },
            "package_height": "1.00",
            "fblWarehouseInventories": [],
            "special_price": 0.0,
            "price": 1000.0,
            "package_length": "1.00",
            "EditableQuantity": 1,
            "package_weight": "1",
            "Available": 1,
            "SkuId": 10164106502
          },
          {
            "Status": "active",
            "quantity": 1,
            "Images": [],
            "SellerSku": "1901875545-1626764445757-3",
            "ShopSku": "1901875545_SGAMZ-10164106504",
            "Url": "https://www.lazada.sg/-i1901875545-s10164106504.html",
            "multiWarehouseInventories": [
              {
                "occupyQuantity": 0,
                "quantity": 1,
                "totalQuantity": 1,
                "withholdQuantity": 0,
                "warehouseCode": "dropshipping",
                "sellableQuantity": 1
              }
            ],
            "package_width": "1.00",
            "saleProp":{
              "size": "38",
              "color_family": "Blue"
            },
            "package_height": "1.00",
            "fblWarehouseInventories": [],
            "special_price": 0.0,
            "price": 1000.0,
            "package_length": "1.00",
            "EditableQuantity": 1,
            "package_weight": "1",
            "Available": 1,
            "SkuId": 10164106504
          }
        ],
        "item_id": 1901875545,
        "primary_category": 6583,
        "attributes": {
          "name": "Test API Self Define Attributes By Boyan 002",
          "description": "<p style=\"margin: 0;\"><span style=\"font-family: none;\"></span></p>",
          "brand": "No Brand",
          "source": "asc",
          "delivery_option_sof": "0"
        },
        "variation": {
          "Variation1": {
            "name": "color_family",
            "label": "Color Family",
            "hasImage": false,
            "customize": false,
            "options": [
              "Red",
              "Blue"
            ]
          },
          "Variation2": {
            "name": "Size",
            "label": "size",
            "hasImage": false,
            "customize": false,
            "options": [
              "34",
              "38"
            ]
          }
        }
      },
      "code": "0",
      "request_id": "0be6f58116276233682554431"
    }

# 2.CreateProduct

PATH: /product/create

  


## 2.1 Request Parameters

### 2.1.1 Explain

Level1 | Level2 | Level3 | Level4 | Description  
---|---|---|---|---  
data | variation | Variation1 | name | Sales attribute names, such as color family, size, etc.Form a ref relationship with "color_family" in the sku below.  
|  |  | hasImage | Sales attribute image settings, Only Variation1 Can set hasImage to true  
|  |  | customize | Whether to customize sales attributes  
|  |  | options | List of sales attribute value names  
|  | Variation2 | name |   
|  |  | hasImage |   
|  |  | customize |   
|  |  | options |   
  
|   
| Variation3 | name | Very few cases will set this property. This attribute is not available for most categories  
  
|   
|   
| hasImage |   
  
  
|   
|   
| customize |   
  
  
|   
|   
| options |   
  
  
|   
| Variation4 | name | Very few cases will set this property. This attribute is not available for most categories  
  
|   
|   
| hasImage |   
  
  
|   
|   
| customize |   
  
  
|   
|   
| options |   
  
| skus | Variation1-name | Variation1-options[i] | Reference the name and option of the variation declaration as the sales attribute and sales attribute valueThe name field of Variation1/Variation2/Variation3/Variation4An option element of Variation1/Variation2Variation3/Variation4  
  
### 2.1.2 Error

Error Code | Error Message  
---|---  
VARIATION_CATEGORY_PROHIBITION | The category is banned from using variation function.  
REMOVE_SKU_PROHIBITION | The seller is prohibited from using the remove SKU function.  
VARIATION_SELLER_PROHIBITION | The seller is prohibited from using the variation function.  
VARIATION_EMPTY | The Variation is Empty  
VARIATION_SIZE_LIMIT | The Variations Size Exceeds Maximum Size Limit, The Size Limit is: 2.   
VARIATION_CONTENT_EMPTY | The Variation Content is Empty, The Variation Node is: __VariationX__  
VARIATION_NAME_EMPTY | The Variation Name is Empty, The Variation Node is: __VariationX__  
VARIATION_IMAGE_MUST_SET_VARIATION1 | Only Variation1 Can set hasImage to true, The Variation Node is: __VariationX__  
VARIATION_NAME_DUPLICATE | The Variation Name Is Duplicate, The Variation Node is: __VariationX__ , The Duplicate Name is: __nameX__  
VARIATION_NAME_LENGTH_LIMIT | The Variation Name's Content Exceeds Maximum Length Limit, The Variation Node is: __VariationX__ , The Length Limit is: 15, The Name is: __nameX__  
VARIATION_OPTIONS_EMPTY | The Variation Options Is Empty, The Variation Node is: __VariationX__  
OPTIONS_SIZE_LIMIT | The Variation Options Exceeds Maximum Size Limit, The Variation Node is: __VariationX__ , The Size Limit is: 50, The Name is: __nameX__  
VARIATION_OPTION_EMPTY | The Variation Option Is Empty, The Variation Node is: __VariationX__  
VARIATION_OPTION_LENGTH_LIMIT | The Variation Name's Content Exceeds Maximum Length Limit, The Variation Node is: __VariationX__ , The Length Limit is: 20, The Option is: optionX;  
VARIATION_OPTION_DUPLICATE | The Variation Option Is Duplicate, The Variation Node is: __VariationX__ , The Duplicate Option is: __optionX, optionX__  
VARIATION_IMAGE_SETTING_ERROR | There is No HasImage Set In The __VariationX__ , But Images Are Found In The SKU: " + sellerSKU  
SKU_VARIATION_OPTION_NOT_EXIST | The SKU Variation Option is Not Exist, The SellerSKU is： __SellerSkuX__ , The SKU Variation Name is: __nameX__ , The SKU Variation Option is: __optionX__  
SKU_VARIATION_NAME_MISSING | The SKU Variation Name is Missing, The SellerSKU is：is： __SellerSkuX__ , The Missing SKU Variation Name is: __nameX__  
SKU_VARIATION_IMAGES_MISSING | The Variation set hasImage true, But The SKU Not Found Images. The SellerSKU is: __SellerSkuX__ , The Variation Name is: __nameX__  
VARIATION_CATEGORY_SIZE_IMAGE | When size is passed in as a standard category attribute, it is not allowed to set hasImage true.  
VARIATION_CATEGORY_ATTRIBUTE_INVALID | This attribute __nameX__ is not found in the category attribute library.  
  
  


### 2.1.3 DEMO

#### CASE1

Create products with standard sales attributes

  

    
    
    {
        "Request": {
            "Product": {
                "PrimaryCategory": "10002019",
                "Images": {
                    "Image": [
                        "https://test.jpg",
                        "https://test1.jpg"
                    ]
                },
                "variation": {
                    "variation1": {
                        "name": "color_family",
                        "hasImage": true,
                        "customize": false,
                        "options": {
                            "option": [
                                "test"
                            ]
                        }
                    }
                },
                "Attributes": {
                    "name": "test product",
                    "description": "test description",
                    "brand": "No Brand",
                    "model": "test",
                    "warranty_type": "Local seller warranty",
                    "warranty": "1 Month",
                    "short_description": "test short description",
                    "Hazmat": "None",
                    "material": "Leather",
                    "laptop_size": "11 - 12 inches",
                    "delivery_option_sof": "No"
                },
                "Skus": {
                    "Sku": [
                        {
                            "SellerSku": "chase test 8",
                            "quantity": "3",
                            "price": "35",
                            "saleProp":{
                                            "color_family": "test"
                                            },
                            "package_height": "10",
                            "package_length": "10",
                            "package_width": "10",
                            "package_weight": "0.5",
                            "package_content": "laptop bag",
                            "Images": {
                                "Image": [
                                    "https://test.jpg"
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

  


#### CASE2

Standard sales attributes (1) + custom sales attributes (1)
    
    
    {
        "Request": {
            "Product": {
                "PrimaryCategory": "10002019",
                "Images": {
                    "Image": [
                        "https://test1.jpg",
                        "https://test2.jpg"
                    ]
                },
                "variation": {
                    "variation1": {
                        "name": "color_family",
                        "hasImage": true,
                        "customize": false,
                        "options": {
                            "option": [
                                "test"
                            ]
                        }
                    },
                    "variation2": {
                        "name": "test prop",
                        "hasImage": false,
                        "customize": true,
                        "options": {
                            "option": [
                                "test custom"
                            ]
                        }
                    }
                },
                "Attributes": {
                    "name": "test product",
                    "description": "test description",
                    "brand": "No Brand",
                    "model": "test",
                    "warranty_type": "Local seller warranty",
                    "warranty": "1 Month",
                    "short_description": "test short description",
                    "Hazmat": "None",
                    "material": "Leather",
                    "laptop_size": "11 - 12 inches",
                    "delivery_option_sof": "No"
                },
                "Skus": {
                    "Sku": [
                        {
                            "SellerSku": "chase test 81",
                            "quantity": "3",
                            "price": "35",
                            "saleProp":{
                                            "color_family": "test",
                              "test prop": "test custom"
                                            },
                            "package_height": "10",
                            "package_length": "10",
                            "package_width": "10",
                            "package_weight": "0.5",
                            "package_content": "laptop bag",
                            "Images": {
                                "Image": [
                                    "https://test.jpg"
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

  


## 2.2 Response Parameters

No change

  


  


# 3\. UpdateProduct

PATH: /product/update

  


## 3.1 Request Parameters

### 3.1.1Explain

Level1 | Level2 | Level3 | Level4 | Description  
---|---|---|---|---  
data | variation | Variation1 | name | Sales attribute names, such as color family, size, etc.Form a ref relationship with "color_family" in the sku below.  
|  |  | hasImage | Sales attribute image settings, Only Variation1 Can set hasImage to true  
|  |  | customize | Whether to customize sales attributes  
|  |  | options | List of sales attribute value names  
|  | Variation2 | name |   
|  |  | hasImage |   
|  |  | customize |   
|  |  | options |   
  
|   
| Variation3 | name | Very few cases will set this property. This attribute is not available for most categories  
  
|   
|   
| hasImage |   
  
  
|   
|   
| customize |   
  
  
|   
|   
| options |   
  
  
|   
| Variation4 | name | Very few cases will set this property. This attribute is not available for most categories  
  
|   
|   
| hasImage |   
  
  
|   
|   
| customize |   
  
  
|   
|   
| options |   
  
| skus | Variation1-name | Variation1-options[i] | Reference the name and option of the variation declaration as the sales attribute and sales attribute valueThe name field of Variation1/Variation2/Variation3/Variation4An option element of Variation1/Variation2Variation3/Variation4  
  
### 3.1.2 Error

Error Code | Error Message  
---|---  
VARIATION_CATEGORY_PROHIBITION | The category is banned from using variation function.  
REMOVE_SKU_PROHIBITION | The seller is prohibited from using the remove SKU function.  
VARIATION_SELLER_PROHIBITION | The seller is prohibited from using the variation function.  
VARIATION_EMPTY | The Variation is Empty  
VARIATION_SIZE_LIMIT | The Variations Size Exceeds Maximum Size Limit, The Size Limit is: __2__.   
VARIATION_CONTENT_EMPTY | The Variation Content is Empty, The Variation Node is: __VariationX__  
VARIATION_NAME_EMPTY | The Variation Name is Empty, The Variation Node is: __VariationX__  
VARIATION_IMAGE_MUST_SET_VARIATION1 | Only Variation1 Can set hasImage to true, The Variation Node is: __VariationX__  
VARIATION_NAME_DUPLICATE | The Variation Name Is Duplicate, The Variation Node is: __VariationX__ , The Duplicate Name is: __nameX__  
VARIATION_NAME_LENGTH_LIMIT | The Variation Name's Content Exceeds Maximum Length Limit, The Variation Node is: __VariationX__ , The Length Limit is: 15, The Name is: __nameX__  
VARIATION_OPTIONS_EMPTY | The Variation Options Is Empty, The Variation Node is: __VariationX__  
OPTIONS_SIZE_LIMIT | The Variation Options Exceeds Maximum Size Limit, The Variation Node is: __VariationX__ , The Size Limit is: 50, The Name is: __nameX__  
VARIATION_OPTION_EMPTY | The Variation Option Is Empty, The Variation Node is: __VariationX__  
VARIATION_OPTION_LENGTH_LIMIT | The Variation Name's Content Exceeds Maximum Length Limit, The Variation Node is: __VariationX__ , The Length Limit is: 20, The Option is: optionX;  
VARIATION_OPTION_DUPLICATE | The Variation Option Is Duplicate, The Variation Node is: __VariationX__ , The Duplicate Option is: __optionX, optionX__  
VARIATION_IMAGE_SETTING_ERROR | There is No HasImage Set In The __VariationX__ , But Images Are Found In The SKU: " + sellerSKU  
SKU_VARIATION_OPTION_NOT_EXIST | The SKU Variation Option is Not Exist, The SellerSKU is： __SellerSkuX__ , The SKU Variation Name is: __nameX__ , The SKU Variation Option is: __optionX__  
SKU_VARIATION_NAME_MISSING | The SKU Variation Name is Missing, The SellerSKU is：is： __SellerSkuX__ , The Missing SKU Variation Name is: __nameX__  
SKU_VARIATION_IMAGES_MISSING | The Variation set hasImage true, But The SKU Not Found Images. The SellerSKU is: __SellerSkuX__ , The Variation Name is: __nameX__  
VARIATION_CATEGORY_SIZE_IMAGE | When size is passed in as a standard category attribute, it is not allowed to set hasImage true.  
VARIATION_CATEGORY_ATTRIBUTE_INVALID | This attribute __nameX__ is not found in the category attribute library.  
  
  


### 3.1.3 DEMO

#### CASE1

No declaration of Variation + new SKU + no SKU picture (except for products containing custom sales attributes);

If you want to add a seller SKU to an existing product, you can refer to the example below；

AssociatedSku: One of the seller SKUs in the target product.

For Example:

If you want to add a C sku to product B, then the value of AssociatedSKU should be filled with A, and A is the seller SKU of product B.
    
    
    {
        "Request": {
            "Product": {
                "ItemId": "2378974109",
                "AssociatedSku": "chase test 8",
                "Attributes":"",
                "Skus": {
                    "Sku": [
                        {
                            "SkuId": "32523532543",
                            "quantity": "3",
                            "price": "35",
                            "saleProp":{
                                            "color_family": "test"
                                            },
                            "package_height": "10",
                            "package_length": "10",
                            "package_width": "10",
                            "package_weight": "0.5",
                            "package_content": "laptop bag"
                        }
                    ]
                }
            }
        }
    }

#### CASE2

No declaration of Variation + modification of standard sales attribute value + no SKU picture, Red -> Green

  

    
    
    {
        "Request": {
            "Product": {
                "ItemId": "2378974109",
                "Attributes": "",
                "Skus": {
                    "Sku": [
                        {
                            "SkuId": "32523532543",
                            "quantity": "3",
                            "price": "35",
                            "saleProp":{
                                            "color_family": "green"
                                            },
                            "package_height": "10",
                            "package_length": "10",
                            "package_width": "10",
                            "package_weight": "0.5",
                            "package_content": "laptop bag"
                        }
                    ]
                }
            }
        }
    }

  


#### CASE3

Declare Variation + Add custom sales attributes + No SKU image
    
    
    {
        "Request": {
            "Product": {
                "ItemId": "2378974109",
                "Attributes": "",
                "variation": {
                    "variation1": {
                        "name": "color_family",
                        "hasImage": false,
                        "customize": false,
                        "options": {
                            "option": ["red"]
                        }
                    },
                    "variation2": {
                        "name": "customProp1",
                        "hasImage": false,
                        "customize": true,
                        "options": {
                            "option": ["customOption1"]
                        }
                    }
                },
                "Skus": {
                    "Sku": [
                        {
                            "SkuId": "32523532543",
                            "quantity": "3",
                            "price": "35",
                            "saleProp":{
                                            "customProp1": "customOption1",
                              "color_family": "red"
                                            },
                            "package_height": "10",
                            "package_length": "10",
                            "package_width": "10",
                            "package_weight": "0.5",
                            "package_content": "laptop bag"
                        }
                    ]
                }
            }
        }
    }

## 3.2 Response Parameters

No change

  


  


# 4\. RemoveSKU

PATH: /product/sku/remove

  


## 4.1 Request Parameters

### 4.1.1 Explain

Level1 | Level2 | Level3 | Level4 | Description  
---|---|---|---|---  
| ItemId |  |  | Product ID that needs to be deleted  
data | variation | Variation1 | name | Sales attributes that need to be deleted  
|  | Variation2 | name | Sales attributes that need to be deleted  
  
|   
| Variation3 | name | Sales attributes that need to be deleted  
  
|   
| Variation4 | name | Sales attributes that need to be deleted  
  
|   
| SellerSku |   
| Sellersku that need to be deleted  
  
  


### 4.1.2 DEMO

#### CASE1

Delete SKU
    
    
    <Request>
        <Product>
            <ItemId>2369252345</ItemId>
            <Skus>
                <Sku>
                    <SkuId>1655712716757</SkuId>
                </Sku>
            </Skus>
        </Product>
    </Request>

  


#### CASE2

Delete standard sales attributes
    
    
    <Request>
        <Product>
            <ItemId>2378950489</ItemId>
            <variation>
                <variation1>
                    <name>color_family</name>
                </variation1>
            </variation>
            <Skus>
                <Sku>
                </Sku>
            </Skus>
        </Product>
    </Request>

#### CASE3

Delete custom sales attributes
    
    
    <Request>
        <Product>
            <ItemId>1911687838</ItemId>
            <variation>
                <variation1>
                    <name>CustomProp1</name>
                </variation1>
            </variation>
            <Skus>
                <Sku></Sku>
            </Skus>
        </Product>
    </Request>

#### CASE4

Delete sales attributes & delete SKU
    
    
    <Request>
        <Product>
            <ItemId>1911687838</ItemId>
            <variation>
                <variation1>
                    <name>color_family</name>
                </variation1>
            </variation>
            <Skus>
                <Sku>
                    <SkuId>1655712716757</SkuId>
                </Sku>
            </Skus>
        </Product>
    </Request>

  


## 4.2 Response Parameters

### 4.2.1 ERROR

Error Code | Error Message  
---|---  
REMOVE_SKU_PROHIBITION | The seller is prohibited from using the remove SKU function.  
SALE_PROPS_DUPLICATE | Sale props is duplicate between sellerSku: __sellerSku1__ and sellerSku: __sellerSku2__  
SALE_PROPS_EMPTY | Sale props can not be set empty when remove sale props  
SALE_PROPS_EMPTY | Sale props of the product id: __9999999__ is 0, can not remove  
CAN_NOT_REMOVE_ALL_SKU | Can not remove all sku  
SELLER_SKU_NOT_FOUND | sellerSku: __SellerSkuX__ not found  
  
### 4.2.3 DEMO
    
    
    {
      "code": "0",
      "request_id": "21411c9216560609727832359"
    }