def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for i in word:
        if i in vowels:
            count +=1
    return count
print (count_vowels('practice'))
print (count_vowels("Edstem"))