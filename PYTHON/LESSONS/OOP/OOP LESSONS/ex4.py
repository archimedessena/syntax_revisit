# Using turtle module to draw a hexagon with different colors

from turtle import * # import module 

# create an object 
draw = Turtle() 

# create colors
colors = ["red", "black", "green", "lime green", "yellow", "pink"]

for col in range(6):
    draw.color(colors[col])
    draw.width(5)
    draw.fd(100)
    draw.rt(60)
    
    

done()