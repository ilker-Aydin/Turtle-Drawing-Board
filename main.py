import turtle

drawing_board = turtle.Screen()

drawing_board.bgcolor("light blue")
drawing_board.title("iko drawing")

turtle_instance= turtle.Turtle()
drawing_board.listen()

def angle_right():
    turtle_instance.right(10)

def turtle_forward():
    turtle_instance.forward(100)
def angle_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_comeBackHome():
    turtle_instance.home()
def turtle_penUp():
    turtle_instance.penup()
def turtle_penDown():
    turtle_instance.pendown()

def changeColorBlue():
    turtle_instance.color("blue")
def changeColorRed():
    turtle_instance.color("red")


drawing_board.onkey(turtle_forward,"space")
drawing_board.onkey(fun=angle_right,key="Down")
drawing_board.onkey(fun=angle_left,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_comeBackHome,key="h")
drawing_board.onkey(turtle_penUp,"u")
drawing_board.onkey(turtle_penDown,"d")
drawing_board.onkey(changeColorBlue,"b")
drawing_board.onkey(changeColorRed,"r")



turtle.mainloop()