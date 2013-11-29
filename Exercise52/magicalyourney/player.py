#
# Author Simen Lie 2013
#
# This is the player module
# This module defines a game, user, and creates the objects in the game(Player,Dragon)
# You can choose from two different maps  and two different players (Musclo, Fasto)
from magicalyourney.objects import *
import random

# This class is used to store and keep all the players(name and score) in a list
# So that we can access it in the game
class Game(object):
	def __init__(self):
		self.players = []
	def add_player(self,player):
		self.players.append("%s : %s" %(player.name, player.score))

# The User class represents the user that plays the game
# Its used to store a name, recent score and the last input the user typed
class User(object):
	def __init__(self, name):
		self.name = name
		self.input = ""
		self.score = 0

#Creating the objects in the game defined in the objects.py module		
dragon = Dragon("Evil Dragon")
#The different heros the user can choose from and a list with the "start-items"
player1 = Musclo("Musclo",["phone"])
player2 = Fasto("Fasto",["phone"])
#Default user
user1 = User("user1234")
#The Game object
game1  = Game()
