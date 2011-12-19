#!usr/bin/env python
print "\n\tStudent Grade calculation\n"
name = raw_input ("\n Enter ur name: " )
marks = int (raw_input ("\n Enter ur marks: "))
if marks <= 20 :
 print "\n", name,"---> you are in Fail, Try to attain pass mark\n"
elif marks <= 40 : 
 print "\n", name,"---> you are in Second class,plz improve ur self\n"
elif marks <= 60 :
 print "\n", name,"---> you are in First class, Good\n"
elif marks <= 100 :
 print "\n", name,"---> you are in distinction, Very good\n"
else:
 print "\n\tplz try correctly, Maximum mark is out of 100 only\n"
 
	
