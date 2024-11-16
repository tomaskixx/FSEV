house = [None, None, None, None, None]
colors_set = ["zlta", "modra", "cervena", "zelena", "biela"]
nationalities_set = ["Brit", "Sved", "Dan", "Nemec", "Nor"]
drinks_set = ["caj", "kava", "mlieko", "pivo", "voda"]
cigars_set = ["Pall Mall", "Dunhill", "Blend", "Blue Master", "Prince"]
animal_set = ["pes", "vtak", "macka", "ryba", "kon"]

for i in range(len(house)):
    house[i] = {
        "farba" : colors_set[:],
        "narodnost" : nationalities_set[:],
        "napoj" : drinks_set[:],
        "cigareta" : cigars_set[:],
        "zviera" : animal_set[:]
    }

#1 Brit žije v červenom dome.
for i in range(5):
    if "Brit" not in house[i]["narodnost"]:
        house[i]["farba"] = [x for x in house[i]["farba"] if x != "cervena"]  
    if "cervena" not in house[i]["farba"]:
        house[i]["narodnost"] = [x for x in house[i]["narodnost"] if x != "Brit"] 

#2 Sved ma psa.
for i in range(5):
    if "Sved" not in house[i]["narodnost"]:
        house[i]["zviera"] = [x for x in house[i]["zviera"] if x != "pes"]
    if "pes" not in house[i]["zviera"]:
        house[i]["narodnost"] = [x for x in house[i]["narodnost"] if x != "Sved"]

#3 Dan pije caj.
for i in range(5):
    if "Dan" not in house[i]["narodnost"]:
        house[i]["napoj"] = [x for x in house[i]["napoj"] if x != "caj"]
    if "caj" not in house[i]["zviera"]:
        house[i]["narodnost"] = [x for x in house[i]["narodnost"] if x != "Dan"]

#4 Zelený dom je hneď vľavo vedľa bieleho domu.
for i in range(4):  
    
    if 'zelena' in house[i]['farba'] and 'biela' in house[i + 1]['farba']:
        house[i]['farba'] = ['zelena']  
        house[i + 1]['farba'] = ['biela']  

#5 Majiteľ zeleného domu pije kávu
for i in range(5):
    if "zelena" not in house[i]["farba"]:
        house[i]["napoj"] = [x for x in house[i]["napoj"] if x != "kava"]
    if "kava" not in house[i]["napoj"]:
        house[i]["farba"] = [x for x in house[i]["farba"] if x != "zelena"]

#6 Osoba, ktorá fajčí Pall Mall, má vtáka.
for i in range(5):
    if "Pall Mall" not in house[i]["cigareta"]:
        house[i]["zviera"] = [x for x in house[i]["zviera"] if x != "vtak"]
    if "vtak" not in house[i]["zviera"]:
        house[i]["cigareta"] = [x for x in house[i]["cigareta"] if x != "Pall Mall"]

#7 Majiteľ žltého domu fajčí Dunhill.
for i in range(5):
    if "zlta" not in house[i]["farba"]:
        house[i]["cigareta"] = [x for x in house[i]["cigareta"] if x != "Dunhill"]
    if "Dunhill" not in house[i]["cigareta"]:
        house[i]["farba"] = [x for x in house[i]["farba"] if x != "zlta"]

#8 Osoba žijúca v strednom dome pije mlieko.
house[2]["napoj"] = ["mlieko"]

#9 Nór býva v prvom dome.
house[0]["narodnost"] = ["Nor"]

#10 Osoba, ktorá fajčí Blend, býva vedľa osoby, ktorá má mačku.
for i in range(4):
    if "Blend" in house[i]["cigareta"]:
        house[i+1]["zviera"] = [x for x in house[i+1]["zviera"] if x != "macka"]
    if "macka" in house[i]["zviera"]:
        house[i+1]["cigareta"] = [x for x in house[i+1]["cigareta"] if x != "Blend"]

#11 Osoba, ktorá má koňa, býva vedľa osoby, ktorá fajčí Dunhill.
for i in range(4):
    if "kon" in house[i]["zviera"]:
        house[i+1]["cigareta"] = [x for x in house[i+1]["cigareta"] if x != "Dunhill"]
    if "Dunhill" in house[i]["cigareta"]:
        house[i+1]["zviera"] = [x for x in house[i+1]["zviera"] if x != "kon"]

#12 Osoba, ktorá fajčí Blue Master, pije pivo.
for i in range(5):
    if "Blue Master" not in house[i]["cigareta"]:
        house[i]["napoj"] = [x for x in house[i]["napoj"] if x != "pivo"]
    if "pivo" not in house[i]["napoj"]:
        house[i]["cigareta"] = [x for x in house[i]["cigareta"] if x != "Blue Master"]

#13 Nemec fajčí Prince.
for i in range(5):
    if "Nemec" not in house[i]["narodnost"]:
        house[i]["cigareta"] = [x for x in house[i]["cigareta"] if x != "Prince"]
    if "Prince" not in house[i]["cigareta"]:
        house[i]["narodnost"] = [x for x in house[i]["narodnost"] if x != "Nemec"]

#14 Nór býva vedľa modrého domu.
for i in range(4):
    if "Nor" in house[i]["narodnost"]:
        house[i+1]["farba"] = [x for x in house[i+1]["farba"] if x != "modra"]
    if "modra" in house[i]["farba"]:
        house[i+1]["narodnost"] = [x for x in house[i+1]["narodnost"] if x != "Nor"]

#15 Osoba, ktorá fajčí Blend, má suseda, ktorý pije vodu.
for i in range(4):
    if "Blend" in house[i]["cigareta"]:
        house[i+1]["napoj"] = [x for x in house[i+1]["napoj"] if x != "voda"]
    if "voda" in house[i]["napoj"]:
        house[i+1]["cigareta"] = [x for x in house[i+1]["cigareta"] if x != "Blend"]

for i in range(5):
    if "ryba" not in house[i]["zviera"]:
        print(house[i]["narodnost"])


for i in range(5):
    print(house[i]["zviera"])
