# Create a program that check wether the password given by the user matched with the stored password
# if the user inputted incorrect password then you should ask him to try again untill he put the correct password
# print access granted when the user password matched our system password
# the user should not have more 5 chances to input his password


password = input('Enter your password: ')
stored_password = 'abu123'
counter = 5

while password != stored_password and counter > 1:
    print('Try again!')
    password = input('Enter your password: ')
    counter -= 1

print()
if password == stored_password:
    print('Access granted!')
else:
    print('Forgot password')
