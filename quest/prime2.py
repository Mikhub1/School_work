from math import sqrt

# Determine if a number is prime
def checkPrime(value):
# assume the number is prime
    isPrime = True
    
    # determine if number is prime
    divisor = 2
    while divisor <= sqrt(value):
        if value % divisor == 0:
            isPrime = False
            break # exit the loop, therefore the return isPrime is not executed
    divisor +=1
    return isPrime

# Compute the first n prime numbers
def main():
    NUMBER_OF_PRIMES = 20
    PRIMES_PER_LINE = 10
    count=0 # number of primes computed
    number=2 # start at 2
    print("The first",NUMBER_OF_PRIMES,"are:")
    while count < NUMBER_OF_PRIMES:
        if checkPrime(number):
            # increment count and and output value
            count+=1
            print("%5d" % number,end="")
            if(count%PRIMES_PER_LINE==0):
                print() # move to next line
            # move to next number to check
        number+=1
main()