#Walk in a triangular path.
#Modify your program to ask the user for the number of sides and lenght
#This works for any regular polygon.
#Let's make the turtle draw a triangle.
#First import the module turtle.
import turtle

#Second open a window.
wn = turtle.Screen()

#Third create a turtle and assign it to a variable.
myTurtle = turtle.Turtle()

angleToTurn = 360/3
sideLength = int(input("Input the required number of sideLenght for your polygon: "))
number_of_sides = int(input("Input the required number of sides for your polygon: "))


for i in range(number_of_sides):
    myTurtle.forward(sideLength)
    myTurtle.left(angleToTurn)
    myTurtle.forward(sideLength)
    myTurtle.right(angleToTurn)
    myTurtle.left(angleToTurn)

wn.mainloop()
