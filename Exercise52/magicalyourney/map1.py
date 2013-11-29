#
# Author Simen Lie 2013
#
# This is the map1 module
# This module create rooms
# and forms the complete map for my game 

from magicalyourney.room import *
import mapdesc
# Creating a room with a name, description, roompoints,objects in the room, obstacles(objects) and a list with all death scenarios
england = Room("England",mapdesc.englandd,40,["boat"],None,mapdesc.eng_list)
boat = Room("Boat",mapdesc.boatd,10,None,None,None)
dragon_island = Room("Dragon Island",mapdesc.dragon_islandd,150,None,player.dragon,None)
gold_island = Room("Gold island",mapdesc.gold_islandd,70,["sword"],None, mapdesc.gold_island_list)
hidden_island = Room("Hidden island",mapdesc.hidden_islandd,150,None,None,mapdesc.hid_list)
generic_death = Room("death", "You died.",None,None,None,None)
england.add_paths({
    'east': boat
})

# Boat Room
boat.add_paths({
    'south': dragon_island,
	'north': gold_island,
	'hidden': hidden_island
})
# England Room
england.add_objects(["them"])

england.add_levels({
	'play': mapdesc.eng_play,
	'kill': "death",
	'joke': "death"
})

england.add_levels({
	'clock': mapdesc.eng_clock,
	'moon': "death",
	'monster': "death"
})
# Hidden Island Room
hidden_island.add_levels({
	'stay': "death",
	'back': mapdesc.hid_won,
})
# Gold Island Room
gold_island.add_objects(["cave"])
gold_island.add_levels({
	'run': "death",
	'cave': mapdesc.gold_cave
})

gold_island.add_levels({
	'iphone': "death",
	'phone': mapdesc.gold_phone
})
gold_island.add_levels({
	'yes': mapdesc.gold_option,
	'no': "death"
})
gold_island.add_levels({
	'leave': mapdesc.gold_leave,
})

gold_island.add_paths({
	'sail': boat
})
# Dragon Island Room
dragon_island.add_levels({
	'sword': "You take up the sword"
})

dragon_island.add_paths({
	'sail': boat
})

dragon_island.add_objects(["dragon"])
# The starting room
START = england
# The users starting inventory when playing this map
start_inventory = ["phone"]

# These are not used
class Level(object):
	def __init__(self, key,value,verb):
		self.key = key
		self.value = value
		self. verb = verb
		
class Direction(object):
	def __init__(self, key,value):
		super(Direction, self).__init__(key,value,verb)
		self.key = key
		self.value = value
		self. verb = "go"
	