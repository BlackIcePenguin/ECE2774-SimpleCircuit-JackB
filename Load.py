class Load:
    # Constructor for the class
    def __init__(self, name:str, bus1:str, p:float, v:float):
        # Attributes
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v
        self.g = self.calc_g()

    # Function for calculating the conductance of the load
    def calc_g(self):
        # Uses P = V^2/R to find R and G = 1/R for conductance, not sure if this works, will test
        self.g = 1 / (self.v**2 / self.p)
        return self.g

if __name__ == '__main__':
    # Test creation of object
    Load1 = Load("Load1", "1", 7.5, 9)
    print(Load1.p)
    print(Load1.v)
    print(Load1.name)
    print(Load1.bus1)
    print(Load1.g)
