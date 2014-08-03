from simulation import Simulation
import common
import json

simulation = Simulation(['uber', 'hitch'])

simulation.run()

# calculations
print(str(len(common.logs['uber'])))
print(str(len(common.logs['hitch'])))
print(str(len(common.vehicleLogs['uber'])))
print(str(len(common.vehicleLogs['hitch'])))
