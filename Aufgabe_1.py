# Sven Wille            ETS 2021        15.11.2021

# Aufgabe 1:
# Schreiben Sie ein Programm, das mithilfe einer for-Schleife alle durch 9 teilbaren Zahlen 
# zwischen zwei zuvor eingegebenen Grenzen in eine Liste schreibt und dann ausgibt.

x = int(input("Neunerreihe zwischen Zahl 1: ")) # Untere Grenze Neunerreihe
y = int(input("und Zahl 2: "))                  # Obere Grenze Neunerreihe
Neunerreihe = []                                # Leere Liste

for i in range (x,y+1):                         # Schleife um alle Zahlen in der angegeben Range  
    if i % 9 == 0:                              # durch 9 teilbar sind
        Neunerreihe += [i]                      # in Liste schreiben

for i in range (0,i+1):                         # Liste ausgeben
    print(Neunerreihe[i])

