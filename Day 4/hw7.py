import random as rd

name = input('What is your name? ')
birth_year = int(input('What year were you born? '))
#year_70after = birth_year + 70

lucky_year = rd.randint(birth_year, birth_year + 70)
years_old = lucky_year - birth_year
print(f'Hello {name}, your lucky year is {lucky_year}')
print(f'You will be {years_old} years old in {lucky_year}')