class Car:
    def __init__(self, make, model):
        self.__make = make  # Hidden attribute
        self.__model = model #Hidden attribute
        self.__fuel = 0
        self.litresPer100km = 8
    
    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getFuel(self):
        return self.__fuel
    
    def addFuel(self, fuel):
        self.__fuel += fuel
    
    def drive(self, distance):
        self.__fuel -= (self.litresPer100km / 100) * distance
    
    def distanceToE(self):
        return (self.__fuel / self.litresPer100km) * 100