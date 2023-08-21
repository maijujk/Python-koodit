
# -----------------------------------------------------------------------------

# Ohjelmoi funktiot: USD2EUR, USD2GBP, USD2JPY niin että ne palauttavat oikein muunnetut valuutta-arvot.
def USD2EUR(maara):

    """

    Muunnetaan maara US Dollareista Euroihin.

        Kerroin: 1 USD = 0.831467 EUR (float)

        palauttaa:

        muunnettu_arvo: Dollarit Euroina (float)

    """

    #TODO: Lisää koodisi tähän
    muunnettu_arvo = maara * 0.831467

    return muunnettu_arvo

def USD2GBP(maara):

    """

    Muunnetaan maara US Dollareista Puntiin.

      kerroin: 1 USD = 0.739472 GBP (float)

      palauttaa:

        muunnettu_arvo: Dollarit Puntina (float)

    """

    #TODO: Lisää koodisi tähän
    muunnettu_arvo = maara * 0.739472

    return muunnettu_arvo

def USD2JPY(maara):

    """

    Muunnetaan maara US Dollareista Jeniin.

    kerroin: 1 USD = 112.656 JPY (float)

    palauttaa:

        muunnettu_arvo: Dollarit Jeneinä (float)

    """

    #TODO: Lisää koodisi tähän
    muunnettu_arvo = maara * 112.656

    return muunnettu_arvo

def paaohjelma():

    maara = float(input("Syötä dollarit USD: $"))

    # Euroiksi

    eur = USD2EUR(maara)

    # Punniksi

    gbp = USD2GBP(maara)

    # Jeneiksi

    jpy = USD2JPY(maara)

    print("${:.2f} USD = {:.2f} EUR, {:.2f} GBP, {:.2f} JPY".format(maara, eur, gbp, jpy))

if __name__ == '__main__':

    paaohjelma()