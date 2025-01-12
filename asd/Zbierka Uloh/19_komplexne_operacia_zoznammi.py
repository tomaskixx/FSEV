'''19. Komplexné operácie so zoznammi [2 body]
Napíšte program, ktorý:
a) Generuje zoznam 20 náhodných čísel v rozsahu 1-100.
b) Rozdelí tieto čísla na párne a nepárne do dvoch samostatných zoznamov.
c) Vypíše priemer každého zoznamu.'''

import random

def iseven(num):
    if (num % 2) == 0: 
        return True


parne = []
neparne = []

for i in range(20):
    temp = random.randint(1,100)
    if iseven(temp):
        parne.append(temp)
    else:
        neparne.append(temp)

print(f"Priemer parnych cisel: {sum(parne)/len(parne)}")
print(f"Priemer neparnych cisel: {sum(neparne)/len(neparne)}")