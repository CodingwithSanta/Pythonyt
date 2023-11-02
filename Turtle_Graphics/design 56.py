from turtle import *
import colorsys
bgcolor("black")
tracer(50)
h = 0
pensize(5)
for i in range(600):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    forward(i)
    left(19)
    backward(i*0.5)
    circle(i*0.1,180)
    h += 0.008
    end_fill()
done()