Shopee supports defining variant structures with up to two levels of specifications. The total number of variants cannot exceed 50.

For example, if an item has a color specification, the color is red, or blue, we call this 1-tier variation.

For example, if the product has color and size specifications, color is red, blue, size is L, XL, we call this 2-tier variation.

 

To add variants when creating an item, please refer to the article on [_Creating product_](<https://open.shopee.com/developer-guide/211>).

To manage variants after creating an item, please refer to this article. 

To manage the stock and price of a variation, please refer to the [_Stock and Price Management_](<https://open.shopee.com/developer-guide/223>) article.

# 1\. Adding variants with same tier structure

Scenario 1: The product has already defined color specifications with red and blue colors, now you need to add black for the middle position of option.

Variant situation:

tier_index| option| model_id  
---|---|---  
tier_index[0]| red| 10000  
tier_index[1]  (To be added）| black (To be added）| -  
tier_index[2]| blue| 20000  
  
**API:**[**_v2.product.update_tier_variation_**](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>)**+**[**_v2.product.add_model_**](<https://open.shopee.com/documents/v2/v2.product.add_model?module=89&type=1>)

 

1.1 Call the [_v2.product.update_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>) API to add a black option first

Request example:
    
    
    {
    
        "item_id": 800250275,
    
        "tier_variation": [
    
            {
    
                "name": "Color",
    
                "option_list": [
    
                    {
    
                        "option": "red"
    
                    },
    
                    {
    
                        "option": "black"
    
                    },
    
                   {
    
                        "option": "blue"
    
                    }
    
                ]
    
            }
    
        ],
    
        "model_list": [
    
            {
    
                "tier_index": [0],
    
                "model_id": 10000
    
            },
    
            {
    
                "tier_index": [2],
    
                "model_id": 20000
    
            }
    
        ]
    
    }

 

 

1.2 Call the [_v2.product.add_model_](<https://open.shopee.com/documents/v2/v2.product.add_model?module=89&type=1>) API to add price, stock, SKU information for the black variant:

Request example:
    
    
    {
    
    "item_id": 800250275,
    
    "model_list": [
    
    {
    
    "tier_index": [1],
    
    "original_price": 30,
    
    "model_sku": "sku-black",
    
    "seller_stock": [
    {
    "stock": 300
    }
    ]}]}

# 2.Adding variants that change tier structure

Scenario 2: The product has defined color specifications, the colors are red and blue, now you need to add size specifications, the sizes include L and XL.

 

Original Variant situation:

tier_index| option| model_id  
---|---|---  
tier_index[0]| red| 10000  
tier_index[1]| blue| 20000  
  
 

Variant situation that change after:

tier_index| option| model_id  
---|---|---  
tier_index[0,0]| red,L| -  
tier_index[0,1]| red,XL| -  
tier_index[1,0]| blue,L| -  
tier_index[1,1]| blue,XL| -  
  
 

*Because the tier structure has been changed, the original model information will be removed after calling API: [_v2.product.init_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>),  which means the original model_id: 10000 and model_id: 20000 will be invalid.

 

**API:**[**_v2.product.init_tier_variation_**](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>)** **

Request example:
    
    
    {
    
      "item_id": 100918691,
    
      "tier_variation": [
    
        {
    
          "option_list": [
    
            {
    
              "option": "red"
    
            },
    
            {
    
              "option": "blue"
    
            }
    
          ],
    
          "name": "color"
    
        },
    
        {
    
          "option_list": [
    
            {
    
              "option": "L"
    
            },
    
            {
    
              "option": "XL"
    
            }
    
          ],
    
          "name": "size"
    
        }
    
      ],
    
      "model": [
    
        {
    
          "original_price": 10,
    
          "model_sku": "sku-red-L",
    
          "normal_stock": 100,
    
          "tier_index": [0,0]
    
        },
    
        {
    
          "original_price":20,
    
          "model_sku": "sku-red-XL",
    
          "normal_stock":200,
    
          "tier_index": [0,1]
    
        },
    
        {
    
          "original_price":30,
    
          "model_sku": "sku-blue-L",
    
          "normal_stock":300,
    
          "tier_index": [1,0]
    
        },
    
       {
    
          "original_price":40,
    
          "model_sku": "sku-blue-XL",
    
          "normal_stock":400,
    
          "tier_index": [1,1]
    
        }
    
      ]
    
    }
    

 

# 3.Deleting variants with same tier structure

Scenario 3: The product has defined color specifications with colors red, blue, and black, and now the blue color needs to be deleted.

 

Original variant situation:

tier_index| option| model_id  
---|---|---  
tier_index[0]| red| 10000  
tier_index[1] (To be deleted）| blue  (To be deleted）| 20000  
tier_index[2]| black| 30000  
  
 

Because to delete the blue color, the tier_index can only be tier_index[0], tier_index[1] after deletion, so we need to overwrite the information of the variant at tier_index[1] with the information of the black variant.

 

Variants situation after deletion

tier_index| option| model_id  
---|---|---  
tier_index[0]| red| 10000  
tier_index[1] | black| 30000  
  
 

**API:**[**_v2.product.update_tier_variation_**](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>)**** to remove option and overwrite the model information at the same time.

Request example:
    
    
    {
    
        "item_id": 800250275,
    
        "tier_variation": [
    
            {
    
                "name": "color",
    
                "option_list": [
    
                    {
    
                        "option": "red"
    
                    },  
    
                   {
    
                        "option": "black"
    
                    }
    
                ]
    
            }
    
        ],
    
        "model_list": [
    
            {
    
                "tier_index": [0],
    
                "model_id": 10000
    
            },
    
            {
    
                "tier_index": [1],
    
                "model_id": 30000
    
            }
    
        ]
    
    }

 

Scenario 4: The product has defined color and size specifications, color is red, blue, size is L, XL, and now all the blue variants need to be deleted.

 

Original variant situation

tier_index| option| model_id  
---|---|---  
tier_index[0,0]| red,L| 10000  
tier_index[0,1]| red,XL| 20000  
tier_index[1,0] (To be deleted）| blue,L (To be deleted）| 30000  
tier_index[1,1] (To be deleted）| blue,XL  (To be deleted）| 40000  
  
 

**API:**[**_v2.product.update_tier_variation_**](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>) to delete both option and model information at the same time.

Request example:
    
    
    {
    
        "item_id": 800250275,
    
        "tier_variation": [
    
            {
    
                "name": "color",
    
                "option_list": [
    
                    {
    
                        "option": "red"
    
                    }
    
                ]
    
            },
    
         {
    
                "name": "size",
    
                "option_list": [
    
                  {
    
                        "option": "L"
    
                    },
    
                    {
    
                        "option": "XL"
    
                    }
    
                ]
    
            }
    
        ],
    
        "model_list": [
    
            {
    
                "tier_index": [0,0],
    
                "model_id": 10000
    
            },
    
            {
    
                "tier_index": [0,1],
    
                "model_id": 20000
    
            }
    
        ]
    
    }
    
    

 

Variants situation after deletion

tier_index| option| model_id  
---|---|---  
tier_index[0,0]| red,L| 10000  
tier_index[0,1]| red,XL| 20000  
tier_index[1,0] | -| -  
tier_index[1,1]| -| -  
  
# 4.Deleting variants that change tier structure

Scenario 5: The product has defined color and size specifications, color is red, blue, size is L, XL, and now all colors need to be deleted.

 

Original variant situation:

tier_index| option| model_id  
---|---|---  
tier_index[0,0]| red,L| 10000  
tier_index[0,1]| red,XL| 20000  
tier_index[1,0] | blue,L | 30000  
tier_index[1,1]| blue,XL| 40000  
  
 

Variant situation after deletion:

tier_index| option| model_id  
---|---|---  
tier_index[0]| L| -  
tier_index[1]| XL| -  
  
 

 

**API:**[**_v2.product.init_tier_variation_**](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>)

Request example:
    
    
    {
    
      "item_id": 100918691,
    
      "tier_variation": [
    
        {
    
          "option_list": [
    
            {
    
              "option": "L"
    
            },
    
            {
    
              "option": "XL"
    
            }
    
          ],
    
          "name": "size"
    
      ],
    
      "model": [
    
        {
    
          "original_price": 10,
    
          "model_sku": "sku-L",
    
          "normal_stock": 100,
    
          "tier_index": [0]
    
        },
    
        {
    
          "original_price":20,
    
          "model_sku": "sku-XL",
    
          "normal_stock":200,
    
          "tier_index": [1]
    
        }  ]
    
    }

# 5.Changing the order of variants

Scenario 6: The item has defined color specifications with colors red and blue. Now the color order needs to be changed to blue, red, with the original variant information retained.

 

Original variant situation

tier_index| option| model_id  
---|---|---  
tier_index[0]| red| 10000  
tier_index[1]| blue| 20000  
  
 

Variant situation after change:

tier_index| option| model_id  
---|---|---  
tier_index[0]| blue| 20000  
tier_index[1]| red| 10000  
  
 

**API:**[**_v2.product.update_tier_variation  _**](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>)

Request example:
    
    
    {
    
        "item_id": 800250275,
    
        "tier_variation": [
    
            {
    
                "name": "color",
    
                "option_list": [
    
                    {
    
                        "option": "blue"
    
                    },  
    
                   {
    
                        "option": "red"
    
                    }
    
                ]
    
            }
    
        ],
    
        "model_list": [
    
            {
    
                "tier_index": [0],
    
                "model_id": 20000
    
            },
    
            {
    
                "tier_index": [1],
    
                "model_id": 10000
    
            }
    
        ]
    
    }

# 6.Changing the option name of the variant

 

Scenario 7: The item has defined a color specification with the colors red and blue. Now the color name needs to be changed to red-A, blue.

 

Original variant situation

tier_index| option| model_id  
---|---|---  
tier_index[0]| red| 10000  
tier_index[1]| blue| 20000  
  
Variant situation after change:

tier_index| option| model_id  
---|---|---  
tier_index[0]| red-A| 10000  
tier_index[1]| blue| 20000  
  
 

**API:**[**_v2.product.update_tier_variation_**](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>)** **

Request example:
    
    
    {
    
        "item_id": 800250275,
    
        "tier_variation": [
    
            {
    
                "name": "color",
    
                "option_list": [
    
                    {
    
                        "option": "red-A"
    
                    },  
    
                   {
    
                        "option": "blue"
    
                    }
    
                ]
    
            }
    
        ],
    
        "model_list": [
    
            {
    
                "tier_index": [0],
    
                "model_id": 10000
    
            },
    
            {
    
                "tier_index": [1],
    
                "model_id": 20000
    
            }
    
        ]
    
    }

# Summary

1.The function of [_v2.product.init_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>) API, including changing 0-tier variation to 1-tier variation / 0-tier variation to 2-tier variation / 1-tier variation to 2-tier variation / 2-tier variation to 1-tier variation.

2.The function of [_v2.product.update_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>) API, including add/delete/update the options, If you still need to keep the original variants information, please use the model_list field.

3\. The function of [_v2.product.add_model_](<https://open.shopee.com/documents/v2/v2.product.add_model?module=89&type=1>) API is adding the new model information, the function of  [_v2.product.delete_model_](<https://open.shopee.com/documents/v2/v2.product.delete_model?module=89&type=1>) API is deleting the variant information.

4\. Sellers who have upgraded CNSC and KRSC can only add/delete variants through global products, so please use the global product API for management, otherwise an error will be reported.

Global Product API| Product API  
---|---  
[ _v2.global_product.init_tier_variation_](<https://open.shopee.com/documents/v2/v2.global_product.init_tier_variation?module=90&type=1>)| [ _v2.product.init_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>)  
[ _v2.global_product.update_tier_variation_](<https://open.shopee.com/documents/v2/v2.global_product.update_tier_variation?module=90&type=1>)| [ _v2.product.update_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.update_tier_variation?module=89&type=1>)  
[ _v2.global_product.add_global_model_](<https://open.shopee.com/documents/v2/v2.global_product.add_global_model?module=90&type=1>)| [ _v2.product.add_model_](<https://open.shopee.com/documents/v2/v2.product.add_model?module=89&type=1>)  
[ _v2.global_product.delete_global_model_](<https://open.shopee.com/documents/v2/v2.global_product.delete_global_model?module=90&type=1>)| [ _v2.product.delete_model_](<https://open.shopee.com/documents/v2/v2.product.delete_model?module=89&type=1>)