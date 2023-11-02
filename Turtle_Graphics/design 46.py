import turtle as t
t.bgcolor("black")
t.speed(15)
color = ["green","yellow","blue","cyan"]
c = 0
for i in range(100):
    t.forward(i*7)
    t.right(144)
    t.color(color[c])
    if c==3:
        c = 0
    else:
        c += 1
t.done()