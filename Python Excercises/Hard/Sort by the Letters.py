def sorting_string(string1):
    dict1={}
    for element in string1:
        for j in element:
            if ord(j) in range(ord('a'),ord('z')+1):
                dict1[element]=j
            
    str2= sorted(string1,key=lambda x : dict1[x])
    return str2

                               
print (sorting_string(["932c", "832u32", "2344b"]))