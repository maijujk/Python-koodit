
# -----------------------------------------------------------------------------

from datetime import datetime
import  os
import random

# luo kansion 
def luo_kansio(nimi):
   os.mkdir(nimi)
  
# laskee montako kansioita on luotu 
def kansio_kpl_maara(kpl):
  print("Olet luonut", kpl, "kansiota.")
  
# generoi automaattisesti luotavan kansion nimen
def nimi_genraattori():
   date = datetime.now()
   x = date.strftime("%d_%m_%Y_")
   k = random.randint(10000, 50000)
   y = (str(x) + str(k))
   luo_kansio(y)
   print(y)

kpl = 0
while True:
 print("\nValitse yksi:")
 print("1) Luo kansio satunnaisella nimellä")
 print("2) Luo kansio nimellä")
 print("3) Tarkista montako kansiota on luotu")
 print("4) Poistu\n")
 valitse = input("Syötä toiminto: ")

 if valitse == "1":
   print("Luotiin kansio satunnaisella nimellä: ", end="")
   x = nimi_genraattori()
   kpl += 1

 elif valitse == "2":
    syote = input("Syötä luotavan kansion nimi: ")
    if (os.path.exists(syote)):
     print("Olet jo luonut kansion nimellä:", syote) 
    else:
     luo_kansio(syote)
     print("Luotiin kansio nimellä:", syote)
     kpl += 1

 elif valitse == "3":
   kansio_kpl_maara(kpl)

 elif valitse =="4":
   break

print("\nKiitos ohjelman käytöstä.")