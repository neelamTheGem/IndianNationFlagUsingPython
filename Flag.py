# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 00:41:52 2021

@author: user
"""
import turtle

sc = turtle.Screen()
sc.bgcolor("Black")
sc.title("Happy Independance Day!! flag using Python|| By NeelamTheGem")


flag = turtle.Turtle()
 
# draws a rectangle given top left position of a rectangle
def draw_filled_rectangle(flag,x,y,width,height,size,color,fill):
  flag.fillcolor(fill)
  flag.pencolor(color)
  flag.pensize(size)
  flag.setheading(0)
 
  flag.begin_fill()
  flag.up()
  flag.goto(x,y)
  flag.down()
  # draw top
  flag.forward(width)
  # draw right
  flag.right(90)
  flag.forward(height)
  # draw bottom
  flag.right(90)
  flag.forward(width)
  # draw left
  flag.right(90)
  flag.forward(height)
  flag.end_fill()


def draw_line():
    for i in range(24):
        flag.penup()
        flag.setpos(20,200)
        flag.pendown()
        flag.forward(35)
        flag.left(15)


draw_filled_rectangle(flag,-100,300,250,70,5,"orange","orange")
draw_filled_rectangle(flag,-100,231,250,70,5,"white","white")


flag.penup()
flag.setpos(52,200)
flag.color("blue")
flag.pendown()
flag.circle(35)

flag.pensize(2)
draw_line()

draw_filled_rectangle(flag,-100,160,250,70,5,"green","green")

flag.penup()
flag.pensize(15)
flag.setpos(-100,315)
flag.pendown()
flag.color("white")
flag.circle(5)

flag.setpos(-105,305)
flag.forward(-520)

draw_filled_rectangle(flag,-220,-220,250,50,5,"#964B00","#C46200")
draw_filled_rectangle(flag,-240,-270,290,70,5,"#964B00","#C46200")

flag.hideturtle()
turtle.done()
