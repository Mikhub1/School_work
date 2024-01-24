from math import*
#Given the amount of punch in a punch bowl, find the number of glasses
#you can fill, as well as the amount of punch left over that will not
#completely fill a glass

punch = float(input("Enter the amount of punch in the bowl:"))
glass = float(input("Enter the glass capacity:"))

# 1 Litre = 33.8140226 ounces
# convert the litres to ounces
punch *= 33.8140226

# Total amount of 6 ounces cups that can be filled
filled = punch//glass
leftover = punch % glass

print("The number of 6.0 ounce glasses that can be filled is",filled)
print("The number leftover ounces is", leftover)
