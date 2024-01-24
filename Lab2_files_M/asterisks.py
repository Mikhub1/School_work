#Given an integer input value, the following code should print approximately
#half the number of asterisks of the given input value, plus 1, 2, 3 or 4
#extra asterisks, depending on the value of b.
b = int(input("Please enter an integer value: "))
a = b//2
asterisk = "*"
if b > 10:
    print(asterisk * a + " *")
elif b > 7:
    print(asterisk * a + " **")
elif b > 4:
    print(asterisk * a + " ***")
elif b > 1:
    print(asterisk * a + " ****")
