#!/usr/bin/env python
# Author :- Rahul Patil<linuxian.com>

import ldap 
import datetime
import subprocess

#-----------------------------------------------------------------
# Provide Ldap DN Details to Perform Ldap Search using anonymouse
#-----------------------------------------------------------------
domain_name = 'linuxian.com'
email_domain = 'linuxian.com' # if your mail domain is different this will becom user@abc.com 
connect_dc = 'ldap://localhost:389'

# Define number of days to send warning alert 
# suppose you have define 14 days and pwd_max_age age is 45 days 
# then it will notify users when 14 days remain to expire password 
# it will send email to that user until user update the new password
pwd_warn_days = 14 
# default password expire in  day as per ldap ppolicy
pwd_max_age = 45 # password should change in days
mail_subject = "Ldap Password Expiry Details"

mail_body = """
Dear %s,
     Your password will expire in %s day(s). We're sorry for the
inconvenience, but we need you to change your password, your 
last password date is %s.

Best Regards,
Linux Admin
"""


def get_user_details():
    	""" Return UID and Last Password Details """
    	# Create bind dn eg. dc=example,dc=com
    	bind_dn = ','.join([ 'dc=' + d for d in domain_name.split('.') ])
    	l = ldap.initialize(connect_dc)
    	# Perform Ldap Search
    	return  l.search_s(
    			bind_dn,
    			ldap.SCOPE_SUBTREE,
    			'(uid=*)',['uid','pwdChangedTime']
    		)


def check_password_expiry():
	"""Check each user ExpiryWarning
        if it more thans WarningDays then it will send Emails
        to that particuler user"""
      	for k,v in ldap_users:
		uid = ''.join(v['uid'])
             	if 'pwdChangedTime' not in v:
			# means password not changed yet from user creation date
			pwd_expire_in_days = 0 
             	  	#print "User " + uid + "  not Updated Password" 
             	try:
               	  	l = ''.join(v['pwdChangedTime'])
             	except:
             	    	pass
             	
             	if 'pwdChangedTime' in v:
             		# Date Calculation to get number of days remains to change password
			d1 = datetime.date.today()
             		d2 = datetime.date(int(l[0:4]),int(l[4:6]),int(l[6:8]))
			# to get number of days password has updated 
             		days_of_password_change = (d1 - d2).days
             		d2 = d2.strftime('%d, %b %Y')
               		pwd_expire_in_days = pwd_max_age - days_of_password_change
                
             	if pwd_expire_in_days <= pwd_warn_days:
			p = subprocess.Popen(['mail', '-s', mail_subject, uid + '@' + email_domain],
						stdin=subprocess.PIPE)
			p.communicate(mail_body % (uid,pwd_expire_in_days,d2))



if __name__ == '__main__':
        ldap_users = get_user_details()
        check_password_expiry()

