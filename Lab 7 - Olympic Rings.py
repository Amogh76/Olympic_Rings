import turtle
from draw_USA_flag import draw_USA_flag
import print_me_first

turtle.bgpic("usa.png")
#Name: draw_USA_flag
#draws flag
#@param none
#@return none
draw_USA_flag()
turtle.penup()
turtle.goto(0, 200)
turtle.pencolor ("blue")
turtle.write("USA OLYMPIC TEAM", align="center", font=("Helvetica", 60, "bold"))
turtle.pensize(8)

RADIUS = 75
STARTING_POINT_X = -200
STARTING_POINT_Y = -300
HSHIFT = 95
VSHIFT = 85

def draw_circlexy(x,y,color):
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(RADIUS)

def draw_circle():
    x = STARTING_POINT_X
    y = STARTING_POINT_Y
    #Name: draw_circlexy
    #takes the initial input to draw the circle
    #@param x,y,color
    #@return none   
    draw_circlexy(x,y,"blue")
    x += HSHIFT
    y -= VSHIFT
    draw_circlexy(x,y,"orange")
    x += HSHIFT
    y += VSHIFT
    draw_circlexy(x,y,"black")
    x += HSHIFT
    y -= VSHIFT
    draw_circlexy(x,y,"green")
    x += HSHIFT
    y += VSHIFT
    draw_circlexy(x,y,"red")

#Name: draw_circle
#takes the initial input to draw the circle
#@param none
#@return olympic rings
draw_circle()
#Name: print_info
#prints name, lab and time
#@param none
#@return none
print_me_first.print_info()
turtle.hideturtle ()


    
