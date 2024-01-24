import turtle
import math

# Ask the user to input two points.
x1, y1 = eval(input("Enter x1 and y1 for point 1, separated by comma: "))
x2, y2 = eval(input("Enter x2 and y2 for point 2, separated by comma: "))

# Calculate distance between points.
distance1 = math.sqrt(x1**2 + y1**2)
distance2 = math.sqrt(x2**2 + y2**2)

# Draw a line between the point (0,0) and each of the points entered by the user.
wn = turtle.Screen()
aTurtle = turtle.Turtle()

# Draw line to point 1
aTurtle.penup()
aTurtle.goto(0, 0)
aTurtle.pendown()
aTurtle.goto(x1, y1)

# Move forward to avoid overlapping messages
aTurtle.penup()
aTurtle.forward(20)

# Draw line to point 2
aTurtle.pendown()
aTurtle.goto(x2, y2)

# Calculate lengths of lines
length1 = round(distance1, 2)
length2 = round(distance2, 2)

# Display the length of each line
aTurtle.penup()
aTurtle.goto(x1 / 2, y1 / 2)
aTurtle.write("Distance 1 = " + str(length1), font=16)

# Move forward to avoid overlapping messages
aTurtle.penup()
aTurtle.forward(20)

aTurtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
aTurtle.write("Distance 2 = " + str(length2), font=16)

# Write beside the longer line 'This is longer'
aTurtle.penup()
if length1 > length2:
    aTurtle.goto(x1, y1)
    aTurtle.forward(20)
    aTurtle.write("This is longer", font=16)
else:
    aTurtle.goto(x2, y2)
    aTurtle.forward(20)
    aTurtle.write("This is longer", font=16)

wn.mainloop()