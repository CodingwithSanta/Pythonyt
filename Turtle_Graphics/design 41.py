from turtle import *
import colorsys
tracer(300)
bgcolor("black")
def draw():
    h = 0
    j = 59
    for i in range(600):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 1/j
        color(c)
        pensize(1)
        up()
        goto(0,0)
        down()
        fd(i)
        lt(89)
        fd(23)
        circle(i,24)
        bk(65)
        circle(i,295)
        rt(58)
draw()
done()        