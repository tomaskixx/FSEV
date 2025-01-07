'''16. Práca s vlastnými metódami [2 body]
Vytvorte triedu Student, ktorá:
a) Má atribúty meno, priezvisko a znamky (zoznam známok).
b) Obsahuje metódu priemer_znamok, ktorá vypočíta priemernú známku.
c) Otestujte na viacerých študentoch.'''

import numpy

class Student:
    def __init__(self, meno, priezvisko, znamky):
        self.meno = meno
        self.priezvisko = priezvisko
        self.znamky = znamky

    def priemer_znamok(self):
        return numpy.average(self.znamky)
    

student1 = Student("John", "Doe", [1, 2, 3, 4, 5])
print(f"Priemer znamok: {student1.priemer_znamok()}")

student2 = Student("Jane", "Smith", [2, 2, 3, 3, 1])
print(f"Priemer znamok: {student2.priemer_znamok()}")

student3 = Student("Richard", "Roe", [1, 1, 1, 1, 1])
print(f"Priemer znamok: {student3.priemer_znamok()}")