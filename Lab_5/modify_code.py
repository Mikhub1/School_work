#Create the empty list 
lst = []

#Get the number of values to be entered 
noOfVal = int(input("How many values in your initial list? "))

#Set up a for loop to obtain one value at a time to create the list
for i in range(noOfVal):
    inNum = int(input("Enter an integer value for your initial list: ") )
    lst.append(inNum)
    
#Use a while loop to accept another list of numbers, terminated by a zero
inNum = int(input("Enter additional integer values, or 0 to terminate: ") )
while inNum != 0 :
   lst.append(inNum) 
    
    
#Print the contents of the list with labels showing their location/index
length = noOfVal
print("%5s   %5s" % ("Index","Value"))
for i in range(length):
    print("%5s   %5s" % (i, lst[i]))

#Print the entire list (see sample output)
print ("The entire list is: ", lst)

#Print the third element from the list 
print("The third element of the list is: ",lst[2]  )

#Print the first element from the list
print("The first element of the list is: ", lst[0]   )

#Print the last element from the list, assuming you do not know
#how many elements are there in the list (use a negative number)
print("The last element of the list is: ",lst[length-1]   )  

#Print the middle element from the list
length = length // 2
print("The middle element of the list is: ",lst[length] )

#Print the sum of all the elements in the list
listSum = 0
for i in range(noOfVal):
    listSum +=  lst[i]
print("The sum of all the values in the list is: ",listSum  )

#Print the elements of the list in reverse
lst.reverse()
print("%5s   %5s" % ("Index","Value"))
for i in range(noOfVal):
    print("%5s   %5s" % (i, lst[i]))
