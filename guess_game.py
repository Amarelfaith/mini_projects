# This program uses the random module to generate a random integer between 1 and 5
# The player have 3 chances to guess the win

import random
guess = int(input('Guess the number between 1 and 5: '))
random_number = random.randint(1, 5)
count = 3
while guess != random_number and count > 1:
    print('Try again!')
    guess = int(input('Guess the number between 1 and 5: '))
    count -= 1
print()
if guess == random_number:
    print(f"Win, the random number is {random_number}")
else:
    print('Loss')