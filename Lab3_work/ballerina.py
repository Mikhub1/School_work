#With each step forward that a ballerina takes, she twirls 5 times.
#Obtain the number of steps the ballerina takes forward as input.
steps = int(input("Enter the number of steps the ballerina takes: "))

#Number of twirls is a constant.
TWIRLS = 5

#Write the outer for loop to keep track of the steps.
start_point = 1
while TWIRLS:
    if start_point <= steps:
        for i in range (1,TWIRLS+1) :
            print("step : ",start_point ,"twirl : ",i, end="")
        start_point += 1
   



    #Write the inner for loop to keep track of the twirls and to generate 
    #the output.  The ballerina twirls 5 times for every step she takes.
    
