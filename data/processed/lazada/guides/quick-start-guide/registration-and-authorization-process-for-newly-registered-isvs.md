## 1\. First register an open platform account

### 1.1 Registration link

<https://open.lazada.com/apps/user/register?spm=a1zq7z.27197301.login_form.1.1db47c73kmujqv>

### 1.2 Precautions for account registration

#### 1.2.1 Registered Email and Password Conditions

a. The password needs English+number+symbol, and the symbol cannot use "!" "<" 、">"；

b. The registered mailbox should not have a "+".

![](https://tida.alicdn.com/oss_1668756768989_null_eGLhAoaM)

#### 1.2.2 After registration, you need to fill in profile information first, and wait for review after submission

![](https://tida.alicdn.com/oss_1668756793006_null_XDgCybaC)

#### 1.2.3 After the profile information is approved, the app can be created

a. There are two steps to create an app.

First, click Apply and wait for the approval before clicking Create App. After the approval, an app in test status will be automatically obtained; 

Step 2: Click Create APP.

![](https://tida.alicdn.com/oss_1668756813338_null_v0InGDZp)

b. It is recommended to select ERP System or Seller in house APP. Their differences are as follows:

The number of authorized sellers is different: the default number of authorized sellers in the ERP system is 300, and can be increased according to the needs of the project;

The number of authorized sellers of the Seller in house APP is 20 by default, and the maximum number is 60;

Different authorization methods:

ERP System: for users who do not need to add white list of sellers;

Seller in house APP: for sellers who need to add white list.

You can find more details below

[https://open.lazada.com/apps/community/detail?id=208](<https://open.lazada.com/apps/community/detail?id=208>)

![](https://tida.alicdn.com/oss_1668756834045_null_8Z4oR8RI)

c. If the app of type seller in house is not whitelisted, the following error messages will appear

![](https://tida.alicdn.com/oss_1668756849213_null_ACjjiIap)

#### 1.2.4 The newly created app is in test status

a. The APP is in the test status: the maximum call amount is ten thousand per days; The validity of the token is 7 days, and the validity of the refresh token is 14 days;

b. Online status: the maximum call volume is 10 million per day; The validity of the token is 30 days, and the validity of the refresh token is 180 days;

If you can ensure that the success rate of app calls is above 85%, you can apply for the app to go online.

![](https://tida.alicdn.com/oss_1668756867050_null_xsmKzq90)

![](https://tida.alicdn.com/oss_1668756879347_null_KbiU03mp)

C.offline: If you want to Offine the app, you can click manage>Apply offine on the app console

![](https://tida.alicdn.com/oss_1668756893418_null_Me1AmmNp)

d. Delete: If you want to delete an app, you can only delete it in test status.

### 1.2.5 Retrieve App Key and App Secret

App Key is the unique identity of an application on Lazada Open Platform. The App Key is one of the parameters that must be included in the request of API calls, and the application will be identified with the App Key by Lazada Open Platform.

App Secret is the key that is assigned to an application by Lazada Open Platform, which ensures the security and reliability of the application source. You must keep the App Secret properly and should not share it with any third party.

Once your application is registered, the App Key and App Secret are assigned to the application automatically. You can view the App Key and App Secret or reset the App Key on the application overview page.

1. Open the home page of the open platform, click**App Console** , and enter **App Management.**  
2\. From the list of your applications, click **Manage** to open the overview page of an application.  
3\. Under the **Advanced Information** section, click **View** to view the App Secret of your application.  
4\. Click **Reset** to reset the App Secret of your application. For the **Old Secret Expires In** field, select the time (in hours) for the old App Secret to expire.After resetting the App Secret, you must update the related information in your application.

![](https://tida.alicdn.com/oss_1668756972069_null_FLY6ZM3h)

![](https://tida.alicdn.com/oss_1668757024311_null_uY4XWgm1)

![](https://tida.alicdn.com/oss_1668757000158_null_z47BI8KV)

## 2\. app authorization

### 2.1 Seller authorization introduction

[https://open.lazada.com/apps/doc/doc?nodeId=10777&docId=108260](<https://open.lazada.com/apps/doc/doc?nodeId=10777&docId=108260>)

#### 2.1.1 Concatenate authorization URL

Sample link for authorization:

[https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=${app](<https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=${app>) call back url}&client_id=${appkey}

Demo:

Authorization links need to be spliced by yourself. Using the above example of authorization links, replace "${appkey}" with app key, and replace "${app call back url}" with callback URL

[https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=https://www.lazada.com&client_id=102802](<https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=https://www.lazada.com&client_id=102802>)

![](https://tida.alicdn.com/oss_1668757055132_null_YHHcqAqT)

![](https://tida.alicdn.com/oss_1668757067178_null_UGASHB5y)

#### 2.1.2 uuid optional

If the **uuid** is not used during authorization, then the next step to generate access_ token, no uuid needs to be passed in the request parameters

[https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=https://www.lazada.com&client_id=102802&**uuid=123**](<https://auth.lazada.com/oauth/authorize?response_type=code&force_auth=true&redirect_uri=https://www.lazada.com&client_id=102802&uuid=123>)

#### 2.1.4 Cross border authorization description

a. The authorization page Crossborder represents the authorized cross-border stores, and the tokens can call the APIs of six sites;  
b. When you select Crossborder authorization, you need to ensure that stores in the six sub sites can log in; Otherwise, you can only use single site authorization.

![](https://tida.alicdn.com/oss_1668757102950_null_mqOVe1nS)

#### 2.1.5 Generate Token with Generated Code

![](https://tida.alicdn.com/oss_1668757123667_null_XwacWa4i)

Note: The code can only be used once. You need to call the [GenerateAccessToken](<https://open.lazada.com/apps/doc/api?path=%2Fauth%2Ftoken%2Fcreate>) API to generate a token within half an hour of code generation

The following is an example of a test tool:

a. Click API Testing Tool

![](https://tida.alicdn.com/oss_1668757147197_null_H8WpeICx)

b.For users using the test tool, Malaysia can be selected as the region. No matter which country is selected when generating the authorization code in the previous step, Malaysia is selected as the region 

Select Malaysia as the region (because there is only one service address of the GenerateAccessToken API [https://auth.lazada.com/rest](<https://auth.lazada.com/rest>) ）

![](https://tida.alicdn.com/oss_1668757169596_null_wKWDL5E6)

c. Pass in the code and uuid (if the uuid is not set in the authorization link, it will not should be filled in, otherwise an error will be reported)

![](https://tida.alicdn.com/oss_1668757187160_null_QJQWR2YB)

d. Response Field Description

Country: on behalf of the authorized country;

refresh_ expires_ In: The expiration time of "refresh_token", in seconds (it will be refreshed when refreshing). If "refresh_token" expires, you need to re authorize the generation of a new token;

expires_ In: "access_token" expiration time, in seconds (when the token is refreshed, it will not be refreshed).

When the "access_token" fails, you can call the RefreshAccessToken API to refresh the token (it is recommended to refresh the token 48 hours in advance)

![](https://tida.alicdn.com/oss_1668757204653_null_omsHEuzA)