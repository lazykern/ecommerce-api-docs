Use these API to upload video content into Lazada Media Center through this API and get the corresponding VideoID. After that, user can attach the videoID on CreateProduct or UpdateProduct step when listing products on Lazada.

![image](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/18857002/1656318126013-519041ca-bb62-48a1-8e65-884a87edaa61.png?x-oss-process=image%2Fresize%2Cw_1500)

# API call example

## 1、InitCreateVideo

Initiate a create video task, response the upload ID. (Max video size: 100mb)

### Example of request

https://api.lazada.com.my/rest/media/video/block/create?fileName=VID_20220627_173223.mp4&fileBytes=794969&app_key=100132&sign_method=sha256&access_token=500002000230jwavWuhdy**************AyXEEjj&timestamp=1656396886224&sign=C86D63CD8037FDF9286EF6E6279A2FF633DD8FCF92454E4980E2085A2ED941A6

![image](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/18857002/1656397079378-b7c166df-5b09-4ddc-8498-3e1d8f3106c2.png)

### Example of response
    
    
    {
      "upload_id": "670A237D27694CFDA74CDE6EC1A99FA5",
      "result_message": "",
      "success": true,
      "result_code": "",
      "code": "0",
      "request_id": "21411dbe16563968862437448"
    }

## 2、UploadVideoBlock

This API is used to upload video files, if the video file is large then it needs to be uploaded in binary chunks.

For example, an 8MB video file needs to be split into chunks of size 3MB, 3MB and 2MB in binary cut, and then requested in three times.

### Example of request

https://api.lazada.com.my/rest/media/video/block/upload?blockCount=1&uploadId=6F963A22F0124EBC8B079638357DA012&blockNo=0&app_key=100132&sign_method=sha256&access_token=50000201609zpuehtgzrl103de538ZdCwhpTxeHeJnwjr0oh1AsqCtxPJ8c2&timestamp=1656323464114&sign=27B1F421503C03C2A1933D897AAA3474AC61E7F2DF589BD3D1F96060E33946E3

![image](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/18857002/1656397257606-2e83c07a-6ab7-4a9b-86ef-e07095c8cfa8.png)

### Example of response
    
    
    {
      "result_message": "",
      "success": true,
      "result_code": "",
      "e_tag": "61F4949269F20AF4D1025F5825552FC3",
      "code": "0",
      "request_id": "2102ebef16563971593057981"
    }

## 3、**CompleteCreateVideo**

Calling this API will combine the binary blocks uploaded when calling the uploadvideoblock API and generate a complete video.

### Example of request

Note: the value of "partNumber" starts from 1

https://api.lazada.com.my/rest/media/video/block/commit?coverUrl=https://sg-live-02.slatic.net/p/ae0f37dbf1c0ef8c560a0f0cfbaac3b6.png&access_token=500002000230jwavWuhdyNfSDLEPzoRaY5g1f874bbbzdpUewqgYDAyXEEjj&videoUsage=pro_main_video&app_key=100132&uploadId=670A237D27694CFDA74CDE6EC1A99FA5&parts=[{"partNumber": 1,"eTag": "61F4949269F20AF4D1025F5825552FC3"}]&sign_method=sha256&sign=A067FA6D2AE4474802FB1780B0568EE5C71297E2E759E312F339A5C449466491&title=hello&timestamp=1656397346312

![image](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/18857002/1656397527396-fb4637af-d5f1-478f-91fc-298fe8169bc1.png)

### Example of response
    
    
    {
      "result_message": "",
      "success": true,
      "result_code": "",
      "video_id": "30073704787",
      "code": "0",
      "request_id": "2140d3fa16563973463281042"
    }

## 4、GetVideo

Call this API to get video information and video status.

Note: only when the video status is "audit_success" can it be used when creating or updating products.

### Example of request
    
    
    {
      "cover_url": "https://sg-live-02.slatic.net/p/ae0f3*****ac3b6.png",
      "video_url": "http://lazvideo.alicdn.com/psp/20220628/7ae02a32-****-****-****-15*******mp4?auth_key=16****39-0-0-5ca4b3db1*******9ad7",
      "result_message": "",
      "success": true,
      "result_code": "",
      "state": "AUDIT_SUCCESS",
      "title": "hello",
      "code": "0",
      "request_id": "2101554016563981396453606"
    }