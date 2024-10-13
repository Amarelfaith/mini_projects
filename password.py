# Create a program that check wether the password given by the user matched with the stored password
# if the user inputted incorrect password then you should ask him to try again untill he put the correct password
# print access granted when the user password matched our system password

password = input('Enter your password: ')
stored_password = 'abu123'

while password != stored_password:
    print('Try again!')
    password = input('Enter your password: ')
print()
print('Access granted!')