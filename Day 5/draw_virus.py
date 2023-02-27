import turtle as t
import random as rd

# draw a virus
n = int(input('Enter number of sides: '))
t.pensize(3)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'gray']
for i in range(n):
    t.color(rd.choice(colors))
    m = rd.randint(10, 200)
    t.forward(m)
    t.left(360/n)
    t.goto(0, 0)

t.exitonclick()