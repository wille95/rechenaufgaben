# Sven Wille            ETS 2021        16.11.2021


# Aufgabe 2:
# Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer bestimmten Summe und einem bestimmten Zinssatz 
# monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.

#Diverse Eingaben
Haus = int(input("Wie teuer war das Haus? "))           # Wie teuer ist das Haus?
Zinssatz = int(input("Wie hoch ist der Zinssatz? "))    # Wie hoch ist der Jahreszinssatz
Jahre = int(input("wie viele Jahre soll der Kredit abbezahlt werden?")) # Wie viel Jahre abbezhalen

Monate = Jahre * 12     # Wie viele Monate insgesamt
Rest = Haus             # Rest zuweisen zur Berechnung
Gesamtzinsen = 0        # Gesamtzisnen zweisen für Berechnung

Tilgung = Haus / Monate  #Tilgung pro Jahr berechnen

print("Die Monatliche Tilgung ist: {0}".format(round(Tilgung,2)))

while (Rest > Tilgung):
    Zinsen = Rest * ((Zinssatz / 100) / 12) # Zinsberechnung
    Gesamtzinsen = Zinsen + Gesamtzinsen    # Gesamtzinsen hochaddieren
    Rest = Rest - Tilgung                  # Tilgung vom Rest abziehen


Gesamtkosten = Haus + Gesamtzinsen + Rest   # Gesamtkosten berechnen
Kosten = Gesamtkosten / Monate              # Kosten pro Monat berechnen
                       
# Diverse Ausgaben
print("Die Gesamten Zinsen auf das Haus sind: {0}".format(round(Gesamtzinsen,2)))
print("Die Gesamtkosten für das Haus sind: {0}".format(round(Gesamtkosten,2)))
print("Es müssen im Durchschnitt montalich {0} Euro für das Haus bezahlt werden.".format(round(Kosten,2)))

