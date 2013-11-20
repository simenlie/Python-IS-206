# -*- coding: utf-8 -*-
from sys import argv

script, first, second, third = argv

another = "Give me another one?"

print "The script is called:", script
print "Your first variable is:", first
print "your secnd variable is:", second
print "Your third variable is:", third

print "Okei, you have given me three arguments to store in variables. %r" % another,
input_user = raw_input()

print "Thanks. The last thing you typed was %r" % input_user 

var = True
while var == True :
	new_input = raw_input("Enter Something more? or 'q' to quit :")
	if(new_input == "q") :
		var = False
		print "You leaving me?! I thought we were friends!"
	else :
		print "Okei, you entered ", new_input
	
	

print "Nice to talk to you! You are more than welcome to run me again"

