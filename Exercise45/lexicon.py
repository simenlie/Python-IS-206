# -*- coding: utf-8 -*-
#
# Author Simen Lie 2013
# This lexicon is based on the one from learnpythontheharday
# The lesicon stores different words in different lists

dir= ["north","south","east","west","down","up","left","right","back","cave","nord","sor","hidden"]
dir_verbs =["go","enter","sail","leave"]
verbs = ["go","play","stop","kill","slay","eat","use","open","make","take","sail","enter","leave","answer","tell","throw","slowly","here"]
stop = ["the","in","of","from","at","it","through","with","now","i","want","a","to","place"]
nouns = ["door","bear","princess","cabinet","iphone","phone", "them","clock","sword","dragon","joke","bomb"]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
		
def igore_case(param):
	return param.lower()

# This function "scans" a sentence and creates a tuple with the
# word and the type of word(based on if the word is present in one of the lists) 
# and add this tuple to a list
def scan(param):
	sentence = []
	words = param.split()
	for word in words:
		if igore_case(word) in dir:
			sentence.append(('direction',igore_case(word)))
		elif igore_case(word) in verbs:
			sentence.append(('verb',igore_case(word)))
		elif igore_case(word) in stop:
			sentence.append(('stop',igore_case(word)))
		elif igore_case(word) in nouns:
			sentence.append(('noun',igore_case(word)))
		elif convert_number(word):
			sentence.append(('number',int(word)))
		else:
			sentence.append(('error',word))
	return sentence