# Summary
To comply with the law and regulation of the EU market, TikTok Shop requires sellers to submit the following information:

1. Manufacturer Information: the manufacturer of the product
2. Responsible Person (RP): the responsible person who ensures a seller's products comply with EU regulations.
3. Extracode: Optional field that can be used if the product SKU includes multiple combined items. Additional IDs in format standards of GTIN, EAN, UPC, or ISBN are accepted.

Developers need to support and guide sellers entering the fields for correct product listings. **The new required fields and API changes are applicable to local sellers in the EU market.**
# Timelines and required actions
| Date | API Changes | Required Actions |
| --- | --- | --- |
| **09/30** | API will support creating manufacturer information and RPs on behalf of sellers, and adding them to products. <br> **Note**: Fields optional from 9/30/24 to 12/13/24 | Integrate the new APIs and start guiding sellers to provide manufacturer and RP information to products |
| **12/13** | Manufacturers and Responsible Persons required in API | Ensure sellers submit the required fields when creating and editing products |
# API changes

| API endpoints | Parameters | Response |
| --- | --- | --- |
| <span style="color: green">[New]</span> Create Responsible Person | `"responsible_person": {` <br> `  "name": "John Doe",` <br> `  "phone_number": {` <br> `    "country_code": "+34",` <br> `    "local_number": "313516642"` <br> `  },` <br> `  "email": "johndoe@gmail.com",` <br> `  "address": {` <br> `    "street_address_line1": "Av. de los Poblados",` <br> `    "city": "Latina",` <br> `    "province": "Madrid",` <br> `    "postal_code": "28044",` <br> `    "country": "Spain"` <br> `  }` <br> `}` | `{` <br> `  "code": 0,` <br> `  "message": "success",` <br> `  "request_id": "202203070749000101890810281E8C70B7",` <br> `  "data": {` <br> `    "responsible_person_id": "66d3cbe4d9c8b09ddca932a7"` <br> `  }` <br> `}` |
| <span style="color: green">[New]</span> Partial Edit Responsible Person | `{` <br> `  "code": 0,` <br> `  "message": "success",` <br> `  "request_id": "202203070749000101890810281E8C70B7"` <br> `}` | `{` <br> `  "responsible_person": {` <br> `    "name": "John Doe",` <br> `    "phone_number": {` <br> `      "country_code": "+34",` <br> `      "local_number": "313516642"` <br> `    }` <br> `  }` <br> `}` |
| <span style="color: green">[New]</span> Search Responsible Person | `{` <br> `  "responsible_person_ids": [` <br> `    "66d3cbe4d9c8b09ddca932a7",` <br> `    "66d3cbe3d9c8b09ddca932a1"` <br> `  ],` <br> `  "keyword": "john"` <br> `}` | Returns the properties of Responsible Person entity |
| <span style="color: green">[New]</span> Create Manufacturer | `{` <br> `  "name": "John Doe",` <br> `  "phone_number": {` <br> `    "country_code": "+65",` <br> `    "local_number": "81234567"` <br> `  },` <br> `  "email": "johndoe@gmail.com",` <br> `  "address": "One Raffles Quay, 1 Raffles Quay, Singapore 048583"` <br> `}` | `{` <br> `  "code": 0,` <br> `  "message": "success",` <br> `  "request_id": "202203070749000101890810281E8C70B7",` <br> `  "data": {` <br> `    "manufacturer_id": "66d3cbe4d9c8b09ddca932a7"` <br> `  }` <br> `}` |
| <span style="color: green">[New]</span> Edit Manufacturer | `{` <br> `  "registered_trade_name": "TikTok Shop Co."` <br> `}` | `{` <br> `  "code": 0,` <br> `  "message": "success",` <br> `  "request_id": "202203070749000101890810281E8C70B7"` <br> `}` |
| <span style="color: green">[New]</span> Search Manufacturer | `{` <br> `  "manufacturer_ids": [` <br> `    "66d3cbe4d9c8b09ddca932a7",` <br> `    "66d3cbe3d9c8b09ddca932a1"` <br> `  ]` <br> `}` | Returns the properties of manufacturer entity |
| [Check Product Listing](https://partner.tiktokshop.com/docv2/page/check-product-listing) | Adding the following properties to responses <br>  <br> * `manufacturer_ids` <br> * `responsible_person_ids` <br> * `sku.extra_identifier_codes` | For the EU market, this endpoint will validate the required fields to check whether the product information is compliant |
| [Create Product](https://partner.tiktokshop.com/docv2/page/create-product), [Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product), and [Partial Edit Product](https://partner.tiktokshop.com/docv2/page/partial-edit-product) | 1. <span style="color: red">Removing</span> the existing `manufacturer` object and its properties: name, address, phone number, email: <br>    ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/EU%20Products%20API%20One%20Pager/removing_manufacturer.png?x-resource-account=public) <br> 2. Adding the following properties to responses <br>    * `manufacturer_ids` <br>    * `responsible_person_ids` <br>    * `sku.extra_identifier_codes` <br> 3. Updating the `certification.files` to support up to 10 files | For the EU market, this endpoint will validate the required fields. Starting from 13-Dec, editing products without correct `manufacturer_ids` and `responsible_person_ids` will fail |
| [Get Product](https://partner.tiktokshop.com/docv2/page/get-product) | No Change | 1. <span style="color: red">Removing</span> the existing `manufacturer` object and its properties: name, address, phone number, email: <br>    ![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/EU%20Products%20API%20One%20Pager/removing_manufacturer.png?x-resource-account=public) <br> 2. Adding the following properties to responses <br>    * `manufacturer_ids` <br>    * `responsible_person_ids` <br>    * `sku.extra_identifier_codes` |
# How to integrate the changes
## How to create compliance entities and attach them to product listing
Starting from **13-Dec**, manufacturers and responsible person(s) information become **required** for sellers' product listing. Developers should integrate the API changes, as well as upgrade their app(s) logic and UI to support sellers submitting manufacturers and responsible person(s).
### Step 1: Create entities for manufacturers
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/EU%20Products%20API%20One%20Pager/create_entities_manufacturers.png?x-resource-account=public)
❗**Important**:
<span style="color: red">The legacy </span><span style="color: red"><code>manufacturer</code></span><span style="color: red"> will be removed from API parameters from </span><span style="color: red"><strong>26-Sep</strong></span><span style="color: red">.</span>



<span style="color: red">If you are sending the </span><span style="color: red"><code>manufacturer</code></span><span style="color: red"> object to version 202309 of the Products API, you need to adjust the implementation. Use the above new method to get and pass </span><span style="color: red"><code>manufacturer_ids</code></span><span style="color: red"> to Products instead of sending manufacturer information for every product.</span>
### Step 2: Create entities for responsible person(s)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/EU%20Products%20API%20One%20Pager/create_entities_responsibleperson.png?x-resource-account=public)
### Step 3: Attach manufacturers and responsible person(s) entities to products
From **Step 1** and **Step 2**, you can get `manufacturer_ids` and `responsible_person_ids`. Use them as required parameters for [Check Product Listing](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-KGBtdMATMovevtxrmUYlY0nrgzc), [Create Product](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-Sw3ud6lMWouX9FxXWpwlOcPDgkz), [Edit Product](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-Fzdmd2v6qo350NxJGBDlw4fngkb), and [Partial Edit Product](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-XnrvdxZGCokzs9xZzgVlIidQgqe).
## How to use `sku.extra_identifier_codes`
This parameter is optional. When the SKU represents a virtual bundle containing multiple individual SKUs, sellers must provide product identifier codes for the virtual bundle SKU.



The parameter is an array of strings (`[]string`) and accepts up to 10 identifier codes. Each identifier code corresponds to a specific SKU within the product bundle.



The supported formats for identifier codes are:

* **GTIN**: 14 digits
* **EAN**: 8, 13, or 14 digits
* **UPC**: 12 digits
* **ISBN**: 13 digits (supports *X* in uppercase as the last digit)

Each SKU must have a unique identifier coe, and duplicates are not allowed.
This parameter can be used for [Check Product Listing](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-KGBtdMATMovevtxrmUYlY0nrgzc), [Create Product](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-Sw3ud6lMWouX9FxXWpwlOcPDgkz), [Edit Product](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-Fzdmd2v6qo350NxJGBDlw4fngkb), and [Partial Edit Product](https://bytedance.sg.larkoffice.com/docx/Pu7edRVn8oeWr8xwpKzl2tjMg3f#share-XnrvdxZGCokzs9xZzgVlIidQgqe).