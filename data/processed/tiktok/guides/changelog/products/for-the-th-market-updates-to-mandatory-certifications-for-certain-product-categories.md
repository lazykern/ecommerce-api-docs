# What is changing?
For the TH market, TikTok Shop is implementing new Mandatory Qualifications for certain product categories.
| **Category** | **New requirement Mandatory Qualifications** |
| --- | --- |
| Tools & Hardware > Hand Tools > Industrial Scales | Important Document Showing Certification of Weights and Measures |
| Kitchenware > Kitchen Utensils & Gadgets > Kitchen Scales | Image of product with 'Do not use the scale for trading' mark |
| For multiple categories of Household Appliances | TIS Certificate Mark on Product Label |

Starting from **2024-09-10**, Products API will be updated to require the above Mandatory Certifications.
# Which markets are affected?
The updates of the requirements apply to the local and cross-border sellers in the TH market
# Who is affected?
Developers with applications that use [Create Product](create-product), [Edit Product](edit-product), and [Partial Edit Product](partial-edit-product)
# Which version is applicable?
The updates of the requirements apply to all versions of the related APIs
# What action is required?
Without mandatory attributes and product certifications for products within specific categories, sellers will not be able to create and update products.
Use the Get Category Rule to check what product certifications are required and pass the product certification files via the Create Product, Edit Product and Partial Edit Product to help sellers submit product certification.