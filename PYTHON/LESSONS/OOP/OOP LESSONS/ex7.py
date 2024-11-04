# Draw different circles with different sizes using turtle module.

from turtle import * 
from random import *

draw = Turtle()  

for i in range(10):
    radius = randint(5, 100)
    x = randint(-200, 200)
    y = randint(-200, 200)  
    
    
    draw.up()
    draw.goto(x,y)
    draw.down()
    
    draw.circle(radius)

done()