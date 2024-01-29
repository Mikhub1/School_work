#Let's make the turtle draw a triangle.
#First import the module turtle.
import turtle

#Second open a window.
wn = turtle.Screen()

#Third create a turtle and assign it to a variable.
myTurtle = turtle.Turtle()

#Walk in a triangular path.
#The number of degrees to turn is equal to 360 divided by the number of sides.
#This works for any regular polygon.

angleToTurn = 360/3
sideLength = 150
number_of_sides = 3

'''
#Draw the triangle.
myTurtle.forward(sideLength)
myTurtle.left(angleToTurn)
myTurtle.forward(sideLength)
myTurtle.left(angleToTurn)
myTurtle.forward(sideLength)
myTurtle.left(angleToTurn)
'''

for i in range(number_of_sides):
    myTurtle.forward(sideLength)
    myTurtle.left(angleToTurn)
wn.mainloop()
