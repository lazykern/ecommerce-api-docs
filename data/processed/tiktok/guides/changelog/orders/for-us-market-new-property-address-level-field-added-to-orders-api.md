# What is changing?
TikTok Shop addresses are organized at a hierarchical level starting from L0 to L3. For example,address level L3 is always a "City". The objects in the `district_info` list in the Orders API now include more information about this hierarchy by including a new `address_level` field which can be one of `["L0", "L1", "L2", "L3"]`.
# Which markets are affected?
This change is only for US markets.
# Who is affected?
Only local sellers who build Connector apps, Multi-Channel Management apps and Direct Integration are affected.
# Which version is applicable?
This change is for **v202309** only, and the legacy API will not be changed.
# What action is required?
We recommend adopting your code to look for these levels as that will provide a more holistic overview of which field to parse. Integrate the "address level" (L0, L1, L2, L3) and regard it as from high level to low level. For example, L3 address level in the US is city, so use L3 address value to map the value to the "city" field in external system Shopify or WooCommerce.
| Region | L0 | L1 | L2 | L3 |
| --- | --- | --- | --- | --- |
| US | US | State | County | City |
| US | US | State | Borough | City |
| US | US | State | Parish | City |
| US | US | State | City | City |
| US | US | Federal District | County | City |
## Get Order List and Get Order Detail
### Parameters
No change
### Responses
The response now contains `district_info.address_level`, with enumerated values `["L0", "L1", "L2", "L3"]`. For different markets ( related to country or region in the real world), same address level value represents different district levels. Please see the table above for the nuances in addresses for the US market.
| Properties |  |  | Type | Sample | Properties description |
| --- | --- | --- | --- | --- | --- |
| code |  |  | int | 0 | Return code for the API call |
| message |  |  | string | Success | Explanation of the return code for the API call. |
| request_id |  |  | string | 202203070749000101890810281E8C70B7 | Request log |
| data |  |  | object |  | Specific return information |
| └ |  | order_id | string | 576461413038785752 | Tiktok shop order id |
| └ |  | district_info |  |  |  |
| └ | └ | address_level_name | string | Country | The name of administrative division that can be used by seller for ship. e.g. state/county/city/district/town etc. |
| └ | └ | address_name | string | United Kingdom | Administrative area name. eg: London |
| └ | └ | address_level | string | L0 | Administrative district level code. eg. US is L0 |
### Error code/message
No change