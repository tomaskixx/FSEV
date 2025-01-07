'''20. Filter s podmienkou [2 body]
Napíšte program, ktorý:
a) Načíta zoznam mien.
b) Odstráni z tohto zoznamu všetky mená kratšie ako 4 znaky.
c) Vypíše výsledný zoznam.'''

mena = []
n = 5

print("Zadajte mena: ")
for i in range(n):
    mena.append(input())

for x in mena:
    if len(x) < 4:
        mena.remove(x)

print(mena)