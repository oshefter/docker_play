#coding=utf-8
import csv
import datetime


import sys
print (sys.version)

today = datetime.date.today()
print ("date=", today)

print ("testing numpy")
x = 3
print ("type of x=",x, "is=",type(x))
 
 
print ("testing csv file")
 
ifile = open("test.csv", "r")
reader = csv.reader(ifile)
 
rownum = 0
for row in reader:
# Save header row.
	if rownum ==0:
		header = row
	else:
		colnum = 0
	rownum += 1
for col in row:
	print (header)
	print ('%-8s: %s' % (header[colnum], col))
	#print ("%s" % col)
	colnum += 1
 
	rownum += 1
 
ifile.close()