'''13. Komplexné dátové štruktúry (zoznamy) [2 body]
Napíšte program, ktorý:
a) Načíta zoznam čísel od používateľa.
b) Nájde a vypíše najmenšie a najväčšie číslo v zozname.
c) Zoradí zoznam a vypíše ho.'''

my_list = []
print("Zadajte 5 celych cisel: ")

for i in range(5):
    my_list.append(int(input()))

my_list.sort()

print(f"Najvacsie cislo: {max(my_list)}")
print(f"Najmensie cislo: {min(my_list)}")
print(f"Zoradene: {my_list}")