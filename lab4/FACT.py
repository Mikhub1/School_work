def fact(n):       #Line 1
    prod = 1       #Line 2
    i = 1          #Line 3
    while i<=n:    #Line 4
        prod *= i  #Line 5
        i += 1     #Line 6
    return prod    #Line 7

def main():        #Line 8
    f = fact(2)    #Line 9
    print(f)       #Line 10

main()             #Line 11