**1.   Introduction**

 

1.1  These Security Measures for Service Providers ("**Guidelines** ") set out the technical security requirements which the Service Provider has to fully comply with and forms a part of the Terms of Use between Lazada and the Service Provider.

 

1.2  In these Measures, unless the context otherwise requires, the following expressions shall have the following meaning: 

  * "**ITSM** " means an IT security manager.
  * "**ITSO** " means an IT security officer.
  * "**Lazada**  **Representative** " means Lazada's employees who liaise with and/or provide instructions to the Service Provider. 
  * "**Service Provider** " means you, or means the entity (if any) for which you are acting on behalf of by entering into the Terms of Use. 
  * "**Services** " means the services which the Service Provider provides to Lazada pursuant to any written agreement which these Guidelines are expressly incorporated into by reference, which shall include without limitation the Terms of Use.
  * "**Sub-Service Provider** " means the Service Provider's sub-contractor, provided that (a) subcontracting is expressly permitted by the Terms of Use or by the terms of any other written agreement between Lazada and the Service Provider relating to the Services and/or the System; and (b) the prior written approval of Lazada has been obtained by the Service Provider from Lazada to Service Provider's engagement of the sub-Service Provider in question; and 
  * "**System** " means all application(s) that interact and/or has been implemented by Service Provider for Lazada for the purposes of providing the Service Provider's Services.



 

 

**2.   Security Objectives **

 

**Clause No.** |  **Requirement Description**  
---|---  
2.1 |  The Service Provider shall provide its Services in accordance with the security requirements as specified in these Measures.   
2.2 |  The Service Provider shall implement security controls that can be integrated with, and work with the systems and services provided by other Lazada-appointed suppliers/Service Providers.  
2.3 |  The Service Provider shall incorporate the following security principles in the design, implementation and operation of the System:   
(a) Confidentiality: non-disclosure of information to unauthorised entities;   
(b) Compliance: conformance to established regulations and standards;    
(c) Availability: accessible and usable when authorised entities demand access;   
(d) Authentication: verification of identities of entities and their claimed attributes;   
(e) Accountability: traceability of an entity's actions to the entity;   
(f) Non-repudiation: assurance of authenticity;   
(g) Integrity: accurate and complete information within the System; and  
(h) Access control: selective authorisation and restricted access or use of assets.  
2.4 |  Upon Lazada's request, the Service Provider shall promptly submit a third party penetration testing report by a certified penetration tester, or a SOC2 / ISO/IEC 27001 certification covering the provision of any proposed software or Software as a Service (SaaS).  
2.5 |  The Service Provider shall provide, all information and security limitations relating to the security design and implementation of the System.   
2.6 |  The Service Provider shall implement security controls to protect the System against unauthorised access, data loss, intrusion, malicious software infection, software vulnerability attacks, and hardware thefts or attacks.  
2.7 |  The Service Provider shall implement the System with no known security backdoors and loopholes.  
2.8 |  The Service Provider shall implement the System with no unauthorised code.  
2.9 |  The Service Provider shall implement appropriate control measures to protect all data, in storage, during processing and during transit.  
2.10 |  The Service Provider shall document all processes, procedures and control measures adequately and properly.  
2.11 |  The Service Provider shall implement and deploy all items of the System with configurations that are security hardened and would address all security vulnerabilities.  
2.12 |  The Service Provider shall have an effective patch management program in place and implement security changes, patches and upgrades in Systems, applications, and databases in a timely manner in accordance with the risk levels.  
2.13 |  The Service Provider shall ensure that the System is resilient against known cyber-attacks and easily reconfigurable to respond to new security threats that may Lazada from time to time.  
  
 

 

**3.   General Security **

 

