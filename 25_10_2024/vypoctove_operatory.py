# Napíšte program, ktorý získa od používateľa dve čísla v rozsahu 1 až 9 (iné nedovolí) a následne s nimi vykoná výpočty: 
# sčítanie (A+B), odčítanie (A-B), násobenie (A×B), delenie (A:B) a umocnenie (A^B).  

print("Zadajte 2 cele cisla medzi 1 az 9: ")
while True:
    num1 = int(input())
    if 1 <= num1 <= 9:
        break #ukonci while cyklus
    else:
        print("Nespravne cislo! Prosim zadajte cislo medzi 1 a 9")

while True:
    num2 = int(input())
    if 1 <= num2 <= 9:
        break
    else:
        print("Nespravne cislo! Prosim zadajte cislo medzi 1 a 9")

print("Sucet cisel: ", num1+num2)
print("Rozdiel cisel: ", num1-num2)
print("Sucin cisel: ", num1*num2)
print("Podiel cisel: ", num1/num2)
print("Umocnenie: ", num1**num2)