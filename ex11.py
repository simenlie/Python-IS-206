# -*- coding: utf-8 -*-
# Skriver ut den f�rste print setningen, deretter m� brukeren skrive inn noe
print "Hvor gammel er du?",
alder = raw_input()

#Etter brukeren har skrevet inn noe og trykt Enter skriver den ut neste print setning
print "Hvor h�y er du?",
hoyde = raw_input()
#Samme som over
print "Hvor mye veier du?",
vekt = raw_input()
#Skriver ut en tekst som kombinerer alt brukeren har skrevet inn
print "S�, du er %r �r gammel, %r h�y og veier %r." % (alder,hoyde,vekt)