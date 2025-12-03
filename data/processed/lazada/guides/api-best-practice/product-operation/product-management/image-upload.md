Convert external image URLs to Lazada image URLs using local upload or URL upload

Note: Only Lazada image Urls can be used when products are created or updated

# Image requirements

Image size maxOriginalMediaByteSize: 3145728;

Maximum Image height maxOriginalImageHeight: 5000;

Maximum Image width maxOriginalImageWidth：5000;

Minimum image height minOriginalImageHeight：330;

Minimum image width minOriginalImageWidth：330;

Maximum image download time limit downloadMediaTimeoutMilliSec：5000；

Supported image formats：jpg、png;

Whether ip Image links are supported：false;

# URL verification requirements

1\. Only ports 80 and 443 are supported.

2\. Perform SSRF verification on the url

3\. Domain blacklist：

"^(http://)?10.*",

"^(http://)?11.*",

"^(http://)?192.*",

"^*.sg94",

"^*.id35"

# Usage examples

## Single image upload

### MigrateImage (Url migration)

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fimage%2Fmigrate>)

#### Example of request
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <Request>     
      <Image>         
        <Url>http://pic4.nipic.com/20091217/3885730_124701000519_2.jpg</Url>     
      </Image> 
    </Request>

#### Example of response
    
    
    {
      "data": {
        "image": {
          "url": "https://vn-live-02.slatic.net/original/bfee8ea9c4797ad704ff2b20323bc92c.jpg"
        }
      },
      "code": "0",
      "request_id": "2101554016563124475412756"
    }

### UploadImage（Local Upload）

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fimage%2Fupload>)

#### Example of request

Parse the image to be uploaded as "byte[]" and put it in the body

#### Example of response
    
    
    {
      "data": {
        "image": {
          "hash_code": "9d06c8f1b19c16231757dae10ab97673",
          "url": "https://id-live-02.slatic.net/p/9d06c8f1b19c16231757dae10ab97673.jpg"
        }
      },
      "code": "0",
      "request_id": "212237bd16563140630542742"
    }

## Batch image migration

Batch image migration is done by a combination of MigrateImages API and GetResponse API calls.

1、The MigrateImages API is called first to upload the URL of the image to be migrated to Lazada and get the "batch_id" in the response.

2、Then call GetResponse API with "batch_id" to get the migration result and the migrated URL.

### MigrateImages

[API Document](<https://open.lazada.com/apps/doc/api?path=%2Fimages%2Fmigrate>)

Note: up to eight pictures can be migrated each time

#### Example of request
    
    
    <?xml version="1.0" encoding="UTF-8" ?>
    <Request>
      <Images>
        <Url>https://img.alicdn.com/imgextra/i2/O1CN016gf7Y02129uqj6A8a_!!6000000006926-0-tps-846-512.jpg</Url>
        <Url>https://img.alicdn.com/imgextra/i3/O1CN01QkEL7m1XNk6kf1PNx_!!6000000002912-0-tps-790-469.jpg</Url>
      </Images>
    </Request>

#### Example of response
    
    
    {
      "batch_id": "2122317116563149177325379d074f",
      "code": "0",
      "request_id": "2122317116563149177322306"
    }

### GetResponse

Do not call this API immediately after calling MigrateImages API, wait for half a second or so before calling this API to get the migrated URL.

#### Example of request

https://api.lazada.co.id/rest/image/response/get?batch_id=2122317116563149177325379d074f&app_key=1****2&sign_method=sha256&access_token=50000300c23r************************************U9RFEZ2&timestamp=1656315445286&sign=A77170123D8904CBB452FDE069FB22ADC60DE479A58B6C5E901223E81762233B

#### Example of response
    
    
    {
      "data": {
        "images": [
          {
            "hash_code": "d85ac36cd40368715f9de77146c636f5",
            "url": "https://id-live-02.slatic.net/p/d85ac36cd40368715f9de77146c636f5.jpg"
          },
          {
            "hash_code": "83008ad9816428e14732200072f6f6e4",
            "url": "https://id-live-02.slatic.net/p/83008ad9816428e14732200072f6f6e4.jpg"
          }
        ]
      },
      "code": "0",
      "request_id": "2122317116563154453228884"
    }