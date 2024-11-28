def convert_to_binary(number):
    binary_32_bit = format(number, '032b')
    flipping_bit = ''
    for i in binary_32_bit:
        if i=='1':
         flipping_bit += '0'
        else:
         flipping_bit +='1'
    actual_value = int(flipping_bit,2)
    return actual_value
x = int(input('enter the number'))
print(convert_to_binary(x))







###return flipping_bit

###print(convert_to_binary(2147483647))

