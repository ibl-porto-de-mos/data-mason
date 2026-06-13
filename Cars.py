class Car:
    def __init__(self, engine, wheels, doors, chassis, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
        self.chassis = chassis
        self.fuel_tank = fuel_tank

    def accelerate(self):
        return "ACELERA AI!!!"   

    def stop(self):
        return "PARE!!"