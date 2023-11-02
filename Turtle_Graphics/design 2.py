import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
h=0
t.pensize(10)
for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=0.005
    t.pencolor(c)
    t.circle(i,90)
    t.rt(30)
    t.circle(i,-90)
    t.circle(-i,-90 )
t.done()