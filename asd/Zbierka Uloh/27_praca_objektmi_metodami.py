'''27. Práca s objektmi a metódami [2 body]
Vytvorte triedu BankovyUcet, ktorá:
a) Má atribúty cislo_uctu, zostatok a metódy na vklad, výber a zobrazenie zostatku.
b) Pridajte kontrolu, či výber neprekročí zostatok.
c) Simulujte transakcie na účte.'''

class BankovyUcet:
    def __init__(self, cislo_uctu, zostatok):
        self.cislo_uctu = cislo_uctu
        self.zostatok = zostatok

    def vklad(self,num):
        self.zostatok += num
        print("Uspesny vklad!")

    def vyber(self,num):
        if num > self.zostatok:
            print("Neuspesny vyber, vyber prekrocil zostatok!")
        else:
            self.zostatok -= num
            print("Uspesny vyber")

    def zobrazenie_zostatku(self):
        print(f"Stav na ucte: {self.zostatok}eur")


ucet = BankovyUcet(1234, 0)

ucet.vklad(100)
ucet.vyber(50)
ucet.zobrazenie_zostatku()