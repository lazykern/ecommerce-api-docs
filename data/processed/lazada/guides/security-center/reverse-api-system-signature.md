# 一、Signature Param: 

The parameter corresponding to the signature is **http_sign.** You can obtain the system-generated signature by retrieving the value of parameter **http_sign**.

  


# 二、How to get http_sign param

The http_sign parameter is placed on the request URL, not in the request body. For example：https://api.taobao.global/test/push?app_key=103602&http_sign=124AEFA4A55F0B84D1E98DB302AA2F94F13348CD7EC36A7DC0A7FC62D545B3DC&sign_method=sha256&timestamp=1729589993688

  


# 三、Signature Algorithm 

  


Using Java code as an example：

  


Input Parameter Explanation

  1. **params** ：All HTTP input parameters, including parameters in the URL and parameters in the body. Attention：In addition to the business parameters, there are three system parameters，namely app_key, sign_method, and timestamp.
  2. **uri** ： api path, You can view the API path on the API documentation.
  3. **body** : Fixed value null
  4. **appSecret** ： app secret



PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

/**

* Sign the API request with body.

*/

public static String signApiRequest(Map<String, String> params, String uri, String body, String appSecret) throws IOException {

// first: sort all text parameters

String[] keys = params.keySet().toArray(new String[0]);

Arrays.sort(keys);

  


// second: connect all text parameters with key and value

StringBuilder query = new StringBuilder();

query.append(uri);

  


for (String key : keys) {

String value = params.get(key);

if (areNotEmpty(key, value)) {

query.append(key).append(value);

}

}

// third：put the body to the end

if (body != null) {

query.append(body);

}

  


// next : sign the whole request

byte[] bytes = encryptHMACSHA256(query.toString(), appSecret);

// finally : transfer sign result from binary to upper hex string

String s = byte2hex(bytes);

  


return s;

}

  


private static byte[] encryptHMACSHA256(String data, String secret) throws IOException {

byte[] bytes = null;

try {

SecretKey secretKey = new SecretKeySpec(secret.getBytes(ApiConstants.CHARSET_UTF_8), "HmacSHA256");

Mac mac = Mac.getInstance(secretKey.getAlgorithm());

mac.init(secretKey);

bytes = mac.doFinal(data.getBytes(ApiConstants.CHARSET_UTF_8));

} catch (GeneralSecurityException gse) {

throw new IOException(gse.toString());

}

return bytes;

}

  


/**

* Transfer binary array to HEX string.

*/

public static String byte2hex(byte[] bytes) {

StringBuilder sign = new StringBuilder();

for (int i = 0; i < bytes.length; i++) {

String hex = Integer.toHexString(bytes[i] & 0xFF);

if (hex.length() == 1) {

sign.append("0");

}

sign.append(hex.toUpperCase());

}

return sign.toString();

}

  


  


  


# 四、Example

  1. api path: /wl/test
  2. input parameters: ![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_param_demo_1729597071773__ZJaY.jpg)
  3. Parameter example of parameter signature
  4. ![](https://lazada-open-platform-public.oss-ap-southeast-1.aliyuncs.com/online/oss_sign_example_1729597543022__Djn5.jpg)