# -*- coding: utf-8 -*-
#
# Author Simen Lie 2013
#
# This module is used to determine the outcome of a parsed sentence
# 

import random
# A lis with messages that is used in the respond_dir 
# function to randomly pick one if the parsed sentence doesnt makes sence
messages = (
"Huh?",
"What was that?",
"I dont understand that"
)
# Function that returns a random message from the messages list
def get_error_message():
	return messages[random.randint(0,len(messages)-1)]

# used if the the input is only one word
def simple_resp(input, list):
	input = str(input)
	if input.isdigit():
		return input
	elif validate_input(input, list):
		return input
	elif input == "yes" or input == "no":
		return input
	else:
		return get_error_message()
		
# Function that determines if the word passed in is 
# present in the list, passed in
# Used by simple_resp and respond_dir functions
def validate_input(word, valid_list):
	if word in valid_list:
		return True
	else:
		return False			

# This function is used to interpret a sentence and return a proper message back
# It takes a sentence valid, a list/tuple room_dir, the lexicon list, and objects
def respond_dir(valid, room_dir, lexicon, objects):
	isVerb = True
	# If the sentence makes sence (if its a direction, that forexample "go" is present and not "kill", "kill north" doesn't make sence)
	if makes_sence(valid,lexicon):
		# Checks that the verb is present in the room path-list/level
		if validate_input(valid.verb, room_dir):
			return check_objects(valid,valid.verb,objects)
		# If the verb is not present in the room path-list/level we check on the sentences object
		elif validate_input(valid.object, room_dir):
			if valid.is_noun:
				return check_objects(valid,valid.object,objects)
			else:
				return valid.object
		# If the sentence object nor verb is present in the room list we try to give a best possible error message
		else:
			if valid.is_noun:
				if valid.object in objects:				
					return "%s can't %s the %s" % (valid.subject,valid.verb,valid.object)
				else:
					return "%s can't %s a %s here. There are none" % (valid.subject,valid.verb,valid.object)
			else:
				if valid.object in objects:				
					return "%s can't %s %s" % (valid.subject,valid.verb,valid.object)
				else:
					return "%s can't %s %s here." % (valid.subject,valid.verb,valid.object)
	# If the sentence doesnt make sence we return the error message function
	else:
		return get_error_message()
		
# Checks that the object in a sentence is present in a list objects,
# if its not returns a proper error message
def check_objects(valid, out,objects):
	if valid.object in objects:
		return out
	else:
		return "There are no %s to %s" % (valid.object,valid.verb)

# Checks if the sentence makes sence.
def makes_sence(sentence, lexicon):
	if sentence.object in lexicon.dir:
		if not sentence.is_noun and sentence.verb in lexicon.dir_verbs:
			return True
		else:
			return False
	else:
		if sentence.is_noun and sentence.verb not in lexicon.dir_verbs:
			return True
		else:
			return False
