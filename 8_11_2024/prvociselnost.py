# Vytvorte program, ktorý zistí, či zadané číslo je prvočíslo. 
# Program použije for cyklus na kontrolu deliteľov čísla 
# (okrem 1 a samotného čísla) a oznámi, či je číslo prvočíslo alebo nie.  

num = int(input("Zadajte cislo: "))
for i in range(2,num):
    if (num % i) == 0:
        print("Cislo nieje prvocislo.")
        break
else:
    print("Cislo je prvocislo.")
    