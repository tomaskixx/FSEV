'''24. Triedenie zložitého zoznamu [2 body]
Napíšte program, ktorý:
a) Načíta zoznam slovníkov obsahujúcich mená a veky osôb.
b) Zoradí zoznam podľa veku vzostupne.
c) V prípade rovnakého veku zoradí podľa mena abecedne.'''

dict = [
    {"meno": "Doe", "vek": 25},
    {"meno": "Roe", "vek": 40},
    {"meno": "Smith", "vek": 25},
    {"meno": "Bloggs", "vek": 40},
]

sorted_dict = sorted(dict, key=lambda x: (x["vek"], x["meno"]))

for item in sorted_dict:
    print(f"{item['meno']} : {item['vek']}")