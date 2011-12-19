#!usr/bin/env python

print "\n"
print " The Available Fruits is\n"
fruits = ["apple","orange","grapes","pineapple"]
print fruits
apple = 30
orange = 25
grapes = 32
pineapple = 50

i = raw_input("\nType the above fruits to know the details of price,\nType the above fruit is case sensitive \nEnter ur fruit : ")
if i == 'apple':
 print "The cost of the apple is :", apple
elif i == 'orange':
 print "The cost of the orange is :", orange
elif i == 'grapes':
 print "The cost of the grapes is :", grapes
elif i == 'pineapple':
 print "The cost of the pineapple is :", pineapple
else:
 print "\nThe fruit is given u are not available.\nTry some other fruits\n"
