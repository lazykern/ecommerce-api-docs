# What is changing?
From June 17, 2024, Platform updated the collection method to support sellers to choose different collection methods for different warehouse content. The parameters "handover_method" in api Ship Package and Batch Ship Package will be useless from Oct. 30, 2024.
# Which markets are affected?
The updates of the requirements apply to the local sellers in the ID, SG, PH, VN, TH and MY markets.
# Who is affected?
Developers with applications that use api Ship Package and Batch Ship Package.
# Which version is applicable?
The updates of the requirements apply to all versions of the related APIs
# What action is required?
Developers need to check whether to use handover_method to update the collection method. It will be useless.
If sellers want to know the order's collection method, they need to go to Seller Center to see the setting of related warehouses. The path is "Orders"->"Manage Orders"->"Fulfillment settings"->"Collection method settings".