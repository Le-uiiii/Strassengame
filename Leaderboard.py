##  1) Commentation Zone---------------------------------------------------------------------------------------
##    Author Leander Gundel + Johannes Loos
##    Language Micropython (Python) v2.0
##    Programm zum Namen für Leaderboard
##    

## 2) Import Zone-----------------------------------------------------------------------------------------------
##

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random
import time
import csv

## 3) Definition Zone-------------------------------------------------------------------------------------------
##

class Strassenspiel(EV3Brick):

    def __init__(self, test_=False,):
        self.tempo = 100   # Bestimmt Geschw. des jeweiligen Motors            
        self.mot =  Motor(port)  
        self.polykoeffizienten = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0} # Koeffizienten der polynom. Beschleunigung
        self.test_ = test_ # Für print-Ausgaben, um den Ablauf zu überprüfen
        self.end_ = False # Variable, ob beendet werden soll; vorher muss self.run_ auf False gesetzt werden 
        self.run_ = True # Variable, ob gerade der Motor laufen soll
        self.modus = modus # Definiert bestimmten Spielmodus
        self.diff_ = diff_ # Definiert Schwierigkeit
        self.l = (port = Port.A, test_ = test_, polykoeffizienten = polykoeffizienten) # Linke Straße
        self.m = (port = Port.B, test_ = test_, polykoeffizienten = polykoeffizienten) # Mittlere Straße
        self.r = (port = Port.C, test_ = test_, polykoeffizienten = polykoeffizienten) # Rechte Straße
        self.ok = ok
        ok = TouchSensor(Port.S2) # Touchsensor für Nameneintrag

        if test_ == True:
           print("Ok")

    
    def writing_name(self):
        opt = 0 # Eingabe
        reg = 1 # Regulierung für Neuladen
        name = " " # Eingegebener Name
        height = 0 # Höhe der Tastatur
        nr = 0 # Anzahl der Buchstaben in Tastatur
        i = 0 # Derzeitige Höhe für hoch und runter
        last = -1 # Letzter derzeitiger Buchstabe in name
        tastatur = ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", # Tastatur
                    "P", "A", "S", "D", "F", "G", "H", "J", "K",
                    "L", "Y", "X", "C", "V", "B", "N", "M", "<"]
        
        while not ok.pressed():
            if opt != reg: # Regulierung für Neuladen
                self.screen.clear()
                for letter in tastatur: # Kreiren der Tastatur
                    if nr == len(tastatur): # Zurücksetzen von nr
                        nr = 0
                    if opt == abs(tastatur[nr]): # Farbliche Markierung der derzeitigen Auswahl
                        self.screen.draw_text(x=15+15*wide, y=25+25*height, text=arg, text_color=Color.WHITE, background_color=Color.BLACK)
                    else:
                        self.screen.draw_text(x=15+15*wide, y=25+25*height, text=arg, text_color=Color.BLACK, background_color=Color.WHITE)
                    if nr < len(tastatur): # Regulierung von wide insgesamt
                        wide = wide + 1
                    if wide == 9: # Regulierung von wide in einer Zeile
                        wide = 0
                        if height < 2: # Heruntergehen + Regulierung der Höhe
                            height = height + 1
                    nr = nr + 1

            reg = opt
            if Button.RIGHT in self.buttons.pressed() and opt != 8 and opt != 17 and opt != 26: # Aktion beim Drücken und Regulierung am Rand 
                opt = opt + 1
            if Button.LEFT in self.buttons.pressed() and opt != 0 and opt != 9 and opt != 18: # Aktion beim Drücken und Regulierung am Rand
                opt = opt - 1
            if Button.UP in self.buttons.pressed() and i > 0: # Aktion beim Drücken und Regulierung am Rand
                opt = opt - 8
                i = i - 1
            if Button.DOWN in self.buttons.pressed() and i < 2: # Aktion beim Drücken und Regulierung am Rand
                opt = opt + 8
                i = i + 1
            if Button.CENTER in self.buttons.pressed() and opt != 26 and last < 13: # Auswählen der Taste und schreiben des derzeitigrn Namens und Regulierung der Namenslänge
                name = name + "".join(tastatur[opt])
                last = last + 1
                self.screen.draw_text(x=15, y=10, text=name)
            elif Button.CENTER in self.buttons.pressed() and opt == 26 and last > -1: # Auswählen der Taste und Löschen eines Buchstabens
                del name[last]
                last = last - 1
                self.screen.draw_text(x=15, y=10, text=name)
        return name
        change_ = 0

    def leaderboard_change(self, name, score, change_):
        
        score =  counter
        username = name
        if change_ == 0 # guckt, ob man aus dem Menü herkommt oder ein neuer Eintrag erstellt werden muss
            leaderboard = ""
            pos = 1

            with open ("Leaderboard.csv", "a", newline='') as file:
                fields=['score', 'name']
                writer=csv.DictWriter(file, fieldnames=fields)
                writer.writerow({'score' : score, 'name' : username})

            with open ("Leaderboard.csv", "r") as file:
                sortlist=["Highscore-Liste"]
                reader=csv.reader(file)
            for i in reader:
                sortlist.append(i)
            for i in range(len(sortlist)):
                if i != 0:
                    sortlist[i][0]=str(sortlist[i][int(0)])

            for i in range(555):
                for i in range(len(sortlist)-1):
                    if i != 0:
                        if sortlist[i][0] < sortlist[i+1][0]: # ordnet die Plätze an
                            change=sortlist[i]
                            sortlist[i]=sortlist[i+1]
                            sortlist[i+1]=change

            for i in range(len(sortlist)-1):
                leaderboard = str(pos) + leaderboard + "".join(sortlist[i]) + str(pos) + ". " # wandelt die Liste in stringformat um
                pos = pos + 1

        position = 0 # macht die Position fürs scrollen 
        reg = 1 # reguliert das Schreiben des Leaderbordes
        maxposition = len(sortlist)
        minposition = 0

        while Button.CENTER in self.buttons.pressed():
            if reg != position:
                self.screen.clear()
                for _ in range(1):
                    self.screen.draw_text(x=15, y=15+15*position, text=leaderboard)
            reg = position
            if (Button.RIGHT in self.buttons.pressed()) or (Button.DOWN in self.buttons.pressed()) and positon =< maxposition:
                position = position + 1
            elif (Button.LEFT in self.buttons.pressed()) or (Button.UP in self.buttons.pressed()) and position >= minposition:
                position = position - 1
        self.menu()
