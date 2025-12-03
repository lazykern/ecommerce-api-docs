# Chapter I Purpose and scope

## 1.1. Purpose

In order to create a standardized, orderly and secure Lazada open platform environment, enhance the application security provided by Lazada open platform partners (hereinafter referred to as “developers” or “you”), thereby protecting the legitimate rights and interests of developers and users. This specification is specially formulated for Lazada Open Platform Partners and Users to implement adequate level of security measures when integrate their services with Lazada Open Platform.

## 1.2. Scope of application

This specification specifies the security guidelines for the development, deployment, operation, maintenance, and management of applications provided by developers, and is applicable to all developers and operators of related applications.

# Chapter II Terms and Definitions

the term | definition
---|---
E-commerce | Business activities in electronic form. It enables the sharing of standardized, unstructured or structured business information between suppliers, consumers, government agencies, and other business partners through any electronic means to manage and execute transactions in commercial, administrative, and consumer activities.
LazOps | Lazada Open Platform, referred to as “LazOps” or “open platform”, refers to the opening of various e-commerce services based on Lazada platform. Some software and supporting materials are provided by Lazada. Developers develop applications through these software and supporting materials to serve themselves or Serve other users of Lazada platform. Developers can invoke specified functional services through the open platform application programming interface, access user-related data provided by Lazada or user authorization, and/or data information from other Lazada applications, or be provided to Lazada by the developer application. Reflow data. Open platforms may include, but are not limited to, one or more APIs, programming tools, and documentation.
Developer | Refers to Lazada members who can apply for and develop applications based on open platforms through effective application and verification. Developers in open platforms can also be called “Lazada Partners”or "Independent Software Vendors (ISV)".
Application | Refers to software or services developed by developers based on open platforms, including both self-use and other applications.
App key & App secret | Refers to the application access account and key granted by Lazada from the developer when applying to develop a new application. The App key is the unique identifier of the application. Lazada uses the App key to identify the identity of the application developer. App secret is the key assigned by Lazada to the application. The key can guarantee the reliability of the application source under certain technical conditions.
Information security | Protecting and maintaining the confidentiality, integrity and availability of information can also include the nature of authenticity, verifiability, non-repudiation, reliability and so on.
Security strategy | A set of rules, guidelines, and practices for managing the security, integrity, and distribution of assets (including sensitive information) within an organization and its systems, especially those that have an impact on system security and related elements.
User | The organization or natural person who uses the application provided by the Taobao partner is based on the registered ID and user information.
Merchant | A legal person, legal entity, other organization or natural person appointed by a legal person or legal person who rents an e-commerce platform for business activities.
Online transaction | A trade in goods or services that occurs between companies (or other organizations), between businesses (or other organizations) and consumers, and between consumers through online means.
Secondary verification | When the user performs some important or sensitive business operations after registering or logging in, the second verification is performed on the user by using a verification code, a short message, a security question, a digital certificate, and the like in addition to the password.
Encryption | Encryption is the process of processing a plaintext file or data into an unreadable piece of code (often called "ciphertext").
Security incident | Specifically, it refers to e-commerce security incidents, including not only security incidents caused by attacks or intrusions on the network, but also malicious acts such as fraud, hacking, and ban on e-commerce applications.
Sensitive data | Sensitive business data include: Product information, such as price, stock, and promotion details. Order and order item details Customer name and contact information Financial and transaction statements
Information security risk | The threat of man-made or natural threats to the use of information systems and their management systems leads to the occurrence of security incidents and their impact on the organization.
OMS | Order Management System (OMS) is a part of the logistics management system. It manages and tracks the orders placed by customers, dynamically grasps the progress and completion of orders, and improves the efficiency of operations in the logistics process, thus saving operating time. And operating costs to improve the market competitiveness of logistics companies.
WMS | Warehouse Management System (WMS) is a function of warehousing, outbound, warehouse transfer, inventory transfer and virtual warehouse management. It integrates batch management, material correspondence, inventory counting, quality inspection management, and virtual warehouse management. Management system that integrates functions such as management and real-time inventory management, effectively controls and tracks the whole process of logistics and cost management of warehouse business, and realizes perfect enterprise warehouse information management.
WAF | Web Application Firewall (WAF), the WAF mentioned in this article refers specifically to a security service provided by Cloud Shield, which provides WEB security protection services for cloud hosts, which can effectively prevent hackers from exploiting application vulnerabilities. .
Webshell | Webshell is often referred to as an anonymous user (intruder) who has some degree of access to the WEB server through the WEB service port. Since it is mostly in the form of web scripts, some people call it a backdoor tool.
DataMoat | DataMoat is the dedicated data security solution for open platform. DataMoat provides following main services to ISV including data protection, data risk detection, and security review collaboration. It provides DataMoat APIs for ISV app to integrate with, in order to achieve account protection.
UEBA | UEBA Device Fingerprinting verification is an automated process in DataMoat. The purpose of Device Fingerprint is to generate a unique identifier of the device that accesses sensitive data for logging purposes.

 

