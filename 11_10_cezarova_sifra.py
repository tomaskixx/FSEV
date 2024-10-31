# def nam definuje funckciu, funckia funguje tak ze vykona kus kodu co je ma v sebe ked ju vyvolas
# tato funkcia zasifruje nas text - preto sa vola cipher
def cipher(text, shift): 
    result = "" # vytvori prazdnu premennu ktora drzi hodnut ""

    for i in range(len(text)): # for je funkcia ktora zopakuje kus kodu i krat, v tomto pripade i = lenght of text (je to cycklus)
        char = text[i] # ulozi pismeno na mieste i v texte ako jeden character

        if char.isupper(): # ak pismeno v char je velke pismeno vykona tento kod
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower(): # ak pismeno je male vykona tento
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else: # pismeno nieje ani velke ani male (cislo, medzera alebo specialny znak) vynecha pismeno a pokracuje v cykle
            result += char

    return result

def decipher(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)

        else:
            result += char

    return result


text = input("Prosim zadajte text: ")
key = int(input("Prosim zadajte kluc: "))

text = cipher(text, key)
print("Zasifrovany text: ", text)

text = decipher(text, key)
print("Desifrovany text: ", text)