#
# Author Simen Lie 2013
#
# This is the room/map description module. 
# This module defines descriptions and messages that is used by Room objects
# And together creates a complete description for one or several maps
# It is currently only used by map1 (my game)

#--HELP--
help = """
COMMANDS:
The 'INVENTORY' command shows you what items you're carrying/have.
The 'HINT' command give you a hint, if you are completely lost.
The 'SCORE' command shows you all the scores for players.
"""

help_func = ["help","inventory","hint","score"]

#England room
englandd ="""
You find yourself in England.
You're walking along a harbour with no money. You're looking for an adventure.
Suddenly you see some gamblers that are looking for people to play with
"""

eng_play = """You start a game with them. The game is a simple riddle and goes like this

'This thing runs but cannot walk, sometimes sings but never talks. 
Lacks arms, has hands; lacks a head but has a face.'"""

eng_clock = """Congratulations! that was the correct answer! You won a boat"""
# a list with all the death scenarios for the room (in same order as levels in the room)
eng_list = ["You Try to kill them. They shoot you in the head","Thats not correct, you lost the game, you walking around until you die..."]

#Boat room
boatd = """You are on your boat, in the middle of the ocean.
You and you crew has sailed for 3 days. Far away, trought the fog, you can glimpse a few islands.
You have to chose where you will go next"""

#Gold Island room
gold_islandd = """A sign says: 'The Gold Island'.
On the island you see a dark cave"""

gold_cave="""In the cave you see gold everywhere.
In addition you hear strange sounds
What do you do?"""

gold_leave="""You see the boat in front of you"""

gold_phone = """you used your Android app to scan the area for monsters.
A monster is registered.
The app prompts you with a option to make the monster go asleep. Do this?"""

gold_option = """The monster fell asleep.
You find a Sword in the gold. You take the sword and the gold.
"""

gold_death1 = """Run? only a coward backs out! While you are running you fell into a trap"""
gold_death2 = """Everybody knows an iPhone cant help you. The monster sees you and cut you in the stomach"""
gold_death3 = """You hit no and tried to go past the Monster and take all the gold
The monster sees you and cut you in the stomach"""
gold_death4 = """Stay? the monster wake up and tear you apart with his bear hands"""
gold_island_list = [gold_death1,gold_death2,gold_death3,gold_death4]

#Dragon Island room
dragon_islandd = """On the Dragon Island
A Dragon flyes over you while it spits a burst of fire against you
Half of the crew are dead. If you have a sword, now is the time to use it. Type: sword"""

#Hidden Island room
hidden_islandd = """On the Hidden Island
Paradise! you have made it
What will you do?
Stay or go back to England with all the gold and live there?
stay, back"""

hid_list = ["You stay and in the night a creature eats you"]
hid_won = "You Go back to England and live happy with all the money. YOU WON!!!!!!!"