# Chapter III Overview

Applications developed by developers provide support and services to merchants on e-commerce platforms and must have the ability to ensure data security in their participation in e-commerce activities. The security requirements imposed by the specification on the application developed by the developer include, but are not limited to, the security setup of hosting environment and the configuration of network protection function, the development of the security function of the application, the security risk notification used by the user, and the security management of the developer's operation.

# Chapter IV Security Technology Configuration of Application , Network & Infrastructure 

## 4.1 Enable LazOps Security Function

This section is a security requirement for the technical configuration of the LazOps infrastructure that the developer application depends on, including: the built-in security of the LazOps security function, the security configuration of the host resources on which the application depends. Security configuration when applying related access.

###  4.1.1 Security Architecture Requirements

This section is a security requirement for the technical configuration provided by LazOps and DataMoat platform to detect common attacks on the authentication system such as brute force attack and account enumeration. 

Security Item | Specific Requirements
---|---
IP Whitelisting | For the APPKEY IP whitelist, the application administrator should set the IP access source range of the application calling Lazada Open API in the LazOps platform, and should bind the host external network IP and not bind the IP network segment; To do this, please login to LazOP platform ( https://open.lazada.com/ ) > click on "APP Console" > click the "Manage" link under each app > Click "IP Whitelist" at the left menu > then add the Server Public IP address that allowed to call the API.
UEBA | All application must implement the UEBA in their application , please refer Security Centre for implementation steps . UEBA Device Fingerprinting verification is an automated process in DataMoat. The purpose of Device Fingerprint is to generate a unique identifier of the device that accesses sensitive data for logging purposes. The output of the Device Fingerprint step is the _ati value which uniquely identifies the browser or the client-side machine that will be associated to the logs collected during Account Risk Control stage.
Account Risk Control | The application should be connected to Lazada DataMoat's account risk control, so that it has the security ability to protect and manage the platform account, and can timely identify the abnormal risks of the account (including but not limited to account theft, brute force, etc.), and Give timely control. Please refer Security Centre for implementation steps
Application Architecture | The application design should implement three-tier architecture and end user should never interact with database directly for data process. The 3 tiers including follows: Presentation Tier : Displays information either on web page or a client-side application. This tier should never store sensitive data such as app credential or customer personal information. Application Tier : Controls application functionality by performing business logic or data process. It prepares information to be presented on presentation tier. Data encryption/decryption is recommended to be implemented at this tier. Data Tier: Houses database servers where information is stored and retrieved. Data in this tier is kept independent of application servers or business logic. Data Tier should never be exposed to the internet for public access. Here are some examples of application fullfill 3-tier architecture: Web Portal with implementation of web sever/component, app server/component and data management component/database. Client side application (e.g. windows app) with back-end app services and centralized database server. Automated back-end script retrieving data form Lazada API and stores the data into existing OMS/ERP/CRM application centralized database. The existing OMS/ERP/CRM is in scope of security review and it should follows 3 tier architecture as described in above examples 1 and 2. Following types of application is not allowed to access unmasked data: Standalone client-side application: the client side application invokes LazOP API directly and all data are retrieved to the client app directly. Encryption key and app secret are stored in the client-side app directly. Scripts that retrieves LazOp API data with no user authentication.
 | 

 

###  4.1.2 Network , Host and Server Security Configurations

Security item | Specific requirements
---|---
Virus & Malware Defenses | Utilize centrally managed anti-virus & anti-malware software to continuously monitor and defend each of the organization’s workstations and servers.
Port , Protocols & Services | Ensure that only network ports, protocols, and services listening on a system with validated business needs are running on each system.
Protect Information through Access Control Lists | Protect all information stored on systems with file system, network share, claims, application, or database specific access control lists. These controls will enforce the principle that only authorized individuals should have access to the information based on their need to access the information as a part of their responsibilities.
Host Based Firewall & Port Filtering | Apply host-based firewalls or port filtering tools on end systems, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed.
Implement Application Firewalls | Place application firewalls in front of any critical servers to verify and validate the traffic going to the server. Any unauthorized traffic should be blocked and logged.
Network Security Configurations | Maintain standard, documented security configuration standards for all authorized network devices. All configuration rules that allow traffic to flow through network devices should be documented in a configuration management system with a specific business reason for each rule, a specific individual’s name responsible for that business need, and an expected duration of the need. Install the latest stable version of any security- related updates on all network devices.
Network access control | a) An organization's internal network domains and external network domains should be seperated and protected by a defined security perimeter such as firewall or virtual private networks. b) Segregation of networks should be based on the value and classification of information stored or processed in the network, levels of trust, or lines of business, e.g. production, staging and QA environment should be segregated and the interaction should be controlled by network access control.

 

