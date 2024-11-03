# Turtle in function form
from turtle import Turtle
def star(t, width, size, color):
    t.color(color)
    t.width(width)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()
    

def circle(t, radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
# Prompt user for input
t = Turtle()    
ask = input("Enter shape")
while ask != "done":
    if ask == "star":
        width = int(input("Enter width:"))
        col = input("Enter a color:")
        size = int(input("Enter a length:"))
    elif ask == "circle":
        radius = int(input("Enter a radius:"))
        col = input("Enter a color:")
        circle(t, radius, col)
    else:
        print("No shape entered")
    ask = input("Enter shape")


#done()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        