#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi
osname = input("Enter the name for the os: ")
#form = cgi.FieldStorage()
#osname = form.getvalue("x")
ostype = input("Enter the os image name: ")

#cmd = "docker run -i -t -d --name {x} {y}".format(x = osname,y = ostype)

cmd = "docker run -i -t -d --name {x} {y}".format(x = osname, y=ostype)


output = sp.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status == 0:
	print("os launched successfully with name {}".format(osname))
else:
	print("some problem occured: {}".format(out))