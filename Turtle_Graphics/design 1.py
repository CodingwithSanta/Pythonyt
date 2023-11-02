import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
def draw():
    h=27
    n=228
    for i in range (1300):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=1/n
        t.pencolor(c)
        t.pensize(8)
        t.fillcolor('black')
        t.begin_fill()
        t.circle(100,steps=5)
        t.fd(78)
        t.rt(280)
        
        t.fd(i)
        t.end_fill()
draw( )
t.done( )