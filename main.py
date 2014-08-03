from simulation import Simulation
import common

simulation = Simulation(['uber', 'hitch'])

simulation.run()

# calculations
print('people created: ' + str(common.groupsCreated))
print('uber logs: ' + str(len(common.logs['uber'])))
print('hitch logs: ' + str(len(common.logs['hitch'])))
