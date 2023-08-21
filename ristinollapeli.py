
# -----------------------------------------------------------------------------

# Ristinollapeli
lista = "789456123"
lista2 = []
pelaaja = ""
i = 0
while True:
 print("{:}{:}{:}".format("o", "-" * 30, "o"), end="")
 print()
 print("|{:^30}|".format("RISTINOLLAPELI"))
 print("{:}{:}{:}\n".format("o", "-" * 30, "o"), end="")
 print()

 print("{:}|{:}|{:}\n{:}".format(lista[0], lista[1], lista[2], "-" * 5))
 print("{:}|{:}|{:}\n{:}".format(lista[3], lista[4], lista[5], "-" * 5))
 print("{:}|{:}|{:}\n".format(lista[6], lista[7], lista[8]))

 if lista[0] == lista[3] == lista[6]:
  break

 elif lista[1] == lista[4] == lista[7]:
  break

 elif lista[2] == lista[5] == lista[8]:
  break

 elif lista[0] == lista[4] == lista[8]:
  break

 elif lista[2] == lista[4] == lista[6]:
  break

 elif lista[0] == lista[1] == lista[2]:
  break

 elif lista[3] == lista[4] == lista[5]:
  break

 elif lista[6] == lista[7] == lista[8]:
  break

 if i % 2 == 0:
   pelaaja = "X"
   
 else:
  pelaaja = "O"

 print("{:}{:}{:}".format("o", "-" * 30, "o"), end="")
 print()
 x = input("|{:} vuoro, valitse numero (1, 9): ".format(pelaaja))
 print("{:}{:}{:}".format("o", "-" * 30, "o"), end="")
 print()
 lista = lista.replace(x, pelaaja)

 if x not in lista2:
   lista2.append(x)
   i += 1

 else:
   continue

print("{:}{:}{:}".format("o", "-" * 30, "o"), end="")
print()
print("|{:^30}|\n|{:^30}|\n|{:^30}| ".format("Peli loppui!", "Voittaja:", pelaaja))
print("{:}{:}{:}".format("o", "-" * 30, "o"), end="")
print()