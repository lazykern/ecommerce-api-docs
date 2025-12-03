Lazada Open Platform API supports both HTTP and HTTPS communication protocol. To ensure data security, it is recommended to make API requests using HTTPS protocol. 

While most APIs are called via GET, some calls that get additional request data are sent via POST. However, sometimes the data that need to be supplied are more than what can be transported in request parameters. In those cases, additional data is sent to the server using a POST request. The request body must be in XML format. All data (including parameter names and values) must be UTF8-encoded.

Each HTTP request URL must include the path of an API. For example, the request for the “/order/get” API should be "[https://api.lazada.sg/rest/order/get"](<https://api.lazada.sg/rest/order/get>). The common parameters and business parameters are included in the request or sent via post.

All API calls return a response document, which indicates the status of the operation (either Success or Error) and optionally provides results and/or details related to the specified action. The response is in JSON format.