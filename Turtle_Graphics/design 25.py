import turtle as t
import math
import colorsys
t.bgcolor("black")
t.speed(0)
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
n = 0
scale = 18
h = 0.6
def draw_flower(n,cl):
    angle = n * 3.7
    r = scale * math.sqrt(n)
    pos_x = r * math.sin(angle)
    pos_y = r * math.cos(angle)
    t.fillcolor(cl)
    go(pos_x,pos_y)
    t.begin_fill()
    t.circle(15)
    t.end_fill()
for i in range(400):
    c = colorsys.hsv_to_rgb(h,1,1)
    draw_flower(i,c)
    h += 0.005
t.done()