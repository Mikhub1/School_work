
'''
Given the values for radius and height of n cylinders,
use functions to find the surface area and the volume 
for each cylinder. Your main program should call the surface area and volume functions for each of the n cylinders.

Surface Area = 2πrh + 2πr2

Volume = πr2h
'''
from math import*

def surface_area(r,h):
    Surface_area = (2*pi*r*h) + (2*pi*r**2)
    print("The surface_area of the cylinder with radius =",r,"m and height = ",h,"m ",Surface_area)

def volume(r,h):
    Volume = pi*r**2*h    
    print("The volume of the cylinder with radius =",r,"m and height = ",h,"m ",Volume)

def main():
    n = int(input("Please enter the number of cylinders you would like to work on: "))

    while n >= 1:
        radius = float(input("Please enter a radius for the cylinder in a reasonable range [1,infinity): "))
        height = float(input("Please enter a height for the cylinder in a reasonable range [1,infinity): "))
        surface_area(radius,height)
        volume(radius,height)
        n -= 1
main()        

