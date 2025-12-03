## Summary
TikTok Shop is obligated to implement the [General Product Safety Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2023.135.01.0001.01.ENG&toc=OJ%3AL%3A2023%3A135%3ATOC) (GPSR) in the EU market, which requires additional documentation to be provided by EU sellers to ensure that all non-food consumer products sold in EU are in full compliance with the new regulations.
In addition to the previous requirements stated ([EU market: Adding compliance required fields to Products API](eu-market-adding-compliance-required-fields-to-products-api)), TikTok Shop now provides new attributes, which can be used as attestation for the exemption of the qualification of Warning and Safety Labelling.
For certain categories, an option is available in Seller Center, Excel Bulk Upload/Edit tools and APIs for sellers to self-declare that there is no safety labeling information on the product package or the product itself.
### How to add GPSR information via Seller center
Please refer to the article [Product Listing Safety and Compliance Requirements](https://seller-es.tiktok.com/university/essay?identity=1&role=1&knowledge_id=1694506739320609&from=policy).
### API Changes
The relevant APIs for this change are [Get Attributes](get-attributes) and [Get Category Rules](get-category-rules)
The labelling field will now be required under certain conditions regarding the new attribute: *Confirm any regulatory marking or label*, which can be retrieved using the API: [Get Attributes](get-attributes). This attribute will not be mandatory until 7 Feb 2025; Use [Get Category Rules](get-category-rules) to check the conditions under which the product certifications are required.
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/EU/1.PNG)
![Image](https://sf16-sg.tiktokcdn.com/obj/eden-sg/jvK_ylwvslclK_JWZ%5B%5B/ljhwZthlaukjlkulzlp/Changelog/EU/2.PNG)