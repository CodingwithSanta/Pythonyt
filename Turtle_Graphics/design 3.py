import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(78)
t.pensize(2)

h=0.001
n=889
for i in range(700):
    
    h+=1/n
    t.up() 
    t.goto(-8,25)
    t.down()
    t.pencolor('brown')
    t.fd(i)
    t.rt(850)
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(16,300)  
    t.end_fill()
    t.speed(70)
    t.lt(180)
    t.bk(i)
    t.fd(i)
    t.rt(6)
    
t.done()        