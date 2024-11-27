def censor_words(string1,wordlist,charactor):
    for i in wordlist:
        string1 = string1.replace(i,charactor*len(i))
    return string1
print (censor_words("The cow jumped over the moon.", ["cow", "over"], "*"))
