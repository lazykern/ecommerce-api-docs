# sign

**Description:** Do sign for seller. Seller or agencies can use this api to sign up the t&c.

**Timeout Period：** the api timeout is 10s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

此接口无入参

  


# modifyAutoTopUpOptionOneConfig

**Description:** Modify auto top up option one config.

**Timeout Period：** the api timeout is 3s, max qps is 100, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

venture | min top up | max top up  
---|---|---  
SG | 5 | 8,333,333,330  
PH | 100 | 17,895,600  
TH | 100 | 8,333,333,300  
VN | 50,000 | 833,333,300,000  
MY | 10 | 8,333,333,330  
ID | 25,000 | 8,333,333,000  
  
## Tax Rate

  


venture | seller type | Taxable  
---|---|---  
SG | Local | 8%  
CB | 0%  
PH | ALL | 12%  
CB | 0%  
TH | ALL | 7%  
CB | 0%  
VN | ALL | 10%  
MY | ALL | 6%  
CB | 0%  
ID | ALL | 11%  
CB | 0%  
  
## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
status | Number | Yes | The option one status.1:ON;0:OFF.  
limitAmount | String | Yes | If balance is lower than this value, auto topUp operation will be done.  
topupAmount | String | Yes | The amount of topUp for each auto topUp.  
  
# addSolution

**Description:** Add sponsor solution.

**Timeout Period：** the api timeout is 3s, max qps is 10, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

**Notes:** For discovery campaign, the max count is 50, make sure do not over this num.Before you invoke this api, make sure the seller is already signed T&C.

There is some business valid you need to know.

You could use this api to add standard or smart campaign, about the autoItemSelect, phase 1 only support manual.The dayBudget & bidPrice & maxBid should meet the standard below.

If the campaign type is smart, make sure your budget is not -1, and if the campaign type is standard, the budget will be -1 or specific value.

The campaign "Start date" and campaign"end date" represent the period during which a campaign will running. For example, if a campaign has a start date of June 1st, 2023 and an end date of June 30th, 2023, it means that the campaign will running from June 1st to June 30th, 2023, provided that the campaign has a valid budget, promoted products, and the seller has sufficient balance.

"minBudgetMap":{

"SG":10,

"PH":100,

"TH":100,

"VN":50000,

"MY":4,

"ID":25000

},

"maxBudgetMap":{

"SG":10000,

"PH":1000000,

"TH":1000000,

"VN":200000000,

"MY":100000,

"ID":100000000

},

"minMaxBidMap":{

"SG":0.05,

"PH":0.48,

"TH":1,

"VN":400,

"MY":0.06,

"ID":250

},

"maxMaxBidMap":{

"SG":20,

"PH":750,

"TH":450,

"VN":330000,

"MY":60,

"ID":200000

},

"minBidPriceMap":{

"SG":0.05,

"PH":0.48,

"TH":1,

"VN":400,

"MY":0.06,

"ID":150

},

