from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource
# Importing the different component sectors

class Circuit:
    def __init__(self, name, i):
        self.name = name
        self.i = i
        self.buses = {}
        self.resistors = {}
        self.loads = {}
        self.vsources = {}

    def add_bus(self, bus: Bus):
        self.buses[bus.name] = bus
        return

    def add_resistor(self, resistor: Resistor):
        instance = (resistor.name, resistor.bus1, resistor.bus2)
        self.resistors[instance] = resistor
        return

    def add_load(self, load: Load):
        instance = (load.name, load.bus1)
        self.loads[instance] = load
        return

    def add_vsource(self, vsource: Vsource):
        instance = (vsource.name, vsource.bus1)
        self.vsources[instance] = vsource
        return

    def set_i(self, current):
        self.i = current
        return

    def print_nodal_voltages(self):
        for bus in self.buses.values():
            print(f'The voltage of Bus {bus.name} is {bus.v} V')
        return

    def print_circuit_current(self):
        print(f'The current of the circuit is {self.i} A')
        return


if __name__ == '__main__':
    # Create a Circuit instance
    circuit = Circuit("Test Circuit", 0)

    # Create some Bus instances
    bus1 = Bus("BusA")
    bus2 = Bus("BusB")
    bus1.set_bus_v(10)
    bus2.set_bus_v(20)

    # Add buses to the circuit
    circuit.add_bus(bus1)
    circuit.add_bus(bus2)

    # Create a Resistor instance
    resistor1 = Resistor("R1", "BusA", "BusB", 100)

    # Add resistor to the circuit
    circuit.add_resistor(resistor1)

    # Create a Load instance
    load1 = Load("L1", "BusA", 50, 5)

    # Add load to the circuit
    circuit.add_load(load1)

    # Create a Vsource instance
    vsource1 = Vsource("V1", "BusA", 12)

    # Add voltage source to the circuit
    circuit.add_vsource(vsource1)

    # Set the current of the circuit
    circuit.set_i(10)

    # Print nodal voltages
    circuit.print_nodal_voltages()

    # Print the circuit current
    circuit.print_circuit_current()

    # Verify the internal dictionaries
    print(f"Buses: {circuit.buses}")
    print(f"Resistors: {circuit.resistors}")
    print(f"Loads: {circuit.loads}")
    print(f"Voltage Sources: {circuit.vsources}")