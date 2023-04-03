from random import randint


def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()

n = int(input('Enter n: '))

numbers = []
if n < 1 or n > 10:
    print('Invalid n')
else:
    for i in range(11):
        numbers.append(n * i)
    print_list(numbers, 'Numbers')
