def pozdrav_podla_casu(cas):
    match cas:
        case cas if cas < 12:
            return "Dobre rano!"
        case cas if cas >= 12 and cas < 18:
            return "Dobry den!"
        case cas if cas >= 18:
            return "Dobry vecer!"
        
print(pozdrav_podla_casu(16))