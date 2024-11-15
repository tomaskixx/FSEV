print("Logicky trezor zadanie:")

while True:
    print("Uroven 1 – AND:")
    a = int(input("Zadajte 1 alebo 0 pre switch A: "))
    b = int(input("Zadajte 1 alebo 0 pre switch B: "))
    
    if a == 1 and b == 1:
        print("Spravne dvere su otvorene")
        break
    else:
        print("Nepsravne, skuste znovu")


while True:
    print("Uroven 2 – OR:")
    a = int(input("Zadajte 1 alebo 0 pre switch A: "))
    b = int(input("Zadajte 1 alebo 0 pre switch B: "))
    
    if a == 1 or b == 1:
        print("Spravne dvere su otvorene")
        break
    else:
        print("Nepsravne, skuste znovu")


while True:
    print("Uroven 3 – NOT:")
    a = int(input("Zadajte 1 alebo 0 pre alarm: "))
    
    if a == 0:
        print("Spravne dvere su otvorene")
        break
    else:
        print("Nepsravne, skuste znovu")


while True:
    print("Uroven 4 – XOR:")
    a = int(input("Zadajte 1 alebo 0 pre switch A: "))
    b = int(input("Zadajte 1 alebo 0 pre switch B: "))
    
    if (a == 1) != (b == 1):  
        print("Spravne dvere su otvorene")
        break
    else:
        print("Nepsravne, skuste znovu")

print("Win!")

