import turtle as t 
import colorsys
t.bgcolor("black")
t.tracer(100)
t.pensize(1)
t.speed(0)
def draw():
    t.up()
    t.goto(9,0)
    t.down()
    h = 0
    n =  78
    for i in range(460):
       c = colorsys.hsv_to_rgb(h,1,1)
       t.color(c)
       h += 1/n
       t.fillcolor("black")
       t.begin_fill()
       t.rt(56)
       t.fd(i)
       t.circle(-24)
       t.end_fill()
       t.circle(23,5.1)
draw()
t.done()        
        