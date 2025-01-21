from Bus import Bus
from Resistor import Resistor
from Load import Load
from Vsource import Vsource
from Circuit import Circuit
from Solution import Solution

# Just initial file creation for now
test_circuit = Circuit("TestCircuit", 0)
# Create some Bus instances
busA = Bus("BusA")
busB = Bus("BusB")
# Add buses to the circuit
test_circuit.add_bus(busA)
test_circuit.add_bus(busB)
# Create a Vsource instance
vsourceA = Vsource("Va", "BusA", 100)
# Add voltage source to the circuit
test_circuit.add_vsource(vsourceA)
# Create a Resistor instance
resistorAB = Resistor("Rab", "BusA", "BusB", 5)
# Add resistor to the circuit
test_circuit.add_resistor(resistorAB)
# Create a Load instance
loadB = Load("Lb", "BusB", 2000, 100)
# Add load to the circuit
test_circuit.add_load(loadB)
# Create the solution object
test_solution = Solution(test_circuit)
# Run the solution solve
test_solution.do_power_flow()


# Print nodal voltages
test_circuit.print_nodal_voltages()

# Print the circuit current
test_circuit.print_circuit_current()
