from fan import *

def displayProperties(f):
    print("Speed :",f.getspeed())
    print("Power :",f.getON())
    print("Radius :",f.getradius())
    print("Colour :",f.getcolour()) 


def main():
    #Create a Fan object with the following attribute values:
    #speed = MEDIUM, radius = 15, colour = "blue", on = False
    fan1 = Fan()
    fan1.setspeed(MEDIUM)
    fan1.setradius(15)
    fan1.setcolour("blue")
    fan1.setON(False)
 
    #Using only the constructor, create a second Fan object (fan2) with the
    #maximum speed, that is yellow in colour, has a radius of 8.5, and is on.
    fan2 = Fan()
    fan2.setcolour("yellow")
    fan2.setspeed(FAST)
    fan2.setradius(8.5)
    fan2.setON(True)

    #Create a third Fan object (fan3) using default attribute values.
    fan3 = Fan()
    fan3.setcolour("black")
    fan3.setspeed(FAST)
    fan3.setradius(4.5)
    fan3.setON(True)


    #Using set methods, change the colour of fan3 to "purple" and
    #the radius to 10.
    fan3.setcolour("purple")
    fan3.setradius(10)
    


    #Display the attributes of fan1, fan2, and fan3 using
    #the displayProperties function that you wrote above.
    displayProperties(fan1)




main()

