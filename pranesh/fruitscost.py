#!usr/bin/env python

print "\n"
print " The Available Fruits is\n"
fruits = ["apple","orange","grapes","pineapple"]
print fruits
apple = 30
orange = 25
grapes = 32
pineapple = 50

i = raw_input("\nType the above fruits to know the details of price,\nType the above fruit is case sensitive \n\nEnter ur fruit : ")
if i == 'apple':
 print "The cost of the apple is :", apple
 print "\nThe Kg of the fruits if u want "
 j = int(raw_input("Enter ur Kg :"))
 print "\nThe cost is ", j * apple, "\n"

elif i == 'orange':
 print "The cost of the orange is :", orange
 print "\nThe Kg of the fruits if u want "
 j = int(raw_input("Enter ur Kg :"))
 print "\nThe cost is ", j * orange, "\n"

elif i == 'grapes':
 print "The cost of the grapes is :", grapes
 print "\nThe Kg of the fruits if u want "
 j = int(raw_input("Enter ur Kg :"))
 print "\nThe cost is ", j * grapes, "\n"

elif i == 'pineapple':
 print "The cost of the pineapple is :", pineapple
 print "\nThe Kg of the fruits if u want "
 j = int(raw_input("Enter ur Kg :"))
 print "\nThe cost is ", j * pineapple, "\n"
else:
 print "\nThe fruit is given u are not available.\nTry some other fruits which listed above :)\n" 
