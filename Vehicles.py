class Car:
    def __init__(self, engine, wheels, doors, chassis, fuel_tank):


        self.engine = engine
        self.wheels = wheels
        self.doors = doors
        self.chassis = chassis
        self. fuel_tank = fuel_tank
    
    def accelerate(self):
        return f"O motor {self.engine} ronca alto e o carro acelera com suas {self.wheels}!"
    
Volkswagen = Car("v8","rodas de liga leve", 4, "chassis", "80 litros")

result = Volkswagen.accelerate()

print(result)
print(f"Tanque: {Volkswagen.fuel_tank}")
