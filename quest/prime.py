from math import *
'''num = int(input("Enter a number > 1 "))
isPrime = True
divisor = 2
while isPrime and divisor <= sqrt(num) :
    if num % divisor == 0:
        isPrime = False
    divisor +=1
if isPrime:
    print(num, " is a prime number")
else:
    print(num, " is not a prime number. It is a multiple of ",
divisor-1)
'''
num = int(input("Enter a number > 1 "))

divisor = 2
while divisor <= sqrt(num) :
    if num % divisor == 0:
        print(num, " is not a prime number. It is a multiple of ", divisor)
        break
    divisor +=1
if divisor==int(sqrt(num))+1:
	print(num, " is a prime number")