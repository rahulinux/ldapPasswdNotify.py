ldapPasswdNotify.py
===================

# Why this script reuqired ?

If you are managing LDAP Server and you want to notify users to change there password via email then this script is useful for you. 

# How it will work ?

This script will check `pwdChangedTime` in each user Object and password change time and As per Default Global Password Policy Password Should be change in 45 days and if  password not been updated  than 31 days ( i.e 45-14  where 45 is password expiry and 14 is warning) then will notify users via email to change password, it will send mail until next password update

# Prerequisites

  - Before using this script, you need following things :

  - By Default there is no restriction for Password Policy, we need to add schema for this. So you can refer following Link to Add pwdpolicy schema into your LDAP Server.

  - <a href="http://linuxian.com/2013/09/26/how-to-implement-pwdpolicy-openldap/">How to implement pwdpolicy OpenLdap</a>

  - This Script is Using Python LDAP API, to perform faster LDAP Query and making it more simple. So you will need to install package python-ldap. which can simply install using Yum

  - This Script is Tested in Python Version 2.4.3, if you are using Old Version, then this script will not work, you need to some modification to get job done.  
    
    
# What else?
If you have any questions or suggestions,  you want to share anything else with me, feel free to drop me an e-mail . 
I appreciate any feedback, including constructive (and polite) criticism, improvement suggestions, questions about usage (if the documentation is unclear), 
