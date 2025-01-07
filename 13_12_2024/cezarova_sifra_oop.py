class CezarovaSifra:
    def __init__(self, key, txt):
        self.key = key
        self.txt = txt
    def sifrovanie(self):
        result = "" 
        for i in range(len(self.txt)): 
            char = self.txt[i] 
            if char.isupper(): 
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower(): 
                result += chr((ord(char) + key - 97) % 26 + 97)
            else: 
                result += char
        return result
    def desifrovanie(self):
        result = "" 
        for i in range(len(self.txt)): 
            char = self.txt[i] 
            if char.isupper(): 
                result += chr((ord(char) - key - 65) % 26 + 65)
            elif char.islower(): 
                result += chr((ord(char) - key - 97) % 26 + 97)
            else: 
                result += char
        return result


txt = input("Zadajte text: ") 
key = int(input("Zadajte kluc: "))

c1 = CezarovaSifra(key, txt)
print(c1.sifrovanie())

