import random as rd

user_number = int(input('Enter a number (1-100): '))
comp_number = 0
count = 0
limit = 7
low = 1
high = 100
while user_number != comp_number:
    comp_number = (low + high) // 2
    print('Computer guessed:', comp_number)
    count += 1
    if user_number == comp_number:
        print('Computer wins!')
    elif comp_number > user_number:
        print('Computer guessed too high!')
        high = comp_number - 1
    else:
        print('Computer guessed too low!')
        low = comp_number + 1
    if count > limit:
        print('Too many tries! Computer lost!')
        break