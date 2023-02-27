import turtle as t

size = int(input('Enter size of the shape: '))

for i in range(3):
    t.forward(size)
    t.left(120)

t.exitonclick()

# Ex: Draw a square

# Ex: Draw an equal polygon with n sides