def count_vowels(string1):
    dictionary = {'A':4,'E':3,'I':1,'O':0,'U':0,'a':4,'e':3,'i':1,'o':0,'u':0}
    result = 0
    for elements in string1:
        if elements in dictionary:
            result += dictionary[elements]
            #else:
            #return "none"
    return result
print (count_vowels("Let\'s test this function."))
print (count_vowels("Do I get the correct output?"))
print(count_vowels("I love edabit!"))        
            
