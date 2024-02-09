from math import*
from random import*
'''
sum = 0
for i in range(501):
    sum = sum + i
print(sum)

a="hello"
for x in a:
    print(x.upper(),end="")

myStr = "hello!"
newStr = ""
for i in myStr:
    newStr = newStr + (i * 2)
    print(newStr)

for letter in 'Python':     # First Example
   if letter == 'h':
        continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")


# Prompt the user to enter 2 integers
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
gcd = 1
k = 2
while k<=n1 and k<=n2:
    if n1%k==0 and n2%k==0:
        gcd = k
    k+=1
print("The greatest common divisor for",n1,"and",n2,"is",gcd)    


n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))
r=1

while r!=0:
    q=n1//n2
    r=n1%n2
    print(n1,"=",n2,"*",q,"+",r)
    n1=n2
    n2=r
print("The greatest common divisor is",n1)


print("Multiplication Table")
print(" ",end="")
for j in range(1,10):
    print(" ",j,end="")
print() # move to new line
print("----------------------------------------")

for i in range(1,10):
    print(i,"|",end="")
    for j in range(1,10):
        print("%4d" % (i*j),end="")
    print()
'''


# Compute the first NUMBER_OF_PRIMES prime numbers

NUMBER_OF_PRIMES = 50
PRIMES_PER_LINE = 10
count=0 # number of primes computed
number=2 # start at 2

print("The first",NUMBER_OF_PRIMES,"primes are:")

while count < NUMBER_OF_PRIMES:
    isPrime = True # assume the number is prime
# determine if number is prime
divisor = 2
while divisor <= sqrt(number):
    if number % divisor == 0:
        isPrime = False
        break # exit the loop
    divisor +=1
if isPrime: # increment count and and output value
    count+=1
    print("%5d" % number,end="")
    if(count % PRIMES_PER_LINE == 0):
        print() # move to next line
# move to next number to check
number+=1