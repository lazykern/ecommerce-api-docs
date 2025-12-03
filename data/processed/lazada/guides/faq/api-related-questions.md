This section lists frequently asked questions about the Lazada APIs and recommended resolution.

  

**Q:** How to list product variations with the **CreateProduct** API?**A:** The product variations must be listed with a single request. That is, in the request body of the **CreateProduct** API, list the product variations in the tags. You can use ‘AssociatedSku’ tag if you want to add some SKUs to an existing product.

  

**Q:** Why is the total number of products shown on the Seller Center portal different from that returned by the **GetProduct** API?**A:** The total number of products shown on the Seller Center portal is the number of SKUs, but the number of products returned by the **GetProduct** API is the number of items. That is, SKUs include variations of items.Please also note that the returned results by API calls are determined by the specified parameters like Filter, Limit, Offset, and time conditions. The maximum number of products returned by a single **GetProduct** call is 500. If no limit value is specified, the **GetProduct** call returns 20 products by default.

  

**Q:** Why does the **GetDocument** API fail to return the needed documents?**A:** Make sure that the status of the specified order item is “RTS” (by calling **SetStatusToReadyToShip**) before calling the **GetDocument** API. Otherwise, the error message E034 will be returned.

  

**Q:** Why does the **GetBrands** API fail to return a known brand?**A:** Check whether the specified parameters filter out some brands. The maximum number of brands that can be returned by a single request is 1,000. If the brand cannot be found in the Seller Center portal either, contact the service team.

  

**Q:** What does the “liverejected” QC status (returned by the **GetQcStatus API**) mean?**A:** The “liverejected” QC status means that online SKUs are made offline by the QC team because of qualification reasons.

  

**Q:** What do the mangrove errors mean? Who should I reach out to?**A:** These errors are caused by a failure to comply to our platform product content rules. These rules are set by the Lazada Content team, please reach out to the Partner Seller Support (<https://sellercenter.lazada.sg/seller/helpcenter>) to find out more about the rules and what you should do. 

We have compiled some frequently encoutered mangrove errors below for your reference.

![image](https://img.alicdn.com/top/i1/LB1rQsceL5G3KVjSZPxXXbI3XXa)

  

**Q:** If I have other technical questions about API, whom shall I contact for technical support?**A:** You can get technical support through DingTalk group ID 24655026315 for English Support, and DingTalk group ID 21909623 for Chinese Support ([Link to download and install DingTalk](<https://tms.dingtalk.com/markets/dingtalk/download>)).