**Clause No.** |  **Requirement Description**  
---|---  
3.1 |  The Service Provider shall comply with all security policies, security standards, security guidelines, and security frameworks that may be issued by  Lazada  from time to time and implement all changes requested by Lazada without delay.  
3.2 |  The Service Provider shall perform security risk assessments on the System pursuant to Clause 12 and maintain an updated risk register.  
3.3 |  The Service Provider shall develop and maintain security policies, security architecture, standards, procedures and processes in accordance with industry standards and best practices. The Service Provider shall keep all such documentation updated and  demonstrate the same to Lazada when requested.  
3.4 |  Where programming is required, the Service Provider shall adopt secure coding practices. The Lazada Representative shall have the right to review software security audit or test reports generated by the Service Provider and the reports generated from the Service Provider's source code analysis tools. The Service Provider's source code analysis tools shall be subjected to Lazada's review when so required.  
3.5 |  Lazada reserves the right to audit the information security controls and processes of the Service Provider and to perform relevant tests to ensure that it is compliant with applicable information security and privacy requirements as well as the requirements under the Terms of Use.   
3.6 |  If the Lazada Representative performs security assessments, security reviews, security audits, surveys, penetration tests, and investigations (including forensics) on the System, the Service Provider shall cooperate and furnish all requested materials in a timely manner, including remediation of all security findings as per clause 12.3.  
3.7 |  The Service Provider shall install endpoint protection agents on the System to protect against any potential data leakages.  
  
 

 

**4.   Cryptography And Digital Certificate Standard **

 

**Clause No.** |  **Requirement Description**  
---|---  
4.1 |  **_Cryptography Standards_** The Service Provider shall use industry-recognised strong cryptography standards for symmetric encryption, digital signature, hashing, key exchanges, random number generators and message authentication codes.  
4.2 |  Proper key management processes must be in place to protect the cryptography keys throughout their lifecycle.  
4.3 |  **_Digital Certificate Standards_** The Service Provider shall use industry-recognised strong digital certificate standards for the implementation of digital certificate and certificate revocation lists in the System.  
  
 

 

**5.   Authentication And Access **

 

**Clause No.** |  **Requirement Description**  
---|---  
5.1 |  The Service Provider shall implement industry-approved access and authentication mechanisms and perform periodic reviews.    
5.2 |  The Service Provider shall ensure that 2-Factor Authentication must be enabled for all Systems processing personal data.  
5.3 |  Where Virtual Private Network ("VPN") is required, the Service Provider shall implement industry-approved VPN mechanisms.  
  
 

 

**6.   User Access Management For Service Provider's Personnel **

 

