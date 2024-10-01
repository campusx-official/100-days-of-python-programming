# Print the first 25 prime numbers.

counter = 0
num = 2

while counter <= 25:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        counter = counter + 1
    num = num + 1