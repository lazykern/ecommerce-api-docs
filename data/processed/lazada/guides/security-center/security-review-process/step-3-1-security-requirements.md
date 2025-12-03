The purpose of this step is to ensure the sensitive information is properly protected. There are two types of sensitive data:

  1. **For p****assword:** to verify that password is hashed with salt, complexity requirements are imposed, password history is maintained, and password expiration date is set. Please use strong hash algorithm such as SHA2 or slow hash functions such as Argon2, PBKDF2, bcrypt or Scrypt . Please note that MD5 and SHA1 are weak and broke. 
  2. **For customer sensitive personal information** : sensitive data should be encrypted with at application level before saving into the database. Please use strong encryption algorithm with adequate key length such as AES with at lease 128 bits key length and in GCM mode.



 

![](https://tida.alicdn.com/oss_1649837291664_null_1QOFOwia)

 

 

 

LazOp team will review the submitted information:

  * If all security requirements are fulfilled, the request will be moved to step 3.2 within 1-5 days. 
  * If any of the security requirements is not met, the request will be rejected with rejection feedback. Please review the feedback and make necessary changes to the application before submitting the step 3.1 form again.