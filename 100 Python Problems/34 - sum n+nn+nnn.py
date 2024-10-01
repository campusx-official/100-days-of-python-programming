# Write a program that accepts an integer (n) and computes the value of n + nn + nnn.

# n + nn + nnn ---> (2 + 22 + 222)

n = input('Enter your number: ')
print('n is:', n)

nn = n + n
print('nn is:', nn)

nnn = n + n + n
print('nnn is:', nnn)

c = int(n) + int(nn) + int(nnn)
print(c)