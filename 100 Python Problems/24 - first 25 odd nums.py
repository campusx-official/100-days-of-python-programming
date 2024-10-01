# Write a program to print the first 25 odd numbers.

flag = 0

i = 1

while True:
    if i % 2 != 0:
        print(i)
        flag = flag + 1
    if flag == 25:
        break 
    i = i + 1