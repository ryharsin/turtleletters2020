	
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
	        tur.pd()
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
		tur.setheading(0)
		tur.pd()
		tur.fd(12)
		tur.right(90)
		tur.fd(10)
		tur.pd()
		tur.fd(40)
		tur.left(90)
		tur.circle(10,180)
		tur.left(180)
		tur.circle(10,180)
		tur.pu()
		tur.left(180)
		tur.fd(28)
		tur.left(90)
		tur.fd(10)
		tur.right(90)
		
	    elif letter == "C":
		tur.setheading(0)
		tur.pd()
		tur.fd(25)
		tur.right(90)
		tur.fd(10)
		tur.right(90)
		tur.pd()
		tur.circle(21,200)
		tur.pu()
		tur.fd(9)
		tur.left(70)
		tur.fd(48)
		tur.right(90)
		
	    elif letter == "D":
		tur.setheading(0)
		tur.pd()
		tur.fd(15)
		tur.right(90)
	        tur.fd(10)
	        tur.pd()
	        tur.fd(40)
	        tur.left(90)
		tur.circle(18,235)
		tur.pu()
		tur.right(150)
		tur.fd(25)
		tur.right(90)
		tur.fd(39)

		
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
		tur.setheading(0)
		tur.pd()
		tur.fd(15)
		tur.right(90)
		tur.fd(10)
		tur.pd()
		tur.fd(40)
		tur.left(180)
		tur.fd(20)
		tur.right(90)
		tur.fd(20)
		tur.backward(20)
		tur.left(90)
		tur.fd(20)
		tur.right(90)
		tur.fd(20)
		tur.(pu)
		tur.fd(5)
		tur.left(90)
		tur.fd(10)
		tur.right(90)

		
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
		 tur.setheading(0)
		 tur.pendown()
		 tur.setpos(-35,-40)
		 tur.right(270)
		 tur.pendown()
		 tur.forward(40)
		 tur.backward(20)
		 tur.right(90)
		 tur.forward(25)
		 tur.right(90)
		 tur.forward(20)
		 tur.right(180)
		 tur.forward(40)

	    elif letter == "I":
		tur.setheading(0)
		tur.pendown()
		tur.left(90)
		tur.forward(50)
		tur.right(90)
		tur.penup()
		tur.forward(10)
		
	    elif letter == "J":
		tur.setheading(0)
		tur.pendown()
		tur.setpos(-35,-15)
		tur.pendown()
		tur.forward(40)
		tur.backward(20)
		tur.right(90)
		tur.forward(40)
		for i in range(11):
   			tur.forward(4)
    			tur.right(15)
		
	    elif letter == "K":
		tur.setheading(0)
		tur.pendown()
		tur.setpos(-35,-40)
		tur.right(270)
		tur.pendown()
		tur.forward(40)
		tur.backward(20)
		tur.right(40)
		tur.forward(30)
		tur.backward(30)
		tur.right(90)
		tur.forward(30)
		tur.clear()


elif letter == "K":
    tur.penup()
    tur.setpos(-35,-40)
    tur.right(270)
    tur.pendown()
    tur.forward(40)
    tur.backward(20)
    tur.right(40)
    tur.forward(30)
    tur.backward(30)
    tur.right(90)
    tur.forward(30)
    tur.clear()

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
		tur.setheading(0)
		tur.pendown()
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
		tur.setheading(0)
		tur.pendown()
	        tur.forward(5)
	        tur.pendown()
	        tur.right(90)
	        tur.forward(60)
	        tur.right(180)
	        tur.forward(60)
	        tur.right(90)
	        tur.forward(40)
	        tur.right(90)
	        tur.forward(30)
	        tur.right(90)
	        tur.forward(40)
	        tur.right(180)
	        tur.forward(40)
	        tur.left(90)
	        tur.forward(30)
	        tur.right(90)	
			
	    elif letter == "Q":
		tur.setheading(0)
		tur.pendown()
		tur.setpos(-35,-40)
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

	    elif letter == "R":
		tur.pendown()
		tur.setpos(-35,-40)
		tur.right(270)
		tur.pendown()
		tur.forward(40)
		tur.right(90)
		for i in range(12):
    			tur.forward(3)
    			tur.right(16)
		tur.right(215)
		tur.forward(30)

	    elif letter == "S":
		tur.pendown()
		tur.setpos(35,45)
		tur.right(185)
		tur.pendown()
		for i in range(9):
			tur.forward(6)
    			tur.left(20)
		for i in range(13):
    			tur.forward(6)
   			tur.right(19)


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
		tur.pendown()
		tur.setpos(-35,-15)
		tur.right(90)
		tur.pendown()
		tur.forward(30)
		for i in range(11):
    			tur.forward(5)
    			tur.left(15)
		tur.left(15)
		tur.forward(40)

	    elif letter == "V":
		tur.pendown()
		tur.setpos(-35,-15)
		tur.left(35)
		tur.pendown()
		tur.right(90)
		tur.forward(50)
		tur.left(115)
		tur.forward(50)
		tur.clear()

		
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
    tur.setheading(0)
    tur.right(45)
    tur.forward(100)
    tur.backward(50)
    tur.right(90)
    tur.forward(50)
    tur.backward(100)
		
    elif letter == "Y":
		 tur.pendown()
		 tur.setpos(-35,-15)
		 tur.left(35)
		 tur.pendown()
		 tur.right(90)
		 tur.forward(50)
		 tur.left(115)
		 tur.forward(50)
		 tur.backward(50)
		 tur.right(150)
		 tur.forward(45)
		 tur.clear()

		
elif letter == "Z":
    tur.setheading(0)
    tur.forward(100)
    tur.backward(100)
    tur.right(51)
    tur.forward(155)
    tur.right(130)
    tur.forward(100)		
	

	        

			
	  
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)
