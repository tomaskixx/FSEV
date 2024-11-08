# Vytvorte program, ktorý zadaný reťazec obráti naopak (vytvorí reverzný reťazec). 
# Použite for alebo while cyklus na postupné pridávanie znakov do nového reťazca v opačnom poradí.

in_string = str(input("Zadaj retazec: "))
out_string = ""
for char in in_string:
    out_string = char + out_string
print(out_string)