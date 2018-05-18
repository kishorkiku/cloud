#!/usr/bin/python2
import time
print"wellcome to cloud service of gcloud"
time.sleep(0.9)
c_user=raw_input("enter cloud credntials :")
c_password=raw_input("enter cloud password : ")

if c_user=='root'and c_password=='123':
 print "plz wait cloud service is about to start"
 execfile('menu.py')
else:
 print"plz check your details"
