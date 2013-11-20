# -*- coding: utf-8 -*-
numbers = []

def looping(number, increment):
	i = 0
	
	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
def looping_for(number, increment):
	
	for i in range(0,number):
		print "At the top i is %d" % i
		numbers.append(i)
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
		
		
		
looping_for(22,5)

print "the numbers: "
for num in numbers:
	print num
