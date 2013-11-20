# -*- coding: utf-8 -*-


user_input = raw_input("Please type the file you want to open ")

file = open(user_input,'w')

print "Okey yo have chosen the file %r " % user_input

user_input2 = raw_input("What do you want it to store? Type it ")

print "Okey, then im going to write this out"
print "Writing..."

file.write(user_input2)
file.close()