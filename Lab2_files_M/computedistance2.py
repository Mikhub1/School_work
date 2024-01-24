import turtle

# Function to determine the location of p2 relative to the line p0p1
def determine_location(x0, y0, x1, y1, x2, y2):
    if x0 == x1:  # Vertical line
        if x2 < x1:
            return "p2 is on the left side of p0p1"
        elif x2 > x1:
            return "p2 is on the right side of p0p1"
        else:
            return "p2 is on p0p1"
    elif y0 == y1:  # Horizontal line
        if y2 < y1:
            return "p2 is below p0p1"
        elif y2 > y1:
            return "p2 is above p0p1"
        else:
            return "p2 is on p0p1"
    else:
        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - x0 * slope
        x_new = (y2 - intercept) / slope
        if x2 > x_new:
            return "p2 is on the right side of p0p1"
        elif x2 < x_new:
            return "p2 is on the left side of p0p1"
        else:
            return "p2 is on p0p1"

# Ask the user to enter the x- and y-coordinates for three points p0, p1, and p2
x0, y0 = eval(input("Enter x0 and y0 for point p0, separated by comma: "))
x1, y1 = eval(input("Enter x1 and y1 for point p1, separated by comma: "))
x2, y2 = eval(input("Enter x2 and y2 for point p2, separated by comma: "))

# Draw a line between p0 and p1
wn = turtle.Screen()
aTurtle = turtle.Turtle()

aTurtle.penup()
aTurtle.goto(x0, y0)
aTurtle.pendown()
aTurtle.goto(x1, y1)

# Write an X to represent the location of p2
aTurtle.penup()
aTurtle.goto(x2, y2)
aTurtle.pendown()
aTurtle.write("X", font=("Arial", 12, "normal"))

# Determine the location of p2 with respect to the line p0p1
location = determine_location(x0, y0, x1, y1, x2, y2)

# Display a message indicating the location of p2
aTurtle.penup()
aTurtle.goto((x0 + x1) / 2, (y0 + y1) / 2)
aTurtle.write(location, font=("Arial", 12, "normal"))

wn.mainloop()