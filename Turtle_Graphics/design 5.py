import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
h=.3
t.pensize(5)
t.speed(100)
def draw(angle,n):
          t.circle(30+n,90)
          t.left(angle)
          t.circle(30+n,90)
t.goto(50,0)
for i in range(110):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h += 0.08
    t.pencolor(c)
    draw(60,i)
    draw(90,i)
    draw(120,i)
    draw(180,i)
t.done() 