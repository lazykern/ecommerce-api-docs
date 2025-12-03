This document is used to introduce the getting, API usage and considerations related to product categories

# 1、GetCategoryTree

This API is used to get the complete category tree of Lazada

## Field Description

Field Name| Field Description  
---|---  
children| List of subcategories of the current category ID  
name| Category Name  
leaf| Determine if the category is a leaf category, only leaf categories can be used to create products  
category_id| The ID of the current category, used when creating products or getting category attributes  
  
## Sample response
    
    
    {
        "data": [
            {
                "children": [
                    {
                        "var": false,
                        "name": "Smartphones",
                        "leaf": true,
                        "category_id": 3
                    },
                    {
                        "var": false,
                        "name": "Tablets",
                        "leaf": true,
                        "category_id": 7
                    },
                    {
                        "var": false,
                        "name": "Landline Phones",
                        "leaf": true,
                        "category_id": 49
                    },
                    {
                        "var": false,
                        "name": "Feature Phones",
                        "leaf": true,
                        "category_id": 42006401
                    }
                ],
                "var": false,
                "name": "Mobiles & Tablets",
                "leaf": false,
                "category_id": 2
            }
          ......
        ]
    }

  


## Sample Analysis

Lazada's product categories are tree-structured, and only leaf nodes can be used to create products. You cannot use branch nodes to create products.

In the sample "leaf = false" means a branch node, a children represents a branch, and a category may have multiple branches.

![image](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/18857002/1655882736301-837d3606-d84a-4ca1-b243-a36f2931aaa4.png)

# 2、GetCategoryAttributes

Use the category ID obtained in the GetCategoryTree API to find the available or required attributes of the target category.

## Field Description

Field Name| Field Description  
---|---  
is_key_prop| If it is 1, it means that this attribute is a key attribute, and the product score will be improved after filling in  
is_sale_prop| If it is 1, it indicates that this attribute is a standard sales/variant attribute  
name| Attribute name.As an attribute name, it must be in English.As an option name, it may respond to the local language depending on the "language_code" of the request.  
input_type| The type of value that can be entered for this attribute1: singleselect: single selection does not support customization2: multiselect: multiselect does not support customization3: enuminput: single choice supports customization4: multienuminput: multi selection supports customization5: text: text can be customized6: numeric: the value can be customized7: date: date can be customized8: richText: rich text can be customized9: img: pictures can be customized  
options| Available options for enumerating attributes of type  
en_name| Option name, this field must be in English, if you need to fill in the enumeration when creating a product please use the value of this field  
is_mandatory| If it is 1, it means that this attribute is required  
attribute_type| If the value is "normal", this attribute should be filled in the "Attribute" field when creating or updating the product.If the value is "sku", this attribute should be filled in the "Sku" field when creating or updating the product.  
label| Name of the field displayed in the seller center (this field cannot be used when creating or updating)  
  
## Example of seller center display

![image](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/18857002/1656311216964-c5ec31cf-f247-48aa-a8ea-16fea3ba6635.png)

