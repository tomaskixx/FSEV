def nahrada_cisel(txt):
    samohlasky = 'AÁEÉIÍYÝOÓUÚaáeéiíyýoóuú'
    for i in samohlasky:
        txt = txt.replace(i, "*")
    return txt

print(nahrada_cisel("Ahoj"))