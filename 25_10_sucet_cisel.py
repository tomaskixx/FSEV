# Napíšte program, ktorý získa od používateľa tri čísla a následne vypíše ich súčet.  

print("Zadajte 3 lubovolne cele cisla: ")
numbers = [int(input()) for i in range(3)]
print("Sucet cisel: ", sum(numbers))