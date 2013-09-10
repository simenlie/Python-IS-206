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

