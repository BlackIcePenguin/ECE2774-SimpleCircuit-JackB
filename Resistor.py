class Resistor:
    # Constructor for the class
    def __init__(self, name, bus1, bus2, r):
        # Attributes
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r
        self.g = self.calc_g()

    # Function for calculating the conductance of the resistor
    def calc_g(self):
        # Calculated the conductance using G = 1/R
        self.g = 1 / self.r
        return self.g

if __name__ == '__main__':
    # Test creation of object
    Res1 = Resistor("R1", "1", "2", 9.4)
    print(Res1.name)
    print(Res1.bus1)
    print(Res1.bus2)
    print(Res1.r)
    print(Res1.g)
