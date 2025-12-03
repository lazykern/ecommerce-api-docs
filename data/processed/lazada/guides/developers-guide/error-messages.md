All API calls will return a response, which indicates the status of the operation (either Success or Error) and optionally provides results and/or details related to the specified action.

When an API call fails, the system returns the request ID and error codes as well. There are 3 categories of common API call errors:

  * SYSTEM: API platform error
  * ISV: Business data error
  * ISP: Backend service error



## API platform error (ISV errors)

The API platform errors usually occur because the request from a user does not fulfill the basic verification. When encountering such errors, check the authority, frequency and other conditions of the applications. Then, check the uploaded parameters for completeness and validity based on the API documentation.

## Business data error (ISP errors)

These errors are the result of a business logic error, these errors are caused if you do not follow the certain business rules set out by the Lazada Platform (e.g. product creation rules, platform policy rules, etc).

When encountering such errors, check whether the corresponding information is uploaded based on the error information. It is recommended to try again after correcting such errors. Should you still receive the error messages, please reach out to the Lazada Partner Seller Support to find out the business 

## Backend service error

The backend service errors are usually caused by the availability of API service. Please try again after some time, if the issue persists, please contact our technical support team.