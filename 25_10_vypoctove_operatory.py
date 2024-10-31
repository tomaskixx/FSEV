# Napíšte program, ktorý získa od používateľa dve čísla v rozsahu 1 až 9 (iné nedovolí) a následne s nimi vykoná výpočty: 
# sčítanie (A+B), odčítanie (A-B), násobenie (A×B), delenie (A:B) a umocnenie (A^B).  

def get_number():
    while True:
        num = int(input())
        if 1 <= num <= 9:
            return num
        else:
            print("Nespravne cislo! Prosim zadajte cislo medzi 1 a 9")

print("Prosim zadajte 2 cele cisla medzi 1 az 9: ")
num1 = get_number()
num2 = get_number()


print("Sucet: ", num1+num2)
print("Rozdiel: ", num1-num2)
print("Sucin: ", num1*num2)
print("Podiel: ", num1/num2)
print("Umocnenie: ", pow(num1,num2))