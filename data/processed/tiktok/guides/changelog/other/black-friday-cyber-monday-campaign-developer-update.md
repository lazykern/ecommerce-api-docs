This document details the information developers must know to successfully support the TikTok Shop (TTS) Black Friday Cyber Monday (BFCM) campaign.


The BFCM campaign aims to increase sales and business growth for our sellers and creators during this year's holiday season. The campaign takes place across the US, local, and cross-border markets, and consists of three main stages:

1. Early Black Friday
2. Official Sale
3. Extended Cyber Monday

![Image](https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/82c358f16d0d40efa06f3c7aa2a52e05~tplv-10qhjjqwgv-image.image)
# BFCM Seller Enrollment
Sellers can enroll in TikTok Shop 2023 Holiday Campaigns such as the BFCM campaign in the Campaigns section of the Seller Center (*Seller Center -> Marketing -> Campaigns*).


TTS only allows sellers that meet a specific set of performance requirements to participate in holiday campaigns. Refer to the 2023 Holiday Campaigns topic within TikTok Shop Academy to learn more about campaign eligibility and policies.
# API Restrictions during BFCM
If eligible and participating sellers use your integrations during the BFCM campaign, we have made some restrictions to how some of our APIs function with the platform. For sellers participating in the BFCM campaign, products will have a campaign price that you *can not* modify via the Update Price API.
## Campaign Price
Sellers participating in the BFCM campaign can set a campaign price for a given product. The campaign price is a promotional price for a product that is lower than the original retail price. This price is set by the seller via the Seller Center for the product(s) they register as part of the BFCM campaign.
As a developer, keep the following in mind:

* You *can't* use the [Update Price API](update-price) to modify the **Campaign Price** field of a BFCM campaign. It does not contain a field for the campaign price.
* The campaign price is independent of the retail price, which is **** the original daily price of the product.
   * The **Campaign Price** field can only be modified by sellers within the Seller Center.
   * You can only use the Update Price API to modify the **Retail Price** field.

**Note:** The campaign price reverts to the retail price once the campaign stock is sold out.
# Managing Inventory during BFCM
**Important:** Based on the possibility of high order rates, there is a risk of overselling. It's the sellers' responsibility to ensure that they have adequate inventory in TTS to support BFCM campaigns. However, we highly recommend communicating with your BFCM participating sellers on how to best sync orders and mitigate any risk of overselling.