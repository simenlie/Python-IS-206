# -*- coding: utf-8 -*-
default = "NO"
title = "s"

def setLan(lang):
	land = lang

def language(language, room):

	if language == "NO" or language == "EN":
		return room_checker(language, room)
	else:
		return room_checker(default, room)
		
def room_checker(language, room):
	if room == "england":
		return englandLN(language)
	elif room == "water":
		pass	
	
	
	
class englandLN(object):
	def __init__(self, lan):
		self.lan = lan
		
	def get(self):
		if self.lan == "NO":
			return {
			'title': "Du befinner deg i England.",
			'sub_title':  "Du har lite penger å må på en eller annen måte ",
			'sub_title2': "få tak i en båt",
			'sub_title3': "Du går langs havnen da du får øye på noen gamblere",
			'sub_title4': "For å spille med dem skriv spill",
			'command1' : "spill"
			}
		elif self.lan == "EN":
			return {
			'title': "You find yourself in England.",
			'sub_title':  "You have no money and have in one way or another ",
			'sub_title2': "get hands on a boat",
			'sub_title3': "You walking along the harbour when you see some gamblers",
			'sub_title4': "to play with them type play",
			'command1' : "play"
			}
	