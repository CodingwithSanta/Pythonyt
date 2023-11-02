import turtle as t
import colorsys

t.tracer(27)
t.bgcolor('black')
def programming_puzzles(): 
    h=67
    n=298
    for i in range(240):
          c=colorsys.hsv_to_rgb(h,1,1)
          h+=1/n
          t.pensize(7)
          t.pencolor(c)
          t.fillcolor('black')
          t.begin_fill()
          t.circle(i,180,steps=3)
          t.rt(92 )
          t.fd(i)
programming_puzzles()

t.done()