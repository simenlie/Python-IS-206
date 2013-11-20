# -*- coding: utf-8 -*-
class Song(object):

	def __init__(self,lyrics):
		self.lyrics = lyrics
		
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
lyrics_one = ["Happy birthday to you",
"I dont want to get sued",
"So I'll stop right there"]
lyrics_two = ["They rally around the family", "With pockets full of shells"]

happy_bday = Song(lyrics_one)

bulls_on_parade = Song(lyrics_two)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()