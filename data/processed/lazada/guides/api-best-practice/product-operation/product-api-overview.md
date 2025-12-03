# Product API Overview

This document is used to describe the classification and specific use of the product API

# 1、Category Attributes API

[API usage guide](<https://open.lazada.com/apps/doc/doc?nodeId=10557&docId=108146>)

## GetCategorySuggestion

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fcategory%2Fsuggestion%2Fget>)

The category will be automatically recommended according to the product name

## GetCategoryTree

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Ftree%2Fget>)

Use this API to get the complete category tree of lazada

## GetCategoryAttributes

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fcategory%2Fattributes%2Fget>)

Use this API to get available, required, and variant attributes in the target category.

## GetUnfilledAttributeItem(For cross boarder sellers Only)

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Funfilled%2Fattribute%2Fget>)

Get the key attributes not filled in the attributes of the specified cross-border product

# 2、Product Management API

## CreateProduct

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fcreate>)

Use this API to create products or add new SKUs to existing product

## UpdateProduct

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fupdate>)

Use this API to update product information (seller SKU cannot be changed)

## UpdatePriceQuantity

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fprice_quantity%2Fupdate>)

Use this API to update SKU prices and total inventory

## UpdateSellableQuantity

[API Document](<https://open.lazada.com/doc/api.htm?spm=a2o9m.11193531.0.0.74596bbewLzLDk#/api?cid=5&path=/product/stock/sellable/update>)

Use this API to update the sellable inventory of the sku in an overriding manner

## AdjustSellableQuantity

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fstock%2Fsellable%2Fadjust>)

Use this API to update the sellable inventory of a sku in an additive or subtractive way

## RemoveProduct

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fremove>)

Use this API to delete a product or sku

## DeactivateProduct

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fproduct%2Fdeactivate>)

Use this API to set the product or sku to deactive state

## SetImages

[API Documen](<https://open.lazada.com/apps/doc/api?path=%2Fimages%2Fset>)

Use this API to update images for variant SKUs

# 3、Image Upload

## MigrateImage

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fimage%2Fmigrate>)

Use this API to convert an external image URL to a Lazada image URL

## MigrateImages

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fimages%2Fmigrate>)

Use this API to upload up to eight external image URLs to Lazada for conversion

## GetResponse

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fimage%2Fresponse%2Fget>)

Use this API to get the conversion results of the MigrateImages API

## UploadImage

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fimage%2Fupload>)

Use this API to upload local images to generate lazada image URL

# 4、Video Upload

# GetVideoQuota

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fmedia%2Fvideo%2Fquota%2Fget>)

Use this API to get the video space capacity available to sellers

## InitCreateVideo

[API Document](<https://open.lazada.com/doc/api.htm?spm=a2o9m.11193494.0.0.f1ae266bioXXeR#/api?cid=32&path=/media/video/block/create>)

Use this API to set the filename and video size for local uploads

## UploadVideoBlock

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fmedia%2Fvideo%2Fblock%2Fcreate>)

Use this API to upload videos in binary chunks

## CompleteCreateVideo

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fmedia%2Fvideo%2Fblock%2Fcommit>)

Add video information to complete the video creation

## GetVideo

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fmedia%2Fvideo%2Fget>)

Use video id to get the information of the successfully uploaded video