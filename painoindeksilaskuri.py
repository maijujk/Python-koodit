
# -----------------------------------------------------------------------------

# Painoindeksilaskuri
def tulkinta(indeksi):
 if indeksi < 16.0:
  print("Vaikea alipaino.")

 elif indeksi > 16.0 and indeksi < 16.99:
  print("Merkittävä alipaino.")

 elif indeksi > 17.0 and indeksi < 18.49:
  print("Lievä alipaino.")

 elif indeksi > 18.5 and indeksi < 24.99:
  print("Normaali paino.")

 elif indeksi > 25.0 and indeksi < 29.99:
  print("Lievä ylipaino.")

 elif indeksi > 30.0 and indeksi < 34.99:
  print("Merkittävä ylipaino.")

 elif indeksi > 35.0 and indeksi < 39.99:
  print("Vaikea ylipaino.")

 elif indeksi > 40.0:
  print("Sairaalloinen ylipaino.")

paino = int(input("Syötä paino (kiloissa): "))
pituus = float(input("Syötä pituus (metreissä): "))
p = pituus * pituus
indeksi = paino / p

print("\nPainoindeksi on {:1.1f} > ".format(indeksi), end="")
tulkinta(indeksi)
print("\nKiitos ohjelman käytöstä")

