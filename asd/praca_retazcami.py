txt = "základy programovania"

#1. Napíšte kód, ktorý zobrazí 3. a posledný znak z reťazca.
print(txt[2], txt[-1])

#2. Z reťazca vypíšte podreťazec od 2. po 5. znak (vrátane).
print(txt[3:6])

#3. Napíšte kód, ktorý vypíše reťazec v opačnom poradí.
temp =''
for char in reversed(txt):
    temp = temp + char
print(temp)

#4. Zistite a vypíšte, koľko znakov má reťazec.
counter = 0
for char in txt:
    counter += 1
print(counter)

#5. Napíšte kód, ktorý prevedie reťazec na veľké písmená.
print(txt.upper())

#6. Zistite, koľkokrát sa v reťazci nachádza písmeno "a".
counter = 0
for char in txt:
    if char == 'a':
        counter += 1
print(counter)

#7. Nahraďte všetky výskyty písmena "a" písmenom "@".
print(txt.replace('a','@'))

#8. Zistite, či reťazec obsahuje slovo "program".
if txt.find("program") > 0:
    print("Obsahuje 'program'")
else:
    print("Neobsahuje 'program'")

#9. Zistite index prvého výskytu písmena "m" v reťazci.
print(txt.index('m'))

#10. Obráťte poradie slov v reťazci.
temp = []
for i in txt.split()[::-1]:
    temp.append(i)
print(" ".join(temp))

#11. Z reťazca vytvorte nový reťazec, ktorý obsahuje iba prvé písmená každého slova.
temp = [word[0] for word in txt.split()]
print(temp)

#12. Odstráňte všetky medzery z reťazca
print(txt.replace(' ',''))