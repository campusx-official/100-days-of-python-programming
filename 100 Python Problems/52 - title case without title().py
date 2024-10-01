# Write a program to convert a string to title case without using the title() function.

a = 'hEllO sAuRABh SinGH dHaMI'
y = a.split()
print(y)

r = ''
for i in y:
    r = r + i[0].upper() + i[1:].lower() + ' '
print(r)