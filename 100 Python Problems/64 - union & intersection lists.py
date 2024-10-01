# Write a program that can perform union and intersection on two given lists.

L1 = [1, 2, 3, 4, 5]
L2 = [3, 4, 5, 6, 7]

union = []
intersection = []

# Union
for i in L1:
    if i not in union:
        union.append(i)
for j in L2:
    if j not in union:
        union.append(j)

# Intersection
for i in L1:
    if i in L2:
        intersection.append(i)

print('Your union list:', union)
print('Your intersection list:', intersection)