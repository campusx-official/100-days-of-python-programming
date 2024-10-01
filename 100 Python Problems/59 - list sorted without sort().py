# Write a program to check whether a list is in ascending order or not.

L = [2, 3, 1, 6, 0]
flag = 0

for i in range(0, len(L)-1):
    if L[i] >= L[i+1]:
        flag = 1
        break

if flag == 0:
    print('Sorted')
else:
    print('Not sorted')