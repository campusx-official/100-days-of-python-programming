# Write a program that can check whether a given string is a palindrome or not.

a = input('Enter your string: ')

rev = ''

for i in range(len(a) - 1, -1, -1):
    rev = rev + a[i]

print(rev)

if rev == a:
    print('Palindrome')
else:
    print('Not a palindrome')