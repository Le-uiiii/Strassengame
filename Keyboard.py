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


## 3) Definition Zone-------------------------------------------------------------------------------------------
##

class Strassenspiel(EV3Brick):

    def __init__(self, test_=False, ok=TouchSensor(Port.S2)): # Touchsensor für Nameneintrag
        self.tempo = 100   # Bestimmt Geschw. des jeweiligen Motors            
        self.mot =  Motor(port)  
        self.polykoeffizienten = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0} # Koeffizienten der polynom. Beschleunigung
        self.test_ = test_ # Für print-Ausgaben, um den Ablauf zu überprüfen
        self.end_ = False # Variable, ob beendet werden soll; vorher muss self.run_ auf False gesetzt werden 
        self.run_ = True # Variable, ob gerade der Motor laufen soll
        self.modus = modus # Definiert bestimmten Spielmodus
        self.diff_ = diff_ # Definiert Schwierigkeit
        #l = (port=Port.A, test_ = test_, polykoeffizienten = polykoeffizienten) # Linke Straße
        #m = (port = Port.B, test_ = test_, polykoeffizienten = polykoeffizienten) # Mittlere Straße
        #r = (port = Port.C, test_ = test_, polykoeffizienten = polykoeffizienten) # Rechte Straße
        self.ok = ok

        if test_ == True:
            print("Ok")

    
    def writing_name(self):
        opt = 0 # Eingabe
        reg = 1 # Regulierung für Neuladen
        name = "" # Eingegebener Name
        height = 0 # Höhe der Tastatur
        nr = 0 # Anzahl der Buchstaben in Tastatur
        i = 0 # Derzeitige Höhe für hoch und runter
        last = -1 # Letzter derzeitiger Buchstabe in name
        wide = 0
        tastatur = ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", # Tastatur
                    "P", "A", "S", "D", "F", "G", "H", "J", "K",
                    "L", "Y", "X", "C", "V", "B", "N", "M", "<"]
        
        while not ok.pressed():
            if opt != reg: # Regulierung für Neuladen
                self.screen.clear()
                for letter in tastatur: # Kreiren der Tastatur
                    if nr > len(tastatur): # Zurücksetzen von nr, height und wide
                        nr = 0
                        height = 0
                        wide = 0
                    if opt == abs(tastatur[nr]): # Farbliche Markierung der derzeitigen Auswahl
                        self.screen.draw_text(x=15+15*wide, y=25+25*height, text=letter, text_color=Color.WHITE, background_color=Color.BLACK)
                    else:
                        self.screen.draw_text(x=15+15*wide, y=25+25*height, text=letter, text_color=Color.BLACK, background_color=Color.WHITE)
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