# Chapter V Application Security Function Development

This section is a security requirement for the security functions that developers should develop and implement, including account management, identity authentication, rights management, and security auditing.

## 5.1 Account, Authentication and Permissions

Security item | Specific requirements
---|---
Login control | The application should identify and authenticate users who log in to the application.
Unique Account | The application should assign different accounts to different users, ensure that one user has one account, and should prohibit multiple people from using the same account.
Multi-store binding | If the application involves accessing/managing multiple Lazada stores (multi-store binding), the application should verify the user's real right to manage the store during the process of binding the user to the associated store. The verification should pass the “Multifactor Authentication” method.
Account lockout | The app should limit repeated access attempts by locking the user account after six login attempts; the lock lasts for at least 30 minutes, or until the administrator activates the user account.
Inactive account deletion | The application should delete or prohibit redundant and expired user accounts in time to avoid the possibilities of shared accounts.
Account permission recovery | The application should promptly clean up and recycle application-related development accounts, test accounts, and background management accounts and permissions, such as when the relevant account user leaves or shifts to the post.
Initial password | The initial password of the application administrator account shall be the password randomly generated by the system to meet the password strength requirement.
Change password | The application should periodically remind the user to modify the password on a regular basis (every 90 days). It is recommended that the password must changed at least every 90 days
Password strength | The password strength should meet the following requirements: a) The application should keep the password history in encrypted form and require that the new password be different from the password used in the last four times; b) The password cannot be empty; c) The default password is not allowed; d) The password is at least 8 digits in length ; e) Contains three or more of uppercase letters, lowercase letters, numbers, and special characters. You cannot use consecutive letters or simple numbers. You cannot use consecutive characters on the keyboard. f) Words that are strongly associated with the user (such as birthday, name) cannot be used.
Password reset | The application should provide the user with a password reset function. The password reset function should ask users to provide existing password or security question & answers set by user during registration process, and the reset password link must be sent to the user by side channel (such as SMS or mail )
Re-verification | When the session is idle for more than 30 minutes, the app should require the user to re-authenticate or reactivate the session.
Multifactor authentication | a) The application should support the identification of two or more combinations of the same user (password verification, mailbox verification, SMS verification, etc.) to achieve user identity authentication; b) In the case of performing sensitive operations (password modification or reset) or sensitive account behavior, the application shall use two or more combined authentication methods. Description: SMS and email authentication can be sent to the trusted mobile phone number or mailbox bound by the user, and the expiration time needs to be set for the authentication information. It is recommended to be 10 minutes.

 

## 

## 5.2 Log Auditing

Security item | Specific requirements
---|---
Audit all user behaviors and actions | The application should provide a security audit function that covers each user and audit important security events. The audit content should include important user behavior (including: all login access, database calls, LazOps calls, access to the client and orders).
Log storage protection | The application should protect the integrity of the stored log audit records from unintended deletions, modifications, or overrides.
Log retention period | The app should save the log for at least six months.
Client device fingerprinting | The application should record and report the logs from the client by integrate with the Device Fingerprint feature in DataMoat.
Application login log | a) The application should record and report all login logs of the application by calling the DataMoat Login API and ComputeRisk API , including but not limited to: 1) The log of the user login application; 2) The application administrator logs in to log in to the background login log; 3) System login by the host. b) The contents of the log should include: time, user's own account in the developer, user's Lazada account, application identification ( App Key ), application name, source IP and login result (success or failure), etc. Please refer Security Center for more details

 

