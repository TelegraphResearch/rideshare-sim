import common
from group import Group
from environment import Environment
from vehicles.uber import Uber
from vehicles.hitch import Hitch
import random
import copy

class Simulation(object):

    def __init__(self, serviceTypes):
        self.time = 60*60*26 #TIME OF SIMULATION
        # 26 hours
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
    
    def csv(self):
        '''
        print logs to stdout
        '''
        columns = [
            'type',
            'spawn',
            'driverAssigned',
            'start',
            'end',
            'size',
        ]

        # headers
        for column in columns:
            print("%s," % column),
        print("\n"),

        # uber logs
        for log in common.logs['uber']:
            print("uber,", end="")
            for key in log:
                print("%s," % log[key], end="")
            print("\n", end="")

        for log in common.logs['hitch']:
            print("hitch,", end="")
            for key in log:
                print("%s," % log[key], end="")
            print("\n", end="")
