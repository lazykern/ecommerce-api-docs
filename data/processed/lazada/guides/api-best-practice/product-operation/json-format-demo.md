# APP Grayscale Time Schedule List:

batch | Starting time | gray scale（%）  
---|---|---  
first batch | 2022.4.13 | 5  
second batch | 2022.4.18 | 20  
The third batch | 2022.4.20 | 50  
fourth batch | 2022.4.25 | 100  
  
  


# The list of supported APIs is as follows：

API Titel | API Path  
---|---  
[CreateProduct](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fcreate>) | /product/create  
[UpdateProduct](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fupdate>) | /product/update  
[UpdatePriceQuantity](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fprice_quantity%2Fupdate>) | /product/price_quantity/update  
[SetImages](<https://open.lazada.com/apps/doc/api?path=%2Fimages%2Fset>) | /images/set  
[DeactivateProduct](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fdeactivate>) | /product/deactivate  
  
  


# 1、CreateProduct API payload demo
    
    
    {
        "Request": {
            "Product": {
                "PrimaryCategory": "10002019",
                "Images": {
                  //must be in array type
                    "Image": [
                        "https://sg-live-02.slatic.net/p/357*****ee06.jpg",
                        "https://sg-live-02.slatic.net/p/f16*****b0.png",
                        "https://sg-live-02.slatic.net/p/17559****ded4.jpg",
                        "https://sg-live-02.slatic.net/p/33a7*****8fb.jpg",
                        "https://sg-live-02.slatic.net/p/04****f6dd0.jpg",
                        "https://sg-live-02.slatic.net/p/f39****c8d48.jpg",
                        "https://sg-live-02.slatic.net/p/c4b****e43e.jpg",
                        "https://sg-live-02.slatic.net/p/5d42****d7.jpg"
                    ]
                },
                "Attributes": {
                    "name": "test product",
                    "description": "test description",         
                    "brand": "No Brand",
                    "model": "test",
                    "waterproof": "Waterproof",
                    "warranty_type": "Local seller warranty",
                    "warranty": "1 Month",
                    "short_description": "",
                    "Hazmat": "None",
                    "material": "Leather",
                    "laptop_size": "11 - 12 inches",
                    "delivery_option_express": "Yes",
                    "Delivery_Option_Instant": "Yes",
                    "delivery_option_economy": "Yes",
                    "delivery_option_standard": "YES",
                    "delivery_option_sof": "No"
                },
                "Skus": {
                  //must be in array type
                    "Sku": [
                        {
                            "SkuId": "234523151512",
                            "quantity": "3",
                            "price": "35",
                            "package_height": "10",
                            "package_length": "10",
                            "package_width": "10",
                            "package_weight": "0.5",
                            "package_content": "laptop bag",
                            "Images": {
                              //must be in array type
                                "Image": [
                                    "https://sg-live-02.slatic.net/p/3d****e.jpg"
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

# 2、UpdateProduct API payload demo
    
    
    {
        "Request": {
            "Product": {
                "PrimaryCategory": "10002019",
                "ItemId": "2096962270",
                "Images": {
                  //must be in array type
                    "Image": [
                        "https://sg-live-02.slatic.net/p/35****06.jpg",
                        "https://sg-live-02.slatic.net/p/f16*****7b0.png"
                    ]
                },
                "Attributes": {
                    "name": "test product",
                    "description": "test description",
                    "brand": "No Brand",
                    "model": "test",
                    "waterproof": "Waterproof",
                    "warranty_type": "Local seller warranty",
                    "warranty": "1 Month",
                    "short_description": "test description",
                    "Hazmat": "None",
                    "material": "Leather",
                    "laptop_size": "11 - 12 inches",
                    "delivery_option_express": "Yes",
                    "Delivery_Option_Instant": "Yes",
                    "delivery_option_economy": "Yes",
                    "delivery_option_standard": "YES",
                    "delivery_option_sof": "No"
                },
                "Skus": {
                  //must be in array type
                    "Sku": [
                        {
                            "SkuId": "234523151512",
                            "quantity": "3",
                            "price": "35",
                            "package_height": "10",
                            "package_length": "10",
                            "package_width": "10",
                            "package_weight": "0.5",
                            "package_content": "laptop bag",
                            "Images": {
                                "Image": [
                                    "https://sg-live-02.slatic.net/p/3d93****8f52e.jpg"
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

# 3、UpdatePriceQuantity API payload demo

## 3.1、single warehouse seller
    
    
    {
        "Request": {
            "Product": {
                "Skus": {
                  //If you need to update multiple SKUs, the attribute must be an array type
                    "Sku": {
                        "ItemId": "1742512445",
                        "SkuId": "11781189655",
                        "SellerSku": "4240kyfd",
                        "Price": "878.00",
                        "SalePrice": "666.00",
                        "SaleStartDate": "2021-11-11",
                        "SaleEndDate": "2021-12-12"
                    }
                }
            }
        }
    }

## 3.2、Multiple warehouse sellers
    
    
    {
        "Request": {
            "Product": {
                "Skus": {
                  //If you need to update multiple SKUs, the attribute must be an array type
                    "Sku": {
                        "ItemId": "2053125344",
                        "SkuId": "11260762907",
                        "SellerSku": "61f951testdcdc",
                        "Price": "1099.00",
                        "SalePrice": "900.00",
                        "SaleStartDate": "2017-08-08",
                        "SaleEndDate": "2021-08-31",
                        "MultiWarehouseInventories": {
                            "MultiWarehouseInventory": [
                                {
                                    "WarehouseCode": "123456",
                                    "Quantity": "20"
                                },
                                {
                                    "WarehouseCode": "789",
                                    "Quantity": "30"
                                }
                            ]
                        }
                    }
                }
            }
        }
    }

# 4、SetImages API payload demo
    
    
    {
        "Request": {
            "Product": {
                "Skus": {
                    //must be an array type
                    "Sku": [
                        {
                            "SkuId": "234523151512",
                            "Images": {
                                //must be an array type
                                "Image": [
                                    "https://sg-live-02.slatic.net/p/e72c0a29206032ea64fced6eb566084f.jpg"
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

# 5、DeactivateProduct API payload demo
    
    
    {
      "Request": {
        "Product": {
          "ItemId": 3865707451,
          "Skus": {
            "SkuId": [
              22332218421,
              22332218422
            ]
          }
        }
      }
    }