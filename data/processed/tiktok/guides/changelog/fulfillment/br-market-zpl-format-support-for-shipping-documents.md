## Summary
To better support our fulfillment APIs in the BR market, we've added the Zebra Programming Language (ZPL) format to our [Get Package Shipping Document](get-package-shipping-document) endpoint.
## Affected markets and versions
This change applies to the following market(s):

* Brazil (BR)

This change applies to the following API version(s):

* 202309 (and later)

## API changes
### Fulfillment APIs
| **Endpoint(s)** | **Change(s)** |
| --- | --- |
| * Get Package Shipping Document | * Added new query parameter: `document_format`. <br> * Shipping labels can be printed as `PDF`(default) or `ZPL`(BR market only). |