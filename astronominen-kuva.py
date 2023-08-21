

# -----------------------------------------------------------------------------

# Lataa tämän päivän astronomisen kuvan, eilisen päivän astronomisen kuvan tai 
# satunnaisen astronomisen kuvan väliltä: 16.6.1995 - (now).
from datetime import date, timedelta
import random
from random import randint 
import os
from urllib. request import urlopen
import requests
import shutil

def hakee(kuva_nimi, kuva_url):
  vastaus = requests.get(kuva_url, stream = True)
  if vastaus.status_code == 200:
    vastaus.raw.decode_content == True
    with open(kuva_nimi, "wb") as tiedosto:
      shutil.copyfileobj(vastaus.raw, tiedosto)

def avaa(url):
  metadata = urlopen(url)
  data = metadata.read()
  data = data.decode("UTF-8")
  data = eval(data)
  kuva_url = data["url"]
  kuva_nimi = data["date"] + ".jpg"
  hakee(kuva_nimi, kuva_url)

def paaohjelma():
 try:
  tanaan = date.today()
  
  a = tanaan.strftime("%Y/")
  b = tanaan.strftime("%m/")
 
  path = os.path.join(a, b)
  if os.path.exists(path):
     os.chdir(path)
    
  else:
     os.makedirs(path)
     os.chdir(path)
 
  binaaridata = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date="
  
  while True:
    print("\nMitä haluat tehdä:\n"
    "1 - ladata tämän päivän astronomisen kuvan.\n"
    "2 - ladata eilisen päivän astronomisen kuvan.\n"
    "3 - ladata satunnaisen astronomisen kuvan väliltä: 16.6.1995 - (now)\n"
    "0 - lopettaa ohjelma\n")
 
    toiminto = int(input("Syötä toiminto: "))
    if toiminto == 0:
     break
  
    elif toiminto == 1:
     tanaan = date.today()
     url = binaaridata + tanaan.strftime("%Y-%m-%d")
     avaa(url)
     print("Päivän astronominen kuva on tallennettu nimellä hakemistoon: {:}{:}.jpg".format(path, tanaan))
    
    elif toiminto == 2:
     tanaan = date.today()
     eilen = tanaan - timedelta(days=1)
     url = binaaridata + eilen.strftime("%Y-%m-%d")
     avaa(url)
     print("Eilisen päivän astronominen kuva on tallennettu nimellä hakemistoon: {:}{:}.jpg".format(path, eilen))

    elif toiminto == 3:
     pvm = date.today().replace(day=16, month=6, year=1995).toordinal()
     tanaan = date.today().toordinal()
     random_day = date.fromordinal(random.randint(pvm, tanaan))
     url = binaaridata + random_day.strftime("%Y-%m-%d")
     avaa(url)
     print("Satunnaisen päivän astronominen kuva on tallennettu nimellä hakemistoon: {:}{:}.jpg".format(path, random_day))

 except Exception as poikkeus: 
     print("\nVirheilmoitus:\n", poikkeus) 

paaohjelma()
print("\nKiitos ojhelman käytöstä")