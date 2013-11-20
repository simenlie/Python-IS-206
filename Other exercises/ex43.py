from sys import exit

class Scene(object):

	def enter(self):
		print "simen"


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "--"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

	def enter(self):
		print "You are dead"
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "You are in the central Corridor"
		print "A Gothon stands in your way. What will you do?"
		
		action = raw_input("> ")
	
		if action == "shoot":
			return 'death'
		elif action == "tell a joke":
			return 'laserWeaponArmory'
			
		
		

class LaserWeaponArmory(Scene):

	def enter(self):
		print " In the Laser weapon armory"
		
		action = raw_input("> ")
		if action == "2":
			return 'the_bridge'
		else:
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print "You are on the bridge"
		print "To get past you have to type in a code"
		action = raw_input("> ")
		if action == "1":
			return 'escapePod'
		else:
			return 'death'

class EscapePod(Scene):

	def enter(self):
		print "You are in the escape Pod"
		return 'finished'

class Map(object):
	scenes = {'death': Death(),
	'central_corridor': CentralCorridor(),
	'laserWeaponArmory': LaserWeaponArmory(),
	'the_bridge': TheBridge(),
	'escapePod': EscapePod()
	
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()