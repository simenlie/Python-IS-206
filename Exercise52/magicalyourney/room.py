#
# Author Simen Lie 2013
#
# This is the room module. This modules has a Room class that can be used 
# to create different type of rooms

import mapdesc
from magicalyourney import player
from magicalyourney import parser

# This class defines a interface/structure and methods for a Room
# The curAction variable in this class is used to 
# hold the response from the user input (and is what the users see in the browser/html)
class Room(object):
	def __init__(self, name, description,points,items,obstacle,gameover):
		self.name = name
		self.points = points
		self.description = description
		self.paths = {}
		self.levels = []
		self.curlevel = 0
		self.totalLevels = 0
		self.curAction = None
		self.commands = None
		self.items = items
		self.obstacle = obstacle
		self.deathMessage = "You are dead"
		self.gameover = gameover
		self.currentDeath = None
		self.won = False
		self.lastAction = ""
		self.objects = []
		global help
		
	# The go function returns the room that the user requested
	# Returns the next room
	def go(self, direction,player):
		# Processing the input with the process_input from the parser module. 
		# This function will return a valid room key (that we can use to find the room in the dictionary)
		process = parser.process_input(direction,self.paths,player.items + self.objects)
		#Checks if the user typed hidden, if the player score is under 200(score he needs to visit the room), None is returned
		if process == "hidden":
			if player.score < 200:
				#prevents the player from getting points for progressing to the same room
				player.score -= 10
				return self
		# pops the element, so the user never can go the same path several times
		next_room = self.paths.pop(process, None)
		if player.score > 280:
			next_room.won = True
			next_room.curAction = "You WON!!!"
		return next_room
	# This function is used to check if the direction input from the user is valid
	def check_key(self, dir,player,game):
		process = parser.process_input(dir,self.paths,player.items + self.objects)
		# If the processed input is no key to a room, the pathExist is set to None
		pathExist = self.paths.get(process, None)
		if not pathExist:
			#CurAction is set to the output/response stored in process variable
			self.curAction = process
			if self.check_help(dir):
				self.help(dir,player,game)
		return pathExist
		
	# This function is used to "navigate trough a room"
	# Each room has levels, and this function will start at level 1 
	# and for each valid level input from the user, increment the current level
	def doAction(self,action,player,game):
		if self.check_help(action):
			return self.help(action,player,game)
		# won the game if the score is over 280
		if player.score > 280:
			self.won = True
		# update current level
		# if the current level isen't the last level, we parse the input
		# and try to get the value from the key(the input) in the level dictionary
		# If its not present in the dictionary, we still assign the parsed user input to the curAction,
		# So we can print it to the user
		if self.curlevel != self.totalLevels:
			if self.gameover:
				self.currentDeath = self.gameover[self.curlevel]
			process = parser.process_input(action,self.levels[self.curlevel],player.items + self.objects)
			self.curAction = self.levels[self.curlevel].get(process, process)
			if process in self.levels[self.curlevel]:
				self.lastAction = self.curAction
				self.curlevel += 1
			return self.curAction
		else:
			# Parse the input and pass the parsed input to the obstacles action function
			process = parser.process_input(action,self.obstacle.commands,player.items + self.objects)
			temp = self.curAction = self.obstacle.action(process,player)
			#The obstacle disappears/dies if the hp is 0
			if self.obstacle.hp < 1:
				self.obstacle = None
			return temp
	# the rooms help function gives the user the possibility to ask for help(help commands)
	# the rooms curAction variable gets the response based on which help command the user types
	# This function is used in the go and doAction function
	def help(self,action,player,game):
		if action == "help":
			self.curAction = help
			return self.curAction
		if action == "hint":
			return self.valid_commands()
		if action == "inventory":
			inventory = ", ".join(player.items)
			self.curAction = inventory
			return self.curAction
		if action == "score":
			players = ", ".join(game.players)
			self.curAction = players
			return self.curAction
	# Function to determine if the user typed a help command
	# Used in go and doAction function
	def check_help(self,action):
		if action in mapdesc.help_func:
			return True
		else:
			return False
	# Adds paths/directions to the room
	def add_paths(self, paths):
		self.paths.update(paths)
	# Used to add objects to the room
	def add_objects(self, objects):
		self.objects += objects
	# Used to add levels to the room
	def add_levels(self, level):
		self.levels.append(level)
		#update levels
		self.totalLevels = len(self.levels)
	# Used to assign the commands in the room/level to the curAction
	# Used in the help function to get hints about which commands are valid
	def valid_commands(self):
		if self.curlevel == self.totalLevels:
			commands = ", ".join(self.paths.keys())
			self.curAction = "You can try one of these: %s. Choose wise..." % commands
			return self.curAction
		else:
			commands2 = ", ".join(self.levels[self.curlevel].keys())
			self.curAction = "You can try one of these: %s. Choose wise..." % commands2
			return self.curAction
#variable to store the map descriptions help string
help = mapdesc.help

