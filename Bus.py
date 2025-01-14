class Bus:
    # Constructor for the class
    def __init__(self, name, v):
        # Attributes
        self.name = name
        self.v = v

    # Sets the bus voltage
    def set_bus_v(self, bus_v):
        self.v = bus_v
        return

if __name__ == '__main__':
    # Test creation of object
    Bus1 = Bus("1", 5.4)
    print(Bus1.v)
    print(Bus1.name)
    Bus1.set_bus_v(7.2)
    print(Bus1.v)
