import turtle as t
import colorsys
t.bgcolor("black")
t.pen()
t.speed(0)
t.pensize(1)
h = 0.3
for i in range(600):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    t.forward(i)
    t.left(30)
    t.forward(i)
    t.right(89)
    t.circle(25,180)
    h += 0.005
t.done()