#
# Author Simen Lie 2013
#
# The Sentence class, and the parsing methods is based on learnpythonthehardway
# This class parses a sentence.

import lexicon
import inputAlgo

class ParserError(Exception):
    pass

class Sentence(object):
	def __init__(self, subject, verb, object,is_noun):
		self.subject = subject[1] #Player
		self.verb = verb[1] #go
		self.object = object[1] #door /north
		self.is_noun = is_noun
		
# --PARSING FUNCTIONS FROM learnpythonthehardway --
def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None

def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

def parse_verb(word_list):
	skip(word_list, 'stop')
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)
	if next == 'noun':
		return match(word_list, 'noun')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")

def parse_object_type(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)
	if next == 'noun':
		return True
	elif next == 'direction':
		return False

def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	is_noun = parse_object_type(word_list)
	obj = parse_object(word_list)
	return Sentence(subj, verb, obj,is_noun)

def parse_sentence(word_list):
	skip(word_list, 'stop')
	start = peek(word_list)
	if start == 'noun':
		subj = match(word_list, 'noun')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		return parse_subject(word_list, ('noun', 'you'))
	else:
		raise ParserError("Must start with subject, object, or verb not: %s" % start)
		
# --MY FUNCTIONS--

# This function will determine if the input is a valid sentence
# Returns True if it is and False otherwise		
def valid_sent(input):
	sent = lexicon.scan(input)
	# Sets the starting values of these to be 1000, since we dont want it to be 0 initially
	verb_index = 1000
	object_index = 1000
	stop_count = 0
	verb_count = 0
	object_count = 0
	for i, item in enumerate(sent):
		if item[0] == "verb":
			verb_index =  i
			verb_count += 1
		if item[0] == "noun" or item[0] == "direction":
			object_index =  i
			object_count += 1
		if item[0] == "stop" and object_index > i:
			stop_count += 1
	total_count = stop_count + verb_count
	# If the object in the sentence is presented right after the verb
	# adding the stopcount.
	# the total_count let us return false, if the user types "go north north"( want the user to type "go north")
	if object_index == verb_index + 1 + stop_count and total_count < 3:
		return True
	# If the verb in the sentence is presented right after the object 
	# and the total_count is greater than 2 ("i play them")
	# adding the stopcount.
	elif verb_index == object_index + 1 + stop_count and total_count > 2:
		return True
	else:
		return False

# This function takes three paramters; input, a list lista and a list objects
# It used the parse sentence to parse a sentence and the inputAlgo module to get 
# a proper response message
# returns the parsed sentence	
def process_input(input, lista, objects):
	if check_utf8_alpha(input):
		if input in lexicon.dir:
			input = "go " + input 
		ignore_case = input.lower()
		temp = check_stop(ignore_case)
		if len(temp) == 1:
			return inputAlgo.simple_resp(temp[0], lista)
		else:
			if valid_sent(ignore_case):
				sent = parse_sentence(lexicon.scan(ignore_case))
				return inputAlgo.respond_dir(sent,lista,lexicon,objects)
			else:
				return inputAlgo.get_error_message()
	else:
		return "Invalid input. Letters and numbers only please."
# Checks if the input is valid ascii, and not non english letters or symbols		
def check_utf8_alpha(input):
	list = input.split()
	returning = True
	for word in list:
		if not word.isalpha():
			returning = False
	return returning		
# runs trough the input and strips away all the stop words
# Returns the list wihtout the stop words
def check_stop(input):
	sent = lexicon.scan(input)
	temp_list = []
	for word in sent:
		if word[0] != "stop":
			temp_list.append(word[1])
	return temp_list