## 5.3 Data Protection

###  5.3.1 Data Access

Security item | Specific requirements
---|---
Access | Prohibit applications from initiating LazOps API data requests from servers outside the Application Associated with the Appkey, including but not limited to ERP/ invoicing software, developer back-end systems, merchant back-end systems, customer relationship management, promotion management, orders Management, order payment, merchandise management, warehouse management system, online ordering application, collaborative office, express delivery application, e-commerce finance, omni-channel ERP , industry / store analysis, customer service.

 

###  5.3.2 Data At Rest

Security item | Specific requirements
---|---
Password storage | The application should encrypt and store the user's password using a secure hashing algorithm with random salt to prevent privileged users from obtaining the user's password, e. g. Argon2, PBKDF2, bcrypt or scrypt . You can refer OWASP cheat sheet for additional reference
Access token storage | The Access Token (authorization token, which is the original Session Key) for which the user data is accessed should be encrypted.
Sensitive data storage | Sensitive data storage should fulfill following requirements: Sensitive data should not be stored in client side and protected by access control. Sensitive data should be encrypted when stored into database with strong encryption algorithm in secured mode. (e.g. AES with at lease 128 bits key length and in GCM mode) Secret key should be protected in key vault which iis away from encrypted data. Secret key should not be stored on client side.
Data backup & recovery | a.)Ensure that all system data is automatically backed up on a regular basis. b.) Ensure that all of the organization’s key systems are backed up as a complete system, through processes such as imaging, to enable the quick recovery of an entire system.

 

###  5.3.3 Data In Transit

Security item | Specific requirements
---|---
Transport layer protection | a) The transmission of sensitive data (such as order data, etc.) in the application must be encrypted and transmitted to achieve the confidentiality of transmission of system management data, authentication credentials and important business data i.e. TLS/SSL b) Only support strong protocol TLS 1.2 or above with strong cryptographic cipher suites. c) Transport layer protection should be implemented in internal network application and back end server-to-serer communication as well. You can refer OWASP cheat sheet for additional reference

 

###  6.3.4 Data In Processing

Security item | Specific requirements
---|---
Data processing | When the application processes or calculates its sensitive data (such as order data, etc.), the components and modules of its related functions should be at server side.
Data Masking | Applications should be desensitized (fuzzy, anonymized, etc.) for presentations involving sensitive data (such as phone numbers, emails, Lazada nicknames, etc.). Recommended desensitization program: a) [Mobile phone number] displays 4 digits after *+. Such as: ******1050; b) [Fixed number] displays the area code and the last three digits, such as 0571-*****123; c) [Mailbox] If the character preceding @ is greater than or equal to 3 characters, the character preceding @ will only display the first 3 digits and add 2 more *, and @ will display its first character, '.' separator and The characters after it, but the other characters in it are uniformly replaced with 2*, for example: con**@1**.com; if there are less than three digits, the characters before @ are all displayed and 2 more* are added, and @The following shows the first character, the '.' separator and the characters after it, but the other characters are replaced by 2*, for example, tt@163.com is displayed as tt**@1**. Com; d) [Lazada nickname] display 1 position for the first/tail, plus * in the middle: for example: a*1; e) [Receipt address] The address of the hidden area/below county level.

 

# Chapter VI Security Management Requirements for Operations

This section is a security requirement for developers to implement security management in the development and operation of developer applications, including: security management of the application development process, related security vulnerability management, and security in daily operation and maintenance.

## 

## 6.1 Vulnerability Management

Security item | Specific requirements
---|---
Vulnerability scanning | Before the application goes online, the developer should perform an authenticated vulnerability scan on the front and back system to ensure that there is no vulnerability in the online application and submit the scan result to Lazada.
Vulnerability fix | Developers should track and manage vulnerabilities, requiring risk vulnerabilities to be fixed in adequate time
Penetration test | Developer conduct regular external and internal penetration tests to identify vulnerabilities and attack vectors that can be used to exploit enterprise systems successfully. The application should be reviewed for security testing/penetration testing through the Lazada Open Platform. The application must ensure that it is free from OWASP Top 10 vulnerabilites including, but not limited to: 1. Injection attacks like SQLi, Command injection 2. Information Leakage 3. Remote code execution 4. File upload vulnerbailities 5. Access control vulnerbailities (Insecure Direct Object Reference) 6. Cross site scripting (Reflected, Stored, DOM) 7. CSRF 8. URL redirection 9. Using vulnerable components The developer may also provide the penetration testing report to Lazada security team but test is conducted independently by an independent third party testers. Developer should perform security testing on applications handling Lazada customer data from time to time in the event of major environmental changes (such as acquisitions, mergers, relocations, etc.), and perform appropriate actions based on security testing results (eg, patch management, Software upgrade, system reinforcement, etc.),
Vulnerability information disclosure | a) Developers should notify Lazada in time when they find that there is a defect in the LazOP. Under no circumstances should it be concealed or maliciously used; b) Developers should promptly notify Lazada when there are security vulnerabilities in self-developed applications, operating systems, and related third-party applications/code components used. Under no circumstances should you attempt to verify weaknesses in a production environment.

 

