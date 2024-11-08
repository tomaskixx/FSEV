# Napíšte program, ktorý prechádza zadaný zoznam čísel a vypočíta priemer hodnôt.
my_list = [1,2,3,4,5]
sum = 0
for i in my_list:
    sum += i
print(sum/len(my_list))