def convert_temperature(degree, bool):
    if bool == 1:
        return (degree * 9/5) + 3
    else:
        return (degree - 32) * (5/9)


bool = int(input("Napiste 1 ked chcete konvertovat °C na °F a napiste 2 ako chete °F na °C: "))
degree = int(input("Napiste stupen co chcete konvertovat: "))
print(convert_temperature(degree, bool))