**Clause No.** |  **Requirement Description**  
---|---  
6.1 |  The Service Provider shall implement control measures to protect all account credentials with access to the System. Upon request by the Lazada Representative, the Service Provider shall provide detailed documentation on the control measures and processes (which shall minimally include the security features, technologies, administration usage processes and procedures that will be utilized).  
6.2 |  The Service Provider shall implement appropriate password policies/guidelines/standards and ensure that passwords comply with such policies/guidelines/standards and in any event, with all requirements set out in this Clause 6.  
6.3 |  The Service Provider shall ensure that passwords are not displayed or transmitted in clear text.  
6.4 |  Where passwords are generated or selected by the System for user/admin/root login ("default password"), the Service Provider shall ensure a compulsory password change is done immediately after the first user login.  
6.5 |  All passwords shall contain a minimum of eight (8) characters and comprise at least two (2) of the following four (4) categories:  
(a) upper case (A through Z);  
(b) lower case (a through z);  
(c) digits (0-9); and  
(d) special characters (! $, #, %, etc.)  
6.6 |  The Service Provider shall ensure all passwords are compared against a list that contains values known to be commonly-used, expected, or compromised. If the chosen password is found in the list, the Service Provider shall ensure that they choose a different password.  
6.7 |  The Service Provider shall ensure that all account passwords are changed periodically based on the system criticality in line with industry standards.  
6.8 |  The Service Provider shall enforce password history as per industry standards and best practices.  
6.9 |  For system administration and other privileged user access, such as server console access, the Service Provider shall deploy authentication mechanisms specified in Clause 5.1.  
6.10 |  The Service Provider shall disallow multiple concurrent logins using the same credentials.  
6.11 |  The Service Provider shall ensure that accounts are locked out after 5 unsuccessful login attempts.  
6.12 |  The Service Provider shall implement timeout or automatic logout features to the System for connections that are inactive for more than 10 minutes.  
6.13 |  The Service Provider shall ensure that all system administrative and functional system accounts created or used by the Service Provider's personnel are not shared.  
6.14 |  The Service Provider shall implement security measures and processes to prevent system administrators, database administrators and other privileged users from any unauthorised access to users' information. The Service Provider shall ensure that the logs are monitored to identify any unauthorised access.  
6.15 |  The Service Provider shall log all authentication events, whether successful or failed.  
6.16 |  The Service Provider shall manage all privileged accounts as follows: (a)    Only authorised administrators who require such access to perform their job functions can be assigned privileged accounts on a need-to-know basis; (b)    All privileged account request(s) must go through an approval and authorisation process before access is granted to the administrator(s) for whom the privileged account request(s) are made; (c)    All privileged accounts must be recorded by the Service Provider; (d)    Individual privileged accounts and passwords must be created for and assigned to individual owners for accountability and traceability; (e)    An account for which the account password is collectively defined by the passwords from multiple custodians in accordance with this Clause, or a "shared privileged account", shall have its ownership assigned to each of the specific custodians for accountability; (f)     Privileged accounts must be disabled and removed when the administrators change their job function or leave the organisation, or when the accounts are no longer needed; (g)    Whenever possible, system built-in privileged accounts shall be removed. If the system built-in privileged accounts cannot be removed, they shall be renamed and the password must be changed immediately, and then disabled where possible; (h)    All privileged accounts must be subject to regular reviews; and (i)     All administrative changes performed using privileged accounts shall have audit trails to facilitate investigation if required.  
6.17 |  The Service Provider shall ensure that all system/services accounts comply with the requirements set out in Clause 6 herein. In addition, for system/services accounts, the Service Provider shall ensure that strong and complex passwords are used and changed on a periodic basis.  
  
###  

###  

### **7.   System Security**

 

**Clause No.** |  **Requirement Description**  
---|---  
7.1 |  The Service Provider shall ensure there are security hardening baselines for the System and system hardening frameworks to govern the process to harden all systems and applications in accordance with industry standards.   
7.2 |  The Service Provider shall, at the minimum, perform the following pre-requisite activities for all items of the System to be connected to Lazada networks :  
  
(a) Apply latest patches of all items of the System; and (b) Apply latest anti-malware signatures.  
  
These need to be applied in accordance with the timeframe as specified in their vulnerability management program.  
7.3 |  Where digital certificates are required, the Service Provider shall: (a) deploy certificates signed by appropriate certifying authorities on the limitation and implement mitigation measures; and (b) develop and implement a tracking mechanism to ensure timely renewal of the digital certificates in accordance with industry standards. In the event that such certificates cannot be used, the Service Provider shall provide documentation or evidence from the product principal(s).  
7.4 |  The Service Provider shall propose and implement appropriate security measures and procedures to minimise the risk of introducing malicious content into the System and network.  
7.5 |  The Service Provider shall remove all test data, test accounts and test credentials from the System before commissioning date and/or the date stipulated by the Lazada Representative.  
7.6 |  All accounts shall be assigned with least privileges and need-to-know basis only.  
7.7 |  The Service Provider shall synchronise the time of all items of the System.  
7.8 |  The Service Provider shall implement audit trail and monitoring mechanisms for all security events including authentication, anomalous activity and all privileged roles activities, such as configuration changes performed.  
7.9 |  The Service Provider shall turn on audit trails of the System and take all necessary steps to protect the audit trails from unauthorised access and accidental and/or deliberate modification or overwriting.  
7.10 |  The Service Provider shall ensure adequate information is captured in the audit trail to facilitate monitoring and investigation. Details should include the following but not limited to:  
a) user identity; b) date and timestamp of information access; c) what information was accessed; d) details of access (e.g. modification); e) source IP address from where the request originated from; f) Records of all successful and unsuccessful log-on attempts (logon and logoff); g) Records of any log-on attempts made from an unknown userID and/or workstation ID; h) Records of all privileged operations (i.e. use of admin / super user accounts); i) Records of all updates/changes to userID access rights; and j) Records of all attempts to delete, write or append certain predefined data entities, or any changes made in their classification label.  
7.11 |  The Service Provider shall maintain a technical security architecture diagram with unique names for all the elements, platforms and/or servers, addresses and connections (with all details) towards other elements, platforms and/or servers and submit them when requested by the Lazada Representative.  
  
 

 

