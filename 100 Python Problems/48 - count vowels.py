# Count the number of vowels in a string provided by the user.

a = input('Enter your string: ')

vowels = 'aeiou'
count = 0

for i in a:
    if i in vowels:
        count = count + 1

print(count)