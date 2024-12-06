def pocet_vyskytob_pismena(txt, pismeno):
    counter = 0
    for char in txt:
        if char == pismeno:
            counter += 1
    return counter


print(pocet_vyskytob_pismena("ahoj",'a'))