from nose.tools import *
from magicalyourney.room import *
from magicalyourney.map1 import *
from magicalyourney.player import *
from magicalyourney.mapdesc import *
from magicalyourney.parser import *
def test_room():
	gold = Room("GoldRoom",
		"""This room has gold in it you can grab. There's a door to the north.""",None,None,None,None)
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room("Center", "Test room in the center.",None,None,None,None)
	north = Room("North", "Test room in the north.",None,None,None,None)
	south = Room("South", "Test room in the south.",None,None,None,None)
	player = player1
	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north',player), north)
	assert_equal(center.go('south',player), south)
	
def test_map():
	start = Room("Start", "You can go west and down a hole.",None,None,None,None)
	west = Room("Trees", "There are trees here, you can go east.",None,None,None,None)
	down = Room("Dungeon", "It's dark down here, you can go up.",None,None,None,None)
	player = player1
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	#assert_equal(start.go('west',player), west)
	assert_equal(start.go('west',player).go('east',player1), start)
	assert_equal(start.go('down',player).go('up',player), start)

#testing the scenario where the user wins the game
def test_game():
	player = player2
	#Giving the player the necessary items to win the game
	player.items = ["phone","boat","sword"]
	game = game1
	assert_equal(START.doAction('play',player,game),eng_play)
	assert_equal(START.doAction('clock',player,game),eng_clock)
	assert_equal(START.go('east',player), boat)
	assert_equal(boat.go('north',player), gold_island)
	assert_equal(gold_island.doAction('cave',player,game),gold_cave)
	assert_equal(gold_island.doAction('use phone',player,game),gold_phone)
	#assert_equal(gold_island.doAction('phone',player,game),gold_phone)
	assert_equal(gold_island.doAction('yes',player,game),gold_option)
	assert_equal(gold_island.doAction('leave cave',player,game),gold_leave)
	assert_equal(gold_island.go('sail',player), boat)
	assert_equal(boat.go('south',player), dragon_island)
	assert_equal(dragon_island.doAction('use sword',player,game),"You take up the sword")
	assert_equal(dragon_island.doAction('point',player,game),"The dragon comes down in front of you")
	assert_equal(dragon_island.doAction('slay',player,game),"You injured the dragon. It flies up high")
	assert_equal(dragon_island.doAction('point',player,game),"The dragon comes down in front of you")
	assert_equal(dragon_island.doAction('slay',player,game),"You injured the dragon. It flies up high")
	assert_equal(dragon_island.doAction('point',player,game),"The dragon comes down in front of you")
	assert_equal(dragon_island.doAction('slay',player,game),"You injured the dragon. It flies up high")
	assert_equal(dragon_island.doAction('point',player,game),"The dragon comes down in front of you")
	assert_equal(dragon_island.doAction('slay',player,game),"you slayed the dragon. Its dead")
	assert_equal(dragon_island.go('sail',player), boat)
	player.score = 281
	assert_equal(boat.go('hidden',player), hidden_island)
	assert_equal(hidden_island.doAction('back',player,game),hid_won) #won the game
	
	#assert_equal(START.go('east',player).go('north',player), gold_island)

#Testing that the users can type phrases in various ways
def test_input_processor():
	messages = (
"Huh?",
"What was that?",
"I dont understand that"
)
	player = player1
	#Giving the player the necessary items so we can test the input on this
	player.items = ["phone","boat","sword"]
	#The phone in gold_island level 2 (starts at 0, so 0 is level 1)
	objects = player.items + gold_island.objects
	assert_equal(process_input("phone", gold_island.levels[1], objects),"phone")
	assert_equal(process_input("use phone", gold_island.levels[1], objects),"phone")
	assert_equal(process_input("use the phone", gold_island.levels[1], objects),"phone")
	assert_equal(process_input("use the phone now", gold_island.levels[1], objects),"phone")
	#Testing errors for phone
	assert_equal(check_list(process_input("use the phosne now", gold_island.levels[1], objects),messages),True)
	player.items = ["boat","sword"]
	objects = player.items + gold_island.objects
	#Testing the phone input when player has no phone
	assert_equal(process_input("use phone", gold_island.levels[1], objects),"There are no phone to use")
	
	#Testing direction in england room
	england.add_paths({
    'east': boat
})
	assert_equal(process_input("east", START.paths, objects),"east")
	assert_equal(process_input("go east", START.paths, objects),"east")
	assert_equal(process_input("go east now", START.paths, objects),"east")
	
	assert_equal(process_input("go north", START.paths, objects),"you can't go north here.")
	assert_equal(process_input("go south", START.paths, objects),"you can't go south here.")
	assert_equal(process_input("go west", START.paths, objects),"you can't go west here.")
	#error message if input is no direction
	assert_equal(check_list(process_input("go phone", START.paths, objects),messages),True)
	
# Since the game gives us random error messages, we have to check if 
# the output we get is in the list we pick a random message from, so that we can test against it
def check_list(out,list):
	if out in list:
		return True
	else:
		return False
	