# Použite while cyklus na opakovanie výzvy pre používateľa, aby zadal pozitívne číslo.
# Cyklus sa zastaví, až keď zadá správny vstup.
user_guess = int(input("Zadajte cele kladne cislo: "))
while user_guess <= 0:
    user_guess = int(input("Nepravne! skuste znova: "))
print("Spravne!")