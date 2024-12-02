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
try:
    x = int(input('Enter the number: '))
    print(convert_to_binary(x))
except ValueError:
    print("Invalid input! Please enter an integer.")
    


## examples
## 2147483647 ➞ 2147483648

## 1 ➞ 4294967294

## 4 ➞ 4294967291






###return flipping_bit

###print(convert_to_binary(2147483647))

