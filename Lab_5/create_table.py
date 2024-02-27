noOfRows = 5 #Table should have 5 rows
noOfCols = 3 #Table should have 3 columns

#Create an empty list
lst_1 = []
noOfRows = 5 #with 5 rows
noOfCols = 3 #and 3 columns

#Enter the data values row-wise
for row in range(5):     #for each row in range 0 - 4
    lst_1.append([])                             #add an empty row
    for col in range(3): #for each column in the row
        val = int(input("Enter an integer value: "))#get a value
        #add the value obtained to the row in the desired column
        lst_1[row].append(val)
        
print()
print("The following is the two dimensional list:")
print("The values of the list are:",lst_1 ) 

#Print the values of the second row
print ("The values of the second row are:",lst_1[1])

#Print the values by columns 
print("Values printed by columns")
for col in range(3):
    print(" | ", end="")
    for row in range(5):
        print(lst_1[row][col], end=" | ")
    print()
