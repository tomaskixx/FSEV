'''18. Polymorfizmus [2 body]
Vytvorte triedy Obdlznik a Kruh, ktoré:
a) Obsahujú metódu vypocet_plochy.
b) Implementujte polymorfizmus tak, aby hlavný program vypočítal plochy rôznych objektov.'''

import math

class Obdlznik:
    def __init__(self, a, b):
        self.a = a
        self.b = b 

    def vypocet_plochy(self):
        return (self.a*self.b)
    
class Kruh:
    def __init__(self, r):
        self.r = r

    def vypocet_plochy(self):
        return (2*math.pi*self.r)

obdlznik = Obdlznik(5,10)
print(f"Plocha obdlznika: {obdlznik.vypocet_plochy()}")

kruh = Kruh(7)
print(f"Plocha kruhu: {kruh.vypocet_plochy()}")