**8.   Information Handling **

 

**  
** **Ref #** |  **Requirement Description**  
---|---  
8.1 |  The Service Provider and all its personnel shall safeguard all information that is entrusted to them. The Service Provider shall ensure that all information entrusted is used only for authorized purposes.  
8.2 |  In the event the Service Provider requires any information to be sent to any third parties, the Service Provider shall ensure that there are legal agreements in place to govern such information-sharing and proper due diligence is conducted before information is shared.  
8.3 |  The Service Provider shall sanitize the information through methods such as obfuscation or masking of sensitive data, sensitive before releasing the approved information to relevant parties pursuant to Clause 8.2.  
8.4 |  The Service Provider shall propose measures to protect information against accidental or unlawful loss, as well as unauthorised access, disclosure, copying, use, or modification. The Service Provider shall implement and document such measures which shall include administrative, technical, physical and personnel control measures. The documentation of such measures shall be made available to the Lazada Representative when requested.  
8.5 |  If the Service Provider suspects or detects any loss of information, the Service Provider shall notify the Lazada Representative immediately. The Service Provider shall take preventive measures to prevent further loss of information and perform investigations to ascertain the root cause of the loss of information. The Service Provider shall take instructions from the Lazada Representative for any further actions that may be required.  
8.6 |  The Service Provider shall not remove or retain, and shall ensure that its personnel, agents, directors, officers, servants and employees shall not remove or retain any information when they are no longer assigned to support the System.  
8.7 |  The Service Provider shall handle and transfer information to Lazada via secured channel(s) specified by Lazada representative.  
8.8 |  The Service Provider shall ensure all personal data (including but not limited to the Customer Name, Phone Number, Email Address, and Address) to be encrypted both in storage and in transit. Encryption algorithm must be based on recommended industry standards.  
8.9 |  The Service Provider shall carry out irreversible anonymisation of personal data (including but not limited to the Customer Name, Phone Number, Email Address, and Address ) as soon as the retention of such data is no longer necessary for the purposes of processing (which shall, in any event, be no longer than ninety (90) days).  
  
 

 

**9.   Log And Media Sanitization And Disposal **

 

**Clause No.** |  **Requirement Description**  
---|---  
9.1 |  The Service Provider shall implement log sanitization processes, media sanitization processes and any other mechanisms to protect Lazada's information. The processes and procedures shall be submitted to the Lazada Representative when requested.  
9.2 |  If the Service Provider is required to send any log information, packet captures or any debug information to Lazada-appointed suppliers or personnel not assigned to support the System, the Service Provider shall comply with the process specified in Clause 8.3.  
9.3 |  The Lazada Representative shall have the right to validate the sanitised logs, packet captures, and debug information on a random sampling basis.  
9.4 |  The Service Provider shall develop standard operating procedures (SOP) to securely dispose Lazada data in accordance with industry-recognized guidelines.  
9.5 |  The Service Provider shall perform media sanitization and disposal in accordance with industry-recognized guidelines.  
  
 

###  

### 10.  IT Security Team

 

**Clause No.** |  **Requirement Description**  
---|---  
10.1 |  The Service Provider shall have suitably qualified personnel to function as IT security subject matter experts and to manage the security operations for the System.  
10.3 |  The Service Provider shall provide the Lazada Representative with the contact numbers of the ITSM and ITSO. The ITSM and ITSO shall be contactable twenty-four (24) hours a day, seven (7) days a week, inclusive of Saturdays, Sundays and Public Holidays.  
  
###  

###  

### 11.  Security Training And Awareness 

 

