from turtle import *
tracer(0)
k = 100
screensize(5000,5000)
left(90)

down()
right(45)
for i in range(7):
    forward(6*k)
    right(45)
    forward(12*k)
    right(135)

up()
for x in range(0,20):
    for y in range(0,20):
        goto(x*k,y*k)
        dot(10)
goto(0,0)
dot(15,'red')
done()
