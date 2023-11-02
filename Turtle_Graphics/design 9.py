import turtle as t
import colorsys
t.bgcolor('black' )
t.tracer (100)
t.pensize (1)
h=0
for i in range (400):
         t.speed(200)
         c = colorsys .hsv_to_rgb(h, 0.8, 1)
         t.pencolor (c)
         h += 0.006

         t.right(119)
         t.circle( -i*0.3,120)
         t.circle(i*0.3, 120)
         t.circle(-i*0.3,90)
         t.circle(i*0.3,90)