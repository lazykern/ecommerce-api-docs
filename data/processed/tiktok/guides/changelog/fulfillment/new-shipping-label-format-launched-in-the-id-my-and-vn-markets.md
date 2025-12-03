# What is changing?
Previously, we announced updates to the format and size of the shipping label file and the shipping label with packing list file.


With the launch of the new shipping label format, there are important changes to the content area on the shipping labels. Developers must ensure they render the shipping labels as-is for printing. Cropping or using OCR methods based on the original label format may result in broken content.


For comprehensive details about this change and the required actions, please review the following content.
# Which markets are affected?
This applies to the ID, MY and VN markets, cross-border and local sellers.
# Who is affected?
Developers with applications that use any version of the `Get Package Shipping Document (V1)` API or the `Get Shipping Document (V1)` API are affected.


If you use the APIs, you need to find whether your applications are using the APIs to get shipping label documents and crop them as images. If your apps don't crop the original shipping label and shipping label with packing list from APIs, there is no action required from your side.


However, because the content area on shipping labels gets smaller, your current methods of cropping images may generate broken images. Also, there may be mistakes if you use OCR methods to extract text based on shipping label documents.
# What action is required?
No specific action required if you render the labels as-is for printing.


If you have the use cases of further processing shipping labels and need to test your application with the new shipping label format, you can refer to our [Use case guide on the new shipping label formats](https://bytedance.feishu.cn/docx/YcG1dX6kwotudMxkWO6cMi8ensf) in ID, MY and VN markets and download sample shipping label document files for testing purposes.


**TikTok Shop periodically updates the format of shipping labels** to meet evolving seller needs. Therefore, render the label as-is for printing and **avoid further processing the shipping label file**.


Developers can also use the `Get Package Shipping Document (V1)` API to generate shipping labels in the PNG format to meet more use cases. Learn more about how to get shipping labels in PNG format from this [developer guide](https://bytedance.feishu.cn/docx/YcG1dX6kwotudMxkWO6cMi8ensf#Ve2vdeldWodWDKxuHpFcugalnrB).