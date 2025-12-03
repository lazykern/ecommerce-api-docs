Lazada Open Platform API is called based on the HTTPS protocol, so programming languages that have an HTTPS access library can be used to call the API. You can use the official SDK directly or assemble HTTP requests according to the Lazada Open Platform protocols to call the APIs.

## Using official SDK to call API

Take the "/order/get" API as example:

JAVA sample code 
    
    
    LazopClient client = new LazopClient(url, appkey, appSecret);
    LazopRequest request = new LazopRequest();
    request.setApiName("/order/get");
    request.setHttpMethod("GET");
    request.addApiParameter("order_id", "16090");
    LazopResponse response = client.execute(request, accessToken);
    System.out.println(response.getBody());
    Thread.sleep(10);
    

.NET sample code
    
    
    ILazopClient client = new LazopClient(url, appkey, appSecret);
    LazopRequest request = new LazopRequest();
    request.SetApiName("/order/get");
    request.SetHttpMethod("GET");
    request.AddApiParameter("order_id", "16090");
    LazopResponse response = client.Execute(request, accessToken);
    Console.WriteLine(response.IsError());
    Console.WriteLine(response.Body);
    

PHP sample code
    
    
    <?php
        include "../IopSdk.php";
    
       $c = new LazopClient(url,appkey,appSecret);
       $request = new LazopRequest('/order/get','GET');
       $request->addApiParam('order_id','16090');
        
       var_dump($c->execute($request, $accessToken));
    ?>
    

Ruby sample code
    
    
    client = LazopApiClient::Client.new(url, appkey, appSecret)
    request = LazopApiClient::Request.new('/order/get','GET')
    request.add_api_parameter("order_id", "16090")
    response = client.execute(request, accessToken)
    puts response.success?
    

Python sample code
    
    
    client = lazop.LazopClient(url, appkey ,appSecret)
    request = lazop.LazopRequest('/order/get','GET')
    request.add_api_param('order_id', '16090')
    response = client.execute(request, access_token)
    print(response.type)
    

**Note** : Most API methods are called via GET, but some API methods have additional request data sent via POST. Therefore, you need to update your code accordingly. The request type of each API is indicated in the API reference documentation.