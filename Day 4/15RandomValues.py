from random import randint


min_str = input("Min: ")
max_str = input("Max: ")
minimum = int(min_str)
maximum = int(max_str)
random1 = randint(minimum, maximum)
random2 = randint(minimum, maximum)
random3 = randint(minimum, maximum)
random4 = randint(minimum, maximum)
random5 = randint(minimum, maximum)

print(f"{random1} {random2} {random3} {random4} {random5}")

print()
input("Press return to continue ...")
