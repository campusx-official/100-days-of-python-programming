# Write a program to merge two given dictionaries.

D1 = {'a': 2, 'b': 3}
D2 = {'c': 4, 'd': 5}

D = {}

for i in D1:
    D[i] = D1[i]
for k in D2:
    D[k] = D2[k]

print(D)