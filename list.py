#!/usr/bin/python

import os,commands,time,sys

print "Plzzz wait for the list......list is upto the mark:"
time.sleep(2)
x="""             
print "press 1 to access SAAS cloud:"
print "press 2 to access StAAS cloud:"
print "press 3 to access IAAS cloud:"
pint "press  4 to access PAAS cloud:"
print "press 5 to access SAAS cloud:"
"""
print x
#choice will store above listed options

choice=raw_input()

if   choice == '1':
	print "NICE CHOICE"
	execfile('saas.py')
elif choice == '2':
	print "Storage cloud is here!!!"
	execfile('obstorag.py')
else:
	print "wrong input"
	execfile('list.py')

