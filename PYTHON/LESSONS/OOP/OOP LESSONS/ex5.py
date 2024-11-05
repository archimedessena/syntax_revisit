# Draw four different rectangle  with different colors

from random import randint
from turtle import * 


draw = Turtle()

for i in range(4):
    r = randint(0,255)
    b = randint(0,255)
    g = randint(0,255)
    color_ = (r/255, b/255, g/255)
    
    x = randint(-200, 200)
    y = randint(-200, 200)
    
    draw.up()
    draw.goto(x,y)
    draw.down()
    
    
    draw.color(color_)
    draw.begin_fill()
    for i in range(4):
        draw.fd(100)
        draw.rt(90)
    draw.end_fill()
    

done()