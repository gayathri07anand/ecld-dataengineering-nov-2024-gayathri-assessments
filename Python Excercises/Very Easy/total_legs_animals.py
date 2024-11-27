def calculator(a,operator,b):
    if operator == "+" :
        return sum(a,b)
    elif operator == "*" :
        return a*b
    elif operator == "-":
        return a-b
    elif operator =="/":
        return a/b
        if b != 0:
            return a/b
        else :
            return "zero division"
    else :
        return "operation not defined"
print (calculator(4,"*",2))


