# Write a program that can convert a 2D list to a 1D list.

L = [1, 2, 3, 4, [5, 7, 8]]

rev = []

for i in L:
    if type(i) == list:
        rev.extend(i)
    else:
        rev.append(i)
print(rev)