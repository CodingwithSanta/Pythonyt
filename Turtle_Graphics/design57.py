import turtle as t
t.bgcolor('black')
t.speed(0)
t.pensize(3)
t.pencolor('red')
def drawcircle(radius):
    for i in range(10 ):
        t.circle(radius)
        radius=radius-10
def drawdes():
     for i in range(10):
         drawcircle(150)
         t.right(36)
drawdes()
t.done()