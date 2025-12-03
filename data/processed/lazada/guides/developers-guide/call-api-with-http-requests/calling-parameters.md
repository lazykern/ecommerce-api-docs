Calls to the API must include system parameters in addition to the parameters associated with the application. Different application specific parameters are needed for different specific APIs.

## System parameters

System parameters are required in the HTTP request of every API call, listed in the following table:

Name | Type | Mandatory ? | Description
---|---|---|---
app_key | String | Yes | The App Key that is assigned to the application.
access_token | String | Conditional | The seller authorization token, which is mandatory for the APIs that require seller authorization.
timestamp | String | Yes | Time when the request is sent, in UTC or digital format, like “2017-11-11T12:00:00Z or 1517886554000”. Note that the difference between the timestamp and UTC time should not exceed 7200 seconds.
sign_method | String | Yes | The algorithm used to generate the signature.
sign | String | Yes | The cryptographic signature, authenticating the request.

 

## Business parameters

In addition to the system parameters that must be included in the API call request, the business parameters for the request are also required. Refer to the API documentation for details about the business parameters of each API.