def can_build(x,y):
    x=str(x)
    y=str(y)
    for i in y:
        if i in x:
            return "True"
        else :
            return"false"
print(can_build("aPPleAL", "PAL"))
print(can_build("aPPleAL", "apple"))

    

