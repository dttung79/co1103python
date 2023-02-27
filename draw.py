# Write a program that asks the user to draw a shape
# Ask for size of the shape (must be greater than 0)
# Ask for color of the edge (must be one of the following: red, green, blue)
# Ask for the type of the shape (must be square, rectangle, triangle)
# then draw the shape

import turtle as t

size = int(input("Enter the size of the shape: "))
color = input("Enter the color of the shape (red/green/blue): ")
shape = input("Enter the type of the shape (square/rectangle/triangle): ")

if size <= 0:
    print("Size must be greater than 0")
    exit()
elif color not in ["red", "green", "blue"]:
    print("Color must be red, green or blue")
    exit()
elif shape not in ["square", "rectangle", "triangle"]:
    print("Shape must be square, rectangle or triangle")
    exit()

t.color(color)
if shape == "square":
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
elif shape == "rectangle":
    t.forward(size)
    t.left(90)
    t.forward(size * 2)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size * 2)
else:
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)

t.exitonclick()