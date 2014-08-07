from simulation import Simulation
import common
import json
from datetime import datetime

simulation = Simulation(['uber', 'hitch'])

simulation.run()

# Save the results of the file to json 
f = open("output/run-%s.json" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'w')
f.write(json.dumps(common.getLogs()))
f.close()
