#
# Author Simen Lie 2013
#
# This module defines objects that can be a part of the game. 
# The objects uses a super-class Object that defines common things for a object (name)

# Super class Object
class Object(object):
	def __init__(self, name):
		self.name = name

# The Player class defines properties of a hero/player/character that the user controls in the game.
# It inherits from the Object class
class Player(Object):
	def __init__(self, name, startItems):
		super(Player, self).__init__(name)
		self.score = 0
		self.items = startItems
		self.crew = 20
		self.dead = False
		self.deadMessage = None
		
# Musclo and Fasto classes defines different heroes in the game and inherits the properties of the Player class
class Musclo(Player):
	def __init__(self, name, startItems):
		super(Musclo, self).__init__(name,startItems)
		self.power = 50
		self.crew = 10

class Fasto(Player):
	def __init__(self, name, startItems):
		super(Fasto, self).__init__(name,startItems)
		self.power = 20
		self.crew = 25
		
# This class represents a Dragon in the game
class Dragon(Object):
	def __init__(self,name):
		super(Dragon, self).__init__(name)
		self.close = False
		self.hp = 100
		self.weakness = 20
		self.commands = {
	'point': "death",
	'slay': "death",
	'help': "death"
}
	def action(self,action,player):
		if "sword" not in player.items:
			player.dead = True
			player.deadMessage = "An invisible sword? Dont think so... You run, but the dragon kills you"
			return "hey"
		if action == "slay" and self.close:
			self.hp -= self.weakness
			if self.hp < 1:
				self.hp = 0
				return "you slayed the dragon. Its dead"
			else:
				self.weakness += (player.power/3)
			self.close = False
			return "You injured the dragon. It flies up high"
		elif action =="point":
			self.close = True
			return "The dragon comes down in front of you"
		else:
			if "help" in action:
				return "slay, point"
			if action == "slay" and not self.close:
				player.crew -= 5
				if player.crew == 0:
					player.dead = True
					player.deadMessage = "All of the crew are gone. The dragon targets you. Fire....You die"
				return "You cant slay the dragon, its too far away. It killed 5 of your crew. Maybe you could point at it..."
			else:
				return action