import turtle as t

size = int(input('Enter size of the shape: '))
n = int(input('Enter number of sides: '))

for i in range(n):
    t.forward(size)
    t.left(360/n)


t.exitonclick()