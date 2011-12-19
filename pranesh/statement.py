#!/usr/bin/python

infilehandle = open("ex.txt","a")
strLines = infilehandle.writelines("\n hai, ravi hw r u ")
print strLines
infilehandle.close()

