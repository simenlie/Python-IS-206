#import lexicon
import random
direction1 = {
    'south': 'test',
	'north': 'test',
	'hidden': 'test'
}

levels = {
	'play': "you played",
	'kill': "death",
	'phone': "death"
}

objects = {
	'them': "you played",
	'phone': "death",
}

messages = (
"Huh?",
"What was that?",
"I dont understand that",
"Is that even a sentence?"
)

def get_error_message():
	return messages[random.randint(0,len(messages)-1)]

def simple_resp(input, list):
	if validate_input(input, list):
		return input
	elif input == "yes" or input == "no":
		return input
	else:
		return "none"
def validate_input(word, valid_list):
	if word in valid_list:
		return True
	else:
		return False

def respond_dir(valid, room_dir, lexicon, expected):
	#if valid in lexicon:
	look_for = ""
	isVerb = False
	if expected == 0:
		look_for = valid.verb
		isVerb = True
	
	else:
		look_for = valid.object
	if makes_sence(valid,lexicon):
	#sjekker pa use, men ma sjekke pa phone
		if validate_input(look_for, room_dir):
			if isVerb:
				return check_objects(valid,look_for)
			else:
				return look_for
		#hvis ikke det finnes i lexicon, sjekker vi om brukeren mente et objekt
		elif validate_input(valid.object, room_dir):
			return check_objects(valid,valid.object)
		
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
	else:
		return messages[random.randint(0,len(messages)-1)]
		
def check_objects(valid, out):
	if valid.object in objects:
		return out
	else:
		return "There are no %s to %s" % (valid.object,valid.verb)
		
def makes_sence(sentence, lexicon):
	if sentence.object in lexicon.dir:
		if not sentence.is_noun and sentence.verb == "go":
			return True
		else:
			return False
	else:
		if sentence.is_noun and sentence.verb != "go":
			return True
		else:
			return False
		
		

#while(True):
#	input = raw_input("direction >")
#	print respond_dir(input,direction1,lexicon.dir)
#	input2 = raw_input("verb >")
#	print respond_dir(input2,levels,lexicon.verbs)	