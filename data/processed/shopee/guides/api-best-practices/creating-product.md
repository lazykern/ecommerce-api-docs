Once you have obtained the product base data, you can start creating products.

# 1\. Uploading media files

Images and videos of your products need to be **pre-stored** in Shopee's media space. So you need to call the MediaSpace API to upload first.

## 1.1 Uploading image

API: [_v2.media_space.upload_image_](<https://open.shopee.com/documents/v2/v2.media_space.upload_image?module=91&type=1>) 

 

Each product must have product images, in addition, we also support insert images to product description. And the product image files need to meet the following requirements:

  * Image size: maximum 10MB
  * Image format: JPG, JPEG, PNG



 

Please note:

  * [_V2.media_space.upload_image_](<https://open.shopee.com/documents/v2/v2.media_space.upload_image?module=91&type=1>) API we only support image file upload, not support URL. When the image is uploaded successfully, you will get the Shopee image URL accessible in each region and a unique image_id. We recommend that you link the Shopee image URL based on the shop region. image_id is for creating products and updating the product image information.
  * If you upload a product image, the request parameter **scene** should be normal; if you upload a product description image, the request parameter scene should be desc, because the product image we will handle as a square image, the description image we will not handle.



 

## 1.2 Uploading video

Product video is optional, we support video files with the following requirements:

  * Video size: max 30MB
  * Video length: 10s~60s
  * Video format: mp4
  * Video pixel requirements: pixel width and height no more than 1280px * 1280px



If your video file is over 4M, you need to split the video file, for example, a 10MB video, you need to split it into 4M, 4M and 2M fragments, because each fragment cannot be larger than 4M.

 

Uploading product videos need four steps:

 

  * Step 1: Call the [v _2.media_space.init_video_upload_](<https://open.shopee.com/documents/v2/v2.media_space.init_video_upload?module=91&type=1>) API. Create a video upload task and get the video_upload_id. Please note that regardless of whether your video has a partition or not, **file_md5 needs to upload the md5 value of the full video file** and file_size is also for the full video file.
  * Step 2: Call the [_v2.media_space.upload_video_part_](<https://open.shopee.com/documents/v2/v2.media_space.upload_video_part?module=91&type=1>) API. When the video file has fragments, the part_seq (should start from 0)  parameter indicates the fragments sequence number, part_content parameter indicates the fragments file. Please finish uploading all the fragments.
  * Step 3: Call the [_v2.media_space.complete_video_upload_](<https://open.shopee.com/documents/v2/v2.media_space.complete_video_upload?module=91&type=1>) API. Video transcoding, when you call this API, Shopee will transcode all the video fragments files you uploaded. The part_seq_list parameter takes the sequence number of all the parts you uploaded, for example, if you uploaded 2 parts, the part_seq_list will be [0,1]. For the upload_cost field you can upload the time of using the upload_video_part API for one video file.
  * Step 4: Call the [_v2.media_space.get_video_upload_result_](<https://open.shopee.com/documents/v2/v2.media_space.get_video_upload_result?module=91&type=1>) API. Get the video transcoding result. Since video transcoding takes some time, you can get the result by calling the [_v2.media_space.get_video_upload_result_](<https://open.shopee.com/documents/v2/v2.media_space.get_video_upload_result?module=91&type=1>) API or by subscribing to the [_Video upload push_](<https://open.shopee.com/push-mechanism/11>). Only when the returned status is SUCCEEDED, you can get the Shopee video URLs and video cover image URLs which are accessible to each market, and at that time, the video_upload_id can be used to create or update the video information of the product.



 

 

After uploading images and videos, you can call [_v2.product.add_item_](<https://open.shopee.com/documents/v2/v2.product.add_item?module=89&type=1>) API to create products, the following will explain some points that need attention in calling [_v2.product.add_item_](<https://open.shopee.com/documents/v2/v2.product.add_item?module=89&type=1>) API.

# 2\. Uploading category and attributes

## 2.1 Uploading category

Products must have category_id. You can only select the leaf category ID in the category tree for the product, otherwise, the API will return an error with Invalid category id.

## 2.2 Uploading attributes

Products must upload all required attributes (attributes with "mandatory": true in the "[_v2.product.get_attribute_tree_](<https://open.shopee.com/documents/v2/v2.product.get_attribute_tree?module=89&type=1>)" API response are considered required). You can refer to the article "Product creation preparation" to learn more about different attribute types. Below are explanations of how to upload different attribute types when calling the "v2.product.add_item" API.

 

When uploading the attribute with "input_type": 1 (SINGLE_DROP_DOWN), you can only upload one "value_id", and this "value_id" must be one of the values from the attribute list returned by the “[ _v2.product.get_attribute_tree_](<https://open.shopee.com/documents/v2/v2.product.get_attribute_tree?module=89&type=1>)” API.

 

Example 1
    
    
    "attribute_list": [
        {
            "attribute_id": 100036,
            "attribute_value_list": [
                {
                    "value_id": 678
                }
            ]
        }
    ]

 

When uploading the attribute with "input_type": 4 (MULTI_DROP_DOWN), you can upload multiple "value_id" values, and these "value_id" values must be be from the attribute list returned by the "[_v2.product.get_attribute_tree_](<https://open.shopee.com/documents/v2/v2.product.get_attribute_tree?module=89&type=1>)" API.

 

Example 2
    
    
    "attribute_list": [
        {
            "attribute_id": 100036,
            "attribute_value_list": [
                {
                    "value_id": 678
                },
                {
                    "value_id": 679
                }
            ]
        }
    ]

 

When uploading the attribute with "input_type": 3 (FREE_TEXT_FILED), you can only upload one "value_id" and specify a custom value. Therefore, you must upload “value_id”: 0 and provide the custom value in the “original_value_name” field.

 

Example 3
    
    
    "attribute_list": [
        {
            "attribute_id": 100061,
            "attribute_value_list": [
                {
                    "value_id": 0,
                    "original_value_name": "customized name"
                }
            ]
        }
    ]

 

i) If the attribute has “input_type”: 3 (FREE_TEXT_FIELD) and requires a unit, you must upload the “value_unit” field as well. (That is, "input_type": 3 & "format_type": 2 (FORMAT_QUANTITATIVE_WITH_UNIT))

 

Example 4
    
    
    "attribute_list": [
        {
            "attribute_id": 100061,
            "attribute_value_list": [
                {
                    "value_id": 0,
                    "original_value_name": "12",
                    "value_unit": "g"
                }
            ]
        }
    ]

 

ii) If the attribute has “input_type”: 3 (FREE_TEXT_FIELD) and requires a date type, you must upload a timestamp in the "original_value_name" field. (That is, "input_type": 3 & "input_validation_type": 4)

 

Example 5
    
    
    "attribute_list": [
        {
            "attribute_id": 100061,
            "attribute_value_list": [
                {
                    "value_id": 0,
                    "original_value_name": "1634526913"
                }
            ]
        }
    ]
    ]

 

For the attribute with "input_type": 2 (SINGLE_COMBO_BOX), you can only upload one "value_id". This "value_id" must be one of the values from the attribute list returned by the "[_v2.product.get_attribute_tree_](<https://open.shopee.com/documents/v2/v2.product.get_attribute_tree?module=89&type=1>)" API (please refer to Example 1) or a user-defined value (please refer to Example 3). If a unit is required, please refer to Example 4. If a date type is required, please refer to Example 5.

 

For the attribute with "input_type": 5 (MULTI_COMBO_BOX), you can upload multiple "value_id" values from the attribute list returned by the "[_v2.product.get_attribute_tree_](<https://open.shopee.com/documents/v2/v2.product.get_attribute_tree?module=89&type=1>)" API, or specify custom values.

 

Example 6
    
    
    "attribute_list": [
        {
            "attribute_id": 100061,
            "attribute_value_list": [
                {
                    "value_id": 0,
                    "original_value_name": "customized name"
                },
                {
                    "value_id": 678
                }
            ]
        }
    ]

 

If a unit is required, please refer to Example 4. If a date type is required, please refer to Example 5.

 

**Summary:**

1) For all attribute types, you must upload a "value_id". When uploading a user-defined value, "value_id" must be 0 and "original_value_name" is required.

2) Regardless of the data type of the value, the "original_value_name" field must be uploaded in string format.

3) When "format_type" is 2 and you upload a user-defined value, you must also upload the "value_unit" field, and the unit should be selected from the "attribute_unit_list" in the response of the "[_v2.product.get_attribute_tree_](<https://open.shopee.com/documents/v2/v2.product.get_attribute_tree?module=89&type=1>)" API. 

 

# 3\. Uploading description

*Please note that we currently support whitelisted sellers to use extended_description, please refer to the [_FAQ_](<https://open.shopee.com/faq?top=162&sub=166&page=1&faq=218>) for details on how to use it.

# 4\. Uploading price

Except for SG/MY/BR/MX/PL markets, we support sellers to upload two decimal prices (original_price), for other marketplaces, only integers are supported, if sellers fill in decimals, we will do rounding.

# 5\. Uploading stock

If the seller does not have a stock warehouse (currently only used by whitelist users) then there is no need to upload the location_id field.

# 6\. Uploading shipment channels and shipping fee

Depending on how the channel calculates the shipping fee, we have divided the channels into several types, you can get the fee_type through [_v2.logistics.get_channel_list_](<https://open.shopee.com/documents/v2/v2.logistics.get_channel_list?module=95&type=1>) API, the types including:

  * **SIZE_SELECTION** : The shipping fee is calculated based on the size ID
  * **SIZE_INPUT** : The shipping fee is calculated according to the specific product dimension, so for this type, the seller needs to upload the length, width ,height and weight for the product.
  * **FIXED_DEFAULT_PRICE** : Fixed shipping fee.
  * **CUSTOM_PRICE** : shipping fee can be customized by the seller.



 

The seller can choose multiple channels for the product.

i)enabled=true means the product is open to this channel and the buyer can choose.

ii) is_free=true means the seller bears the shipping fee, i.e. the product is shipped, the buyer does not need to bear the shipping fee, and all channel types support setting up shipping.

 

1) For the **SIZE_SELECTION** channel, the size_id must be uploaded, and **size_id** can be obtained through [_v2.logistics.get_channel_list_](<https://open.shopee.com/documents/v2/v2.logistics.get_channel_list?module=95&type=1>) API.

_Example 1:_

_  "logistic_info":[_

_     {_

_             "sizeid":1,_

_             "enabled":true,_

_             "is_free":false,_

_             "logistic_id":80101_

 _         }]_

 

2）For the **SIZE_INPUT** channel, the **weight** and **dimension** must be uploaded.

_Example2:_

_     "weight": 1,_

_    "dimension":{_

_         "package_height":11,_

_         "package_length":11,_

_         "package_width":11_

 _     },_

_  "logistic_info":[_

_     {_

_             "enabled":true,_

_             "is_free":false,_

_             "logistic_id":80101_

 _         }]_

 

3）For the **CUSTOM_PRICE** channel, the **shipping_fee** must be uploaded.

_Exapmle 3：_

 _   "logistic_info":[_

_         {_

_             "shipping_fee":23.12,_

_             "enabled":true,_

_             "is_free":false,_

_             "logistic_id":80103_

 _         }]_

_"logistic_info":[_

_         {_

_        _

_             "enabled":true,_

_             "logistic_id":80103_

 _         }]_

# 7\. Creating Variants

When you create the item successfully, [_v2.product.add_item_](<https://open.shopee.com/documents/v2/v2.product.add_item?module=89&type=1>) will return the item_id, which is the unique identifier of the item. If you also need to define specifications and create multiple option variants, such as the color and size, you can call [_v2.product.init_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>) API for the next step. We will create model_id for each variation, which will be the unique identifier of the variation.

 

**Scenario 1:** The product has size specifications and the size contains XS, S, and M. We call this 1-tier variation product.

 

tier_index| size| price| stock| SKU  
---|---|---|---|---  
tier_index[0]| XS| 100| 10| sku1  
tier_index[1]| S| 200| 20| sku2  
tier_index[2]| M| 300| 30| sku3  
  
 

 

[_v2.product.init_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>) API request example:
    
    
    {
    
        "item_id": 800188562,
    
        "tier_variation": [
    
            {
    
                "name": "size",
    
                "option_list": [
    
                    {
    
                        "option": "XS",
    
                        "image": {"image_id":"82becb4830bd2ee90ad6acf8a9dc26d7"}
    
                    },
    
                    {
    
                        "option": "S",
    
            "image": {"image_id":"72becb4830bd2ee90ad6acf879dc26d7"}
    
                    },
    
                    {
    
                        "option": "M",
    
          "image": {"image_id":"92becb4830bd2ee90ad6acf8a9dc26d7"}
    
                    }
    
                ]
    
            }
    
        ],
    
        "model": [
    
            {
    
                "tier_index": [0],
    
                "original_price": 100,
    
                "model_sku": "sku1",
    
                "normal_stock": 10
    
            },
    
            {
    
                "tier_index": [1],
    
                "original_price": 200,
    
                "model_sku": "sku1",
    
                "normal_stock": 20
    
            },
    
           {
    
                "tier_index": [2],
    
                "original_price": 300,
    
                "model_sku": "sku3",
    
                "normal_stock": 30
    
            }
    
        ]
    
    }

 

 

 

**Scenario 2:** The product has color and size specifications, the color includes red and blue, and the size includes XL and L. We call this 2-tier variation product.

 

tier_index| color| size| price| stock| SKU  
---|---|---|---|---|---  
tier_index[0,0]| Red| XL| 100| 10| sku1  
tier_index[0,1]| Red| L| 200| 20| sku2  
tier_index[1,0]| Blue| XL| 300| 30| sku3  
tier_index[1,1]| Blue| L| 400| 40| sku4  
  
 

[_v2.product.init_tier_variation_](<https://open.shopee.com/documents/v2/v2.product.init_tier_variation?module=89&type=1>) __ API request example:
    
    
     {
    
      "item_id": 100917481,
    
      "tier_variation": [
    
        {
    
          "name": "color",
    
          "option_list": [
    
            {
    
              "image": {"image_id": "82becb4830bd2ee90ad6acf8a9dc26d7"},
    
              "option": "Red"
    
            },
    
            {
    
              "image": {"image_id": "72becb4830bd2ee90ad6acf879dc26d7"},
    
              "option": "Blue"
    
            }
    
          ]
    
        },
    
        {
    
          "name": "size",
    
          "option_list": [
    
            {
    
              "option": "XL"
    
            },
    
            {
    
              "option": "L"
    
            }
    
          ]
    
        }
    
      ],
    
      "model": [
    
         { 
    
          "tier_index": [0,0],
    
          "original_price": 100,
    
          "normal_stock": 10,
    
          "global_model_sku": "sku1"
    
        },
    
        {
    
         "tier_index": [0,1],
    
          "original_price": 200,
    
          "normal_stock": 20,
    
          "global_model_sku": "sku2"
    
        },
    
        {
    
          "tier_index": [1,0],
    
          "original_price": 300,
    
          "normal_stock": 30,
    
          "global_model_sku": "sku3"
    
        },
    
        {
    
         "tier_index": [1,1],
    
          "original_price": 400,
    
          "normal_stock": 40,
    
          "global_model_sku": "sku4"
    
        }
    
      ]
    
    }

 

**Please note that**

1\. The options you define will be displayed on the Shopee mall side in order. Shopee currently only supports the definition of up to 2-tier variation.

2\. You can define an image for each variant. If it is a 2-tier variation product, you can only define the first layer of options, that is, in the example, you can define variant images based on color, but not based on size. Once you want to add variant images, all the options in the first layer need to define the image. The image needs to be uploaded by calling the [_v2.media_space.upload_image_](<https://open.shopee.com/documents/v2/v2.media_space.upload_image?module=91&type=1>) API first.

3\. The tier_index must start from 0 and not overflow, otherwise an error will be reported.

*4.It is recommended that you create variants after an interval of 5 seconds after creating an item, because there may be a delay in creating item data.

5\. After successful creation you can call [_v2.product.get_model_list_](<https://open.shopee.com/documents/v2/v2.product.get_model_list?module=89&type=1>) API to get the model id corresponding to each tier_index.