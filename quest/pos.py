def max(num1,num2):
    result = num1 if num1>num2 else num2
    return result
#x = float(input("Enter a value: "))
#y = float(input("Enter a value: "))
#z = max(x,y)
#print("The maximum is:",z)

def print_area(width=1, height=2):
    area = width*height
    print("The area is",area)
#print_area()
    

def calc_area(w,h):
    if w<=0 or h<=0:
        print("Invalid width or height") 
        return
    return(w*h)

print(calc_area(5,6))

