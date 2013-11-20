# -*- coding: utf-8 -*-

#Importing argv from sys module
from sys import argv

#Delegating two variables to the argv
script, input_file = argv

#creating a function with one parameter. The function prints out the content of the file
def print_all(f):
	print f.read()
	
#Creating a function with one parameter. The function rewinds the file to line 0. 
def rewind(f):
	f.seek(0)
	
#A function with two parameters. prints the content that is passed in to these parameters. 
#It prints out one line of the content of the file
def print_a_line(line_count,f):
	print line_count, f.readline()
	
#Gives a variable the value of the content of a file(opens it)
current_file = open(input_file)

#Prints out a string
print "First let's print the whole file:\n"

#Calling the function print_all with a variabel as parameter
print_all(current_file)

#Prints out a string
print "Now let's rewind, kind of like a tape."

#Calling the function rewind with a variabel as parameter
rewind(current_file)

#Prints out a string
print "Let's print three lines:"

#Declaring a vriabel and setting the value to one
current_line = 1
#Calls the print_a_line function with two variables as parameters
print_a_line(current_line, current_file)

#Incrementing the value of current_line by one
current_line += 1

#Calls the print_a_line function with two variables as parameters
print_a_line(current_line, current_file)

#Incrementing the value of current_line by one
current_line += 1

#Calls the print_a_line function with two variables as parameters
print_a_line(current_line, current_file)