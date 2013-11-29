# -*- coding: utf-8 -*-
import rooms
import parser

class Player(object):
	def __init__(self, name, items, points, crew):
		self.name = name
		self.items = items
		self.points = points
		self.crew = crew

class Engine(object):
	def __init__(self, player, map):
			self.player = player
			self.map = map
	def play(self):
		current_room = self.map.get_room()
		print '-' * 20
		print "Welcome %s" % self.player.name
		while True:
			next = current_room.enter()
			current_room = self.map.set_room(next)
			player.points = rooms.points
			player.items = rooms.items
			player.crew = rooms.crew
		
			print '-' * 40
			print "Name: %s Items: %s XP: %s CREW: %s " % (player.name, player.items, player.points, player.crew)
			print '-' * 40
			
			
class Map(object):
	
	dic = rooms.get_room_list()
	def __init__(self, room):
		self.room = room

	def get_room(self):
		return self.set_room(self.room)
		
	def set_room(self, room):
		return self.dic.get(room)
		
map = Map('welcome')
player = Player("Simen", [], 0, 20)
engine = Engine(player, map)
engine.play()
