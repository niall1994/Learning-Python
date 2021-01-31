#challenge 60
import turtle

for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

#Challenge 61
for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)

#challenge 62
for i in range(0,360):
    turtle.forward(0.5)
    turtle.right(0.5)

#Challenge 63
for j in range(0,3):
    turtle.penup()
    if j != 0:
        turtle.forward(110)
    turtle.pendown()
    turtle.color("black","red")
    turtle.begin_fill()
    for i in range(0,4):
       turtle.forward(100)
       turtle.right(90)
    turtle.end_fill()

#Challenge 64
turtle.color("black","yellow")
turtle.begin_fill()
for i in range(0,5):

    if i == 0:
        turtle.left(72)
    else:
        turtle.right(144)    

    turtle.forward(100)

turtle.end_fill()

#challenge 65

turtle.forward(100)
turtle.right(90)

turtle.penup()
turtle.forward(15)
turtle.pendown()

turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.forward(15)
turtle.pendown()

turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.right(180)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)

#Challenge 66
turtle.clear()
degrees = 360. / 8.
colors = ("black","green","blue","red","purple","pink")
import random

for i in range(0,8):
    col = random.choice(colors)
    turtle.pencolor(col)
    turtle.forward(100)
    turtle.right(degrees)

#challenge 67
turtle.clear()
for j in range(0,12):
    turtle.right(30)
    for i in range(0,8):
        col = random.choice(colors)
        turtle.pencolor(col)
        turtle.forward(100)
        turtle.right(degrees)

#Challenge 68

turtle.clear()

line_num = random.randint(0,20)
degrees = 360 / line_num
line_length = random.randint(50,100)
turtle.color("black",random.choice(colors))
turtle.begin_fill()
for i in range(0,line_num):
    turtle.forward(line_length)
    turtle.right(degrees)
turtle.end_fill()









