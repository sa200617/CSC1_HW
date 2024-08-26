'''
Suhani Aggarwal
'''

def hello():
    print("Welcome to CS1 @ RIT!")
hello()

import turtle

def donut():
    turtle.circle(50)
    turtle.right(90)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)
    turtle.circle(100)

donut()


def draw_plus():
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.down()
    turtle.left(180)
    turtle.forward(100)
    turtle.up()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.down()
    turtle.left(180)
    turtle.forward(100)
    turtle.home()



def draw_asterisk():
    draw_plus()
    turtle.left(45)
    draw_plus()
draw_asterisk()
