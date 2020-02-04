import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	tur.setheading(0)
	tur.pendown()
	tur.back(40)
	tur.left(270)
	tur.forward(25)
	tur.left(90)
	tur.forward(25)
	tur.back(25)
	tur.left(270)
	tur.forward(25)
	tur.left(90)
	tur.forward(40)
	tur.penup()
	tur.forward(10)
	tur.pendown()
    elif letter == "F":
	    pass
    elif letter == "G":
	tur.setheading(0)
	tur.pendown()
	tur.left(90)
	tur.forward(20)
	tur.left(90)
	tur.forward(20)
	tur.back(20)
	tur.left(90)
	tur.forward(20)
	tur.right(90)
	tur.forward(20)
	tur.right(45)
	tur.forward(30)
	tur.right(45)
	tur.forward(20)
	tur.right(45)
	tur.forward(20)
	tur.right(45)
	tur.forward(25)
	tur.penup()
	tur.forward(10)		
    elif letter == "H":
	    pass
    elif letter == "I":
	tur.setheading(0)
	tur.pendown()
	tur.left(90)
	tur.forward(50)
	tur.right(90)
	tur.penup()
	tur.forward(10)
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	tur.setheading(0)
	tur.left(90)
	tur.forward(50)
	tur.back(50)
	tur.right(90)
	tur.forward(40)
	tur.penup()
	tur.forward(10)
    elif letter == "M":
	    pass
    elif letter == "N":
	tur.setheading(0)
	tur.pendown()
	tur.right(90)
	tur.forward(50)
	tur.back(50)
	tur.left(30)
	tur.forward(60)
	tur.left(150)
	tur.forward(53)
	tur.back(53)
	tur.right(90)
	tur.penup()
	tur.forward(50)
    elif letter == "O":
	tur.setheading(0)
	tur.circle(25)
	tur.penup()
	tur.left(180)
	tur.forward(25)
	tur.left(90)
	tur.forward(10)
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	tur.setheading(0)
	tur.pendown()
	tur.forward(40)
	tur.back(20)
	tur.right(90)
	tur.forward(50)
	tur.left(90)
	tur.penup()
	tur.forward(70)
	tur.left(90)
	tur.forward(25)
	tur.pendown()
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	tur.setheading(0)
	tur.right(90)
	tur.forward(50)
	tur.left(150)
	tur.forward(40)
	tur.right(120)
	tur.forward(40)
	tur.left(150)
	tur.forward(50)
	tur.penup()
	tur.right(90)
	tur.forward(50)
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
