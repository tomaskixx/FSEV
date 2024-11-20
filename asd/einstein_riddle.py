'''
Brit žije v červenom dome.
Švéd chová psy.
Dán pije čaj.
Zelený dom je hneď naľavo od bieleho.
Obyvateľ zeleného domu pije kávu.
Ten, kto fajčí cigarety Pall Mall, chová vtáky.
Obyvateľ žltého domu fajčí cigarety Dunhill.
Ten, kto žije v prostrednom dome, pije mlieko.
Nór žije v prvom dome.
Ten, kto fajčí cigarety Blends, žije vedľa chovateľa mačiek.
Chovateľ koní žije vedľa toho, kto fajčí cigarety Dunhill.
Ten, kto fajčí cigarety Blue Master, pije pivo.
Nemec fajčí cigarety Prince.
Nór žije vedľa modrého domu.
Sused toho, kto fajčí cigarety Blends, pije vodu.
'''

COLORS = ['Cervena', 'Zelena', 'Biela', 'Zlta', 'Modra']
NATIONALITIES = ['Brit', 'Sved', 'Dan', 'Nor', 'Nemec']
DRINKS = ['Caj', 'Kava', 'Mlieko', 'Pivo', 'Voda']
CIGARS = ['Pall Mall', 'Dunhill', 'Blends', 'Blue Master', 'Prince']
PETS = ['Pes', 'Vtak', 'Macka', 'Kon', 'Ryba']

houses = [{'farba': '', 'narodnost': '', 'napoj': '', 'zviera': '', 'cigara': ''} for _ in range(5)]

#1 Nór žije v prvom dome.
houses[0]['narodnost'] = NATIONALITIES[4]

#2 Nór žije vedľa modrého domu.
for i, house in enumerate(houses):
    if house['narodnost'] != NATIONALITIES[4]:
        continue

    if i == 0:
        # If Nor lives in the first house, the second house is Modry
        houses[i + 1]['farba'] = COLORS[4]
        break

    if i == 4:
        # If Nor lives in the fifth house, the fourth house is Modry
        houses[i - 1]['farba'] = COLORS[4]
        break

    if houses[i + 1]['farba'] == '' and houses[i - 1]['farba'] != '':
        # If the house to the right is empty and the one to the left isn't, the right house is Modry
        houses[i + 1]['farba'] = COLORS[4]
        break

    if houses[i + 1]['farba'] != '' and houses[i - 1]['farba'] == '':
        # If the house to the right isn't empty and the one to the left is, the left house is Modry
        houses[i - 1]['farba'] = COLORS[4]
        break

#3 Ten, kto žije v prostrednom dome, pije mlieko.
houses[2]['napoj'] = DRINKS[2] # Mlieko

#4 Zelený dom je hneď naľavo od bieleho.    #5 Obyvateľ zeleného domu pije kávu.
for i in range(len(houses)):  
    # Check if houses i and i+1 have empty COLORS and if the Green house has empty or Kava for drink
    if (
        i < len(houses) - 1 and  # Check if last item in loop
        houses[i]['farba'] == '' and    
        houses[i+1]['farba'] == '' and 
        (houses[i]['napoj'] == '' or houses[i]['napoj'] == DRINKS[1])
    ):
        houses[i]['farba'] = COLORS[1] # Zelena
        houses[i+1]['farba'] = COLORS[2] # Biela
        break


#6 Brit žije v červenom dome.
for i in range(len(houses)): 
    if houses[i]['farba'] == '' and houses[i]['narodnost'] == '': # Finds the firt house where Color and Nationality is empty
        houses[i]['farba'] == COLORS[0]                           # If so, fills in Red and Brit
        houses[i]['narodnost'] == NATIONALITIES[0]
        break
    if houses[i]['farba'] == '' and houses[i]['narodnost'] != '': # Finds last house without Color
        houses[i]['farba'] = COLORS[3] # Fills in Yellow
        break

#7 Obyvateľ žltého domu fajčí cigarety Dunhill.
for i in range(len(houses)): 
    if houses[i]['farba'] == COLORS[3]: 
        houses[i]['cigara'] = CIGARS[1] # Dunhill
        break

#8 Osoba, ktorá má koňa, býva vedľa osoby, ktorá fajčí Dunhill
for i, house in enumerate(houses):
    if house['cigara'] != CIGARS[1]:
        continue

    if i == 0:
        # If Nor lives in the first house, the second house is Modry
        houses[i + 1]['zviera'] = PETS[3]
        break

    if i == 4:
        # If Nor lives in the fifth house, the fourth house has Kon
        houses[i - 1]['zviera'] = PETS[3]
        break

    if houses[i + 1]['zviera'] == '' and houses[i - 1]['zviera'] != '':
        # If the house to the right is empty and the one to the left isn't, the right house is Modry
        houses[i + 1]['zviera'] = PETS[3]
        break

    if houses[i + 1]['zviera'] != '' and houses[i - 1]['zviera'] == '':
        # If the house to the right isn't empty and the one to the left is, the left house is Modry
        houses[i - 1]['zviera'] = PETS[3]
        break

