
# -----------------------------------------------------------------------------

# Tulostaa arvion taitojen tasosta
def taitotaso(prosentti):
 if prosentti == 0:
   print("Alkeis")
 elif prosentti == 20:
   print("Selviytyjä")
 elif prosentti == 40:
   print("Osaaja")
 elif prosentti == 60:
   print("Taitaja")
 elif prosentti == 80:
   print("Noviisi")
 elif prosentti == 100:
   print("Mestari")

# Lukee vastaukset tiedostosta, tulostaa montako % meni oikein ja listaa oikeat ja väärät vastaukset
print("Kerro viisi ensimmäisistä 20:stä alkuaineesta jaksollisessa järjestelmässä:")
tiedosto = open("alkuaineet.txt", "r")
lista = tiedosto.readlines()
lista = [rivi.replace("\n", "") for rivi in lista]
#lista = [rivi.title() for rivi in lista]
print(lista)
oikea = []
vaara = []
i = 1
prosentti = 0
while i <= 5:
  vastaus = input("Aine{:d}: ".format(i))  
  vastaus = vastaus.title()

  if vastaus.lower() in lista and vastaus not in oikea: 
    oikea.append(vastaus)
    i += 1
    prosentti += 20
    
  elif vastaus in oikea or vastaus in vaara:
   print(vastaus, "oli jo syötetty. Duplikaatit eivät ole sallittuja.")
  
  else:
    vaara.append(vastaus)
    i += 1

tiedosto.close()
x = (", ".join(oikea)) 
z = (", ".join(vaara)) 

print("\n{:}% oikein. Oikein: {:}. Väärin: {:}.".format(prosentti, x, z))
print("Taitotaso:", end=" ") 
taitotaso(prosentti)
print("Kiitos ohjelman käytöstä.")

# eof