#!/usr/bin/python

import os,commands,time,sys
print "welcome to the Storage cloud !!!!"
time.sleep(2)
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "_______________________________"
print "_______________________________"
print "###############################"
time.sleep(3)

user=raw_input("Type user name to access nova cloud:")
password=raw_input("Type the user password:")

if user  =='root' and password  =='redhat':
	print "Access Granted!!!!!!"
	execfile('obstcli.py')

else:	
	print "Authentication failed closing storage Project.Try again!!!!!!"
	execfile('obstorag.py')

	exit()
