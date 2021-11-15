# Sven Wille            ETS 2021        15.11.2021

# Aufgabe 1:
# Schreiben Sie ein Programm, das mithilfe einer for-Schleife alle durch 9 teilbaren Zahlen 
# zwischen zwei zuvor eingegebenen Grenzen in eine Liste schreibt und dann ausgibt.

x = int(input("Neunerreihe zwischen Zahl 1: ")) 
y = int(input("und Zahl 2: "))
Neunerreihe = []

for i in range (x,y+1):  
    if i % 9 == 0:
        Neunerreihe += [i]

for i in range (0,i+1): 
    print(Neunerreihe[i])

