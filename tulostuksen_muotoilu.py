
# -----------------------------------------------------------------------------

#Ohjelma, joka tulostaa annetun listan (aineet) mukaan kauppalistan. 
#Listassa tulee olla:
#1. rivi: päivämäärä @-merkki ja kellonaika (24h muoto)
#2. rivi: miinusmerkeillä tehty jakoviiva (-)
#3. rivi: tyhjä väli
#4. rivi: juokseva numero (alk. 1), - tuotteen nimi, tuotteen kpl-määrän mukainen kokonaishinta
#5. rivi: Tuotteen kpl-määrä @-merkki Euromerkki (€), yksikköhinta
#Viimeisellä rivillä kokonaishinta Euromerkki (€) ja kokonaishinta

# kauppalista tulosteen muotoilua 
from datetime import datetime

data = [["APPELSIINI", 2.0, 1.99],[
"OLIIVIÖLJY", 1.0, 10.99],["TOMAATTI", 2.6, 1.29],["MAITO 1L", 1.0, 3.45],["VOI", 1.0, 2.99],["LOHI", 1.0, 1.69],["JUUSTO 1/2 KG", 2.0, 4.99]]

date = datetime.now()
x = date.strftime("%d.%m.%Y @ %H:%M")
print(x)

print("-" * 23, end="")
print()
print()

i = 1
sum = 0
for rivi in data:
  y = rivi[1] * rivi[2]
  print(i, "- {:<13} {:>2} {:.2f}\n{:>5.1f} @ € {:1.2f}".format(rivi[0], "€", y, rivi[1], rivi[2]))
  i += 1
  sum += y

print("-" * 23, end="")
print()

print("{:>17} {:>2} {:.2f}".format("YHTEENSÄ", "€", sum))