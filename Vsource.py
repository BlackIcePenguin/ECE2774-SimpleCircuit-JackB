class Vsource:
    # Constructor for the class
    def __init__(self, name, bus1, v):
        self.name = name
        self.bus1 = bus1
        self.v = v

if __name__ == '__main__':
    # Test creation of object
    Source1 = Vsource("V1", "1", 5.4)
    print(Source1.v)
    print(Source1.name)
    print(Source1.bus1)