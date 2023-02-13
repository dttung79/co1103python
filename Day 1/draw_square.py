import turtle as t

# draw a square of size 100, above is an equilateral triangle of same size
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
# move to the upper left corner
t.penup()
t.left(90)
t.forward(100)
t.right(90)

t.pendown()
# draw an equilateral triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)



# wait for the user to close the window
t.mainloop()