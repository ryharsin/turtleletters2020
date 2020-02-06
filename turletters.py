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
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	tur.penup()
	tur.setpos(-35,-40)
	tur.right(270)
	tur.pendown()
	tur.forward(40)
	tur.right(135)
	tur.forward(28)
	tur.left(100)
	tur.forward(28)
	tur.right(145)
	tur.forward(40)
	tur.clear()
	tur.penup()
	
	
    elif letter == "N":
	tur.penup()
	tur.setpos(-35,-40)
	tur.left(180)
	tur.pendown()
	tur.forward(40)
	tur.right(150)
	tur.forward(47)
	tur.left(150)
	tur.forward(43)
	tur.clear()

	
    elif letter == "O":
	tur.penup()
	tur.setpos(-35,-15)
	tur.left(180)
	tur.pendown()
	for i in range(20):
    		tur.forward(8)
    		tur.left(18)
	tur.clear()

	
    elif letter == "P":
	tur.penup()
	tur.setpos(-35,-40)
	tur.right(90)
	tur.pendown()
	tur.forward(40)
	tur.right(90)
	for i in range(12):
    		tur.forward(3)
    		tur.right(16)
	tur.clear()
	
	
    elif letter == "Q":
	tur.penup()
	tur.setpos(-35,-40)
	tur.right(175)
	tur.pendown()
	for i in range(23):
    		tur.forward(8)
    		tur.left(18)
	tur.penup()
	tur.left(90)
	tur.forward(15)
	tur.right(180)
	tur.pendown()
	tur.forward(30)
	tur.clear()

    elif letter == "R":
	tur.penup()
	tur.setpos(-35,-40)
	tur.left(135)
	tur.pendown()
	tur.forward(40)
	tur.right(90)
	for i in range(12):
    		tur.forward(3)
    		tur.right(16)
	tur.right(215)
	tur.forward(30)
	tur.clear()
	
	
    elif letter == "S":
	tur.penup()
	tur.setpos(0,10)
	tur.right(190)
	tur.pendown()
	for i in range(11):
    		tur.forward(6)
    		tur.left(20)
	for i in range(13):
		tur.forward(6)
    		tur.right(19)

    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
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
