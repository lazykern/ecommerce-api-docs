Once your developer account is approved, you can create new Apps in the Shopee Open Platform Console [**_Create App_**](<https://open.shopee.com/myconsole/management/app>) page.

# App types

 

There are several types of Apps on Shopee Open Platform, each designed for different purposes.

 

 

  * **ERP System** : Such Apps are for managing key business processes. This App type is suitable if you provide software services to Shopee sellers.
  * **Product Management** : Such Apps are for managing product-related processes.
  * **Order Management** : Such Apps are for managing processes related to order and fulfillment.
  * **Accounting and Finance** : Such Apps are for managing processes related to finance and order reconciliation processes.
  * **Marketing** : Such Apps are for managing processes related to marketing.
  * **Seller In-house System** : Use this App type if you are a Shopee seller managing your own Apps.
  * **Customer Service** : Such Apps are for managing processes related to customer service.



 

Different types of developer accounts can create different types of Apps.

 | **                                                                              Developer account types**  
---|---  
**App Types**  
 | **Third-party Partner Platform (ISV)**| **Registered Business Seller**| **Individual Seller**| **Individual Third Party***  
 **ERP System**|                        ✓|  |  |    
**Product Management**|                        ✓|  |  |                ✓  
**Order Management**|                        ✓|  |          |                ✓  
**Accounting and Finance**|                        ✓|  |  |                ✓  
**Marketing**|                        ✓|  |  |    
**Customer Service**|                        |  |  |    
**Seller In House System**|   |                    ✓|            ✓|    
  
 

The **Individual Third Party** developer account types are no longer supported and have been replaced with **Individual Seller** , **Registered Business Seller** , and **Third-party Partner Platform (ISV)**.

 

If you originally registered as an **Individual Seller** or **Registered Business Seller** but your team has grown and started to serve other sellers, you can switch to **Third-party Partner Platform (ISV)**. Once approved, your App type will automatically change from Seller In-house System to ERP System. For more details, please see our [_FAQs_](<https://open.shopee.com/faq?top=174&sub=175&page=1&faq=207>), Q.3.

 

Different types of Apps have different API and push permissions. You can create different types of Apps according to your needs.

**App type**| **API permissions**  
---|---  
ERP System| All API except Chat API and Ads API  
Seller In-house System| All API including Chat API  
Product Management| View [_API permission list_](<https://open.shopee.com/faq?top=186&sub=187&page=1&faq=236>)  
Order Management| View [_API permission list_](<https://open.shopee.com/faq?top=186&sub=187&page=1&faq=237>)  
Accounting and Finance| View [_API permission list_](<https://open.shopee.com/faq?top=186&sub=187&page=1&faq=238>)  
Marketing| View [_API_](<https://open.shopee.com/faq?top&sub=187&page=1&faq=239>)[ _permission_](<https://open.shopee.com/faq?top=186&sub=187&page=1&faq=239>)[ _list_](<https://open.shopee.com/faq?top&sub=187&page=1&faq=239>)  
Customer Service| View [_API permission list_](<https://open.shopee.com/faq?top=186&sub=187&page=1&faq=240>)  
Ads Service| View [_API Permission list_](<https://open.shopee.cn/faq/281>)  
  
 

Learn more about the [_notifications available under Push Mechanism for different types of Apps_](<https://open.shopee.com/developer-guide/18>). 

 

⚠️**Note**  
 Newly created Apps only have v2.0 API permissions, and cannot call v1.0 APIs.  
 You can check your App permissions under the **API Permission** section on the App details page.![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=eDqo5LJt8%2B5FXmB9YRLwFDIQe%2Bjsw1%2FP5RpxiwdttN9RyGHSgosQZPm6hIsI5Sjh%2FQwMw4tecSp5JvoJL5KvvQ%3D%3D&image_type=png)  
---  
  
# Creating an App

 

1\. Log in to Shopee Open Platform [Console](<https://open.shopee.com/myconsole/management/app?from=header>), select **Create App**. On the **Create App** page under **Basic Information** , you can edit your **App Type** , **App Name** , **App Description** , and **App Logo**.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=9jpXuffGmGDFRjflp%2B1Xr%2Be67sF7Y8KB8%2BdIswqz5WxrEUs05rDEa1gMgH3KlMcoPBXVGxpUgmbJrdg%2Ftf5f6A%3D%3D&image_type=png)![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=3hgBqdB%2BbBmXuq5rNdubrzeXFs2eHNu9TWOh2tYkDJ0k3Hlv5%2FdLSoTmAiuFO9hKsDyrexrlzS%2BE5ou%2BOGHWAg%3D%3D&image_type=png)

 

2\. After you’ve successfully created your App, you’ll get a Test Partner ID and Test Key. These can only be used for testing in the sandbox environment, but not in the production environment. 

# Submitting your App to Go Live

 

1\. Once you’ve finished testing your App, select the App from the **App List** page, then select **Go Live**.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=moZtmnGBMiju5DsqeXERmvL1Y00tYzWQHOqYEkIshwtNYsZl8npGg2VnOkMe8TOHwlIqi8yJsrx8ysQuBc2EdA%3D%3D&image_type=png)

 

2\. On the **Go Live** page, fill in the relevant information.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=%2FrMEmFFL1Bcs1lTymV0rt2p%2FxT9rtevFz%2B%2BNyKeJItDC5N78KbSWGGatALzEwM7onu0y6Y5U7GKIyVcAC3eMyQ%3D%3D&image_type=png)

 

3\. Your App will be reviewed 24 hours after submission. Once approved, you can view the **Live Partner_id** and**Live Key** corresponding to the App under the **App Key** section. These can be used in the production environment.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=AkT4ZdS0c%2FqeaMFqYaqudvuE4q558KVUzlqpDPRen1VIc77y4%2BYBz93VTh%2B9HD5UPyFmS3LzmScBGzDtaEnpSQ%3D%3D&image_type=png)

# Switching to the production environment

 

Once you're ready, you can switch to the production environment.

1\. Switch to the **Live Partner_id** and **Live Key** to complete the authorization.

2\. Switch to the HTTP Address of the production environment. You can find the HTTP Address in your API documents. Here’s an example: 

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=gAD9FTupnb%2FbC5yNJW1VgvottDpI9JK96WCPuSK%2BhJcVxe2vpsDDObRs2nyQB38jbW7jhuRfVqgK5cnXJBtx0w%3D%3D&image_type=png)⚠️**Notes**  
 

  * [_https://openplatform.shopee.cn/_ ](<https://openplatform.shopee.cn/>)is only open to developers in Mainland China.
  * [_https://partner.shopeemobile.com/_](<https://partner.shopeemobile.com/>) is open to local developers.

  
 Select the HTTP Address that corresponds to the server location where you want to call the Open API.  
---  
  
 

3\. (Optional) If you need to subscribe to [_Push Mechanism notifications_](<https://open.shopee.com/developer-guide/18>), you can enable the settings within the production environment. 

 

4\. (Optional) If you need to add a whitelist of Shopee addresses in your system, please call the [_v2.public.get_shopee_ip_ranges_](<https://open.shopee.com/documents/v2/v2.public.get_shopee_ip_ranges?module=104&type=1>) API of the production environment to obtain the IP address of the production environment.

# Viewing your App status 

Once you’ve created your App, you’ll see 1 of the following App statuses. Each status has a different set of restrictions that limit the use of the App.

**Status**| **Description**| **Product environment restrictions**  
---|---|---  
Developing| App is under development| 1\. Apps cannot be authorized to access shop data in the production environment2\. Unable to call production environment APIs  
Online| App is online| 1\. Apps can be authorized to access shop data in the production environment2\. Able to call production environment APIs  
New App authorizations restricted | New authorizations for the App are restricted| 1\. Apps cannot be authorized to access shop data in the production environment2\. Existing App authorizations to access shop data are not affected3\. Able to call production environment APIs  
   
API calls restricted| App is restricted from calling all APIs| 1\. Apps cannot be authorized to access shop data in the production environment2\. Existing App authorizations to access shop data are not affected3\. Unable to call production environment APIs  
Suspended| App is offline| 1\. Apps cannot be authorized to access shop data in the production environment2\. Existing App authorizations to access shop data will be removed3\. Unable to call production environment APIs  
⚠️**Note**  
 If a developer violates Shopee Open Platform policies, their App status may be changed to one of the following:

  * New App authorizations restricted
  * API calls restricted
  * Suspended

If your App status is updated, you will receive an email notification explaining why in your developer account’s registered email. You can also view the reason on Shopee Open Platform Console.  
 Regardless of the App status, you can continue to use the Test Partner ID in the sandbox environment to authorize shops and test APIs.  
---  
  
# Resetting your App keys

 

If your App keys have been compromised or want to change them for other security reasons, you can reset your keys.

 

1\. To reset your App keys, select the App, then select **Edit**.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=jIju3cTxx5XE%2FPR8N8SK%2BYD3cemArIoSgtFZl0xbBV7wsiv7pVXKLzsdb2KuFyKTQ0TRMx4dMqB5R7zrnciYcg%3D%3D&image_type=png)

 

2\. Under **Basic Information** , select **Reset** under **Test Key** or **Live Key**. Then, select **Submit** at the bottom of the page to complete the key reset.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=dH6SzFRIPm44VPPzvmCyG4%2BuCCmf7N3OYTlVuYtub3KJzq1rtEESThLeVtYfatlIhBBLpAIatuh9%2FVdqkhwlkQ%3D%3D&image_type=png)

# Deleting an App

If you no longer need an App, you can select the App and **Delete** it.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=%2BEpsEt75MuvcLpKaFSc4uiPLdwJOLtU5%2B8892L8BHP54hPo%2B6pd1WTzA%2Bd0xZ72Yxnc%2BcFGo55OylpLDsaF0bg%3D%3D&image_type=png)⚠️**Note  ** After you delete an App, these items will become invalid:

  * Partner ID and Key obtained 
  * All existing shop authorizations

Do proceed with caution.  
---  
  
# FAQs

 

**Q1: What is the maximum number of Apps I can create?**

A: You can create up to 10 Apps.

 

**Q2: Can an App authorize shops from different markets?**

A: Yes.

 

**Q3: Is there a maximum number of shops an App authorize shops?**

A: Currently, there is no limit.

 

**Q4: Can the review process for an App to go live be expedited?**

A: No. You should submit your App for review at least 24 hours before the expected live date to ensure that it can go live on time in the production environment. 

 

**Q5: If my system is using a dynamic IP address, how do I fill in the Declaration of IT Assets?**

A: You can select the option **IP address(es) unavailable** and add your reason below.

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=pfRRBnJkqxA2pmnIKhE6HPt4%2FWcwtXeNs1A2vRWUsUdMP%2F5SvZJ8yOSQ%2BMW5j5jhylIzLB6WG1sVdWu%2FmeKDJw%3D%3D&image_type=png)

⚠️ Note: Y _ou’re strongly encouraged to use static IP addresses. If you use dynamic IP addresses, we will request for regular declarations of your IT assets to perform security checks._

 

**Q6: When do I need to update my IT assets?**

A: Once your static IP address has changed, please update your IT assets in the Shopee Open Platform Console.

 

**Q7: My IT asset IP address exceeds the character limit of the text box**

A: You can select the option **IP address(es) unavailable** , add your reason in the text box below. Then, submit the [_IT Assets form_](<https://shopeeregionalops.typeform.com/to/TLAcHECK?typeform-source=open.shopee.com>).

![](https://open.shopee.com/opservice/api/v1/image/download/?image_id=nB2hfjKZ9Yg6MxXnlqle9R9XQms6W9oaes%2BI2tyyJPJhc1lPha%2Bh1j5nSiBp8u0xdrjcyJ50qZkRnbwpR2TjTA%3D%3D&image_type=png)