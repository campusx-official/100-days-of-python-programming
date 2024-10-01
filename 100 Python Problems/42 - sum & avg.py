# Write a program that continues to accept a number from the user until the user enters zero.
# Display the sum and average of all the numbers.

num = int(input('Enter your number: '))

add = 0
avg = 0
count = 0

while True:
    if num != 0:
        add = add + num
        count = count + 1
        avg = add / count
        num = int(input('Another number please: '))
    else:
        print('Thank you')
        break

print('Your sum is:', add)
print('Your average is:', avg)