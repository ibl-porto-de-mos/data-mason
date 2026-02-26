class TheArch:
    def __init__(self, builder, size):
        self.builder = builder
        self.size = size
        self.passengers = []

    def load_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"{passenger} has boarded the ark.")

    def describe(self):
        return f"This ark was built by {self.builder}, size {self.size}, with passengers: {self.passengers}"

# Creating an instance (object)
noah_arch = TheArch("Noah", "300 cubits")
noah_arch.load_passenger("Noah")
noah_arch.load_passenger("Sheep")
print(noah_arch.describe())