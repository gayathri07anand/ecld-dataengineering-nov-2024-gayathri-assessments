def reverse(sentence):
    word =sentence.split()
    reversed = word[::-1]
    string = " ".join(reversed)
    return string
print (reverse('what is your name'))