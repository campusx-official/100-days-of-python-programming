# Write a function that accepts a number and returns its factorial.
# You cannot use any loops.

def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number-1)

result = fact(3)
print(result)