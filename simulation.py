import common
from group import Group
from environment import Environment
from vehicles.uber import Uber
from vehicles.hitch import Hitch
import random
import copy

class Simulation(object):

    def __init__(self, serviceTypes):
        self.time = 100 #TIME OF SIMULATION
        self.envs = []
        for serviceType in serviceTypes:
            self.envs.append(Environment(serviceType))

    def run(self):
        while common.clock < self.time:
            common.clock += 1
            group = Group() if self.needGroup() else None

            for env in self.envs:
                # Need to make a copy of the object to avoid pointer issues
                env.step(copy.deepcopy(group))

        for env in self.envs:
            while env.stillRunning():
                common.clock += 1
                env.step(None) # no group passed in

    def needGroup(self):
        if random.random() < .1:
            return True
        return False
