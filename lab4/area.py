'''

#AreaOfTriangles.py
#Compute the area of triangles using Heron's formula
import math

a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))
s = (a+b+c)/2.0
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is", format(area, '.2f'))

a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))
s = (a+b+c)/2.0
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is", format(area, '.2f'))

a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))
s = (a+b+c)/2.0
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is", format(area, '.2f'))
'''

#AreaOfTriangles_sol1.py
#Compute the area of triangles using Heron's formula
import math

def findArea(a,b,c):
    s = (a+b+c)/2.0
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is", format(area, '.2f'))

n = int(input("How many trangles are to be processed? "))
for t in range (n):
    a = float(input("Enter the length of side 1: "))
    b = float(input("Enter the length of side 2: "))
    c = float(input("Enter the length of side 3: "))
    findArea(a,b,c)

