"maxBidPriceMap":{

"SG":20,

"PH":750,

"TH":450,

"VN":330000,

"MY":60,

"ID":200000

}

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
endDate | String | Yes | Campaign end date.Make sure end date is later than  or equal to start date and current time.   
platform | Number[] | Yes | Placements determine where shoppers will see your promoted products.3:Search Result Page;4:Just For You Page  
autoCreative | Number | Yes | Lazada automatically set creatives for your products.1:ON;0:OFF.  
autoKeyWord | Number | Yes | Let Lazada automatically set keyword for your products.1:manual(I want to select keywords manually for my product selection.);2:auto(Let Lazada optimiz the keywords relating to your products in real time to maximize the campaigns' performance)  
campaignObjective | Number | Yes | Your campaign objective helps detemine your bidding strategy - coordinating wiht the upgrading of Sponsored Discovery,we highly recommend to choose '2.Sales' as your campaign type,to helps increase your store sales efficiently.Please be noticed that hte '1.Traffic' will be stop optimized by the end of Aug.[Updated Aug 8th]  
campaignType | Number | Yes | Unlock different ways to bids, select products, and keywords with campaign types.1:Standard;2:Smart.Please noted that this parameter might will be updated since Mid of July， 2023  
campaignModel | Number | Yes | Fine granularity to distinguish solutions.Phase 1, this field is 99.  
maxBid | String | Yes | Max bid determines the highest amount that you're willing to pay for a click on your promoted product.String type, -1 means automated bid setting  
autoItemSelect | Number | Yes | The way the product be selected.1:manual(I want to select products manually from my store.);2:auto(Let Lazada optimize the products within the campaigns in real-time to maximize the campaigns' performance).Phase 1, we only support manual.  
dayBudget | String | Yes | Budget indicates the maximum amount you’re willing to pay each day.-1 means no limit budget  
campaignName | String | Yes | Campaign name.Less than 200 char.  
startDate | String | Yes | Campaign start date.  
adgroupViewDTOlistWithFeed | Object[] | Yes | Adgroup list.  
adgroupName | String | Yes | Adgroup name, normally is product name,  
bidPrice | String | Yes | This is the maximum bid price that you have set for your campaign.Please make sure this field is meeted the standard above.  
autoKeyword | Number | Yes | Let Lazada automatically set keyword for your products.1:manual(I want to select keywords manually for my product selection.);2:auto(Let Lazada optimize the keywords relating to your products in real time to maximize the campaigns' performance).This must be the same as the campaign  
audienceViewDTOList | Object[] | No | This setting allows you to bid higher on premium audiences that are more likely to convert in your store.This field will work for sponsor recommend.  
adCrowdTag | Number | No | 1:on store visitors in the past 15 days;2:on in-market audiences for similar products;3:Store Awareness Audience;4:Store Interest Audience  
discount | Number | No | The discount you want to give.eg:10 means 10% discount.  
itemId | Number | Yes | Product id.  
bidwordViewDTOList | Object[] | No | Bid word list.This field will work for sponsor search.  
keyword | String | No | The specific keyword.eg:shoe.  
bidPrice | String | No | This is the maximum bid price that you have set for your campaign.Please make sure this field is meeted the standard above.  
autoItemSelect | Number | Yes | The way the product be selected.1:manual(I want to select products manually from my store.);2:auto(Let Lazada optimize the products within the campaigns in real-time to maximize the campaigns' performance).This field need to be same as campaign's autoItemSelect.  
autoCreative | Number | Yes | Let Lazada automatically set creatives for your products.1:ON;0:OFF.This must be the same as the campaign.  
  
  


# addAdgroupBatch

**Description:** Do add adgroup for one campaign.

**Timeout Period：** the api timeout is 3s, max qps is 100, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

**Notes:** There is some basic valid for param, including campaignId,adgroupViewDTOList and the itemId & bidPrice in adgroupViewDTOList is necessary, and the campaignId should be a real one, ortherwise you will receive an error.

Max count of adgroup of one campaign is 100, please do not add more than 100 adgroup. And also be affirmed, this api only support those mannual select product campaign, do not support auto select product campaign.

There is also some business valid, the bidPrice should between max and min of standard by venture,you could refer the table below.

  


"minBudgetMap":{

"SG":5,

"PH":50,

"TH":100,

"VN":25000,

"MY":4,

"ID":25000

},

"maxBudgetMap":{

"SG":10000,

"PH":1000000,

"TH":1000000,

"VN":200000000,

"MY":100000,

"ID":100000000

},

"minBidPriceMap":{

"SG":0.05,

"PH":0.48,

"TH":1,

"VN":400,

"MY":0.06,

"ID":150

},

"maxBidPriceMap":{

"SG":20,

"PH":750,

"TH":450,

"VN":330000,

"MY":60,

"ID":200000

}

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
campaignId | Number | Yes | Campaign id which you want to add into.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
adgroupViewDTOList | Object[] | Yes | Adgroup list  
adgroupName | String | Yes | The adgroup name, normanlly is the product name.  
autoItemSelect | String | Yes | The way the product be selected.1:manual(I want to select products manually from my store.);2:auto(Let Lazada optimize the products within the campaigns in real-time to maximize the campaigns' performance).This must be the same as the campaign.  
bidPrice | String | Yes | Let Lazada automatically set cost-effective bid prices for your products.Please make sure this field is meeted the standard above.  
itemId | Number | Yes | Product id.  
autoCreative | Number | Yes | Let Lazada automatically set creatives for your products.1:ON;0:OFF.This must be the same as the campaign.  
autoKeyword | Number | Yes | Let Lazada automatically set keyword for your products.1:manual(I want to select keywords manually for my product selection.);2:auto(Let Lazada optimize the keywords relating to your products in real time to maximize the campaigns' performance).This must be the same as the campaign.  
bidwordViewDTOList | Object[] | No | Bid word list.This field work when the scene is sponsor search.  
keyword | String | No | The specific keyword.eg:shoe.Max count of keyword of one adgroup is 100.  
bidPrice | String | No | Let Lazada automatically set cost-effective bid prices for your products.Please make sure this field is meeted the standard above.  
audienceViewDTOList | Object[] | No | This setting allows you to bid higher on premium audiences that are more likely to convert in your store.This field work when the scene is sponsor recommend.  
adCrowdTag | Number | No | 1:on store visitors in the past 15 days;2:on in-market audiences for similar products;3:Store Awareness Audience;4:Store Interest Audience  
discount | Number | No | The discount you want to give.eg:10 means 10% discount.  
  
# deleteCampaign

**Description:** Delete campaign.

**Timeout Period：** the api timeout is 3s, max qps is 100, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
campaignIdList | Number[] | Yes | Campaign id list.Make sure all the campaign id is real and valid.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
  
# deleteAdgroupBatch

**Description:** Delete adgroup batch.

**Timeout Period：** the api timeout is 3s, max qps is 100, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
adgroupIdList | Number[] | Yes | Adgroup id list. Make sure all the adgorup id is real and valid.  
  
  
  


# getAccountSignInfo

**Description:** Get seller account sign status. This api is to check wheather the seller sign the T&C or not.

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

此接口无入参

  


# getAutoTopUpOptionOneConfig

**Description:** Get auto top up option one config.

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

此接口无入参

  


  


# getCampaign

**Description:** Get campaign list with bizCode by seller.

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
bizCode | String | Yes | Discovery:sponsoredSearch.Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
campaignId | Number | Yes | The campaign id, make sure this id is real and valid.  
  
# getCampaignCount

**Description:** Get campaign count with bizCode for each solution type.

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

  


## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
  
# getLatestSignInfo

**Description:** Get the latest url of sign(T&C).

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

此接口无入参

  


  


# getReportOverview

**Description:** Get report overview for the bizCode.

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
lastStartDate | String | Yes | The data window "last start date" and data window "last end date" represent the last period based on the current period with the same duration , and it shows the campaign's performance during that period. For example, if a seller chooses a data window "start date" and " end date" from June 1st to June 30th, 2023, then the data window "last start date" and "last end date" is from May 2nd to May31th,the it means that the performance of the campaign will be calculated for the period between those dates.  
endDate | String | Yes | The data window "start date" and data window "end date" represent the period during which the campaign's performance is calculated. For example, if a seller chooses a data window from June 1st to June 30th, 2023, it means that the performance of the campaign will be calculated for the period between those dates.End date, make sure later than or equal to startDate.  
useRtTable | Boolean | Yes | If you need to search data for today, then use true, otherwise false.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.  
lastEndDate | String | Yes | The data window "last start date" and data window "last end date" represent the last period based on the current period with the same duration , and it shows the campaign's performance during that period. For example, if a seller chooses a data window "start date" and " end date" from June 1st to June 30th, 2023, then the data window "last start date" and "last end date" is from May 2nd to May31th,the it means that the performance of the campaign will be calculated for the period between those dates.  
startDate | String | Yes | The data window "start date" and data window "end date" represent the period during which the campaign's performance is calculated. For example, if a seller chooses a data window from June 1st to June 30th, 2023, it means that the performance of the campaign will be calculated for the period between those dates.  
  
  


  


# getReportOverviewMetric

**Description:** get report overview metric

The data window "start date" and data window "end date" represent the period during which the campaign's performance is calculated. For example, if a seller chooses a data window from June 1st to June 30th, 2023, it means that the performance of the campaign will be calculated for the period between those dates.

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
metricType | Number | Yes | The type pf metric.1:spend;2:impressions;3:clicks;4:ctr;5:units sold;6:revenue;7:cpc;8:roi;9:store order;10:store a2c;11:product order.  
endDate | String | Yes | End date.  
useRtTable | Boolean | Yes | If you need to search data for today, then use true, otherwise false.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.  
startDate | String | Yes | Start date.  
  
  


  


# listCategory

**Description:** List category that you have in your shop. It usually displayed within the Product selection module

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
parentId | Number | No | The category parent id.  
  
# listKeywordByAdgroup

**Description:** List keyword by adgroup. It usually displayed within the keyword selection module for adding keyword for existing campaign

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
campaignObjective | Number | Yes | Your campaign objective helps determine your bidding strategy - Traffic objective helps you to increase the number of clicks to your store, while sales objective helps to increase your store’s sales.1:Traffic;2:Sales.Please noted that this parameter might will be updated since Mid of July ，2023  
campaignType | Number | Yes | Unlock different ways to bids, select products, and keywords with campaign types.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
itemId | Number | Yes | Product id.Please make sure the item id is real and valid.  
adgroupId | Number | Yes | Adgroup id.Please make sure the adgroup id is real and valid.  
  
# listKeywordByItem

**Description:** List keyword by item.It usually displayed within the keyword selection module for adding keyword during new campaign creation

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

  


## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
campaignObjective | Number | Yes | Your campaign objective helps determine your bidding strategy - Traffic objective helps you to increase the number of clicks to your store, while sales objective helps to increase your store’s sales.1:Traffic;2:Sales.  
campaignType | Number | Yes | Unlock different ways to bids, select products, and keywords with campaign types.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
itemId | Number | Yes | Product id.Please make sure the item id is real and valid.  
  
# searchAdgroupList

**Description:** Search adgroup with bizCode by seller. It can be shown on camapaign detail page

**Note:** The startDate and endDate below is use to query data indicators of these campaign, not use to to query by campaign duration.

The data window "start date" and data window "end date" represent the period during which the adgroup's performance is calculated. For example, if a seller chooses a data window from June 1st to June 30th, 2023, it means that the performance of the adgroup will be calculated for the period between those dates.

**Timeout Period：** the api timeout is 3s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
pageSize | Number | Yes | Page size.No more than 200.  
endDate | String | Yes | Campaign end date.Make sure this is later than startDate.  
campaignId | Number | Yes | Campaign id.Make sure this is real and valid.  
pageNo | Number | Yes | Page number.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
adgroupName | String | No | Adgroup name for fuzzy search.  
startDate | String | Yes | Campaign start date.  
onlineStatus | Number | No | The campaign online status.1:Online;0:Offline;9:deleted.Please do not use other num.  
  
# searchCampaignList

**Description:** Search campaign list with bizCode for sellers. The data window "start date" and data window "end date" represent the period during which the campaign's performance is calculated. For example, if a seller chooses a data window from June 1st to June 30th, 2023, it means that the performance of the campaign will be calculated for the period between those dates.

**Timeout Period：** the api timeout is 10s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

**Notes:** The startDate and endDate below is use to query data indicators of these campaign, not use to to query by campaign duration.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
startDate | String | Yes | Campaign start date.  
endDate | String | Yes | Campaign end date.Make sure this is later than startDate.  
pageNo | String | Yes | Page number.  
pageSize | String | Yes | Page size.No more than 200.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
onlineStatus | Number | No | The campaign online status.1:Online;0:Offline;9:deleted.Please do not use other num.  
  
# searchKeyword

**Description:** Search keyword with specific word on keyword selection module

**Timeout Period：** the api timeout is 10s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
campaignObjective | Number | Yes | Your campaign objective helps determine your bidding strategy - Traffic objective helps you to increase the number of clicks to your store, while sales objective helps to increase your store’s sales.1:Traffic;2:Sales.  
campaignType | Number | Yes | Unlock different ways to bids, select products, and keywords with campaign types.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
itemQuery | String | Yes | The word you do not want to put in the result.  
itemId | Number | Yes | Product id.Make sure this item is real and valid.  
searchWord | String | Yes | The specific word.eg:shoe  
  
# searchProductWithPage

**Description:** Search product on Product Selection Module for Campaign Creation and Adding Products to Existing Campaigns

**Timeout Period：** the api timeout is 10s, max qps is 100, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

**Notes:** This api should be invoked before you do add a campaign/solution.Some of the params below is you clicked In the previous step, like campaignObjectLive,maxCpc,campaignType.And we will search product with some algo indicator(bidPrice) using your campaignObjectLive,maxCpc,campaignType.

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
brandName | String | No | Prodct brand name.  
campaignType | Number | Yes | Unlock different ways to bids, select products, and keywords with campaign types.Please noted that this parameter might will be updated since Mid of July，2023  
pageSize | Number | Yes | Page size.No more than 200.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
placementList | Number[] | Yes | Placements determine where shoppers will see your promoted products.3:Search Result Page;4:Just For You Page  
productName | String | No | Product name to fuzzy search.  
campaignObjectLive | Number | Yes | Your campaign objective helps determine your bidding strategy - Traffic objective helps you to increase the number of clicks to your store, while sales objective helps to increase your store’s sales.1:Traffic;2:Sales.Please noted that this parameter might will be updated since Mid of July，2023  
eligible | Number | Yes | Only search product which is eligible|ineligible.1:eligible;0:ineligible.  
pageNo | Number | Yes | Page number.  
sellerSku | String | No | Product sellerSku.  
maxCpc | String | Yes | Max bid determines the highest amount that you're willing to pay for a click on your promoted product.-1 means automated bidding setting  
categoryId | Number | No | Input category id to exact search.  
itemIdBlackList | Number[] | No | Input item id which you do not want put into result.  
  
  


# updateAdgroupBatch

**Description:** Update adgroup batch.

**Timeout Period：** the api timeout is 10s, max qps is 100, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

**Notes:** You could invoke this api to update your adgroup status for phase 1.The adgroup will only be _advertised when campaign & adgroup status is online._

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
adgroupViewDTOList | Object[] | Yes | Adgroup list  
adgroupId | Number | Yes | Adgroup id.  
switchStatus | String | Yes | Is the adgroup online rightnow.1:ON:0:OFF.Please do not use other num.  
  
# updateCampaign

**Description:** Update campaign with status field.

**Timeout Period：** the api timeout is 10s, max qps is 100, make sure do not over these num, especially qps, otherwise you may be blacklisted or limited request count for a while.

**Notes:** You could invoke this api to update your campaign duration,name,budget and status.

The campaign "Start date" and campaign"end date" represent the period during which a campaign will running. For example, if a campaign has a start date of June 1st, 2023 and an end date of June 30th, 2023, it means that the campaign will running from June 1st to June 30th, 2023, provided that the campaign has a valid budget, promoted products, and the seller has sufficient balance.

  


"minBudgetMap":{

"SG":10

"PH":100,

"TH":100,

"VN":50000,

"MY":4,

"ID":25000

},

"maxBudgetMap":{

"SG":10000,

"PH":1000000,

"TH":1000000,

"VN":200000000,

"MY":100000,

"ID":100000000

},

## Parameters

**Name** | **Type** | **Required or not** | **Description**  
---|---|---|---  
campaignId | Number | Yes | Campaign id.Make sure the id is real and valid.  
campaignName | String | No | Campaign name.No more than 200 char.  
startDate | String | No | Campaign start date.  
endDate | String | No | Campaign end date.Make sure end date is later than or equal to start date and current time.  
dayBudget | String | No | Budget indicates the maximum amount you’re willing to pay each day.This field need to meet the standard above.  
bizCode | String | Yes | Decided to choose which advertisement solution.SD:sponsoredSearch.Phase 1 only support sponsoredSearch as bizCode which is shown as Sponsor Discovery in ASC.  
switchStatus | Number | No | Campaign swtich status.1:Online;0:Offline.Please do not use other num.