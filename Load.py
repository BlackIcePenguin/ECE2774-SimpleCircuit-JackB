class Load:
    # Constructor for the class
    def __init__(self, name, bus1, p, q):
        # Attributes
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.q = q
        self.g = self.calc_g()

    # Function for calculating the conductance of the load
    def calc_g(self):
        # Uses P = V^2/R to find R and G = 1/R for conductance, not sure if this works, will test
        self.g = 1 / (self.bus1.v**2 / self.p)
        return self.g

if __name__ == '__main__':
    # Test creation of object
    Load1 = Load("Load1", "1", 7.5, 9)
    print(Load1.p)
    print(Load1.q)
    print(Load1.name)
    print(Load1.bus1)
    print(Load1.calc_g())
