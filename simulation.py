import common
from group import Group
from vehicles.uber import Uber
from vehicles.hitch import Hitch

class Simulation(object):
    """
    OMG PSEUDOCODE
    """

    def __init__(self):
        self.time = 10000 #TIME OF SIMULATION
        self.envs = [uber, hitch]
        self.clock = 0 # to start

    def run():
        while self.clock < self.time:
            self.clock += 1
            group = self.genGroup() if self.needGroup() else None
            for env in self.envs:
                env.step(group)
        for env in envs:
            while env.stillRunning():
                self.clock += 1
                env.step() # no group passed in

    def getLogs():
        logs = {}
        for env in self.envs:
                logs[str(env)] = env.getLogs()
