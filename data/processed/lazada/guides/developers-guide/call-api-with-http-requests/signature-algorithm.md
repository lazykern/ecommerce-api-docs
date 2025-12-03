Lazada Open Platform verifies the identity of each API request, and the server will also verify whether the call parameters are valid. Therefore, each HTTP request must contain the signature information. The requests with invalid signature will be rejected.

Lazada Open Platform verifies the identity of the requests by the App Key and Secret that are assigned to your application. The App Secret is used to generate the signature string in the HTTP request URL and server-side signature string. It must be kept strictly confidential.

If you compose HTTP request manually (instead of using the official SDK), you need to understand the following signature algorithm.

The process of generating the signature is as follows:

  1. Sort all request parameters (including system and application parameters, but except the “sign” and parameters with byte array type) according to the parameter name in ASCII table. For example:



PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

Before sort: foo=1, bar=2, foo_bar=3, foobar=4

After sort: bar=2, foo=1, foo_bar=3, foobar=4

  1. Concatenate the sorted parameters and their values into a string. For example:



PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

bar2foo1foo_bar3foobar4

  1. Add the API name in front of the concatenated string. For example, adding the API name “/test/api”:



PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

/test/apibar2foo1foo_bar3foobar4

  1. Encode the concatenated string in UTF-8 format and make a digest by the signature algorithm (using HMAC_SHA256). For example:



PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

hmac_sha256(/test/apibar2foo1foo_bar3foobar4)

  1. Convert the digest to hexadecimal format. For example:



PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

hex("helloworld".getBytes("utf-8")) = "68656C6C6F776F726C64"

  


**Sample code for JAVA**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

/**

* Sign the API request with body.

*/

public static String signApiRequest(Map<String, String> params, String body, String appSecret, String signMethod, String apiName) throws IOException {

// first: sort all text parameters

String[] keys = params.keySet().toArray(new String[0]);

Arrays.sort(keys);

  


// second: connect all text parameters with key and value

StringBuilder query = new StringBuilder();

query.append(apiName);

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

byte[] bytes = null;

if(signMethod.equals(Constants.SIGN_METHOD_HMAC)) {

bytes = encryptWithHmac(query.toString(), appSecret);

} else if(signMethod.equals(Constants.SIGN_METHOD_SHA256)) {

bytes = encryptHMACSHA256(query.toString(), appSecret);

}

  


// finally : transfer sign result from binary to upper hex string

return byte2hex(bytes);

}

  


private static byte[] encryptHMACSHA256(String data, String secret) throws IOException {

byte[] bytes = null;

try {

SecretKey secretKey = new SecretKeySpec(secret.getBytes(Constants.CHARSET_UTF8), Constants.SIGN_METHOD_HMAC_SHA256);

Mac mac = Mac.getInstance(secretKey.getAlgorithm());

mac.init(secretKey);

bytes = mac.doFinal(data.getBytes(Constants.CHARSET_UTF8));

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

  


**Sample code for C#**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

public static string SignRequest(IDictionary<string, string> parameters, string body, string appSecret, string signMethod, string apiName)

{

// first : sort all key with asci order

IDictionary<string, string> sortedParams = new SortedDictionary<string, string>(parameters, StringComparer.Ordinal);

  


// second : contact all params with key order

StringBuilder query = new StringBuilder();

query.Append(apiName);

foreach (KeyValuePair<string, string> kv in sortedParams)

{

if (!string.IsNullOrEmpty(kv.Key) && !string.IsNullOrEmpty(kv.Value))

{

query.Append(kv.Key).Append(kv.Value);

}

}

  


// third : add body to last

if (!string.IsNullOrEmpty(body))

{

query.Append(body);

}

  


// next : sign the string

byte[] bytes = null;

if (signMethod.Equals(Constants.SIGN_METHOD_SHA256))

{

HMACSHA256 sha256 = new HMACSHA256(Encoding.UTF8.GetBytes(appSecret));

bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(query.ToString()));

}

  


// finally : transfer binary byte to hex string

StringBuilder result = new StringBuilder();

for (int i = 0; i < bytes.Length; i++)

{

result.Append(bytes[i].ToString("X2"));

}

  


return result.ToString();

}

  


**Sample code for PYTHON**

PlainBashC++C#CSSDiffHTML/XMLJavaJavascriptMarkdownPHPPythonRubySQL

def sign(secret,api, parameters):

#===========================================================================

# @param secret

# @param parameters

#===========================================================================

sort_dict = sorted(parameters)

parameters_str = "%s%s" % (api,

str().join('%s%s' % (key, parameters[key]) for key in sort_dict))

  


h = hmac.new(secret.encode(encoding="utf-8"), parameters_str.encode(encoding="utf-8"), digestmod=hashlib.sha256)

  


return h.hexdigest().upper()

For the signature sample codes in other programming languages, refer to the source code of the official SDK.