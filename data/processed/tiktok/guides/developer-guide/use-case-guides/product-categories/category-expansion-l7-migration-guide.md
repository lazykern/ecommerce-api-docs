# Introduction
This guide explains the steps you have to take so you can successfully migrate from 3-level categories to 7-level categories. We broadly cover three scenarios:

* Creating a new product in the L7 Category
* Updating an existing product to the L7 Category
* Manually mapping products between categories

# Getting the new leaf category ID
Products can only be assigned to leaf categories, therefore you need to get the new leaf category ID to create products in the new L7 category or update products to the new L7 category. You can get the new leaf category ID in the following ways:
## Method 1 [Recommended]

1. Call Upload Image and upload product images
2. Call Get Recommended Category API and provide image, product title and description to get leaf category ID

## Method 2

1. Call [Get Categories](get-categories) endpoint to get a list of all the categories
2. The categories with `is_leaf == true` in the response data are leaf categories. Get the leaf category ID from the corresponding `category_id` parameter.

# Using Recommend Category API
The [Recommend Category](recommend-category) API can be used to get recommend leaf category in TikTok Shop.

* The required field is product title, but we will be requiring product description and image by 6/30.
* We will return recommended categories based on the incoming parameters. *If the relevance is low, we will not return recommended categories and an error message will be displayed.*
* *If the shop_id is passed in as a parameter, the category recommendation will filter out categories that the merchant does not have permission to access, and return the relative status for categories.*
* The return parameters will provide the corresponding language of the Seller's market.
* The error code **12052913:No matching categories**.
   * Please edit the product name and try again. Make sure to enter the full product name.
* The text inside the images will not be used for category recommendations.
* You can either provide a 1:1 mapping feature or category template feature to better help sellers fill in the required info based on category rules.

# Creating A New Product
**If you are using Listing Schema** when creating a new product, perform these steps:

1. Call Check Listing Prerequisites and ensure the store can accept new product listings
2. Call Upload Image endpoint to upload the product image
3. Call Get Recommended Category API and provide image, product title and description to get leaf category ID
4. Call Get Listing Schemas with the leaf category ID to get the required and supported attributes of that category
5. Call Create Product by providing the relevant information to create the product

**If you are NOT using GET Listing Schemas or the Recommend Category API**, follow these instructions:

1. Call Check Listing Prerequisites and ensure the store can accept new product listings
2. Call Upload Image endpoint to upload the product image
3. Call Get Categories endpoint to get a list of all the leaf categories
4. Call Get Attributes to get a list of all the attributes that are supported and required by the category
5. Call Get Category Rule to get a list of all the rules of the category, like size chart requirements, product qualifications, etc
6. Call Create Product by providing the relevant information to create the product

# Updating an Existing Product
## Batch upgrade (all active products)
![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/0ada0d162223427a81e05c2ed8ea1240~tplv-10qhjjqwgv-image.image)
To update all active products in the entire store, please follow these steps:

1. Show a button to the seller that can be pressed to trigger the batch upgrade
2. Call the [Upgrade Category API](create-category-upgrade-task) and provide the shop code
3. TikTok Shop will take all the active products belonging to this shop and begin upgrading them
4. TikTok Shop will send webhook updates with the category upgrade results
5. If the webhooks aren't working or if you need to poll for updates, you can call the GET Category Upgrade Detail endpoint

<span style="background-color: rgb(255, 245, 235)">📌 </span><span style="background-color: rgb(255, 245, 235)"><strong>Note</strong></span><span style="background-color: rgb(255, 245, 235)">: For newly listed active products, you must wait at least </span><span style="background-color: rgb(255, 245, 235)"><strong>24 hours</strong></span><span style="background-color: rgb(255, 245, 235)"> before upgrading the category. The Upgrade Category API will be unable to recognize a product that has been active for less than 24 hours.</span>
## Single product update
When updating an existing product, perform these steps:

1. Get the new leaf category ID using one of the steps described in the "Getting the new leaf category ID" section
2. Call Partial Edit Product with the new category ID and any modified attributes

## Map Categories between a platform and TikTok Shop

1. Allow the seller to select a product
2. Get the leaf category ID of that product using the steps above
3. Associate the new leaf category ID with the category of the product