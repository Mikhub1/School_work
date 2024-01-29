#Initalize the counters to keep track of the red and green marbles.
red_count = 0
green_count = 0


#Get a value for the variable colour as "r" for red or "g" for green.
colour = input("Enter r for red and g for green and b to end:")
#This will be the loop control variable (lcv).


#Set the condition to terminate using a sentinel value.
while colour != 'B' and colour != 'b':

    #Check the colour of the marble and update the count for that colour.
    if colour == "r" or colour == "R":
        red_count +=1
    elif colour == "g" or colour == "G":
        green_count +=  1

    #Don't forget the modification of the loop control variable (lcv).
    colour = input("Enter marble colour as r (red) or g (green), b to end: ")

#Print the counts for the two colours and compute and print the 
#percentage of each colour.
print("Number of red marbles in the bag:", red_count)
print("Number of green marbles in the bag:", green_count)
redPercent = red_count/(red_count+green_count)*100
greenPercent = green_count/(red_count+green_count)*100
print("The percentage of red marbles is: %.2f" % redPercent)
print("The percentage of green marbles is: %.2f" % greenPercent)

