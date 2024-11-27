class calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
calculator = calculator()
print ("difference between two numbers",calculator.subtract(10,5))
print ("adding two numbers",calculator.add(4,8))
print ("multiply two numbers",calculator.multiply(5,100))
print ("divide two numbers",calculator.divide(100,5))
        
