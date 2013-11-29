# -*- coding: utf-8 -*-
import language
from sys import exit
import parsera

def get_room_list():
	return {'england': England(),
'welcome': welcome_room(),
'boat': Boat(),
'death': Death(),
'dragon_island': DragonIsland(),
'gold_island': GoldIsland(),
'lost': Loose(),
'hidden_island': HiddenIsland(),
'won': WonRoom()}

points = 0
items = []
crew = 20
days = 3

visited = {'england': False,
'welcome': False,
'boat': False,
'dragon_island': False,
'gold_island': False, 
'hidden_island': False}

options = ["nord", "sor"]

class England(object):
	roomPoints = 50
	def enter(self):
		country = language.language("EN","england").get()
		print country.get('title')
		print country.get('sub_title')
		print country.get('sub_title2')
		print country.get('sub_title3')
		print country.get('sub_title4')
		
		action = raw_input("> ")
		action = parsera.process_input(action, ["play"], ["them"])
		print '-' * 10

		if action == country.get('command1'):
		
			print "You ar starting a game with them"
			print "They gives you a riddle"
			print "\"This thing runs but cannot walk, sometimes sings but never talks. "
			print "Lacks arms, has hands; lacks a head but has a face.\""
			action = raw_input("> ")
			action = parsera.process_input(action, ["clock"], [])
			print '-' * 10
			if action == "clock":
				print "You won a boat : + %s XP" % self.roomPoints
				global items
				items.append("Boat")
				global points
				points = self.roomPoints
				return 'boat'
			else:
				return 'lost'
		else:
			print "You give up this oppurtunity and walks around and do nothing"
			return 'lost'
			
class welcome_room(object):
	
	def enter(self):
		print "In this game your task is to explore several islands and the mysteries on them"
		return 'england'



class Boat(object):
	
	def enter(self):
		
		if visited['gold_island']:
				for i in options:
					if i == "nord":
						options.remove(i)
						
		if visited['dragon_island']:
			for i in options:
				if i == "sor":
					options.remove(i)
		
		print "You are on your boat"
		print "You and you crew has sailed for %s days" % days
		print "You have to chose where you will go next"
		if points >= 200:
			options.append('hidden')
			print options
		else:
			print options
		action = raw_input("> ")
		action = parsera.process_input(action, ["nord","sor","hidden"], [])
		if action == "nord":
			if visited['gold_island']:
				print "Already been here"
				return 'boat'
			else:
				return 'gold_island'
		
		elif action == "sor":
			return 'dragon_island'
		elif action == "hidden" and points >= 200:
			return 'hidden_island'
		else:
			print '-' * 10
			print "Not a command"
			return 'boat'
		
		
class GoldIsland(object):
	roomPoints = 100
	
	def enter(self):
		global days
		days += 1
		visited['gold_island'] = True
		print "On the Gold Island"
		print "You and your crew just found a cave"
		print "In the cave you see gold everywhere"
		print "In addition you hear strange sounds"
		print "What do you do?"
		action = raw_input("> ")
		if action == "use iphone":
			print "Everybody knows an iPhone cant help you"
			return 'death'
		elif action == "use phone":
			print "you used your Android app to scan the area for monsters"
			print "A monster is registered"
			print "The app prompts you with a option to make the monster go asleep. Do this?"
			action = raw_input("[findMyMonsters]> ")
			if action == "yes":
				print "The monster fell asleep"
				print "You find a Sword in the gold. You take it"
				items.append("Sword")
				print "you and your crew take all the gold and rush back to the boat"
				global points
				points += self.roomPoints
				has_boat = False
				for i in items:
					if i == "Boat":
						has_boat = True
				if has_boat:				
					return 'boat'
				else:
					print "You have no boat to get off the Island"
					print "You starve..."
					return 'death'
			elif action == "no":
				print "You hit no and tried to go past the Monster and take all the gold"
				print "The monster sees you and cut you in the stomach"
				return 'death'
			else:
				print "What was that?"
				print "Well, it took to long time"
				print "The monster cut you in the stomach"
				return 'death'
		else:
			print "Tip: use your phone. Lets hope you dont own a iphone - ha ha ha"
			return 'gold_island'

class DragonIsland(object):
	
	done = True
	dragon = "far"
	dragon_life = 2
	roomPoints = 200
	def enter(self):
		global days
		days += 1
		if visited['dragon_island']:
			print "What will you do?"
			action = raw_input("> ")
			if "sword" in action and "Sword" in items:
				
				while self.done:
					
					global crew
					print "Crew remaining: %s" % crew
					if crew == 0:
						print "All of the crew are gone"
						print "The dragon targets you"
						print "Fire...."
						return 'death'
				
					print "What do you do with the sword?"
					print "slay, point"
					action = raw_input("[Excalibur]>")
					print "-" * 10
					if action == "slay" and self.dragon == "far":
						print "you cant slay the dragon. Its too far away"
						crew -= 1
					elif action == "slay" and self.dragon == "close":
						if self.dragon_life != 0:
							print "you hurt the dragon"
							print "It flies up high"
							self.dragon_life -= 1
							self.dragon = "far"
						else:
							print "you slayed the dragon. Its dead"
							print "Congrats!"
							global points
							points += self.roomPoints
							self.done = False
							
							return 'boat'
					elif action == "point" and self.dragon == "close":
						crew -= 1
					elif action == "point" and self.dragon == "far":
						print "the dragon comes down"
						crew -= 1
						self.dragon = "close"
			else:
				print "you dont have a Sword"
				print "Maybe you can find a sword on another Island"
				action = raw_input("Go back to the boat?> ")
				if action == "yes":
					return 'boat'
				else:
					print "Without a sword you are helpless"
					print "The Dragon kills you all"
					return 'death'
		else:
			print "On the Dragon Island"
			print "A Dragon flyes over you while it spits a burst of fire against you"
			print "Half of the crew are dead"
			crew /= 2
			visited['dragon_island'] = True
			return 'dragon_island'
		
class HiddenIsland(object):
	def enter(self):
		global days
		days += 1
		print "On the Hidden Island"
		print "Paradise! you have made it"
		print "What will you do?"
		print "Stay or go back to England with all the gold and live there?"
		print "stay, back"
		action = raw_input("> ")
		if action == "stay":
			return 'won'
		elif action == "back":
			print "A big Shark jumps up from the water and bite you in the head"
			return 'death'
		else:
			print "I dont know what that means..."
			print "This probably means you've got a flu..."
			return 'death'
class Death(object):
	def enter(self):
		print "You are slowly getting weaker..."
		print "You die"
		exit(1)
		
class Loose(object):
	def enter(self):
		print "You lost the game"
		exit(1)
		
class WonRoom(object):
	def enter(self):
		print "You Won the game with %s in the crew left and %s points" % (crew,points)
		exit(1)