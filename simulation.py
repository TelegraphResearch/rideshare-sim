import common
from group import Group
from environment import Environment
from vehicles.dedicated import Dedicated
from vehicles.pooled import Pooled
import random
import copy

class Simulation(object):

    def __init__(self, serviceTypes):
        self.time = common.simLength
        self.envs = []
        for serviceType in serviceTypes:
            self.envs.append(Environment(serviceType))

    def run(self):
        while common.clock < self.time:
            common.clock += 1
            if common.clock % 10000 == 0:
                print(common.clock)

            group = Group() if self.needGroup() else None

            for env in self.envs:
                # Need to make a copy of the object to avoid pointer issues
                env.step(copy.deepcopy(group))

        for env in self.envs:
            env.sendVehicleLogs()

    def needGroup(self):
        if random.random() < common.needGroupFrequency:
            return True
        return False
