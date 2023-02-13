

import turtle

# set up window
window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Draw a Cat")

# create turtle
cat = turtle.Turtle()
cat.shape("turtle")
cat.color("black")
cat.speed(7)

# draw cat
cat.penup()
cat.goto(100, 0)
cat.pendown()

# ears
cat.right(90)
cat.forward(50)
cat.left(90)
cat.forward(20)
cat.left(90)
cat.forward(20)
cat.right(90)
cat.forward(20)
cat.right(90)
cat.forward(20)
cat.left(90)
cat.forward(50)

# face
cat.left(90)
cat.forward(50)
cat.left(90)
cat.forward(20)
cat.left(90)
cat.forward(30)
cat.right(90)
cat.forward(20)
cat.right(90)
cat.forward(30)
cat.left(90)
cat.forward(20)

# eyes
cat.penup()
cat.left(90)
cat.forward(15)
cat.right(90)
cat.forward(10)
cat.pendown()
cat.dot(10, "blue")

cat.penup()
cat.forward(20)
cat.pendown()
cat.dot(10, "blue")

# nose
cat.penup()
cat.left(90)
cat.forward(20)
cat.right(90)
cat.forward(5)
cat.pendown()
cat.dot(5, "orange")

# mouth
cat.penup()
cat.right(90)
cat.forward(10)
cat.left(90)
cat.pendown()
cat.forward(20)

window.exitonclick()