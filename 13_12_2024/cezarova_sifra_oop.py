class Ceasar:
    def __init__(self, key, text):
        self.__key = key
        self.__text = text

    def key_input(self):
        self.key = int(input("Zadajte kluc: "))

    def text_input(self):
        self.text = input("Zadajte text: ") 

    def sifrovanie(self):
        result = "" 
        for i in range(len(self.text)): 
            char = self.text[i] 
            if char.isupper(): 
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower(): 
                result += chr((ord(char) + key - 97) % 26 + 97)
            else: 
                result += char
        return result
    
    def desifrovanie(self):
        result = "" 
        for i in range(len(self.text)): 
            char = self.text[i] 
            if char.isupper(): 
                result += chr((ord(char) - key - 65) % 26 + 65)
            elif char.islower(): 
                result += chr((ord(char) - key - 97) % 26 + 97)
            else: 
                result += char
        return result


text = input("Zadajte text: ") 
key = int(input("Zadajte kluc: "))
sifra1 = Ceasar(key, text)
print(sifra1.sifrovanie())

