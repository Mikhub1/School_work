#Find the GCD for 72 and 54.
#Initialize the two variables with each of the numbers.
val1 = 104
val2 = 54

#Continue looping until one of the integers becomes zero.
while val1 != 0 and val2 != 0:
    #Replace the larger integer with the computed difference of 
    #the two given values.
    if val1 > val2:
        val1 = val1 - val2
    else:
        val2 = val2 - val1

#Print out the non-zero integer.
if val1 > 0:
    print(val1,"is the GCD")
else:
    print(val2,"is the GCD")


