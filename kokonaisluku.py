
# -----------------------------------------------------------------------------

# Kysyy käyttäjältä kokonaislukuja, lisää ne listaan, jos ei kokonaisluku kysyy uudestaan niin kauan että on, jos k lopttaa.
def L(lista):
  print("\nSyötä kokonaisluku lisättäväksi listaan tai “K” keskeytä")
  while True:
   luku = input("Syötä kokonaisluku, tai “K”: ")
   if luku.isdigit():
    lista.append(luku)
   elif luku == "k" or luku == "K":
     break
   else:
     print(luku, "ei ole kokonaisluku.")

# Käy läpi listan luvut ja laskee ne yhteen.
def S(lista):
    summa = 0
    for i in lista:
     i = int(i)
     summa += i
    print("\nSyötettyjen lukujen summa")
    print(summa)

# Kysyy käyttäjältä valintaa l tai s, jos muu kysyy uudestaan niin kauan että s tai l.
lista = []
print("Tulostetaan raporttina allekain kaikki syötetyt luvut (“L”) tai tulostetaan \nVAIN lukujen summa (“S”)")
while True:
 valinta = input("Valitse raporttityyppi (“L”) tai (“S”): ")

# käy läpi listan ja tulostaa listan luvut allekkain ja lukujen summan.
 if valinta == "l" or valinta == "L": 
   L(lista)
   print("\nSyötetyt luvut:")
   for i in lista:
     print(i)
   S(lista)
   break
 
 # Tulostaa luujen summan.
 elif valinta == "s" or valinta == "S":
   L(lista)
   S(lista)
   break

 else:
  print(valinta, "raporttityyppiä ei ole.")
  
print("\nKiitos ohjelman käytöstä.")

# eof