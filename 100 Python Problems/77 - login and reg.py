# Write a dummy program that can perform login and registration using a menu-driven approach.

database = {}

def user_menu():
    user_input = input('''
    1. Enter 1 to Register
    2. Enter 2 to Login
    3. Enter 3 to Exit
    ''')
    
    if user_input == '1':
        register()
    elif user_input == '2':
        login()
    else:
        print('Bye')

def register():
    name = input('Enter your name: ')
    email = input('Enter your email id: ')
    password = input('Enter your password: ')
    
    database[email] = [name, password]
    
    print('Registration successful')
    print()
    
    user_menu()

def login():
    email = input('Enter your email id: ')
    password = input('Enter your password: ')
    
    flag = 0
    
    for i in database:
        if email == i:
            flag = 1
            if password == database[i][1]:
                print('Welcome')
            else:
                print('Incorrect credential')
    
    if flag == 0:
        print('Email not found')

user_menu()