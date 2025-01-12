'''28. Iterátory a generátory [3 body]
Napíšte generátor, ktorý:
a) Postupne generuje Fibonacciho čísla.
b) Zastaví generovanie, keď hodnota presiahne 10 000.
c) Uložte tieto čísla do zoznamu a vypíšte ich.'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

nums = []
i = 0
while fibonacci(i) < 10000:
    i += 1
    nums.append(fibonacci(i))

for x in nums:
    print(x)
