import random

bet_value = int(input("Enter bet amount: "))
bet_number = int(input("Enter number you want to bet on: "))

spin_result = random.randint(0,36)

if bet_number == spin_result:
    bet_value = bet_value * 13
else:
    bet_value =0

print("Spin result:", spin_result)
print("Your reward", bet_value)