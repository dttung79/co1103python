import random as rd

def my_max(numbers):
    curr_max = numbers[0]
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] > curr_max:
            curr_max = numbers[i]
    
    return curr_max

def my_sum(numbers):
    s = 0
    n = len(numbers)
    for i in range(n):
        s = s + numbers[i]
    
    return s

def my_min(numbers):
    curr_min = numbers[0]
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] < curr_min:
            curr_min = numbers[i]
    
    return curr_min

def search(numbers, x):
    found = False
    n = len(numbers)
    for i in range(n):
        if x == numbers[i]:
            found = True # switch the flag
    return found

def search_pos(numbers, x):
    found_pos = None
    n = len(numbers)
    for i in range(n):
        if x == numbers[i]:
            found_pos = i
            break
    return found_pos

def print_menu():
    print("1. Find the max")
    print("2. Find the min")
    print("3. Calculate the sum")
    print("4. Search existance")
    print("5. Search position")
    print("6. Exit")

## main program
numbers = [rd.randint(1, 100) for i in range(20)]
print(numbers)
while True:
    print_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f'The max is {my_max(numbers)}')
    elif choice == 2:
        print(f'The min is {my_min(numbers)}')
    elif choice == 3:
        print(f'The sum is {my_sum(numbers)}')
    elif choice == 4:
        x = int(input('Enter the number to search: '))
        if search(numbers, x) == True:
            print(f'{x} is in the list')
        else:
            print(f'{x} is not in the list')
    elif choice == 5:
        x = int(input('Enter the number to search: '))
        pos = search_pos(numbers, x)
        if pos == None:
            print(f'{x} is not in the list')
        else:
            print(f'{x} is in the list at position {pos}')
    elif choice == 6:
        print('Bye!')
        break