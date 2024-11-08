# Napíšte program, ktorý počíta počet samohlások v zadanom reťazci.
vowels = "aeiouAEIOU"
counter = 0
user_string = str(input("Zadajte lubovolnu vetu: "))

for char in user_string:
    if char in vowels:
        counter += 1

print("Pocet samohlasok vo vete je: ",counter)