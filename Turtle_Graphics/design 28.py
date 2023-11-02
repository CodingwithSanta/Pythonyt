import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(50)
h = 0.0
t.pensize(1)
for i in range(500):
     c = colorsys.hsv_to_rgb(h,1,1)
     h += 0.005
     t.pencolor(c)
     for j in range(2):
         t.fd(i)
         t.rt(120)
         t.fd(100)
         t.rt(120)
     t.rt(60*2+1)
t.done()
     