#9 Dán pije čaj.    #10 Ten, kto fajčí cigarety Blue Master, pije pivo.
for i in range(len(houses)):
    # Find house where there's no Blend smoker and not Dan
    if (
        (houses[i]['cigara'] != CIGARS[3] and houses[i]['cigara'] != '')
        and (houses[i]['narodnost'] != NATIONALITIES[2] and houses[i]['narodnost'] != '')
    ):
        houses[i]['napoj'] = DRINKS[4]
        break
    
#11 Osoba, ktorá fajčí Blend, má suseda, ktorý pije vodu.
for i, house in enumerate(houses):
    if house['napoj'] != DRINKS[4]:
        continue

    if i == 0:
        # If Nor lives in the first house, the second house is Modry
        houses[i + 1]['cigara'] = CIGARS[2]
        break

    if i == 4:
        # If Nor lives in the fifth house, the fourth house has Kon
        houses[i - 1]['cigara'] = CIGARS[2]
        break

    if houses[i + 1]['zviera'] == '' and houses[i - 1]['zviera'] != '':
        # If the house to the right is empty and the one to the left isn't, the right house is Modry
        houses[i + 1]['cigara'] = CIGARS[2]
        break

    if houses[i + 1]['zviera'] != '' and houses[i - 1]['zviera'] == '':
        # If the house to the right isn't empty and the one to the left is, the left house is Modry
        houses[i - 1]['cigara'] = CIGARS[2]
        break
    
#12 Osoba, ktorá fajčí Blue Master, pije pivo.
for i in range(len(houses)): # Find the one house without CIGARS and DRINKS
    if houses[i]['napoj'] == '' and houses[i]['cigara'] == '':
        houses[i]['cigara'] = CIGARS[3] # Assign Blue Master and Pivo
        houses[i]['napoj'] = DRINKS[3]
        break

#13 Dán pije čaj.
for i in range(len(houses)): # Find house with no NATIONALITIES and DRINKS
    if houses[i]['napoj'] == '' and houses[i]['narodnost'] == '':
        houses[i]['napoj'] = DRINKS[0] # Assign Caj
        houses[i]['narodnost'] = NATIONALITIES[2] # Assign Dan
        break

#14 Nemec fajčí Prince.
for i in range(len(houses)): # Find house with no NATIONALITIES and CIGARS
    if houses[i]['cigara'] == '' and houses[i]['narodnost'] == '':
        houses[i]['cigara'] = CIGARS[4] # Assign Prince
        houses[i]['narodnost'] = NATIONALITIES[4] # Assign Nemec
        break

#15 Osoba, ktorá fajčí Pall Mall, má vtáka.
for i in range(len(houses)):
    if houses[i]['cigara'] == '': # Find remaining house with no Cigar
        houses[i]['cigara'] = CIGARS[0] # Assign Pall Mall
        houses[i]['zviera'] = PETS[1] # Assign Vtak

#16 Osoba, ktorá fajčí Blend, býva vedľa osoby, ktorá má mačku.
for i, house in enumerate(houses):
    if house['cigara'] != CIGARS[3]:
        continue

    if i == 0:
        # If Nor lives in the first house, the second house is Modry
        houses[i + 1]['zviera'] = PETS[2]
        break

    if i == 4:
        # If Nor lives in the fifth house, the fourth house has Kon
        houses[i - 1]['zviera'] = PETS[2]
        break

    if houses[i + 1]['zviera'] == '' and houses[i - 1]['zviera'] != '':
        # If the house to the right is empty and the one to the left isn't, the right house is Modry
        houses[i + 1]['zviera'] = PETS[2]
        break

    if houses[i + 1]['zviera'] != '' and houses[i - 1]['zviera'] == '':
        # If the house to the right isn't empty and the one to the left is, the left house is Modry
        houses[i - 1]['zviera'] = PETS[2]
        break

#17 Švéd má psa.
for i in range(len(houses)):
    if houses[i]['narodnost'] == '': # Find remaining house with no Nationality
        houses[i]['narodnost'] = CIGARS[1] # Assign Sved
        houses[i]['zviera'] = PETS[0] # Assign Pes
        break

# Solution
for i in range(len(houses)):
    if houses[i]['zviera'] == '':
        print(houses[i]['narodnost'], "vlastni rybu")