**Clause****No.** |  **Requirement Description**  
---|---  
11.1 |  The Service Provider shall ensure that all its personnel and the personnel of any Sub-Service Provider or third-party suppliers assigned to manage the System undergo yearly training (at the minimum) on the following but not limited to:   
(a) IT security threats and protection; (b) Security awareness; (c) Phishing or other cybersecurity attacks; (d) Data security and data privacy; (e) Security policies, processes and procedures required for their work; (f) Lazada's data and information handling requirements; and  
(g) Processes for reporting issues that may lead to an IT security incident. The Service Provider shall periodically review the content of its security training to ensure that it remains current and relevant. The review should take into consideration changes in its and/or Lazada's IT security requirements, prevalent and emerging risks, current legal obligations under applicable data protection, privacy and cybsersecurity laws and the evolving cyber threat landscape.  
11.2 |  The Service Provider shall conduct training for all its personnel (including staff of any Sub-Service Provider or third-party suppliers) pursuant to Clause 11.1, and maintain records of completion and provide to Lazada Representative when requested. The Service Provider shall periodically review the content of its security training to ensure that it remains current and relevant.  
11.3 |  The Service Provider shall ensure that its existing staff (including staff of any Sub-Service Provider or third-party suppliers) are informed of any content changes to security policies, processes and procedures relating to the System as soon as practicable.  
11.5 |  The Service Provider shall ensure that all its personnel (including personnel of any Sub-Service Provider or third-party suppliers) are aware of their security responsibilities, accountability and liability when carrying out their respective duties.  
  
##  

##  

## 12.  Indepenent Security Assessments

 

**Clause No.** |  **Requirement Description**  
---|---  
12.1 |  The Service Provider shall, at no additional cost to Lazada, engage an independent security assessor (i.e. not affiliated with or related in any manner to the Service Provider) to perform the Pre-Commissioning Security Assessment ("PCSA"). Subsequent security assessments have to be performed at least once every 12 months, or whenever the system undergoes major changes or updates. All security assessments, including the PCSA, shall be performed in accordance with industry standards.  
12.2 |  Upon request by the Lazada Representative, the Service Provider shall provide any industry-recognized certifications and accreditations held by the independent security assessor's organization and their personnel conducting the IT penetration testing.  
12.3 |  The Service Provider shall implement vulnerability management program and ensure that all security risks and findings identified, managed and documented from the activities as specified in Clause 12.1 in a timely manner and records shall be provided to the Lazada Representative when requested.  
12.4 |  The Service Provider shall address and remediate all security risks and findings identified in the Security Assessment in accordance with the timeframe as specified in the requirements as below, unless otherwise instructed by the Lazada Representative. -        For PCSA:  o   Critical / High: All findings to be patched before system commissioning -        For subsequent Security Assessments: All vulnerabilities should be fixed as per the timelines in accordance with the Service Provider's vulnerability management program referred to in Clause 12.3.    
  
 

 

**13.   IT Security Incident Management **

 

