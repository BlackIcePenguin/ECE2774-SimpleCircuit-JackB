from Circuit import Circuit

class Solution:
    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        # Calculating the current equation, with the stated vsource/(res1 + Rload)
        bus_a_key = list(self.circuit.buses.keys())[0]  # Gets first bus key
        bus_b_key = list(self.circuit.buses.keys())[1]  # Gets second bus key
        vsource_key = list(self.circuit.vsources.keys())[0]  # Gets first voltage source key
        resistor_key = list(self.circuit.resistors.keys())[0]  # Gets first resistor key
        load_key = list(self.circuit.loads.keys())[0]  # Gets first load key


        # Will try hardcoding with the names for now, need to check how to make it general
        current = self.circuit.vsources[vsource_key].v / (self.circuit.resistors[resistor_key].r + 1/self.circuit.loads[load_key].g)
        self.circuit.set_i(current)
        vb = current * 1/self.circuit.loads[load_key].g
        self.circuit.buses[bus_b_key].set_bus_v(vb)
        va = self.circuit.vsources[vsource_key].v
        self.circuit.buses[bus_a_key].set_bus_v(va)