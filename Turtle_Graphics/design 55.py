import turtle as t
t.bgcolor("black")
t.speed(5)
t.begin_fill()
t.fillcolor("#1DB954")
t.pencolor("#1DB954")
t.pensize(2)
t.circle(100)
t.end_fill()
t.penup()
t.goto(40,50)
t.pendown()
t.left(150)
t.forward(0)
t.pensize(16)
t.pencolor("black")
t.circle(80,60)
t.penup()
t.goto(50,85)
t.pendown()
t.pensize(16)
t.right(60)
t.forward(0)
t.circle(100,60)
t.penup()
t.goto(60,120)
t.pendown()
t.pensize(20)
t.right(60)
t.forward(0)
t.circle(120,60)
t.penup()
t.goto(130,55)
t.pendown()
t.goto(-90,-100)
t.down()
t.pencolor("#1DB954")
t.write("Spotify", font = ("ariel",15,"bold"))
t.hideturtle()
t.done()   
