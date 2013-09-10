# -*- coding: utf-8 -*-
# Skriver ut den første print setningen, deretter må brukeren skrive inn noe
print "Hvor gammel er du?",
alder = raw_input()

#Etter brukeren har skrevet inn noe og trykt Enter skriver den ut neste print setning
print "Hvor høy er du?",
hoyde = raw_input()
#Samme som over
print "Hvor mye veier du?",
vekt = raw_input()
#Skriver ut en tekst som kombinerer alt brukeren har skrevet inn
print "Så, du er %r år gammel, %r høy og veier %r." % (alder,hoyde,vekt)