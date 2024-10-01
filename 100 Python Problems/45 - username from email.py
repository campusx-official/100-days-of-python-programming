# Extract the username from a given email.
# For example, if the email is saurabh@gmail.com, then the username should be saurabh.

email = input('Enter your email: ')
username, domain = email.split('@')
print(username)