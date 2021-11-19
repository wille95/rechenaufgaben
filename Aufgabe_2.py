# Sven Wille            ETS 2021        17e.11.2021


# Aufgabe 2:
# Sie bauen ein Haus und wollen wissen wieviel Geld Sie bei einer bestimmten Summe und einem bestimmten Zinssatz 
# monatlich zahlen müssen, wenn Sie in 10 Jahren schuldenfrei sein wollen.

#Diverse Eingaben
Haus = int(input("Wie teuer war das Haus? "))           # Wie teuer ist das Haus?
Zinssatz = int(input("Wie hoch ist der Zinssatz? "))    # Wie hoch ist der Jahreszinssatz
Jahre = int(input("wie viele Jahre soll der Kredit abbezahlt werden?")) # Wie viel Jahre abbezhalen

# Annuitätsdarlehnen
# Beispiel: Ein Annuitätendarlehen von 100.000 EUR soll in 20 Jahren bei einem Zinssatz von 6 % 
# in monatlichen Zahlungsterminen zurückgezahlt werden. Der Annuitätenfaktor ist für diese Daten 0,087185. 
# Der jährliche zu zahlende Betrag ist damit 100.000 • 0,087185 = 8.718,50 EUR.
# Der monatliche Betrag ist damit 8718,50 / 12 = 726,54 EUR

Zinsfaktor = Zinssatz/100   # Zinsfaktor

Annuität = (((1+Zinsfaktor)**Jahre)*Zinsfaktor)/(((1+Zinsfaktor)**Jahre) - 1)   # Berechnung des Annuitätendarlehen

Kosten_pro_Jahr = Annuität * Haus       # Berechnung der Kosten pro Jahr

Monatsbetrag = Kosten_pro_Jahr / 12     # Berechnung der Kosten pro Monat


print("Es müssen im Durchschnitt montalich {0} Euro für das Haus bezahlt werden.".format(round(Monatsbetrag,2)))

# Quelle = http://www.wirtschaftslexikon24.com/d/annuitaetenfaktor/annuitaetenfaktor.htm