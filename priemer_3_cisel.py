# Napíšte program, ktorý získa od používateľa tri čísla a následne vypíše ich priemer zaokrúhlený na 1 desatinné miesto. 

print("Zadajte 3 lubovolne cele cisla: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
print("Primer cisel: ", round((num1+num2+num3)/3,1))