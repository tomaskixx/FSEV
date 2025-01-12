def overenie_hesla(heslo):
    #Dĺžka je aspoň 8 znakov.
    if len(heslo) < 8:
        return "Heslo musi mat aspon 8 znakov"
    
    #Obsahuje aspoň jedno veľké písmeno.
    condition = False
    for char in heslo:
        if char.isupper():
            condition = True
    if condition == False:
        return "Heslo musi mat aspon 1 velke pismeno"

    #Obsahuje aspoň jedno malé písmeno.
    condition = False
    for char in heslo:
        if char.islower():
            condition = True
    if condition == False:
        return "Heslo musi mat aspon 1 male pismeno"

    #Obsahuje aspoň jedno číslo.
    condition = False
    for char in heslo:
        if char.isdigit():
            condition = True
    if condition == False:
        return "Heslo musi mat aspon 1 cislo"


print(overenie_hesla("Qwerty123"))