num = int(input("Zadajte cislo: "))
for i in range(2,num):
    if (num % i) == 0:
        print(num, "nieje prvocislo")
        break
else:
    print(num, "je prvocislo")
    