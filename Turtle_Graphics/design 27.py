import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(10000000)
h = 0
for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.008
    t.color(c)
    t.up()
    t.goto(-300,20)
    t.down()
    t.lt(180)
    t.fd(150)
    t.write("Turtle", font=("verdana" ,10 , "italic"))
    t.lt(2)
    t.write("pyhon", font=("verdana" , 80 , "italic"))
    t.done()