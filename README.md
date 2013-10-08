ldapPasswdNotify.py
===================

This script will check `pwdChangedTime` in each user Object and password change time and As per Default Global Password Policy Password Should be change in 45 days and if  password not been updated  than 31 days ( i.e 45-14  where 45 is password expiry and 14 is warning) then will notify users via email to change password, it will send mail until next password update
