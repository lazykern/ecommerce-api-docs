# Summary
## What are we launching
A dangerous good (also known as hazardous material or hazmat) is any product capable of posing an unreasonable risk to health, safety, and property during shipping, storage, and handling. These goods can contain flammable, corrosive, pressurized, or otherwise harmful substances. As a result, dangerous goods must be handled and transported with special care and safety measures and can have additional transportation requirements (such as specific marking and labeling of packages or special handling).
Sellers are responsible for identifying if their listed products qualify as dangerous goods and shipping and labeling these products in a compliant manner, according to applicable laws and regulations.
In order to do this, we are launching new required attributes to Get Attributes API. These attributes must be filled by the seller in order to list products in hazmat categories.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ[[/ljhwZthlaukjlkulzlp/Changelog/Hazmat%20changelog/5439949b-610d-4d21-8112-3b8482ca86a8.png)
More information on hazmat policy and categories can be found on [Seller Academy](https://seller-us.tiktok.com/university/essay?knowledge_id=7071657567962926&role=1&course_type=1&from=search&identity=1).
## When are we launching it
API enforcement for product listings (Create and Edit Product APIs) with hazmat attributes will begin after **++January 5th++**.
## Impact
All existing and new listings must comply and provide hazmat information after January 5th to avoid be taken down.
## Which markets are impacted?
Only US market will be impacted at this time.
# API Changes
These changes to the API are going to be **released on July 20, 2024.** A list of attributes names and IDs for Hazmat information:
| **attribute.name** | **attribute.id** | **attribute.values.name** | **attribute.values.id** | **Supported input type** |
| --- | --- | --- | --- | --- |
| > Contains Batteries or Cells? | 101610 | Batteries | 1024358 | Select one value for the listed options |
|  |  | Cells | 1024359 | Select one value for the listed options |
|  |  | None | 1000325 | Select one value for the listed options |
|  |  | Not Sure | 1024360 | Select one value for the listed options |
| >> Battery Type | 100216 | Lithium Ion | 1024361 | Select one value for the listed options |
|  |  | Lithium Metal | 1023433 | Select one value for the listed options |
|  |  | Lead/Cadmium/Mercury | 1024362 | Select one value for the listed options |
|  |  | Alkaline | 1024363 | Select one value for the listed options |
|  |  | Other | 1020869 | Select one value for the listed options |
| >>> How Batteries Are Packed | 101611 | Batteries Built-In | 1024364 | Select one value for the listed options |
|  |  | Batteries Packed Separately | 1024365 | Select one value for the listed options |
|  |  | Batteries Only | 1024366 | Select one value for the listed options |
| >>> Number of Batteries or cells | 101623 |  |  | Custom text input |
| >>> Battery or Cell Capacity in Wh | 101624 |  |  | Custom text input |
| >>> Battery or Cell Capacity in grams | 101625 |  |  | Custom text input |
| >>> Battery or Cell Weight in grams | 101614 |  |  | Custom text input |
| > Flammable Liquid | 101574 | Yes | 1000058 | Select one value for the listed options |
|  |  | No | 1000059 | Select one value for the listed options |
|  |  | Not Sure | 1024360 | Select one value for the listed options |
| >> Flammable Liquid Volume in ml | 101626 |  |  | Custom text input |
| > Aerosols | 101571 | Yes | 1000058 | Select one value for the listed options |
|  |  | No | 1000059 | Select one value for the listed options |
|  |  | Not Sure | 1024360 | Select one value for the listed options |
| >> Aerosol Liquid Volume in ml | 101627 |  |  | Custom text input |
| > Other Dangerous Goods or Hazardous Materials | 101619 | Yes | 1000058 | Select one value for the listed options |
|  |  | No | 1000059 | Select one value for the listed options |
|  |  | Not Sure | 1024360 | Select one value for the listed options |
## 1.[Get Attributes](get-attributes)
### Parameters
No change
### Responses
Adding two properties:

* Adding `requirement_conditions` to response, indicating if the product attribute is required based on the conditions in this object. If any of the conditions are met, the attribute is required; otherwise, it is not.
* Adding `value_data_format` property, to specify the type and structure of data expected for that attribute, such as strings, integers or positive decimal value.

### Error code/message
No change
## 2.[Get Category Rules](get-category-rules)
### Parameters
No change
### Responses
Adding `requirement_conditions` to response, indicating if the product attribute is required based on the conditions in this object. If any of the conditions are met, the attribute is required; otherwise, it is not.
### Error code/message
No change