def cipher(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
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