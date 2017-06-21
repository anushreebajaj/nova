#!/usr/bin/python

import os,commands,time,sys

print "Plzzz wait for the list......list is upto the mark:"
time.sleep(2)
x="""             
print "press 1 to access object storage:"
print "press 2 to access Block storage:"
print "press 3 to access File storage:"
"""
print x
#choice will store above listed options

choice=raw_input()

if   choice == '1':
	print "NICE CHOICE"
	execfile('drive.py')
elif choice == '2':
	print "Block storage is performing later"
elif choice == '3':
	print "file storage is also performing later"
else:
	print "wrong input"
	execfile('obstcli.py')

