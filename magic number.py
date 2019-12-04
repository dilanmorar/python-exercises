# Magic number game
# prompt the user for input
# generate a random number using a python library (should be between 1-10)
# check the the number against a magic number
# let the user know if he/she won or
# if the guess was above or under
# Make it so you keep playing until we say: 'No more Magic'

import random
magic_number = random.randint(0,10)

number = int(input('Choose a number between 0-10: '))
counter = 0

while number != magic_number:
    print('You lost')
    counter += 1
    print('Number of guesses:',counter)
    if number < magic_number:
        print('You guessed too low')
    else:
        print('You guessed too high')
    number = int(input('Try again, pick a number between 0-10: '))
    magic_number = random.randint(0, 10)

if number == magic_number:
    print('You won!')
    print('No more magic')