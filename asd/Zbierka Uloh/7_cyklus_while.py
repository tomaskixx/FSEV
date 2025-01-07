'''7. Cyklus (while) [1 bod]
Vytvorte hru „Hádaj číslo“:
a) Generujte náhodné číslo od 1 do 100.
b) Používateľ opakovane háda číslo, až kým neuhádne.
c) Po každom pokuse program povie, či je číslo vyššie alebo nižšie.'''

import random

print("Hádaj číslo!")
guess = 0
ran = random.randint(1,100)

while guess != ran:
    guess = int(input("Zadajte cele cislo medzi 1-100 (vratane): "))
    if guess < ran:
        print("Cislo je vyssie...")
    else:
        print("Cislo je nizsie...")

print(f"Uhadli ste cislo, bolo to {ran}")