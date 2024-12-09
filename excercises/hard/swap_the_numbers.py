
def find_other_number(a, b, c):
    return (a, b)[(c == a)]
print (find_other_number(1,5,5))
a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
try:
    print(find_other_number(a,b,c))
except ValueError:
    print("Invalid input! Please enter an integer.")






    
    
    