
def is_triplet(a,b,c):
    a,b,c = sorted([a,b,c])
    if (a**2) + (b**2) == c**2:
        return "pythagorean triplet"
    else:
        return "not a pythagorean triplet" 
print (is_triplet(4,5,6))    

