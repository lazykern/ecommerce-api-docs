# 1\. Introduction

The Lazada Sponsored Solutions API provides developers with a programmatic interface to directly interact with the Lazada Sponsored Solutions platform, streamlining the management of complex or large Lazada Sponsored Solutions accounts and campaigns

Here are some common use cases:

  * Automated account management: 


    * Lazada Sponsored Solutions API has made it possible to automate routine account management tasks, such as creating new campaigns, set daily budgets, and set start and end date for campaign. This saves time and reduces the need for manual input


  * Customized reporting


    * The Lazada Sponsored Solutions API supports a wide range of data points and metrics, allowing developers to create custom reports that meet their specific needs. 


  * Sponsored Solutions campaign management based on inventory


    * The Lazada Sponsored Solutions API allows developers to integrate inventory data from their eCommerce platform with their Lazada Sponsored Solutions campaigns


  * Integration of Lazada Sponsored Solutions by ERP* software into respective system


    * Brands, agency and sellers can manage their campaigns more easily and monitor their Sponsored Solutions campaign performance, without having to switch between different platforms



Note: 

ERP stands for Enterprise Resource Planning, which is a software system designed to manage and automate end-to-end business processes across a company.

The use of LSS Open API is subject to Lazada Open Platform Developer Agreement and Terms of Services.

  


## Lazada Sponsored Solutions API can be useful for:

By leveraging the Lazada Sponsored Solutions API, software can be built to manage accounts at the granular level of customers and keywords, offering the same capabilities as the Lazada Marketing Solutions UI, but programmatically. The API is beneficial for various types of companies, including:

  * Media agencies
  * Enterprise Resource Planning (ERP) software system
  * Big brands managing a large number of accounts, with needs beyond the capabilities of the Lazada Sponsored Solutions UI



  


## Open API Phase 1 Overview:

Phase 1 includes Sponsored Discovery solution scope of Lazada Sponsored Solutions. Discover the benefits of Sponsored Solutions API Phase 1 as below -

Campaign management| 

  * Get campaign information


  *     * Campaign Name, Campaign ID, Budget, Duration. 
    * Sync up the Campaign list


  * Search campaign


  *     * Search the campaign by keywords


  * Create campaign


  *     * Set a name for the campaign
    * Set Daily budget
    * Set start and end dates of the campaign (The default Campaign objective is sales-oriented, and the Campaign type is automated)


  * Delete campaign
  * Product management 


  *     * Show Product information (Product name, Product quality score, Units sold, quantity, retail price, PDP PV, CVR)
    * Update products status (You can set campaign product status on or off)
    * Search products


  *     *       * Search the product by keywords
      * Product Category filtering

