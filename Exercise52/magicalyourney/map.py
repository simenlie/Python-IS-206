import mapdesc
from magicalyourney import player
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
		self.deathMessage = "You are dod"
		self.gameover = gameover
		self.currentDeath = None
		self.won = False
	
	def go(self, direction,player):
		#Checks if the user typed hidden, if the player score is under 200(score he needs to visit the room), None is returned
		if direction == "hidden":
			if player.score < 200:
				#prevents the player from getting points for progressing to the same room
				player.score -= 10
				return self
		#pops the element, so the user/player never can go the same path several times
		return self.paths.pop(direction, None)
	
	def check_key(self, dir):
		pathExist = self.paths.get(dir, None)
		if not pathExist:
			self.curAction = "What does that mean?"
		return pathExist
		
	
	def doAction(self,action,player):
		#won the game if the score is over 400
		if player.score > 280:
			self.won = True
		#update current level
		if self.curlevel != self.totalLevels:
			if self.gameover:
				self.currentDeath = self.gameover[self.curlevel]
			self.curAction = self.levels[self.curlevel].get(action, "What does that mean?")
			if self.curAction != "What does that mean?":
				self.curlevel += 1
			return self.curAction
		else:
			#Saves what the obstacle object returns, so that we can check if the obsctale is killed before we return the return statement
			temp = self.curAction = self.obstacle.action(action,player)
			#The obstacle disappears/dies if the hp is 0
			if self.obstacle.hp < 1:
				self.obstacle = None
			return temp

	def add_paths(self, paths):
		self.paths.update(paths)
		
	def add_levels(self, level):
		self.levels.append(level)
		#update levels
		self.totalLevels = len(self.levels)
	def checkJourney(self):
		if self.curlevel == self.totalLevels:
			self.commands = ", ".join(self.paths.keys())			
			return self.commands
		else:
			self.commands = ", ".join(self.levels[self.curlevel].keys())		
			return self.commands


england = Room("England",mapdesc.england,40,None,None,mapdesc.eng_list)
boat = Room("Boat",mapdesc.boat,10,None,None,None)
dragon_island = Room("Dragon Island",mapdesc.dragon_island,150,None,player.dragon,None)
gold_island = Room("Gold island",mapdesc.gold_island,70,["Sword"],None, mapdesc.gold_island_list)
hidden_island = Room("Hidden island",mapdesc.hidden_island,150,None,None,mapdesc.hid_list)

england.add_paths({
    'continue': boat
})

boat.add_paths({
    'south': dragon_island,
	'north': gold_island,
	'hidden': hidden_island
})

england.add_levels({
	'play': mapdesc.eng_play,
	'dodge!': "death",
	'tell a joke': "death"
})

hidden_island.add_levels({
	'stay': "death",
	'back': mapdesc.hid_won,
})


england.add_levels({
	'clock': mapdesc.eng_clock,
	'moon': "death",
	'monster': "death"
})

gold_island.add_levels({
	'use iphone': "death",
	'use phone': mapdesc.gold_phone
})
gold_island.add_levels({
	'yes': mapdesc.gold_option,
	'no': "death"
})

gold_island.add_paths({
	'sail': boat
})

dragon_island.add_levels({
	'sword': "You take up the sword"
})

dragon_island.add_paths({
	'sail': boat
})



START = england