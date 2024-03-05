SLOW = 1
MEDIUM = 2
FAST = 3

class Fan:

    #Complete the initializer method with default values for
    #speed as SLOW, on as False, colour as blue and radius as 5.
    def __init__(self, speed = SLOW, On = False, colour = "blue", radius = 5):
        self.speed = speed
        self.On = On
        self.colour = colour
        self.radius = radius



    #Provide getter and setter methods for each attribute.
    def getspeed(self):
        return self.speed
    def setspeed(self,speed):
        self.speed= speed
        
    def getON(self):
        return self.On
    def setON(self, On):
        self.On = On
        
    def getcolour(self):
        return self.colour
    def setcolour(self,colour):
        self.colour = colour

    def getradius(self):
        return self.speed
    def setradius(self,radius):
        self.radius = radius 

