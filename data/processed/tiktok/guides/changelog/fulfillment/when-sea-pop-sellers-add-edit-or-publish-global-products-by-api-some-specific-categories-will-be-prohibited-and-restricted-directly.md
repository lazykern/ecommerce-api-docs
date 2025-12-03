# What is changing?
When adding, editing or publishing global products by API to single or multiple warehouses in mainland China or Hong Kong, SEA POP sellers can successfully call API without error message even these products are prohibited and restricted in some target markets, but these products would be rejected at the release stage. From December 30 2024, when SEA POP sellers add, edit or publish these kinds of global products by API, they will get an error message "The warehouse is unavailable because this product cannot be shipped to the target market from this warehouse" with error code 12052364.
# Which markets are affected?
The updates of the requirements apply to the POP sellers for the SG, PH, VN, TH and MY markets.
# Who is affected?
Developers with applications that use Create Global Product, Edit Global Product and Publish Global Product.
# Which version is applicable?
The updates of the requirements apply to all versions of the related APIs
# What action is required?
Developers need to check whether to use these APIs and handle this error message.