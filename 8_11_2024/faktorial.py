# Napíšte program, ktorý vypočíta faktoriál zadaného čísla pomocou cyklu.

num = int(input("Enter an integer: "))
factorial = 1
for i in range(num):
  factorial = factorial*(i+1)
print(factorial)