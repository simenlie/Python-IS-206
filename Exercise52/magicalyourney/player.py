class User(object):
	def __init__(self, name):
		self.name = name
		self.score = 0

class Player(object):
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.items = []
		self.crew = 20
		self.dead = False
		self.deadMessage = None
		
class Dragon(object):
	def __init__(self,name):
		self.name = name
		self.close = False
		self.hp = 100
		self.weakness = 20
	def action(self,action,player):
		if "Sword" not in player.items:
			player.dead = True
			player.deadMessage = "An invisible sword? Dont think so... You run, but the dragon kills you"
			return "hey"
		if action == "slay" and self.close:
			self.hp -= self.weakness
			if self.hp < 1:
				self.hp = 0
				return "you slayed the dragon. Its dead"
			else:
				self.weakness += 7
			self.close = False
			return "You injured the dragon. It flies up high"
		elif action =="point":
			self.close = True
			return "The dragon comes down in front of you"
		else:
			if "help" in action:
				return "slay, point"
			player.crew -= 5
			if player.crew == 0:
				player.dead = True
				player.deadMessage = "All of the crew are gone. The dragon targets you. Fire....You die"
			return "You cant slay the dragon, its too far away. It killed 5 of your crew. Maybe you could point at it..."
			

dragon = Dragon("Evil Dragon")		
player1 = Player("player1234")
user1 = User("user1234")
