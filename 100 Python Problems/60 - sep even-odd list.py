# Create two lists from a given list where the first list will contain all the odd numbers from the original list, and the second one will contain all the even numbers.

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

L_even = []
L_odd = []

for i in L:
    if i % 2 == 0:
        L_even.append(i)
    else:
        L_odd.append(i)

print('List of even values:', L_even)
print('List of odd values:', L_odd)