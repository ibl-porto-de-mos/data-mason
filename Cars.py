class Car:
    def __init__(self,enginen, wheels, doors, chassis, fuel_tank):


        self.e = enginen
        self.w = wheels
        self.d = doors
        self.c = chassis
        self. ft = fuel_tank
    
    def acelerar (self,x,y):
     return "Pão de Queijo"
    
Automóveis = Car ( "acelerar", "Parar", "construtor")

Fabrica = Automóveis.acelerar("Carros são muito legais")

print(Fabrica)