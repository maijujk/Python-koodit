# Tee ratkaisusi tähän:
class Maksukortti:
    def __init__(self, alkusaldo: float):
        self.saldo = alkusaldo

    def syo_edullisesti(self):
        if self.saldo >= 2.6:  # Tarkista, onko saldo riittävä
            self.saldo -= 2.6

    def syo_maukkaasti(self):
        if self.saldo >= 4.6:  # Tarkista, onko saldo riittävä
            self.saldo -= 4.6
            
    def lataa_rahaa(self, luku: float):
        if luku < 0:
            raise ValueError("Kortille ei saa ladata negatiivista summaa")
        self.saldo += luku
            
    def __str__(self):
        return f"Kortilla on rahaa {self.saldo:.1f} euroa"  # Yksi desimaali tarkkuudella

pekan_kortti = Maksukortti(20)
matin_kortti = Maksukortti(30)

pekan_kortti.syo_maukkaasti()
matin_kortti.syo_edullisesti()

print(f"Pekka: {pekan_kortti}")
print(f"Matti: {matin_kortti}")

pekan_kortti.lataa_rahaa(20)
matin_kortti.syo_maukkaasti()
print(f"Pekka: {pekan_kortti}")
print(f"Matti: {matin_kortti}")

pekan_kortti.syo_edullisesti()
pekan_kortti.syo_edullisesti()

matin_kortti.lataa_rahaa(50)
print(f"Pekka: {pekan_kortti}")
print(f"Matti: {matin_kortti}")


# Kokeillaan lataamista negatiivisella summalla
kortti2 = Maksukortti(10)
try:
    kortti2.lataa_rahaa(-10)
except ValueError as e:
    print(e)
