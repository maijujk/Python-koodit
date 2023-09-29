
# -----------------------------------------------------------------------------

#Kirjoittaa tiedostoon
koira_tiedosto = open("koirat.txt", "w")

koira_tiedosto.write("Mäyräkoira\n")
koira_tiedosto.write("lammaskoira\n")
koira_tiedosto.write("Noutaja\n")
koira_tiedosto.write("Beagle\n")

koira_tiedosto.close()

# Lukee tiedostosta ja tulostaa
koira_tiedosto = open("koirat.txt", "r")

koirat = koira_tiedosto.readline().strip()
while koirat:
 print(koirat)
 koirat = koira_tiedosto.readline().strip()
 
koira_tiedosto.close()

# Lisää uuden sanan ja tulostaa kaikki sanat listana
koira_tiedosto = open("koirat.txt", "a+")

koira_tiedosto.write("Gorgi\n")
koira_tiedosto.seek(0)
koirat = koira_tiedosto.readlines()
print(koirat)

kaikki = koira_tiedosto.read()
print(kaikki)

koira_tiedosto.close()
