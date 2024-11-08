# Pomocou for cyklu vygenerujte čísla násobkov 3 medzi 1 a 30.
numbers_list = []
for i in range(30+1):
    if(i % 3 == 0 and i != 0):
        numbers_list.append(i)
print(numbers_list)