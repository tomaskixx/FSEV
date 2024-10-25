def encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i.lower()) - 97 for i in key]  
    
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():  

            if char.isupper():
                offset = 65 
            else: 
                offset = 97  

            value = (ord(char) - offset + key_as_int[i % key_length]) % 26
            encrypted_text.append(chr(value + offset))
        else:
            encrypted_text.append(char)  

    return ''.join(encrypted_text)

def decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i.lower()) - 97 for i in key] 
    
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha(): 
            if char.isupper():
                offset = 65 
            else:
                offset = 97  

            value = (ord(char) - offset - key_as_int[i % key_length]) % 26
            decrypted_text.append(chr(value + offset))
        else:
            decrypted_text.append(char)  

    return ''.join(decrypted_text)
    
# Example usage
plaintext = input("Zadajte prosim plaintext: ")
key = input("Zadajte prosim kluc: ")

encrypted = encrypt(plaintext, key)
print("Sifrovany text:", encrypted)

decrypted = decrypt(encrypted, key)
print("Povodny text:", decrypted)
