# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15

#Checks if cars is greater than people, if it is it checks if people is greater than buses, then it prints out additional information
if cars > people:
	print "We should take the cars"
	if cars > people and people > buses:
		print "The bus have no room for us"
#else if the cars is less than people
elif cars < people:
	print "We should not take the cars."
# if no one of these are true then this will be printed
else:
	print "We can't decide."
	
#if buses is greater than cars it will print this
if buses > cars:
	print "That's too many buses"
# else if buses are less than cars it will print this
elif buses < cars:
	print "Maybe we could take the buses."
# if no one of the two if's over are true, this will be printed
else:
	"We still can't decide"

#if people are greater than buses in numbers this will be executed and printed
if people > buses:
	print "Alright, let's just take the buses."
# if the condition over is not met(true) this else statement will be executed and print out the text
else:
	print "Fine, let's stay home then."
	
#executes this statement if people are greater than buses or if cars are less than buses
if people > buses or cars < buses:
	print "We can possible take the bus. I dont know if the cars are enough"
else:
	print "I dont know what we should do!"