# Check whether a whole number is
# 1) divisible by 5 and divisible by 6
# 2) divisible by 5 or divisible by 6
# 3) divisible by 5 or 6 but not by both
num = float(input("Enter a number: "))
num = int(num)

divisibleBy5 = num % 5 == 0
divisibleBy6 = num % 6 == 0

if divisibleBy5 and divisibleBy6:
    print(num, " is divisible by 5 and 6")
if divisibleBy5 or divisibleBy6:
    print(num, ' is divisible by 5 or 6')
if (divisibleBy5 or divisibleBy6) and \
    not(divisibleBy5 and divisibleBy6):
    print(num, " is divisible by 5 or 6, but not both")

