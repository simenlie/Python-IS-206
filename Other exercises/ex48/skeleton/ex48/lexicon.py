# -*- coding: utf-8 -*-
dir= ["north","south","east","west","down","up","left","right","back"]
verbs = ["go","stop","kill","eat"]
stop = ["the","in","of","from","at","it"]
nouns = ["door","bear","princess","cabinet"]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
		
def igore_case(param):
	return param.lower()

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

#Bare brukt for slik at brukeren kan skrive inn en setning for å teste
#input = raw_input("> ")

#print scan(input)