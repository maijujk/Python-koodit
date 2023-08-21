
# -----------------------------------------------------------------------------

#Muotoilee muutujat suoraan printatessa
nelja = "45"
seit = "75"
sata = "100"

print(nelja, seit, sata)
print("{:s}{:s}{:s}".format(nelja, seit, sata))
print("{:s}, {:s} ja {:s}.".format(nelja, seit, sata))
print()

# Tehtävä 2
print("{:s}, {:s} ja tämä tulee ennen sataa, kun ulkona ei sada! {:s}.".format(nelja, seit, sata))
print()

# Tehtävä 3
# Printtaa muuttujien laskutoimitukset 
luku1 = 41
luku2 = 4

print("Jakolaskun tulos on:", luku1 / luku2)
print("Jakolaskun jakojäännös on:", luku1 % luku2)
print()

#Tehtävä 4
# Tallentaa hinnat muuttujiin 
a = float(input("Anna ensimmäisen tuotteen hinta: "))
b = float(input("Anna toisen huotteen hinta: "))
c = float(input("Anna kolmannen huotteen hinta: "))

# Printtaa muuttujat pyöristettynä {:.0f} 0 = desimaalien määrä, f = float
print("Ensimmäisen tuotteen hinta on pyöristettynä {:.0f} EUR, toisen tuotteen hinta on  pyöristettynä {:.0f} EUR ja kolmannen tuotteen hinta on pyöristettynä {:.0f} EUR.".format(a, b, c))

# Printtaa muuttujan yhteen vastauksen kahden desimaalin tarkkuudella
yhteen = a + b + c
print("Kaikkien tuotteiden yhteenlaskettu hinta kahden desimaalin tarkkuudella on {:.2f} EUR.".format(yhteen))

# alapuolella oleva teksti kopioitu käytettävä tyyliopas wordista!
print("Kiitos ohjelman käytöstä")

# eof