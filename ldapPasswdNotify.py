#!/usr/bin/env python
# Author :- Rahul Patil<linuxian.com>
# Date :- Thu Sep 26 23:46:09 IST 2013

import sys
import os

#-----------------------------------------------------------------
# Provide Ldap DN Details to Perform Ldap Search using anonymouse
#-----------------------------------------------------------------
Domain = 'linuxian.com'
EmailDomain = 'abc.om' # if your mail domain is different this will becom user@abc.com 
ConnectDC = 'ldap://localhost:389'
# if 14 days remains to expire password then it will send email to that user 
# until user update the new password
PwdWarnDays = 14  

Subject = "Ldap Password Expiry Details"

MsgBody = """
Dear %s,
	Your Password Will be Expire in %s, we request you to please
change your password, your last password change date is %s

Best Regards,
Linux Admin
"""


def GetUserDetails():
    	""" This Function Will save all details in file
    	it will use ldap search query for the same."""
    	# Create bind dn eg. dc=example,dc=com
    	BindDN = ','.join([ 'dc=' + d for d in Domain.split('.') ])
    	#
    	import ldap 
    	l = ldap.initialize(ConnectDC)
    	# Perform Ldap Search
    	return  l.search_s(
    			BindDN,
    			ldap.SCOPE_SUBTREE,
    			'(uid=*)',['uid','pwdChangedTime']
    		)


def CheckExpiry():
        """ 
        This Function will Check each user ExpiryWarning
        if it more thans WarningDays then it will send Emails
        to that particuler user
        """
      	 import datetime
         for k,v in Users:
              		uid = ''.join(v['uid'])
              		if 'pwdChangedTime' not in v:
              				pass
                		  	#print "User " + uid + "  not Updated Password" 
              		try:
              	  		  l = ''.join(v['pwdChangedTime'])
              		except:
              		    	pass
              		
              		if 'pwdChangedTime' in v:
              			# To extrace year month day
              			d1 = datetime.date.today()
              			d2 = datetime.date(int(l[0:4]),int(l[4:6]),int(l[6:8]))
              			DaysOfPasswordChange = (d1 - d2).days
              			d2 = d2.strftime('%d, %b %Y')
              
              			ExpireIn = pwdMaxAge - DaysOfPasswordChange
              
              			# if password not changed before 14 days 
              			if ExpireIn <= PwdWarnDays:
              				SendMail = "echo '" + MsgBody % (uid,ExpireIn,d2) + "' \
              						  mail -s " + '"' + Subject + '"' + ' ' + \
              						  uid + '@' + EmailDomain 
              				#os.system(SendMail)
              				print SendMail



if __name__ == '__main__':
        Users = GetUserDetails()
        CheckExpiry()
