import turtle
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("white")
t.color("white")
t.up()
t.goto(-80,50)
t.down()
t.fillcolor("black")
t.begin_fill()
t.forward(200)
t.setheading(270)
s = 360
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)


t.forword(180)
s = 270
for i in range(9):
    s = s - 10
    t.sethrading(s)
    t.forword(10)

t.forword(200)              
s = 180
for i in range(9):
    s = s - 10
    t.sethading(s)
    t.forword(10)
    
t.forword(180)
s = 90
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forword(10)
t.forword(30)
t.end_fill()
t.up()
t.color("black")
t.setheading(270)
t.forword(240)
t.setheading(0)               
t.down()
t.color("red")
t.fillcolor("#E50914")
t.begin_fill()
t.forword(30)
t.setheading(90)
t.forword(180)
t.setheading(180)
t.forword(30)
t.setheading(270)
t.forword(180)
t.end_fill()
t.setheading(0)
t.up()
t.forword(75)
t.down()
t.color("red")
t.fillcolor("#E50914")
t.begin_fill()
t.forword(30)
t.setheading(90)
t.forword(180)
t.setheading(180)
t.forword(30)
t.setheading(270)
t.forword(180)
t.end_fill()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.setheading(113)
t.forword(195)
t.setheading(0)
t.forword(31)
t.setheading(293)
t.forword(196)
t.end_fill()
t.hideturtle()
turtle.done()