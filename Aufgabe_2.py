# Sven Wille            ETS 2021        15.11.2021


# Aufgabe 2:
# Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer 
# bestimmten Summe und einem bestimmten Zinssatz monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.

Jahre = 10              # in 10 Jahren soll abbezahlt sein
Monate = Jahre * 12     # Wie viele Monate insgesamt

Haus = int(input("Wie teuer war das Haus? "))           # Wie teuer ist das Haus?
Zinssatz = int(input("Wie hoch ist der Zinssatz? "))    # Wie hoch ist der Jahreszinssatz
Tilgung = Haus // Jahre                                 # Welche Monatliche Tilgung ist erforderlich?
Gesamtzinsen = 0                                        # Variable für Gesamtzinsen 
Haus_allein = Haus                                      # Variable zur Berechnung

while Haus != 0 :                                       # Bedingung bis Haus ungleich 0 ist, soll...                       
    Zinsen = Haus * Zinssatz/100                        # Berechnung Zinsen pro Jahr
    Haus = Haus - Tilgung                               # Was kostet das Haus nach der Tilgung pro Jahr
    Gesamtzinsen = Zinsen + Gesamtzinsen                # Zusammenrechnung der Gesamtzinsen

Gesamtkosten = Haus_allein + Gesamtzinsen               # Berechnung Gesamtkosten
Kosten = Gesamtkosten / Monate                          # Berechnung Kosten pro Monat

# Diverse Ausgaben
print("Die Gesamten Zinsen auf das Haus sind: {0}".format(Gesamtzinsen))
print("Die Gesamtkosten für das Haus sind: {0}".format(Gesamtkosten))
print("Es müssen montalich {0} Euro für das Haus bezahlt werden.".format(Kosten))

