# -*- coding: utf-8 -*-
#Imports the argv module from sys
from sys import argv

#Says that the argument is to be splitted in two variables
script, filename = argv

#Creates a variable that stores a file in it by using open function
txt = open(filename)

#Prints out the filename and calls a function without parameters to be able to read the content of the file
print "Here's your file %r:" % filename
print txt.read()
txt.close()
#Prints out a message and setting a variable to store raw input, user is prompted for input
print "Type the filename again:"
file_again = raw_input("> ")
#Setting a variable to store the file again
txt_again = open(file_again)

#reads out the content by calling the read() function
print txt_again.read()
txt_again.close()