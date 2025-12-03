## Summary
In the Brazil market, marketplace sellers are required to upload invoices to marketplace before they can fulfill the order. So the API workflow has been adjusted and new fields added to fit into the invoicing process.
## Affected Markets and Versions
This change applies to the BR market and v202309 of the API.
## API Changes
Please refer to the [developer guide](https://bytedance.sg.larkoffice.com/docx/YOIKdbMUtotNTFxNjx2chiitnOd) on how to manage BR market by effectively using the invoicing and fulfillment APIs
### Get Order List, Get Order Detail
Responses have the following new properties:

* `need_upload_invoice`: Whether an invoice needs to be uploaded (only for Brazil market).
   * UNKNOWN
   * NEED_INVOICE
   * NO_NEED
   * INVOICE_UPLOADED
* `CPF`: CPF (invoice number) used to issue an invoice. Exclusive for the Brazil market.
* `CPF_name`: Name belonging to the CPF number for the Brazil market.

### Upload Invoice
A new [Upload Invoice endpoint](upload-invoice) to upload the invoice document. **Note**: Applicable only for local sellers in the Brazil market.
### Get Package Shipping Document
A new input parameter `INVOICE_LABEL`. For Brazil market only, document_size is fixed to A6, and you don't need to specify document_size.
### Get Warehouse List
[Get Warehouse List](get-warehouse-list) retrieves all warehouse information associated with the seller. Compared with other markets (e.g. US market), the warehouse entity of Brazil market has four address lines, with each indicating:
| Field | Description |
| --- | --- |
| address_line1 | The first line of the warehouse address, like street name and street number. **Note:** For Brazilian market, this represents the neighborhood or district. |
| address_line2 | The second line of the warehouse address, like flat, apartment, or suite. **Note:** For Brazilian market, this represents the street name. |
| address_line3 | This represents the street number. If it's s/n, it means null. **Note:** Available only in Brazilian market. |
| address_line4 | This represents supplementary information, like flat, apartment, or suite (optional). **Note:** Available only in Brazilian market. |
### Webhook: Invoice Status Change
A [new webhook that is triggered](36-invoice-status-change) when the status of an invoice upload changes after using the POST Upload Invoice endpoint. **Note**: The POST Upload Invoice API is currently only applicable to the Brazil market.