import turtle as t
from time import sleep
t.bgcolor("black")
t =[Turtle(), Turtle()]
x = 6
colors = [ "red", "yellow","blue" , "lime","green" ,"violet"]
for index, i in enumerate(t):
    t.speed(0)
    t.color("white")
    t.shape("circle")
    t.shapesize(0.3)
    t.width(3)
    t.pu()
    t.seth(90)
    t.fd(350)
    t.seth(-180)
    t.pd()
    t[0].pu()

t.delay(0)
t.speed(0)
t.pensize(2)
t.ht()
t.sleep(4)
for i in colors:
    color(i)
    for i in range(360):
        t[0].fd(x)
        t[0].lt(1)
        t.pu()
        goto(t[0].pos())
        t.pd()
        t[1].fd(2 *x)
        t[1].lt(2)
        goto(t[1].pos())
t.done()