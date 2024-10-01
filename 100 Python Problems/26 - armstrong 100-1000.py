# Print all the Armstrong numbers in the range of 100 to 1000.

for num in range(100, 1000):
    i = num
    a = num % 10
    num = num // 10
    b = num % 10
    c = num // 10
    if (a**3) + (b**3) + (c**3) == i:
        print(i)
    i = i + 1