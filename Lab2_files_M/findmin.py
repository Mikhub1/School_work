#This program finds and prints the smallest number.
x = int(input("Please enter the first integer number: "))
y = int(input("Please enter the second integer number: "))
z = int(input("Please enter the third integer number: "))
        
if x < y and x < z:
    print("The smallest number is:", x)
elif y < x and y < z:
    print("The smallest number is:", y)
else:
    print("The smallest number is:", z)
