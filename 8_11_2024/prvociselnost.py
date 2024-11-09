# Vytvorte program, ktorý zistí, či zadané číslo je prvočíslo. 
# Program použije for cyklus na kontrolu deliteľov čísla 
# (okrem 1 a samotného čísla) a oznámi, či je číslo prvočíslo alebo nie.  


num = int(input("Enter an integer: "))
if num < 2:
    print("Not prime")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Is prime")
