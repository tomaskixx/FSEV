def is_palindrome(txt):
    txt = txt.replace(" ","")
    txt = txt.lower()

    return txt == txt[::-1]
    

print(is_palindrome("tenet"))