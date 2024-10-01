# Write a program to find the maximum item in a list without using the max function.

L = [2, 3, 5, 6, 8, 9]
max = L[0]

for i in L:
    if i > max:
        max = i
print(max)