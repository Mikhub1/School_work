#Use the outer loop to step through all the numbers between 5 and 10000.
perfect_list = list()
for number in range(5,10000):
    #Initialize the variable divSum to accumulate the sum of all the divisors.
    divsum = 0

    #Initialize the variable divisor to be half the number to start.
    divisor = number//2
    

    #Continue to loop while the divisor is more than or equal to 1.
    while divisor >= 1:
        #Check if the number can be divided evenly by the divisor.
        if number % divisor == 0:
            #Update the sum.
            divsum += divisor
        #Update the divisor, modification of the lcv.
        divisor -= 1

    
    #Check if the number is equal to the sum, print the number if it is.
    if number == divsum:
        print("This is a perfect number: %2.2d"%number)
        perfect_list.append(number)
    else:
        print("Not a perfect number: %2.2d"%number)
print()
print(perfect_list)
