Python-IS-206
=============
- Exercise 22
- Exercise 26
- Excercise 45
- Exercise 52
- App-engine

<h2>Exercise 22</h2>
<h2>Exercise 26</h2>
<h2>Exercise 45</h2>
<h2>Exercise 52</h2>
<h4>Om spillet</h4>
Det første du gjør er å velge et map og lage et brukernavn.
Mens du spiller vil scoren din øke, samt at du vil få nye items.
Hvis du dør eller vinner og velger spill igjen, vil du få med din forrige score,
slik at du kan prøve å slå din gamle score. Du kan skrive kommandoer på forskjellige måter. 
Spillet har en enkel parser som forstår enkle formuleringer av den samme tingen.

Eksempel på kommandoer som tolkes likt:
  - phone
  - use phone
  - use the phone
  - use the phone now

<h4>Instruksjoner</h4>

  - git clone
  - Skrive inn $env:PYTHONPATH = "$env:PYTHONPATH;." (PowerShell)
  - Kjøre bin/app.py
  - Åpne localhost og spill
  - (sessions blir lagret i /sessions -og kan slettes fra denne mappen, hvis ønskelig)

PowerShell:
```PowerShell
    $env:PYTHONPATH = "$env:PYTHONPATH;." #Trengs for at import skal fungere
    cd path/to/game/folder
    python bin/app.py
```

 

<h4>Tester</h4>
Spillet har totalt 6 tester.
  - Sjekker input prosessering



<h4>Nyttige kommandoer</h4>
  - HELP kommandoen gir deg en forklarende tekst om andre kommandoer
      - INVENTORY lister alle objektene spilleren har
      - HINT gir deg hint til noen kommandoer du kan prøve
      - SCORE gir deg en liste over alle spillerne og scoren deres

<h5>Kommandoer for å vinne spillet (i denne rekkefølgen)</h5>
```PowerShell
    play, clock, east, north, phone, yes, sail, south, sword, point, slay, point, slay, point, slay, point, slay, sail, hidden, back
```
kommandoene kan formuleres på andre måter("play with them" etc) 

<h2>App Engine</h2>
  - http://simen-app.appspot.com/
