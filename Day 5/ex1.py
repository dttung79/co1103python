# Write a guess number game
# Computer generates a random number between 1 and 10
# User guesses the number
# If the user guesses the correct number, print "You win!" and stop the game
# If the user's number is greater than computer's number , print "Too high!"
# If the user's number is less than the computer's number, print "Too low!"

import random as rd

comp_number = rd.randint(1, 10)
user_number = 0
count = 0
while user_number != comp_number:
    user_number = int(input('Enter a guess:'))
    count += 1
    # if the user guesses the correct number, print "You win!" and stop the game
    if user_number == comp_number:
        print('You win!')
    elif user_number > comp_number:
        print('Too high!')
    else:
        print('Too low!')
    if count > 5:
        print('Too many tries! You lose!')
        break