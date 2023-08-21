
# -----------------------------------------------------------------------------

from datetime import datetime

#print(x.strftime("%d.%m.%Y"))
print()
# Tulostaa inputista!!!!!!!!!!

z = datetime.today()
x = datetime(2021, 12, 24)
y = datetime(2021, 5, 1)
jouluun = x - z
vappuun = y - z
 
print("Jouluun on", jouluun, "päivää ja vappuun" ,vappuun, "päivää.")
print()
#Tee ohjelma, joka ilmoittaa, kumpi on lähempänä nykyistä päivämäärää talvipäivänseisaus (21.12.) vai kesäpäivänseisaus (21.6.).
z = datetime.today()
x = datetime(2021, 12, 21)
y = datetime(2021, 6, 21)

jouluun = x - z
vappuun = y - z
print("Talvipäiväseisaus on", jouluun, "päivää ja kesäpäivänseisaus" ,vappuun, "päivää.")
if jouluun < vappuun:
  print("Talvi")
else:
  print("Kesä")