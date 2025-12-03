# What is changing?
TikTok Shop is implementing safety-related Mandatory Attributes and Product Safety and Compliance Image requirements for Toys, Beauty Products, Electronics, Food & Beverage, and Pet Food categories.
Starting from **2024-06-19**, Products API will be updated to require safety-related Mandatory Attributes and Product Certifications (known as Mandatory Product Safety and Compliance Image Requirements in the image below).
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/03886c034a8c41b3ae77094bce5d1691~tplv-10qhjjqwgv-image.image" width="1280px" /></div>

# Which markets are affected?
The updates of the requirements apply to the local sellers in the UK market
# Who is affected?
Developers with applications that use [Create Product](create-product), [Edit Product](edit-product), and [Partial Edit Product](partial-edit-product)
# Which version is applicable?
The updates of the requirements apply to all versions of the related APIs
# What action is required?
Without mandatory attributes and product certifications for products within specific categories, sellers will not be able to create and update products.
Use the Get Attributes to check what attributes are mandatory and pass attribute values via the Create Product, Edit Product, and Partial Edit Product to help sellers fill in the attribute values.
Use the Get Category Rule to check what product certifications are required and pass the product certification files via the Create Product, Edit Product and Partial Edit Product to help sellers submit product certification.