## 6.2 Operation and maintenance security

Security item | Specific requirements
---|---
Information Security Point of Contact | Developers should provide the contact details of full time information security personnel (development, testing, operation and maintenance, management, etc.) to Lazada and maintain secure contact and communication on a regular basis.
Change management | a) Developers should identify key change requirements in application development and operations and develop relevant change plans; b) Developers should establish relevant change processes and approval mechanisms; c) When the relevant system changes, the developer shall notify all relevant personnel (development, testing, operation and maintenance, management, etc.); when the change is implemented, it must be recorded and the records should be properly kept.
Incident Response | a) The developer ensure that there are written incident response plans that define roles of personnel as well as phases of incident handling/management. b) The developer shall establish a team responsible for the online incident response, clarifying the role of the security incident response and the responsible personnel / organization and any security incident should report to Lazada through Lazada Open Platform tickets d) Developers should monitor security vulnerabilities and threat intelligence of related software programs and timely fix security vulnerabilities in applications and related support systems; e) Developers should document and maintain security vulnerabilities and suspicious events in all reports, analyze the cause of the incident, monitor developments, and take steps to avoid security incidents;

 

# Chapter VII User Security Guidance

This section is a security requirement for the developer to apply and pay attention to the relevant security risks in the process of being used, including: through the user manual and system prompts to inform users how to effectively use the application's security features, and the bad user behavior that users should pay attention to and avoid.

## 7.1 User Manual

Security item | Specific requirements
---|---
Introduction to security functions | For seller users of the app, developers should provide detailed and comprehensive operational guidance documents (such as help files and paper documents) that are easy for users to query and guide users to use or configure the security features of the app provided by the developer. Should be written in the document security features provided in applications introduced for the user affect the operating system security (such as changing passwords, configure permissions, etc.), it should be clearly prompted the risks associated with the operation; to affect the normal operation of the application Key configuration items and actions, as well as warning signs are applied to the documentation and indicate their possible impact.
Data interaction between applications | a) The developer should inform the user to protect the password, including: verifying the password strength and prompting the user to set a strong password, setting the password to modify the default period, expiring the prompt to change the password, and the password must not be stored locally; b) The developer should inform the user of the insecure daily use behavior and basic security recommendations for the safe use of the terminal: including: screen security security settings, timely upgrade of the operating system, effective installation of anti-virus software, and proper configuration of the host firewall , application software download and installation; c) The developer should inform the user of the safe use of the mobile terminal, including: setting the screen unlock password or pattern, effective installation of anti-virus software, etc.; d) Developers should inform users of the security management of removable storage including: thumb drive, external hard should be securely stored & access to the storage should be password protected, etc. e) Developers should inform users of the safe access to the Internet, including: wireless Internet access, Internet access, email, social networking, instant messaging, online transactions, etc. f) Developers should inform users to prevent social engineering-based fraud, including: Based on people: physical unauthorized access; Based on the phone: the deception of the caller's phone; Based on email: phishing attacks, email address spoofing; Based on instant messaging software: spoofing through WhatsApp, Messenger, etc.
 | 

 

## 7.2 Security Awareness Training 

Security item | Specific requirements
---|---
Security Awareness Training | a.)Create a security awareness program for all workforce members to complete on a regular basis to ensure they understand and exhibit the necessary behaviors and skills to help ensure the security of the organization. The organization’s security awareness program should be communicated in a continuous and engaging manner. b.) Developers security lead must attend the LazOps security awareness program once in a year.
Secure Coding Training | Ensure that all software development personnel receive training in writing secure code for their specific development environment and responsibilities.