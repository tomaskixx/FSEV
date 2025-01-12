'''29. Viacúrovňové dedenie [3 body]
Vytvorte hierarchiu tried:
a) Zviera (atribúty: meno, vek).
b) Cicavec (pridáva atribút: spôsob pohybu).
c) Pes (pridáva metódu: šteká).
d) Otestujte dedenie a volanie metód na objektoch rôznych úrovní.'''


class Zviera:
    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

class Cicavec(Zviera):
    def __init__(self, meno, vek, sposob_pohybu):
        super().__init__(meno, vek)
        self.sposob_pobyhu = sposob_pohybu

class Pes(Cicavec):
    def __init__(self, meno, vek, sposob_pohybu):
        super().__init__(meno, vek, sposob_pohybu)

    def steka(self):
        print("Haf!\n")


zviera = Zviera("Doe", 6)
cicavec = Cicavec("Bea", 4, "po styroch")
pes = Pes("Molly", 3, "po styroch")

#Len trieda 'Pes' ma definovanu metodu steka(), ostatne triedo to nemaju, try nam vyhodi chybu
try:
    zviera.steka()
except:
    print("steka() metoda neexistuje pre triedu 'Zviera'\n")

try:
    cicavec.steka()
except:
    print("steka() metoda neexistuje pre triedu 'Cicavec'\n")

try:
    pes.steka()
except:
    print("steka() metoda neexistuje pre triedu 'Pes'")