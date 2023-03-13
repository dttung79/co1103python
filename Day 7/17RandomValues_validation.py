from random import randint

# Function with default values
def random(minimum=1, maximum=100):
    return randint(minimum, maximum)

random1 = random(100, 200)
random2 = random(95)
random3 = random()
random4 = random()
print(f"{random1} {random2} {random3} {random4}")


print()
input("Press return to continue ...")