# Write a program to replace an item with a different item if it is found in the list.

L = [1, 2, 3, 4]

find = int(input('Enter the number you want to replace: '))
replace = int(input('Enter your number: '))

for i in range(0, len(L)):
    if find == L[i]:
        L[i] = replace
        print(L)
        break
else:
    print('Not found')