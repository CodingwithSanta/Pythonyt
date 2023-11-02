import turtle as t
t.bgcolor("black")
t.speed(0)
c=["red","purple","yellow"]
for i in range(500):
    t.pencolor(c[i%3])
    t.forward(i*4)
    t.right(121)
t.hideturtle()
t.done()