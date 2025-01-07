'''15. Objekty a triedy [2 body]
Vytvorte triedu Kruh, ktorá:
a) Má atribút polomer.
b) Obsahuje metódy na výpočet obvodu a plochy kruhu.
c) Otestujte triedu s rôznymi hodnotami polomeru.'''

import math 

class Kruh:
    def __init__(self, polomer):
        self.polomer = polomer

    def vypocet_obvodu(self):
        return (2*math.pi*self.polomer)
    
    def vypocet_plochy(self):
        return (math.pi*pow(self.polomer, 2))
    
kruh1 = Kruh(5)
print(f"Obvod kruh1 : {kruh1.vypocet_obvodu()}")
print(f"Plocha kruh1 : {kruh1.vypocet_plochy()}")

print()

kruh2 = Kruh(7)
print(f"Obvod kruh2 : {kruh2.vypocet_obvodu()}")
print(f"Plocha kruh2 : {kruh2.vypocet_plochy()}")




        