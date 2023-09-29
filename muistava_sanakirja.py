# tee ratkaisu tänne   
def lisaa_sana():            
    suomi = input("Anna sana suomeksi: ")
    enkku = input("Anna sana englanniksi: ")
    with open("sanakirja.txt", "a") as tiedosto:
        tiedosto.write(f"{suomi} - {enkku}\n")
        print("Sanapari lisätty")
    
def hae_sana():
    sana = input("Anna sana: ")
    with open("sanakirja.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.rstrip()     # poistaa rivinvaihdot ja tyhjät alusta ja lopusta
            osat = rivi.split(":")
            vastaus = osat[0]
            if sana in rivi:
                print(f"{vastaus}")
       

while True:
    print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
    valinta = int(input("Valinta: "))
    if valinta == 1:
        lisaa_sana()
    elif valinta == 2:
        hae_sana()
    elif valinta == 3:
        print("Moi!")
        break
        