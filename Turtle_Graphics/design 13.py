import turtle as t 
import colorsys
t.bgcolor("black")
t.tracer(20)
t.pensize(3)
h=0.1
for i in range(280):
    c=colorsys.hsv_to_rgb(h,1,1)
    h +=000.1
    t.pencolor(c)
    t.left(120)
    t.circle(i-90,180)
    t.left(120)
t.done()