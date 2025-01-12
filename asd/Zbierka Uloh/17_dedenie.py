'''17. Dedenie [2 body]
Vytvorte triedy Zamestnanec a Manazer, kde:
a) Zamestnanec má atribúty meno a plat.
b) Manazer dedí Zamestnanec a pridáva atribút oddelenie.
c) Vypíšte informácie o manažérovi a zamestnancovi.'''

class Zamestanec:
    def __init__(self, meno, plat):
        self.meno = meno
        self.plat = plat

    def info(self):
        print("\nZamestanec - Info")
        print(f"Meno: {self.meno}")
        print(f"Plat: {self.plat}")

class Manazer(Zamestanec):
    def __init__(self, meno, plat, oddelenie):
        super().__init__(meno, plat)
        self.oddelenie = oddelenie

    def info(self):
        print("\nManazer - Info")
        print(f"Meno: {self.meno}")
        print(f"Plat: {self.plat}")
        print(f"Oddelenie: {self.oddelenie}")


zamestnanec = Zamestanec("John Doe", 24000)
manazer = Manazer("Richard Roe", 40000, "HR")

zamestnanec.info()
manazer.info()