API versioning enables TikTok Shop to continuously improve and expand our API capabilities while maintaining a seamless user experience as the API evolves.
When breaking changes are introduced to TikTok Shop APIs, these changes will be rolled out through new API versions. Breaking changes in APIs often occur to improve overall functionality, introduce new capabilities, or enhance security measures. These changes are necessary to keep pace with evolving technologies and user needs. To ensure seamless integration, and to take advantage of these improvements, staying updated to the latest API versions is crucial.
**Examples of non-breaking and breaking changes:**

* Non-breaking change: [US and UK markets: Exchange orders](us-and-uk-markets-exchange-orders).
* Breaking change: [EU GPSR Communication Doc - adding Responsible person, Manufacturer and Safety label information](eu-gpsr-communication-doc-adding-responsible-person-manufacturer-and-safety-label-information).

# API release schedule and version naming
Currently, new API versions are rolled out on monthly basis. Not all APIs will be updated every month.
The nomenclature of API version (e.g., `202303`) is derived from the year and month of its launch.
# Selecting API versions in API reference docs
API versions are assigned at the API level, meaning different APIs may have different versions. For example, the latest version of Create Product API is `202212`(released in Dec, 2022), while the latest version of Get Order Details API could be named `202312`.
The API reference page displays the latest version of the API by default. On this page, you have the option to choose from a dropdown menu to view other supported versions. By clicking on a version name within the dropdown menu, you can access the reference doc for the specific API version.
Different APIs from different versions can generally be mixed and matched, but need to be tested thoroughly. For the most part, we recommend using the latest version of the API available, and if possible, use the same version.
<div style="text-align: center"><img src="https://p16-arcosite-va.ibyteimg.com/tos-maliva-i-10qhjjqwgv-us/789f5cc8741c4c32a8644deecb834606~tplv-10qhjjqwgv-image.image" width="676px" /></div>

# Specifying an API version when calling an API
After version 202309, you need to pass `version` in path to request the correct version of the API. For example,
```HTTP
https://open-api.tiktokglobalshop.com/product/202309/products/1729435271479265816
```

# Upgrading to a new API version
Before upgrading to a new API version, we suggest you read the changelog and the API reference docs of the new API version to learn what changes are included and how to integrate the new API version. Select the dropdown menu and click a version name to see the API reference for that version.
# Retiring a version of an API
After a new version of an API is released, the prior version will be available for a minimum of 2 months.
When an API is scheduled for retirement, the announcement is communicated via [our changelog](https://partner.tiktokshop.com/docv2/changelog) at least 2 months before its permanent retirement.
If you use a retired or invalid version, the API will return an error in the response stating that the API version is not supported.
```Thrift
{
    "code":36009014,
    "data":null,
    "message":"The version name is invalid, please check and retry."
}
```

# Staying updated
## Changelog
The changelog is your go-to source for staying informed about all API changes, both major and minor changes. Regularly checking the Changelog ensures you're up-to-date with the latest changes, allowing you to proactively respond to changes and deliver a superior app experience to your users.
### Latest API changes

* [API Version 202309](introducing-api-version-202309)