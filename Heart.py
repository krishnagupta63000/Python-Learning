import turtle
import math

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
t = turtle.Turtle()
turtle.tracer(0)

t.speed(0)
t.hideturtle()
t.penup()
t.color("#ffb6c1")

for scale in range(11,17):
    for i in range(120):
        angle = i * (math.pi*2)/120
        x = 16 * (math.sin(angle)**3) * scale
        y = (13 * math.cos(angle)-5 * math.cos(2*angle)-2 * math.cos(3*angle)- math.cos(4*angle)) * scale

        t.goto(x,y)
        t.write("My Name is Krishna", align="centre", font=("Areal", 8, "bold"))
        turtle.update()
        turtle.done()