def priority_sort(list1,set1):
    list_new = [x for x in list1 if x not in set1]
    set_new = [y for y in set1 if y in list1]
    result = list(set_new)+sorted(list_new)
    return result
print (priority_sort([5, 4, 3, 2, 1], {2, 3}))
print (priority_sort([5, 4, 3, 2, 1], {3, 6}))
print(priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}))