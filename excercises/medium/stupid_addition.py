#Create a function that takes two parameters and, 
 #if both parameters are strings, add them as if they were integers or 
#if the two parameters are integers, concatenate them.


def stupid_addition(a,b):
    if isinstance(a,str) and isinstance(b,str):
        return int(a)+int(b)
    elif isinstance(a,int) and isinstance(b,int):
        return f"{a}{b}"
    elif type(a)!= type(b):
        return "none"
print (stupid_addition(1,2))
print (stupid_addition("1","2"))
print (stupid_addition("1",2))
