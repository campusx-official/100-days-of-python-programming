# Write a program that calculates the in-hand salary after deducting HRA (10%), DA (5%), PF (3%), and tax.
# If the salary is between 5-10 lakh, apply a 10% tax;
# for salaries between 11-20 lakh, apply a 20% tax;
# for salaries above 20 lakh, apply a 30% tax.
# If the salary is between 0-1 lakh, print 'k'.

user_input = float(input('Enter your annual salary: '))

if user_input > 500000 and user_input < 1000000:
    tax = (10/100) * user_input
    temp_salary = user_input - tax
elif user_input > 1000000 and user_input < 2000000:
    tax = (20/100) * user_input
    temp_salary = user_input - tax
else:
    tax = (30/100) * user_input
    temp_salary = user_input - tax
    
print('After salary reduction:', temp_salary)

hra = (10/100) * temp_salary
da = (5/100) * temp_salary
pf = (3/100) * temp_salary

inhand_salary = (temp_salary - hra - da - pf) / 12
print('Inhand salary is:', inhand_salary)

if inhand_salary <= 999:
    print(inhand_salary)
elif inhand_salary >= 1000 and inhand_salary <= 9999:
    print(inhand_salary / 1000, 'k')
elif inhand_salary >= 100000 and inhand_salary <= 9999999:
    print(inhand_salary / 1000000, 'l')
else:
    print(inhand_salary / 10000000, 'Cr')