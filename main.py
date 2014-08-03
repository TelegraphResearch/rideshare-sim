from simulation import Simulation
import common
import json

simulation = Simulation(['uber', 'hitch'])

simulation.run()

# calculations
simulation.csv()
