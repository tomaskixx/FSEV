'''12. Metódy pre reťazce [2 body]
Napíšte program, ktorý:
a) Načíta od používateľa reťazec.
b) Zistí počet písmen, číslic a medzier v reťazci.
c) Prevedie reťazec na veľké písmená a vypíše ho.'''

letter_count = 0
num_count = 0
space_count = 0

str = input("Zadajte retazec: ")

for char in str:
    if char.isalpha():
        letter_count += 1
    elif char.isnumeric():
        num_count += 1
    elif char.isspace():
        space_count += 1

print(f"Pocet pismen: {letter_count}")
print(f"Pocet cisel: {num_count}")
print(f"Pocet medzier: {space_count}")

print(str.upper())