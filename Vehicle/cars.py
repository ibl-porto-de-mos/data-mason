class car:
     
    def __init__(self, engine, whells, doors, fuel_tank, chassis): 
        self.engine = engine
        self.whells = whells
        self.doors = doors
        self.fuel_tank = fuel_tank
        self.chassis = chassis


    def acelerar(self, x):
        self.velocidade = 1000
        print(f"O carro acelerou para {self.velocidade} km/h")

    def parar(self):
        self.velocidade = 0
        print("O carro parou")