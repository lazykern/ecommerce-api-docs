## 1\. First, you need to have an open platform account and an app key

### 1.1 Link to Register Lazop Account

[https://open.lazada.com/apps/user/register?spm=a1zq7z.27197301.login_form.1.21fd7c73o7cUsS](<https://open.lazada.com/apps/user/register?spm=a1zq7z.27197301.login_form.1.21fd7c73o7cUsS>)

### 1.2 Precautions

a. Do not use the password used to register your account "!" Symbol, otherwise an error may be reported

b. After the account is registered, the profile information needs to be filled in before the app key is created. The next step can be carried out only after the account is approved

c. It is suggested that the created app type is seller in house or ERP. The API call permissions of these two types of APPs are relatively comprehensive, so as to avoid the need to apply for permissions again later

![](https://tida.alicdn.com/oss_1667555436123_null_qBbAyBJA)

## 2\. Create a test order

### 2.1 Borrow a test account

If you want to create a test order, select an area other than SG and CB; At present, CB belongs to the cross border account and cannot create a test order. SG belongs to the test account in Singapore. Due to the national policy of Singapore, the order does not support the COD delivery method. For the test order in the sandbox system, only the COD payment method can directly create a test order; So if you want to create a test order, you can select the accounts in five other regions except SG or CB.

The payment method of the test order created in the sandbox system by default is COD.

![](https://tida.alicdn.com/oss_1667555532954_null_o5wpfBml)

#### 2.1.1 Introduction to the page of successful borrowing

![](https://tida.alicdn.com/oss_1667555595587_null_PpkXDkah)

### 2.2 Create Test Case

#### 2.2.1 Test Case Page Description

Each app key can create 10 cases every day. After reaching the upper limit, you can release the account and re borrow it

![](https://tida.alicdn.com/oss_1667555728859_null_nB2J0uPh)

#### 2.2.2 How to find items in the seller center_ id

a. Click the login button to enter the Seller Center

**![](https://tida.alicdn.com/oss_1667555799261_null_bPj6SXbU)**

b. Find the Manage Products column, select a product at random, click Edit, and enter the background of the Seller Center

**![](https://tida.alicdn.com/oss_1667555819212_null_YtzaQMgG)**

c. The number in front of "Shop_SKU" is "item_id"

**![](https://tida.alicdn.com/oss_1667555852607_null_lXyav21k)**

d. If you want to test the quick and proper delivery of the order, you can change the transportation mode of the goods to shipped By Seller

![](https://tida.alicdn.com/oss_1667555875843_null_cyGq9rrz)

### 2.3 Log in to the Test Seller Account and the Test Buyer Account at the same time and find the test order just created

![](https://tida.alicdn.com/oss_1667555937879_null_8dW0jtvx)

![](https://tida.alicdn.com/oss_1667555955051_null_DI6ftPjE)

### 2.4 Change the status of the test order in the seller center

#### 2.4.1 Step 1 pending>packed

First, click the To Pack column to find the order in pending status, click print only, and then the order will change to packed status

![](https://tida.alicdn.com/oss_1667556031323_null_hRUJLq9l)

#### 2.4.2 Step 2: Packed>Ready to ship

Then click the Ready To Ship button to set the order status to RTS

![](https://tida.alicdn.com/oss_1667556083659_null_EP1Gd4pl)

#### 2.4.3 Step 3 Ready to ship>successful delivery

In order to facilitate testing, it is recommended that all test orders use goods that support self delivery. Test orders created by such goods can be directly set to delivery status in the seller's center to facilitate the reverse process of testing orders later

![](https://tida.alicdn.com/oss_1667556113869_null_SM0LDsHB)

#### 2.4.4 The order has been delivered

![](https://tida.alicdn.com/oss_1667556145783_null_zR1tbG0O)

![](https://tida.alicdn.com/oss_1667556155522_null_ckQ1pZD5)

## 3\. The following is the reverse process of the test order

### 3.1 Refund only

#### 3.1.1 First find the order that has been properly placed on the test buyer account page and click RETURN

![](https://tida.alicdn.com/oss_1667556240022_null_6l1Npo71)

![](https://tida.alicdn.com/oss_1667556253970_null_WLpLFPLj)

#### ![](https://tida.alicdn.com/oss_1667556266311_null_wJVNGqSc)

#### 3.1.2 Find this order in the Return Orders column of the seller's shop, and select the corresponding refund method. Here, select the first return only

![](https://tida.alicdn.com/oss_1667556448872_null_7lpjeduA)

![](https://tida.alicdn.com/oss_1667556465080_null_ac9934Id)

![](https://tida.alicdn.com/oss_1667556480098_null_DGlSio7E)

### ![](https://tida.alicdn.com/oss_1667556494160_null_g5oTLWGf)

### 3.2 Return refund

#### 3.2.1 The seller selects the return&return method

![](https://tida.alicdn.com/oss_1667556592211_null_yy72BiGS)

![](https://tida.alicdn.com/oss_1667556610681_null_EDWKz62c)

**3.2.2 The buyer chooses the logistics method of return**

![](https://tida.alicdn.com/oss_1667556667265_null_U3gKNJw6)

#### ![](https://tida.alicdn.com/oss_1667556682002_null_KFcP9JfF)

#### 

#### 3.2.3 The seller waits to receive the buyer's package

![](https://tida.alicdn.com/oss_1667556706372_null_qkyXNwD5)

#### 3.2.4 The seller receives the buyer's package

![](https://tida.alicdn.com/oss_1667556761215_null_23A7KvJb)

![](https://tida.alicdn.com/oss_1667556780103_null_VXLYfF2D)

![](https://tida.alicdn.com/oss_1667556796987_null_XubVWc8F)

#### 3.2.5 The seller verifies the package and chooses to agree to refund or refuse to refund. This example chooses to agree

![](https://tida.alicdn.com/oss_1667556894452_null_niGSrjNp)

![](https://tida.alicdn.com/oss_1667556907566_null_TCQt2qQ0)

#### 3.2.6 Wait for Lazada to complete the refund

![](https://tida.alicdn.com/oss_1667556982040_null_pKFIgYGC)

![](https://tida.alicdn.com/oss_1667556998142_null_Utc38SgC)

![](https://tida.alicdn.com/oss_1667557010373_null_Qww4zY8y)