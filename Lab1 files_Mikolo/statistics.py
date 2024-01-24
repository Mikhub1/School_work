#This program inputs four integer values and computes and prints the highest
#and lowest of the values.  The program also computes the average and 
#prints all the computed values with appropriate labels.
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
c = int(input("Enter the third value: "))
d = int(input("Enter the fourth value: "))
        
#Compute the values
lowest = min(a,b,c,d)
highest = max(a,b,c,d)
average = (a+b+c+d)//4

#Print the values with appropriate labels
print("The lowest value is",lowest)
print("The highest value is",highest)
print("The average of all the values is",average)