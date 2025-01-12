'''14. Komplexné dátové štruktúry (slovníky) [2 body]
Vytvorte program, ktorý:
a) Načíta mená a veky 5 osôb do slovníka.
b) Vypíše meno najstaršej a najmladšej osoby.'''

dict = {}

for i in range(5):
    key = input(f"Zadajte {i+1} kluc: ")
    value = int(input(f"Zadajte {i+1} hodnotu: "))
    dict[key] = value

print(f"Najstarsia osoba: {max(dict.values())}")
print(f"Najmladsia osoba: {min(dict.values())}")