Developers can refer to this [API documentation](<https://open.lazada.com/apps/doc/api?path=%2Fsponsor%2Fsolutions%2Fcampaign%2FgetCampaign>) for further details  
---|---  
Sponsored Solutions campaign tools and setting| 

  * Auto top up setting


  *     * API will provide you with suggestions for both the auto top-up threshold and the amount to top up
    * Auto top up setting on and off


  * Sign up to the Sponsored discovery terms and conditions

Developers can refer to this [API documentation](<https://open.lazada.com/apps/doc/api?path=%2Fsponsor%2Fsolutions%2Fwallet%2FmodifyAutoTopUpOptionOneConfig>) for further details  
Reports and Insights| 

  * Get report overview


  *     * You can see 'product' information in the report (Product name, Product quality score, Units sold, quantity, retail price, PDP PV, CVR)
    * You can see insights from the campaign (Spend, impressions, Clicks, Store units sold, Store Revenue, CPC, Store ROI)


  * Get report trend chart


  *     * You can draw trend chart by getting x-axis (time) and y-axis (spend and impressions) data from API

Developers can refer to this [API documentation](<https://open.lazada.com/apps/doc/api?path=%2Fsponsor%2Fsolutions%2Freport%2FgetReportOverviewMetric>) for further details  
  
## It is important to note that the Lazada Sponsored Solutions API Phase 1 does not support:

  * Other Solutions besides Sponsored Discovery
  * Manual top up
  * Sponsored Discovery key words editing
  * Managing bid price



# 2\. Getting Started

## How to get started with Lazada Sponsored Solutions API:

Follow these steps to get started with Lazada API:

  * [Become a developer](<https://open.lazada.com/apps/doc/doc?nodeId=10396&docId=108001>) \- Register a UAC (unified account center) account and sign up as a Lazada developer.
  * [Register your application](<https://open.lazada.com/apps/doc/doc?nodeId=10398&docId=108002>) in one of the application categories - Submit the request and Lazada admins will review and approve your request.
  * [Retrieve App Key and App Secret](<https://open.lazada.com/apps/doc/doc?nodeId=10433&docId=108055>) of your application - The unique identity of your application on the Lazada Open Platform.
  * [Request API permission](<https://open.lazada.com/apps/doc/doc?nodeId=10535&docId=108131>) for your application, so that your application can initiate calls to Lazada APIs.
  * [Start development of your application](<https://open.lazada.com/apps/doc/doc?nodeId=10536&docId=108132>) \- Learn how to interact with Lazada API. You could find more technical details from the Developer’s Guide section.



## How to get started with Lazada Sponsored Solutions API:

  * [Lazada Sponsored Solutions API List](<https://open.lazada.com/apps/doc/api?path=%2Fsponsor%2Fsolutions%2FaddSolution>) \- Scroll down to the bottom to see the list of API that we provide for this version
  * [Sponsored solution API best practice](<https://open.lazada.com/apps/announcement/detail?spm=a1zq7z.27201205.0.0.5a707c737yI8Po&docId=1816>) 《Sponsored Solutions API best practice》



  


# 3\. Endpoints

Here are a list of service endpoints by country:

**Region**| **Endpoint**  
---|---  
Vietnam| <https://api.lazada.vn/rest>  
Singapore| <https://api.lazada.sg/rest>  
Philippines| <https://api.lazada.com.ph/rest>  
Malaysia| <https://api.lazada.com.my/rest>  
Thailand| <https://api.lazada.co.th/rest>  
Indonesia| <https://api.lazada.co.id/rest>  
  
Please visit this link for a comprehensive list of addSolution end-points: [https://open.lazada.com/apps/doc/api?path=%2Fsponsor%2FSolutions%2FaddSolutions](<https://open.lazada.com/apps/doc/api?path=%2Fsponsor%2Fsolutions%2FaddSolution>)

# 4\. Typical use cases and Tips

  1. **Notification**  
Access the DingTalk or other instant messaging app notification system, and notify the stakeholders in real time, thus Ops can minimize the need to constantly monitor ad performance data.
  2. **Monitoring**  
According to real-time reports and defined monitoring indicators, such as cost/roi/pv/uv, etc., real-time notification to Sponsored Solutions campaign operations , or intelligent Sponsored Solutions campaign management. For example, if the ROI of a particular campaign falls below the threshold set previously, the Sponsored Solutions campaign can be automatically stopped or the Sponsored Solutions campaign of a specific product can be stopped via the API. This allows you to optimize your marketing spend and increase ROI without having to constantly monitor performance data. With the Lazada Sponsored Solutions API, you can streamline your marketing management process and achieve greater efficiency and effectiveness in your campaigns.
  3. **Report**


     1. Cross-store and multi-dimensional data analysis
     2. Analyze data in a more comprehensive and tailored manner



This allows for a more customized approach to your marketing strategies, resulting in better performance and higher ROI. Instead of relying on general analysis, you can drill down into specific areas of your campaign and identify opportunities for optimization.

  4. **Creative (In phase 2)**  
The feature can automatically filter out low-efficiency creatives and replace them on a regular basis, saving time and effort for the user. This ensures that the creatives are always optimized for the best performance.
  5. **Delivery (Bid management in phase 2)**  
Batch operations of campaigns/units, such as creating, pausing, enabling, and adjusting bids in batches through excel. Making campaign management more efficient and saving you valuable time.



# 5\. Technical support resources

  * If you have any tech-related queries, our dedicated tech support team is here to help. 


    * To connect with our technical support, please download and register for [DingTalk](<https://www.dingtalk.com/en>) app
    * You can reach out to them on Dingtalk by searching for the tech support group using the group ID 21783515



# 6\. Conclusion

The Lazada Sponsored Solutions API provides programmatic access to the Lazada Sponsored Solutions platform, enabling developers to manage large or complex Lazada Sponsored Solutions accounts and campaigns more efficiently.

With the API, you can build software that manages accounts from the customer level down to the keyword level, automate tasks such as filtering out low-efficiency creatives and replacing them, and perform cross-store and multi-dimensional data analysis.

The API also allows for batch operations of campaigns/units, such as creating, pausing, enabling, and adjusting bids in batches through excel, and offers customized data analysis to help you make informed decisions.

Using our API can save you time, increase efficiency, and help you optimize your Sponsored Solutions campaign campaigns more effectively.

**Next Steps:**

If you're interested in using Lazada Sponsored Solutions API, please review the documentation to get started.

Explore additional features such as our advanced data analysis tools and automated creative filtering.

For agencies, consider participating in our [Preferred Partner Program](<https://www.lazadasolutions.com/student/activity/1516331-lazada-sponsored-solutions-preferred-partner-program>) for added benefits and support.

Contact our customer support team if you have any questions or need assistance getting started.