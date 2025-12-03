Order Access Log

http://eco-ueba.lazada.com/event/order

With the order access log we can clearly know who acquired what information, through which application, and when. Such logs are very helpful for us in detecting data leaks.

Parameter | Type | Necessary | Description
---|---|---|---
userId | string | Y | The ID or name of the user who is accessing orders in the ISV account system. The specific user should be able to be located using the incoming parameter. Optional account formats: 1) Company Name: Sub-account. 2) Pass actual login accounts if they are unique in the application’s account system. 3) Identification Codes for Independent Deployments: Sub-account.
userIp | string | Y | Client IP of this access request.
ati | string | Y | For applications with B/S architecture, a cookie _ati will be generated under the domain name after device fingerprint is accessed. The value of the cookie named _ati can be acquired from HTTP requests on the server side. For applications with C/S architecture, the client will generate a symbolic client SID for itself and send it to servers as _ati when accessing servers after device fingerprint is accessed.
appId | string | Y | The App Key assigned by Lazada Open Platform.
appName | string | Y | While for the names of login applications, the app or domain name can be used.
url | string | Y | URL of client requests.
tradeIds | string | Y | Order number list separated by English semicolons. A maximum of 100 records is allowed each time. It should be split into multiple requests if there are more than 100 records.
operation | string | Y | Operations performed on orders. For example, print orders.
time | string | Y | It supports two formats: (1) Integral timestamps that are accurate to the millisecond, and the number of milliseconds since January 1, 1970 12:00 AM. (2) Strings in yyyy-MM-dd HH:mm:ss format.
appKey | string | Y | The App Key issued by DataMoat.
sign | string | Y | API call signature.

 

See below for relevant parameter settings for users if there are order reading operations (for example, reading and processing orders by timed tasks) triggered by non-user requests on servers:

ati： Set it to 0000000000

userId：Set it to “System”

userIp： Set it to server IP

url：Set it to the name of the current processing task. You can also fill in the same value as that of the operation.