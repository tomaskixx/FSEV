def kalkulacka(num1, operator, num2):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        
print(kalkulacka(10, '+', 5))