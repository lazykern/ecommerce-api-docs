Lazada Open Platform provides an API testing tool named "API Explorer" for you to test the APIs on the platform. 

Take the following steps to start the API Explorer:  
1\. Open the **APP Console** and click **Manage** for your application.  
2\. On the **App Management** page, click **API Explorer** from the left navigation panel.  
3\. On the API Explorer page, enter the marketplace and API name, and specify the parameters to test APIs.

Please note that the API Explorer uses online data from the production environment.

## Parameter description

Description of the API Explorer parameters is as follows:

**Name** | **Description** | **Sample value**  
---|---|---  
Region | Name of the marketplace (6 Lazada Ventures). For details about the URL of the production environment for each venture, see [API endpoint URLs](<https://open.lazada.com/apps/doc/doc?nodeId=10443&docId=108065>). | Singapore  
API Path | Path of the API to be tested. For the list of API path, see [API name mapping](<https://open.lazada.com/apps/doc/doc?nodeId=10557&docId=108146>). | /brands/get  
HTTP Method | Most APIs are called via GET, some calls that get additional request data are sent via POST. | GET or POST  
App Key | The unique identity of your application on Lazada Open Platform, which is generated when the application is created. | 100126  
Access Token | The token that is required for your application to access sensitive data of sellers. For details, see [Configure seller authorization](<https://open.lazada.com/apps/doc/doc?nodeId=10777&docId=108260>). |   
Business parameters | The business parameters for the API that is to be tested. |   
Request | When the parameters are specified, click the **Start Test** button, the request URL is generated and displayed in the **Request** field. | For the "/brands/get" API, the request URL can be: 
    
    
    https://api.lazada.sg/rest/brands/get?offset=100&limit=1&app_key=100126&sign_method=hmac&timestamp=1520045034634&sign=0CBC5F17611DB5B3A9D66926A3D1C3CF  
  
Response | The API response body for the specified parameters. | For the "/brands/get" API, the response can be: 
    
    
    {
      "data": [
        {
          "name": "Cold Mountain",
          "brand_id": 23980,
          "global_identifier": "cold_mountain"
        }
      ],
      "code": "0",
      "request_id": "0be6fdce15200450346451004"
    }