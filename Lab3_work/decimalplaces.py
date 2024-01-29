#Write the program to produce the output where the numbers in order from 1 to 100000 are printed on one line
#and the numbers in reverse order (100000 to 1) 

decimals = 1
while decimals <= 100000:
    print(decimals,end=" ")
    decimals *= 10 
print()

decimals //= 10
while decimals >= 1:
    print(decimals, end=" ")
    decimals //= 10
print()
 
