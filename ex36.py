# -*- coding: utf-8 -*-

items = []
itemsAvailable = ["Sword","Knife","Axe"]
first_time = True
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
	
def sand_room():
	print "You are in a land of sand. Watch out for creatures hiding in the sand"
	player_info()
	
def player_info():
	print "Your items are:", items
	
start(first_time)