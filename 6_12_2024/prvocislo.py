def is_prime(num):
    if num < 2:
        return "Nieje prvocislo"
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return "Nieje prvocislo"
        else:
            return "Je prvocislo"
        


print(is_prime(9))