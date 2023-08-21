
# -----------------------------------------------------------------------------

# Päivittää hinnan olemassa olevaan elintarvikkeeseen elintarvikehakemistossa. 
elintarvikehakemisto = {'Leipä':2.26, 'Kaurajuoma':3.62, 'Suklaa':1.59}

try: 
 nimi = input("Syötä tuotteen nimi, jonka hintaa muutetaan: ")
 if nimi not in elintarvikehakemisto:
   print("Tuotetta", nimi, "ei ole!")

 else:  
    hinta = float(input("Anna uusi hinta:"))
    elintarvikehakemisto[nimi] = hinta
    print("Tuotteen", nimi, "uusi hinta on:", elintarvikehakemisto[nimi])

except ValueError:
    print("Et antanut uutta hintaa tuotteelle {:}!".format(nimi))

print("Kiitos ohjelman käytöstä.")

