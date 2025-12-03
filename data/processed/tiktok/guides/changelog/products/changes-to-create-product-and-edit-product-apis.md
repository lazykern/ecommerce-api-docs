# Summary
When sellers create or edit products via API, they can pass values to optional product fields such as GTIN, product attributes, and brand_id. If the format validation fails for these fields, previously the API call would fail. Now, the API call will succeed by adopting sane defaults. The API will return a new property, `warnings.message` and will contain information on which fields have been reset. Only the following parameters are affected:

* `brand_id`
* `identifier_code`
* `product_attributes`

# What is changing?
## Brand ID (brand_id)
| Before | After |
| --- | --- |
| API calls fail when the brand chosen does not fit the product category | * API calls will be successful and the brand parameter will default to "No Brand". <br> * New property `warnings.message` will be returned indicating the original brand value is wiped out and defaulted to "No Brand". |
## Identifier Code (identifier_code)
| Before | After |
| --- | --- |
| API calls fail when the GTIN format (14 digits, the last digit is character) is not correct. | * Only applies for the **GTIN** type <br> * API calls will be successful and the `identifier_code.code` parameter value will be empty. <br> * New property `warnings.message` will be returned indicating the GTIN value is wiped out and reset to default. |
## Product Attributes (product_attributes)
| Before | After |
| --- | --- |
| API calls fail when product attributes value are in the wrong format. Format validation rules vary according to different attributes and markets. | * API calls will be successful and the `product_attributes.values.name` parameter value will be empty. <br> * New property `warnings.message` will be returned indicating the fields that are reset to default. |
# What markets & sellers are affected?
**All** **markets** and **all** **sellers** are impacted by this change.
# What versions are these changes for?
This change is applicable to **all** **versions**.
# Required Actions
We recommend adopting this new version and taking advantage of the feature where API calls will not fail but reset to defaults.