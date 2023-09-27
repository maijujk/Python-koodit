# tee ratkaisu tänne
if False:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koetiedot = input("Koepisteet: ")
    kurssintiedot = input("nimi: ")
    
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat.csv"
    tehtavatiedot = "tehtavat.csv"
    koetiedot = "koepisteet.csv"
    kurssintiedot = "kurssi.txt"
    tulos1 = "tulos.txt"
    tulos2 = "tulos.csv"
 
with open(kurssintiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(":")
        if osat[0] == "nimi":
            kurssinnimi = osat[1].strip()
        if osat[0] == "laajuus opintopisteina":
            kurssinlaajuus = osat[1].strip()
            # print(f"{osat[0]}: {kurssinlaajuus}")

def arvosana(pisteet):
    a = 0
    rajat = [15, 18, 21, 24, 28]
    while a < 5 and pisteet >= rajat[a]:
        a += 1
    return a
 
def pisteiksi(lkm):
    return lkm // 4
 
opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        opiskelijat[osat[0]] = f"{osat[1]} {osat[2].strip()}"
 
tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            continue
        summa = 0
        for i in range(1, 8):
            summa += int(osat[i])
        tehtavat[osat[0]] = summa
 
kokeet = {}
with open(koetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(";")
        # ohitetaan otsikkorivi
        if osat[0] == "opnro":
            continue 
        summa = 0
        for i in range(1, 4):
            summa += int(osat[i])
        kokeet[osat[0]] = summa
    
with open(tulos1, "w") as tiedosto:
    ekarivi = (f"{kurssinnimi}, {kurssinlaajuus} opintopistettä\n")
    tiedosto.write(ekarivi)
    tiedosto.write("="*(len(ekarivi)-1)+"\n")
    tiedosto.write(f"nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana\n")
    print(ekarivi)
    print("="*(len(ekarivi)-1)+"")

    print(f"nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana")

    for opnro, nimi in opiskelijat.items():
        tehtavia = tehtavat[opnro]
        teht_pist = pisteiksi(tehtavia)
        koe_pist = kokeet[opnro]
        yht_pist = teht_pist + koe_pist
        tiedosto.write(f"{nimi:30}{tehtavia:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana(yht_pist):<10}\n")
    
        print(f"{nimi:30}{tehtavia:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana(yht_pist):<10}")
    print()
with open(tulos2, "w") as tiedosto:
    for opnro, nimi in opiskelijat.items():
        yht = kokeet[opnro] + pisteiksi(tehtavat[opnro])
        rivi = f"{opnro};{nimi};{arvosana(yht)}"
        # print(f"{opnro};{nimi};{arvosana(yht)}")
        tiedosto.write(rivi+"\n")
print()
print(f"Tulokset talletettu tiedostoihin {tulos1} ja {tulos2}")