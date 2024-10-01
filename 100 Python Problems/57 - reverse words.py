# Write a program that can reverse the words of a given string.
# For example, if the input is 'Hello how are you',
# the output should be 'you are how Hello'.

a = input('Enter your string: ')
x = a.split()
rev = []

for i in range(len(x)-1, -1, -1):
    rev.append(x[i])
y = ' '.join(rev)
print(y)