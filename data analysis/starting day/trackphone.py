import turtle
import colorsys

t=turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
h=0

for i in range (360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    t.color(c)
    t.goto(0,0)
    t.fd(150+i/5)
    t.lt(150)
    t.left(120)
    t.fd(150+i/4)

    t.left(100)
    h+=2.004

t.done()    