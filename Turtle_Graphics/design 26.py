import turtle as t
import colorsys
t.bgcolor("black")
t.speed(0)
h = 0.3
t.ht()
for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    t.left(9)
    t.forward(i*0.3)
    t.right(45)
    t.backward(i*0.3)
    t.left(19)
    t.forward(i*0.5)
    h += 0.005
t.done()