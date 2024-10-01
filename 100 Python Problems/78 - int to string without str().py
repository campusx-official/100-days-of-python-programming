# Write a program that can convert an integer to a string without using str().

def convert(number):
    digits = '0123456789'
    result = ''
    
    while number != 0:
        current_num = number % 10
        result = digits[current_num] + result
        number = number // 10
        
    return result

print(type(convert(23)))

# number = 234
# currect_num = 4
# result = 4

# number = 23
# current_num = 3

# result = 3 + 4 = 34

# number = 2