import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(10)
t.pensize(10)
h = 0
for i in range(600):
     c = colorsys.hsv_to_rgb(h,1,1)
     h += 0.005
     t.color(c)
     t.up()
     t.goto(0,0)
     t.fd(i)
     t.down()
     t.circle(i/3,20)
     t.lt(45)
t.done()