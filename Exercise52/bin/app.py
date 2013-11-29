# -*- coding: utf-8 -*-
# 
# Author Simen Lie 2013
#
# The Structure is based on the structure from http://learnpythonthehardway.org/book/ex52.html
#
# This is the main module. This is where the application is started from 
# This module gives functionality to play a text based game presented in html.
# You can choose from two different maps  and two different heroes

import web
from magicalyourney import room
from magicalyourney import map1
from magicalyourney import map2
from magicalyourney import player

urls = (
  '/start', 'StartEngine',
  '/game', 'GameEngine',
  '/', 'Index',
  '/reset', 'Reset',
  '/resetU', 'ResetUser'
)
# a dictionary with all the maps. Used to get the map the user selects
maps = {"map1" : map1,"map2":map2}
# a dictionary with all the heroes. Used to get the hero the user selects
heros = {"hero1" : player.player1,"hero2":player.player2}
# Global variables that stores the (current) map and hero
CHOSEN_MAP = map1
CHOSEN_HERO = player.player1
app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'room': None,'player': None,'user': None,'game': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

# This class purpose is to start a new game
# It stores the player score in the user score(so the user can see his last score)
# Adds the player to the game class list of players(for checking the scores of the players who played the game)
# Sets the room to the first room(in the chosen map) and stores a new player in the player session
# Returns: redirect to /game
class Reset(object):
    def GET(self):
		#the user can see his last-game score
		session.user.score = session.player.score
		session.game.add_player(session.user)
		global CHOSEN_MAP
		global CHOSEN_HERO
		session.room = CHOSEN_MAP.START
		session.player = CHOSEN_HERO
		startPage = "/game"
		web.seeother(startPage)

# This class purpose is to start a new game with a new user (and if desired, a new map)
# Returns: redirects to /start where the user can choose a map and a username	
class ResetUser(object):
    def GET(self):
		global CHOSEN_HERO
		session.game.add_player(session.user)
		session.room = None
		session.player = CHOSEN_HERO
		session.user = None
		startPage = "/start"
		web.seeother(startPage)

# This class purpose is to determine if the user currently have a game (session) or not
# Returns: Redirects to either /start (new user) or /game (user and game stored in session)
class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
		if not session.game:
			# First time the user starts a game, a game session is created (keeping track of players score)
			session.game = player.game1
		if session.user:
			#Flushes the last input from the user when starting a new game
			session.user.input = ""
		if not session.user:
			return web.seeother("/start")
		else:
			if session.room == None:
				global CHOSEN_MAP
				global CHOSEN_HERO
				session.room = CHOSEN_MAP.START
				if session.player:
					#the user can see his last-game score
					session.user.score = session.player.score
					# add the "old player" to the games score list, before setting a new player
					session.game.add_player(session.user)
				session.player = CHOSEN_HERO
				
		web.seeother("/game")
		
# This class purpose is to render the form where the user can create a username and choose a map
class StartEngine(object):
	def GET(self):
		# Checks that the user session is not yet stored
		if not session.user:
			return render.index()
		else:
			web.seeother("/")
	def POST(self):
		# Username is default set to None, and map to map1
		form = web.input(username=None,map="map1",hero="hero1")
		if form.username:
			if not session.user:
				#Creates a new user
				session.user = player.User(form.username)
		else:
			#If the user dont want to type a username, a default is set
			session.user = player.user1
		global CHOSEN_MAP
		global CHOSEN_HERO
		#Sets the CHOSEN_MAP and CHOSEN_HERO variables to the map and hero the user selected
		CHOSEN_MAP = maps.get(form.map)
		CHOSEN_HERO = heros.get(form.hero)
		web.seeother("/")

# This class is the game class, that handles the interaction between the user and the game
# It renders the html for the user with room, player and user passed in so we can present information about this to the user
class GameEngine(object):
	def showRoom(self):
		return render.show_room(room=session.room,player = session.player, user = session.user)

	def GET(self):
		if session.room:
			# If the player is dead we store the html with the last room in a variable, 
			# sets the room variable to None and return the html. In this way the user can still se the last room(where he died)
			# If we set the rooms session to none before we write/return the html, the room we pass along is gone
			if session.player.dead or session.room.name == "death":
				ret = self.showRoom()
				session.room = None
				return ret
			else:
				return self.showRoom()
		else:
			# If there are no room session, we just renders a html saying you died (users deleting sessions, errors etc)
			return render.you_died()

	def POST(self):
		form = web.input(action=None)
		
		# Before we pass the input along, we want to make it lowercase so the functions can interpret it correctly
		if not form.action:
			web.seeother("/game")
		else:
			# Store what the user typed, so we can render it with the html
			session.user.input = "> " + form.action
			input = form.action.lower()
			room_stuff(input)

# This function is the core of the game. in this function all calculation is done. 
# Its used in the GameEngine class
def room_stuff(input):
	if session.room and input:
		# Checks if the current level in the room is the last level and that no obstacles is in the room
		# Based on this we can decide if the user is allowed to go to the next room, 
		# or if he still has some levels/obstacles to beat in the room before moving on
		if session.room.curlevel == session.room.totalLevels and not session.room.obstacle:
				
			# If a room has some items, the player gets them
			if session.room.items:
				add_item(session.room.items,session.player.items)
			# Checks if the user input word is a key in the room path dictionary, 
			# this prevents the user from dying when he mistypes
			if not session.room.check_key(input,session.player, session.game):
				web.seeother("/game")
			else:
				# Since the player has beaten all levels in the room, he gets the room points added to his score
				session.player.score += session.room.points
				# Moving along to the next room
				session.room = session.room.go(input, session.player)
				if session.room:
					web.seeother("/game")
				else:
					web.seeother("/game")
		# If the user still have levels/obstacles to beat in the room
		else:
			action = session.room.doAction(input,session.player, session.game)
			if action == "death":
				session.player.dead = True
				session.player.deadMessage = session.room.currentDeath
				web.seeother("/game")
			else:
				web.seeother("/game")

# Used in the room_stuff function to add items to the players inventory
# Checks if the user already have the item
def add_item(list, list2):
	for item in list:
		if not item in list2:
			list2.append(item)

if __name__ == "__main__":
    app.run()