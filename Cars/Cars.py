class Car:
    def __init__(self, Engine, wheels, doors, chassis,fuel_tank):
        self.Engine = Engine
        self.wheels = wheels
        self.doors = doors
        self.chassis = chassis
        self.fuel_tank = fuel_tank

    def acelerar(self,x):
        return "ACELERA AI!!!!"
    
    def parar(self):
        return "parou"