# What is changing?
The TH marketplace has introduced new product certification requirements for two categories. Starting from **2024-08-10**, Products API will be updated to require safety-related Product Certifications.
| Category | New requirement for Mandatory Attributes or Mandatory Qualifications | Example |
| --- | --- | --- |
| Phones & Electronics > Audio & Video > Walkie Talkies | * Approval Certificate for Telecommunication Equipment | ![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/bcec3c7b61b84ebe893e4d2ad9131af6~tplv-10qhjjqwgv-image.image) <br>  |
| Health > Medical Supplies > Sleep & Snoring | * Medical Device Advertising License <br> * FDA Registration No. on Product Label | ![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/30ec09a9058c480fa95a11af2a8b3b5a~tplv-10qhjjqwgv-image.image) <br>  |
# Which markets are affected?
The updates of the requirements apply to the local and cross-border sellers in the TH market
# Who is affected?
Developers with applications that use [Create Product](create-product), [Edit Product](edit-product), and [Partial Edit Product](partial-edit-product)
# Which version is applicable?
The updates of the requirements apply to all versions of the related APIs
# What action is required?
Without mandatory attributes and product certifications for products within specific categories, sellers will not be able to create and update products.
Use the Get Attributes to check what attributes are mandatory and pass attribute values via the Create Product, Edit Product, and Partial Edit Product to help sellers fill in the attribute values.
Use the Get Category Rule to check what product certifications are required and pass the product certification files via the Create Product, Edit Product and Partial Edit Product to help sellers submit product certification.