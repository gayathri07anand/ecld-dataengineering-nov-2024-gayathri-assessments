def find_fulcrum(array):
    n = len(array)
    for i in range(0,n):
        left_sum = sum(array[0:i])
        right_sum = sum(array[i+1:n])
        if left_sum==right_sum:
            return array[i]
    return -1
print (find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]))
print (find_fulcrum([9, 1, 9]))
print (find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))

print(find_fulcrum([8, 8, 8, 8]))