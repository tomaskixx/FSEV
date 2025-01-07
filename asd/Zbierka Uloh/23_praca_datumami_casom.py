'''23. Práca s dátumami a časom [2 body]
Vytvorte program, ktorý:
a) Načíta aktuálny dátum a čas.
b) Vypočíta rozdiel medzi dvoma dátumami zadanými používateľom vo formáte YYYY-MM-DD.
c) Vypíše počet dní, hodín a minút medzi nimi.'''

import datetime

print(f"Aktualny datum a cas: {datetime.datetime.now()}")

temp = input('Zadajte prvy datum vo formate YYYY-MM-DD: ')
year, month, day = map(int, temp.split('-'))
date1 = datetime.date(year, month, day)

temp = input('Zadajte druhy datum vo formate YYYY-MM-DD: ')
year, month, day = map(int, temp.split('-'))
date2 = datetime.date(year, month, day)

print(f"Rozdiel medzi prvym a druhym datumom: {date1 - date2}")