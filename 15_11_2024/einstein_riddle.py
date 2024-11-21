colors = ['Cervena', 'Zelena', 'Biela', 'Zlta', 'Modra']
nationalities = ['Brit', 'Sved', 'Dan', 'Nor', 'Nemec']
drinks = ['Caj', 'Kava', 'Mlieko', 'Pivo', 'Voda']
cigars = ['Pall Mall', 'Dunhill', 'Blends', 'Blue Master', 'Prince']
pets = ['Pes', 'Vtak', 'Macka', 'Kon', 'Ryba']

houses = [None] * 5

for i in range(5):
    houses[i] = {
        'farba': '',
        'narodnost': '',
        'napoj': '',
        'zviera': '',
        'cigara': ''
    }

houses[0]['narodnost'] = nationalities[4]

for i in range(len(houses)):  
    if houses[i]['narodnost'] == nationalities[4]:
        match i:
            case 0:
                houses[i + 1]['farba'] = colors[4]
                break
            case 4:
                houses[i - 1]['farba'] = colors[4]
                break
            case _ if houses[i + 1]['farba'] == '' and houses[i - 1]['farba'] != '':
                houses[i + 1]['farba'] = colors[4]
                break
            case _ if houses[i + 1]['farba'] != '' and houses[i - 1]['farba'] == '':
                houses[i - 1]['farba'] = colors[4]
                break

houses[2]['napoj'] = drinks[2]

for i in range(len(houses)):  
    if (
        i < len(houses) - 1 and
        houses[i]['farba'] == '' and
        houses[i + 1]['farba'] == '' and
        (houses[i]['napoj'] == '' or houses[i]['napoj'] == drinks[1])
    ):
        houses[i]['farba'] = colors[1]
        houses[i + 1]['farba'] = colors[2]
        break

for i in range(len(houses)): 
    if houses[i]['farba'] == '' and houses[i]['narodnost'] == '':
        houses[i]['farba'] = colors[0]
        houses[i]['narodnost'] = nationalities[0]
        break
    if houses[i]['farba'] == '' and houses[i]['narodnost'] != '':
        houses[i]['farba'] = colors[3]
        break

for i in range(len(houses)): 
    if houses[i]['farba'] == colors[3]:
        houses[i]['cigara'] = cigars[1]
        break

last_index = len(houses) - 1

for i in range(len(houses)):  
    if houses[i]['cigara'] == cigars[1]:  
        match i:
            case 0:
                houses[i + 1]['zviera'] = pets[3]
                break
            case _:
                if i == last_index:
                    houses[i - 1]['zviera'] = pets[3]
                    break
                elif i < last_index and houses[i + 1]['zviera'] == '' and houses[i - 1]['zviera'] != '':
                    houses[i + 1]['zviera'] = pets[3]
                    break
                elif i > 0 and houses[i + 1]['zviera'] != '' and houses[i - 1]['zviera'] == '':
                    houses[i - 1]['zviera'] = pets[3]
                    break

for i in range(len(houses)):
    if (
        (houses[i]['cigara'] != cigars[3] and houses[i]['cigara'] != '') and
        (houses[i]['narodnost'] != nationalities[2] and houses[i]['narodnost'] != '')
    ):
        houses[i]['napoj'] = drinks[4]
        break

for i in range(len(houses)):
    if houses[i]['napoj'] == drinks[4]:
        match i:
            case 0:
                houses[i + 1]['cigara'] = cigars[2]
                break
            case _:
                if i == last_index:
                    houses[i - 1]['cigara'] = cigars[2]
                    break
                elif i < last_index and houses[i + 1]['cigara'] == '' and houses[i - 1]['cigara'] != '':
                    houses[i + 1]['cigara'] = cigars[2]
                    break
                elif i > 0 and houses[i + 1]['cigara'] != '' and houses[i - 1]['cigara'] == '':
                    houses[i - 1]['cigara'] = cigars[2]
                    break

for i in range(len(houses)):
    if houses[i]['napoj'] == '' and houses[i]['cigara'] == '':
        houses[i]['cigara'] = cigars[3]
        houses[i]['napoj'] = drinks[3]
        break

for i in range(len(houses)):
    if houses[i]['napoj'] == '' and houses[i]['narodnost'] == '':
        houses[i]['napoj'] = drinks[0]
        houses[i]['narodnost'] = nationalities[2]
        break

for i in range(len(houses)):
    if houses[i]['cigara'] == '' and houses[i]['narodnost'] == '':
        houses[i]['cigara'] = cigars[4]
        houses[i]['narodnost'] = nationalities[4]
        break

for i in range(len(houses)):
    if houses[i]['cigara'] == '':
        houses[i]['cigara'] = cigars[0]
        houses[i]['zviera'] = pets[1]

for i in range(len(houses)):
    if houses[i]['cigara'] == cigars[3]:
        match i:
            case 0:
                houses[i + 1]['zviera'] = pets[2]
                break
            case _:
                if i == last_index:
                    houses[i - 1]['zviera'] = pets[2]
                    break
                elif i < last_index and houses[i + 1]['zviera'] == '' and houses[i - 1]['zviera'] != '':
                    houses[i + 1]['zviera'] = pets[2]
                    break
                elif i > 0 and houses[i + 1]['zviera'] != '' and houses[i - 1]['zviera'] == '':
                    houses[i - 1]['zviera'] = pets[2]
                    break

for i in range(len(houses)):
    if houses[i]['narodnost'] == '':
        houses[i]['narodnost'] = cigars[1]
        houses[i]['zviera'] = pets[0]
        break

for i in range(len(houses)):
    if houses[i]['zviera'] == '':
        print(houses[i]['narodnost'])
