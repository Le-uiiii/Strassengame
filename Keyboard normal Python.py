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
        
while True:
    if opt != reg: # Regulierung für Neuladen
            for letter in tastatur: # Kreiren der Tastatur
                if nr == len(tastatur): # Zurücksetzen von nr
                        nr = 0
                print(letter)                    
                if nr < len(tastatur): # Regulierung von wide insgesamt
                    wide = wide + 1
                if wide == 9: # Regulierung von wide in einer Zeile
                    wide = 0
                    if height < 2: # Heruntergehen + Regulierung der Höhe
                        height = height + 1
                nr = nr + 1
    reg = opt
    b = input("Hey")
    if b == "Rechts" and opt != 8 and opt != 17 and opt != 26: # Aktion beim Drücken und Regulierung am Rand
        opt = opt + 1
        print("Rechts")
    if b == "Links" and opt != 0 and opt != 9 and opt != 18: # Aktion beim Drücken und Regulierung am Rand
        opt = opt - 1
        print("Links")
    if b == "Oben" and i > 0: # Aktion beim Drücken und Regulierung am Rand
        opt = opt - 8
        i = i - 1
        print("Oben")
    if b == "Unten" and i < 2: # Aktion beim Drücken und Regulierung am Rand
        opt = opt + 8
        i = i + 1
        print("Unten")
    if b == "Click" and opt != 26 and last < 13: # Auswählen der Taste und schreiben des derzeitigrn Namens und Regulierung der Namenslänge
        name = name + "".join(tastatur[opt])
        last = last + 1
        print(name)
        print("Click")
    elif b == "Click2" and opt == 26 and last > -1: # Auswählen der Taste und Löschen eines Buchstabens
        del name[last]
        last = last - 1
        print(name)
        print("Click2")