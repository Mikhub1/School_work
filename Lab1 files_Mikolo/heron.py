from math import*
#Write a Python program that uses Heron's formula to calculate the area of
#a triangle given the lengths of its three sides (in centimetres). Your
#program should read the lengths as three floating point numbers from the standard input. 

#Tell user to enter 3 inputs
a = float(input("Enter a value for the 3 sided triangle:"))
b = float(input("Enter a value for the 3 sided triangle:"))
c = float(input("Enter a value for the 3 sided triangle:"))

#Heron's formular
#Semi perimeter value for the triangle is required
s = (a + b +c)/2

#Formular for area
area = sqrt(s*(s-a)*(s-b)*(s-c))

print("The value of area based on heron's formular is:",area)
