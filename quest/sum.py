def sum(a,b): # definition of sum function
    result=0
    for i in range(a,b+1):
        result+=i
    return result


def main(): # definition of main function
    print("Sum from 1 to 10 is",sum(1,10))
    print("Sum from 20 to 37 is",sum(20,37))
    print("Sum from 35 to 49 is",sum(35,49))
main() # call the main function