**Clause No.** |  **Requirement Description**  
---|---  
13.1 |  The Service Provider shall implement & adhere to the IT security incident handling framework and IT security incident handling technical standard operating procedures ("IT Security Incident Handling Technical SOP") that specify the detailed procedures of handling different types of IT security incidents as per industry standards. The IT Security Incident Handling Technical SOP shall minimally include malware activity, inappropriate usage or unauthorised access, unauthorised disclosure of sensitive data (including personal data), web defacement, suspicious network activities, Distributed Denial-of-Service ("DDoS") and network scanning and reconnaissance, and shall be submitted to Lazada prior to the commissioning date and/or upon request. The Service Provider shall incorporate such changes required by the Lazada Representative into the IT Security Incident Handling Technical SOP.  
13.2 |  The Service Provider shall carry out and complete a first review of the IT Security Incident Handling Technical SOP within 12 months after the commissioning date and/or upon request. Thereafter, the Service Provider shall review the IT Security Incident Handling Technical SOP minimally on an annual basis or as required by the Lazada Representative. All changes to the IT Security Incident Handling Technical SOP shall be subjected to the Lazada Representative.  
13.3 |  In the event of any IT security incidents, the Service Provider shall:  
(a) Investigate, resolve and recover from the IT security incident; and   
(b) Retain all information related to the IT security incident in an incident report and incident record for the duration of the System.  
13.4 |  The Service Provider shall assign suitably qualified personnel as the primary point of contact for all IT security incidents related to the System.  
13.5 |  The ITSO shall take all necessary actions to ensure that all IT security incident are handled and managed in accordance with the IT security incident handling framework and the approved IT Security Incident Handling Technical SOP. The Service Provider shall also implement measures to prevent the occurrence of IT security incidents. The Service Provider shall support the Lazada Representative and Lazada-appointed suppliers in resolving IT security incidents.  
13.6 |  The Service Provider shall ensure that the ITSO and the requisite resources are available to carry out immediate investigation and implement workaround solutions in the event of an IT security incident.  
13.7 |  Responding, Initial Diagnosis and Escalation: The ITSO shall inform the parties listed in the IT Security Incident Handling Technical SOP within the expected response timeline specified by Lazada.  
13.8 |  Responding, Initial Diagnosis and Escalation: The information to be provided shall include the incident reference number, description, date and time, and the impact (including the affected parties) of the incident.  
13.9 |  Investigation, Diagnosis and Resolution: The ITSO shall resolve the IT security incident or implement a workaround within the expected resolution timeline specified by Lazada.  
13.10 |  Resolution for preventing recurrence incidents: For cases where workarounds are implemented, the ITSO shall identify the root causes and implement permanent resolutions.  
13.11 |  Closure: The IT security incident record or report shall be closed only with the Lazada Representative's approval. The Lazada Representative shall have the right to verify the details in the incident record or report and the Service Provider shall cooperate to facilitate such verifications.  
13.12 |  IT security incident response exercises: After the System has been commissioned, the Service Provider shall conduct internal IT security incident response exercises at least once a year to ascertain its ability to manage and handle IT security incidents. The Service Provider shall submit an annual plan that details the incident response exercises that will be conducted for that particular year. The Service Provider shall present its incident response exercise findings and improvement plan after each exercise to the Lazada Representative.  
13.13 |  The Lazada Representative may conduct IT security incident response exercises from time to time. These exercises can include testing the Service Provider's readiness to deploy emergency security patches to the System. The Service Provider shall provision and commit the necessary resources and personnel to participate in the IT security incident response exercises.  
  
###  

###  

### 14.  Personal Computer, Email & Storage Device Security Controls

###  

**Clause No.** |  **Requirement Description**  
---|---  
14.1 |  The Service Provider shall ensure that all approved endpoints used by the Service Provider for the provision of the System are not used for other purposes or projects unless otherwise specified in the Terms of Use or in any other written agreement between Lazada and the Service Provider in relation to the System.  
14.2 |  The Service Provider shall manage the approved endpoints in accordance with the requirements as specified in Clause 9.  
14.3 |  The Service Provider shall update all approved endpoints with relevant security updates, patches, configurations and anti-malware signatures to prevent any security vulnerabilities from being exploited.  
14.4 |  The Service Provider shall ensure there are adequate controls to protect against malware in email, spoofed emails or spam emails in all email communications with Lazada.  
14.5 |  The Service Provider shall ensure access to their email accounts are using strong authentication and industry recognised strong encryption.  
14.6 |  Lazada shall have the rights to stipulate and enforce additional control measures for approved endpoints, email and removable storage media without notice to the Service Provider. The Service Provider shall fully comply with all control measures issued by Lazada at all times. In the event of security breaches, security violations, or malware infections on approved endpoints and removable storage media, the Service Provider shall notify the Lazada Representative immediately without delay.  
  
###  

###  

### **15.   Applicaiton And API Security**

 

**Clause No.** |  **Requirement Description**  
---|---  
15.1 |  Where API is present, the Service Provider shall ensure their Application Programming Interfaces (APIs) are not vulnerable to the latest version of OWASP API Security Top 10 Risks.  
15.2 |  Where programming or API is required, the Service Provider shall ensure all applications and APIs are compliant with the latest version of these Security Measures.  
15.3 |  The Service Provider shall be able to comply with role-based authentication for the use/reuse of API for multiple services. Users should be able to access only allowed resources/procedures/methods in the API complying with "need to know" principle.  
  
 

 

 

#