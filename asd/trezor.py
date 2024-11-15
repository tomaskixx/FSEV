def invalid_user_input():
    print("Nespravny input, skuste este raz")
    user_inputs()
    return a,b

def user_inputs():
    a = int(input("Spinac A: "))
    b = int(input("Spinac B: "))
    return a,b


input("Stlacte 'Enter' aby ste zapli hru: Logicky Trezor...\n")
print("\nUroven 1 - AND\nAby ste otvorili dvere, musia byť oba spínače aktívne. Zadajte 1 alebo 0 pre spínač A a B:")
a, b = user_inputs()
while a != 1 or b != 1:
    invalid_user_input()

print("\nUroven 2 - OR\nAspon jeden zo spínačov musí byť aktívny, aby ste otvorili bránu. Zadajte 1 alebo 0 pre spínač A a B:")
a, b = user_inputs()
while a != 1 and b != 1:
    invalid_user_input()

print("\nUroven 3 - NOT\nAby ste otvorili tajné dvere, musíte deaktivovať alarm. Zadajte 1 (zapnutý) alebo 0 (vypnutý):")
a, b = user_inputs()
while a != 0:
    invalid_user_input()

print("\nUroven 4 - XOR\nDvere sa otvoria iba vtedy, ak je len jeden zo spínačov aktívny, ale nie oba. Zadajte 1 alebo 0 pre spínač A a B:")
a, b = user_inputs()
while a == b:
    invalid_user_input()

print("\nGG! Vyhrali ste!")