# Napíšte program, ktorý vypočíta faktoriál zadaného čísla pomocou cyklu.

num = int(input("Zadajte cislo: "))
factorial = 1
for i in range(num):
  factorial = factorial*(i+1)
print("Faktorial :",factorial)