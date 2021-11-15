# Sven Wille            ETS 2021        15.11.2021


# Aufgabe 3:
# Ermitteln Sie für einen festgelegten Zahlenbereich die Primzahlen 
# und schreiben Sie diese in eine Liste. Geben Sie die Liste anschließend aus.

print("Gebe Den Zahlenbereich ein, indem alle Primzahlen ermittelt werden sollen.")
min = int(input("Untere Grenze: ")) 
max = int(input("Obere Grenze: "))

Zahlen = list(range(min,max+1)) # Zahlen Liste erstellen von dem Bereich
Prim = Zahlen                   # Zahlenliste Primliste zuweisen

print(Zahlen)                   # Liste ausgeben

for i in range (min,max+1):         
    if i < 2:                   # Bedingung 0 und 1 rausnehmen
        Prim.remove(i)          # alles kleiner als 2 aus Liste streichen
    else:
        for k in range (2,i):   # for - Schleife von 2 bis i, also 1 muss nicht überprüft
                                # werden und die Zahl selber nicht denn jede Zahl ist durch sich selbst teilbar
             if i % k == 0:     # wenn Restlos Teilbar dann keine Primzahl also:
                 Prim.remove(i) # Zahl aus Zahlenreihe entfernen
                 break          # Bricht die innere For-schleife ab

print(Prim)                     # Liste Primzahlen ausgeben



