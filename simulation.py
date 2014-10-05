import common
from group import Group
from environment import Environment
from vehicles.uber import Uber
from vehicles.hitch import Hitch
import random
import copy

class Simulation(object):

    def __init__(self, serviceTypes):
        self.time = common.simLength #TIME OF SIMULATION
        # 26 hours
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
