import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(50)
h = 0.0001
n = 220
for i in range(800):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    t.up()
    t.goto(-8,25)
    t.down()
    t.color("black")
    t.pensize(1)
    t.bk(90)
    t.lt(18)
    t.rt(9)
    t.fd(i)
    t.fillcolor(c)
    t.begin_fill()
    t.circle(i,80,steps=2)
    t.end_fill()
t.done()