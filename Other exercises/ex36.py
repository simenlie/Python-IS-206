# -*- coding: utf-8 -*-

from sys import exit

items = []
itemsAvailable = ["Sword","Knife","Axe"]
first_time = True
commands = ["left","right","back","forward"]
creature = "Lion"
def start(bool):
	if bool:
		print "Welcome to The Journey"
		print "You are in a strange place"
		print "Before you start your Journey pick a weapon"
		print "Weapons avaiable:", itemsAvailable
		picked = raw_input("> ")
		
		for i in itemsAvailable :
			if i == picked:
				items.append(picked)
				print "Okei, you picked a %s. Time will show if that was a good choice" % i
				
		player_info()
		bool = False
	print "A voice gives you two options"
	print "It says: Choose Forrest or Sand"
	choice = raw_input("> ")
	
	if "forrest" in choice:
		forrest_room()
	elif "sand" in choice:
		sand_room()
	else:
		start(bool)
	
def forrest_room():
	print "You are in the forrest. Big creatures lives here"
	player_info()
	print "Commands:", commands
	
	command = raw_input("> ")
	go(command)
		
def lion_room():
	print "A big %s is right in front of you" % creature
	player_info()
	print "What would you do?"
	action = raw_input("> ")
	
	if "sword" in action and "Sword" in items:
		print "You killed the lion"
		print "Behind the %s an Axe lays, will you swap the Axe with the %s?" % (creature, items[0])
		user = raw_input("> ")
		if user == "yes":
			for i in range(len(items)):
				items.pop(i)
			items.append("Axe")
		elif user == "no":
			print "Okei, you keeping your %s" % items[0]
	else:
		print "Only the sword kan kill the Mighty Lion"
		dead()
		
	print "Commands: right"
	user_input = raw_input("> ")
	if user_input == "right":
		forrest_room()
			
	
def sand_room():
	print "You are in a land of sand. Watch out for creatures hiding in the sand"
	player_info()
	print "Your commands are:", commands
	print "Something strange is going on..."
	print "Where are we?"
	print "If we only knew..."
	command = raw_input("> ")
	go(command)
	
def go(command):
	if command == commands[0]:
		lion_room()
	elif command == commands[1]:
		print "Just a wall, nothing special"
		print "Wait..."
		print "There are some paintings on the wall"
		print "...."
		print "It looks like a animal, maybe a Tiger... Or a Lion..."
		print "Another painting shows something shiny, maybe a crystal or diamond?"
		forrest_room()
	elif command == commands[2]:
		start(False)
	elif command == commands[3]:
		diamond_room()
	else:
		forrest_room()

def diamond_room():
	print "Diamonds, Diamonds, Diamonds! Diamonds are everywhere"
	print "What will you do?"
	player_info()
	print "Commands: take, back"
	user_inp = raw_input("> ")
	if user_inp == "take":
		print "The room is begining to shake and fall apart"
		print "if only you had an Axe to create a way out"
		if "Axe" in items:
			print "You have an Axe!!!"
			print "You got yourself out with all the diamonds"
			sucess()
		else:
			print "You only have:"
			for i in items:
				print i
			print "You are buried alive"
			dead()
	elif user_inp == "back":
		forrest_room()
	else:
		diamond_room()
	
	
def player_info():
	print "Your items are:", items
	
def dead():
	print "Game over"
	exit(0)

def sucess():
	print "You won the game"
	exit(0)
	
start(first_time)