## Sample response
    
    
    {
      "data": [
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "description",
          "input_type": "richText",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Long Description (Lorikeet)",
          "id": 100005530
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "short_description",
          "input_type": "richText",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Short Description",
          "id": 100005505
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "name",
          "input_type": "text",
          "options": [],
          "is_mandatory": 1,
          "attribute_type": "normal",
          "label": "Name",
          "id": 100005571
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "video",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Video URL",
          "id": 100005577
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "__images__",
          "input_type": "img",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "Images",
          "id": 40000
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "color_thumbnail",
          "input_type": "img",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "Color Thumbnail",
          "id": 100007607
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "phone_type",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Smartphone",
              "en_name": "Smartphone",
              "id": 21416
            },
            {
              "name": "feature phone",
              "en_name": "feature phone",
              "id": 106474
            }
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Phone Type",
          "id": 100007542
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "Plug_Type",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Universal",
              "en_name": "Universal",
              "id": 1488
            },
            .......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Plug Type",
          "id": 120013475
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 1,
          "name": "color_family",
          "input_type": "multiEnumInput",
          "options": [
            {
              "name": "Olive",
              "en_name": "Olive",
              "id": 330
            },
            .......
          ],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "Color",
          "id": 100005683
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 1,
          "name": "storage_capacity_new",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Not Specified",
              "en_name": "Not Specified",
              "id": 20884
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "Storage Capacity",
          "id": 100005939
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "sim_slots",
          "input_type": "singleSelect",
          "options": [
            {
              "name": "2",
              "en_name": "2",
              "id": 53248
            },
            .......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "SIM card Slots",
          "id": 100005874
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "power_consumption",
          "input_type": "enumInput",
          "options": [
            {
              "name": "5000 and Up",
              "en_name": "5000 and Up",
              "id": 72010
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Power Consumption",
          "id": 100005948
        },
        {
          "advanced": {
            "is_key_prop": 1
          },
          "is_sale_prop": 0,
          "name": "resolution",
          "input_type": "enumInput",
          "options": [
            {
              "name": "HD",
              "en_name": "HD",
              "id": 6896
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Resolution",
          "id": 100005887
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "warranty",
          "input_type": "enumInput",
          "options": [
            {
              "name": "4 Years",
              "en_name": "4 Years",
              "id": 54716
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Warranty",
          "id": 100005502
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "pixel_ppi",
          "input_type": "enumInput",
          "options": [
            {
              "name": "200-300 PPI",
              "en_name": "200-300 PPI",
              "id": 73907
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "PPI",
          "id": 100006073
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "package_content",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "What's in the box",
          "id": 100005496
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "camera_back",
          "input_type": "enumInput",
          "options": [
            {
              "name": "No Camera",
              "en_name": "No Camera",
              "id": 65634
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Primary(Back) Camera Resolution",
          "id": 100005944
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "network_connections",
          "input_type": "multiEnumInput",
          "options": [
            {
              "name": "3G",
              "en_name": "3G",
              "id": 55014
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Network Connections",
          "id": 100005819
        },
        {
          "advanced": {
            "is_key_prop": 1
          },
          "is_sale_prop": 0,
          "name": "display_size_mobile",
          "input_type": "enumInput",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Screen Size (inches)",
          "id": 100006049
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "phone_features",
          "input_type": "multiEnumInput",
          "options": [
            {
              "name": "Gyro",
              "en_name": "Gyro",
              "id": 20388
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Phone Features",
          "id": 100006060
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "brand",
          "input_type": "singleSelect",
          "options": [],
          "is_mandatory": 1,
          "attribute_type": "normal",
          "label": "Brand",
          "id": 20000
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "video_resolution",
          "input_type": "enumInput",
          "options": [
            {
              "name": "1080p",
              "en_name": "1080p",
              "id": 65341
            },
            ....
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Video Resolution",
          "id": 100006033
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "model",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Model",
          "id": 100005650
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "type_of_battery",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Lithium polymer battery",
              "en_name": "Lithium polymer battery",
              "id": 55425
            },
            ....
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Type of Battery",
          "id": 100005788
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "camera_front",
          "input_type": "enumInput",
          "options": [
            {
              "name": "No Camera",
              "en_name": "No Camera",
              "id": 65634
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Camera Front",
          "id": 100005919
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "processor_type",
          "input_type": "enumInput",
          "options": [
            {
              "name": "NVIDIA",
              "en_name": "NVIDIA",
              "id": 1219
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Processor Type",
          "id": 100006040
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "input_voltage",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Other",
              "en_name": "Other",
              "id": 53135
            },
            .......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Input Voltage",
          "id": 100005787
        },
        {
          "advanced": {
            "is_key_prop": 1
          },
          "is_sale_prop": 0,
          "name": "Number_of_Camera",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Dual",
              "en_name": "Dual",
              "id": 780
            },
            .......
            {
              "name": "Single",
              "en_name": "Single",
              "id": 122942014
            }
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Number_of_Camera",
          "id": 120080601
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 1,
          "name": "Variation",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "Variation",
          "id": 120122201
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "screen_type",
          "input_type": "enumInput",
          "options": [
            {
              "name": "LCD",
              "en_name": "LCD",
              "id": 42547
            },
            {
              "name": "VGA",
              "en_name": "VGA",
              "id": 49297
            },
            {
              "name": "AMOLED",
              "en_name": "AMOLED",
              "id": 55012
            },
            {
              "name": "OLED",
              "en_name": "OLED",
              "id": 65324
            },
            {
              "name": "TFT LCD",
              "en_name": "TFT LCD",
              "id": 73760
            },
            {
              "name": "IPS LCD",
              "en_name": "IPS LCD",
              "id": 73761
            },
            {
              "name": "QVGA",
              "en_name": "QVGA",
              "id": 89540
            },
            {
              "name": "Super AMOLED HD",
              "en_name": "Super AMOLED HD",
              "id": 115235
            }
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Screen Type",
          "id": 100006086
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "condition",
          "input_type": "singleSelect",
          "options": [
            {
              "name": "NEW",
              "en_name": "NEW",
              "id": 12055
            },
            {
              "name": "Refurbish",
              "en_name": "Refurbish",
              "id": 65550
            },
            {
              "name": "Export",
              "en_name": "Export",
              "id": 65569
            },
            {
              "name": "Telco Set",
              "en_name": "Telco Set",
              "id": 65577
            }
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Condition",
          "id": 100005888
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "operating_system",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Android",
              "en_name": "Android",
              "id": 3816
            },
            {
              "name": "iOS",
              "en_name": "iOS",
              "id": 54798
            },
            {
              "name": "Blackberry OS",
              "en_name": "Blackberry OS",
              "id": 54810
            },
            {
              "name": "Windows Mobile",
              "en_name": "Windows Mobile",
              "id": 123994292
            }
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Operating System",
          "id": 100005762
        },
        {
          "advanced": {
            "is_key_prop": 1
          },
          "is_sale_prop": 0,
          "name": "battery_capacity",
          "input_type": "enumInput",
          "options": [
            {
              "name": "Under 1000 mAh",
              "en_name": "Under 1000 mAh",
              "id": 106374
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Battery Capacity",
          "id": 100005965
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "mpn",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "MPN",
          "id": 100007628
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "ram_memory",
          "input_type": "enumInput",
          "options": [
            {
              "name": "1GB",
              "en_name": "1GB",
              "id": 54758
            },
            ......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "RAM memory",
          "id": 100005768
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "gtin",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "GTIN",
          "id": 100007627
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "warranty_type",
          "input_type": "singleSelect",
          "options": [
            {
              "name": "International Manufacturer Warranty",
              "en_name": "International Manufacturer Warranty",
              "id": 75172
            },
            ......
          ],
          "is_mandatory": 1,
          "attribute_type": "normal",
          "label": "Warranty Type",
          "id": 100005515
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "Name_CN",
          "input_type": "richText",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Name_CN",
          "id": 120188201
        },
        ......
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "product_warranty_en",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Warranty Policy (English)",
          "id": 100005503
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "package_length",
          "input_type": "numeric",
          "options": [],
          "is_mandatory": 1,
          "attribute_type": "sku",
          "label": "Package Length (cm)",
          "id": 100005497
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "Delivery_Option_Instant",
          "input_type": "singleSelect",
          "options": [
            {
              "name": "Yes",
              "en_name": "Yes",
              "id": 14800
            },
            {
              "name": "No",
              "en_name": "No",
              "id": 20776
            }
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Delivery Option",
          "id": 120074405
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "product_warranty",
          "input_type": "text",
          "options": [
            {
              "name": "Not Specified",
              "en_name": "Not Specified",
              "id": 20884
            },
            ......
            {
              "name": "Skinny",
              "en_name": "Skinny",
              "id": 72829
            }
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Warranty Policy",
          "id": 100005563
        },
        ......
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "SellerSku",
          "input_type": "text",
          "options": [],
          "is_mandatory": 1,
          "attribute_type": "sku",
          "label": "SellerSKU",
          "id": 100005546
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "Hazmat",
          "input_type": "multiSelect",
          "options": [
            {
              "name": "Liquid",
              "en_name": "Liquid",
              "id": 6026
            },
            .......
          ],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Dangerous Goods",
          "id": 100007127
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "special_from_date",
          "input_type": "date",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "Start date of promotion",
          "id": 100005523
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "special_price",
          "input_type": "numeric",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "sku",
          "label": "Special Price",
          "id": 100005528
        },
        {
          "advanced": {
            "is_key_prop": 0
          },
          "is_sale_prop": 0,
          "name": "name_ms",
          "input_type": "text",
          "options": [],
          "is_mandatory": 0,
          "attribute_type": "normal",
          "label": "Name (Malay)",
          "id": 100005573
        },
        .......
        }
      ],
      "code": "0",
      "request_id": "2101554016563075653198457"
    }