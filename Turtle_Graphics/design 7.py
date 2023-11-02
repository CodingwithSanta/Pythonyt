from turtle import*
bgcolor('black')
pensize(5) 
for i in range(120):
    color('silver')
    speed(200)
    h=0
    fd(i*2)
    lt(200)
    fd(i*2)
    rt(100)
    
    for i in range(2):
        rt(60)
done()