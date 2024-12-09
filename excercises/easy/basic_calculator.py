def calculator(x, operator, y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

print(calculator(2, "+", 2))  
print(calculator(2, "*", 2))  
print(calculator(4, "/", 2)) 
