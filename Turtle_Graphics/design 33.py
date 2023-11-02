import turtle as t
import colorsys
t.bgcolor("black")
t.pen()
t.speed(0)
h = 0.4
t.goto(-60,0)
for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    t.begin_fill()
    t.circle(50,120)
    t.forward(i)
    t.left(170)
    t.forward(i)
    t.end_fill()
    h += 0.005
t.done()