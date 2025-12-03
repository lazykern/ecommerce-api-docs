Taking the GetOrder (/order/get) API call as example, the steps of assembling the HTTP request is as follows:

  


**Step 1. Populate parameters and values**

Common parameters:

  * app_key = "123456"
  * access_token = "test"
  * timestamp = "1517820392000"
  * sign_method = "sha256"



Business parameters:

  * order_id = "1234"

  


**Step 2. Sort all parameters and values according to the parameter name in ASCII table**

  * access_token = "test"
  * app_key = "123456"
  * order_id = "1234"
  * sign_method = "sha256"
  * timestamp = "1517820392000"

  


**Step 3. Concatenate the sorted parameters and their values into a string**
    
    
    access_tokentestapp_key123456order_id1234sign_methodsha256timestamp1517820392000
    

  


**Step 4. Add the API name in front of the concatenated string**
    
    
    /order/getaccess_tokentestapp_key123456order_id1234sign_methodsha256timestamp1517820392000
    

  


**Step 5. Generate signature**  
Assuming that the App Secret is "helloworld", the signature is:
    
    
    hex(sha256(/order/getaccess_tokentestapp_key123456order_id1234sign_methodsha256timestamp1517820392000))=4190D32361CFB9581350222F345CB77F3B19F0E31D162316848A2C1FFD5FAB4A
    

  


**Step 6. Assemble HTTP request**  
Encode all the parameters and values (with the "sign" parameter) using UTF-8 format (the order of parameters can be arbitrary).
    
    
    http://api.lazada.com/rest/order/get?app_key=123456&access_token=test&timestamp=1517820392000&sign_method=sha256&order_id=1234&sign=4190D32361CFB9581350222F345CB77F3B19F0E31D162316848A2C1FFD5FAB4A