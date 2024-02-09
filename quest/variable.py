'''
Notes:
A parameter is the variable defined within the parentheses during function definition

An argument is a value that is passed to a function when it is called. 
It might be a variable, value or object passed to a function or method as input. 
They are written when we are calling the function




def f1():
    localVar = 2
    print(globalVar)
    print(localVar)
globalVar = 1
f1()
print(globalVar)
print(localVar) 


def f1():
    x = 2
    print("x in f1 =",x)
x = 1 #global variable
f1()
print("x outside =",x)


def f2(a):
    print("a=",a)
#    print("y=",y)
def f1(x):
    y=3
    print("x=",x)
    f2(x)

f1(4)
            '''

def main():
    x=1
    print("Before function call, x=",x) # output 1
    increment(x)
    print("After function call, x=",x) # output 1

def increment(n):
    n+=1
    print("Inside function, after increment, n=",n) # output 2
main()