import common
from group import Group
from environment import Environment
from vehicles.uber import Uber
from vehicles.hitch import Hitch

class Simulation(object):
    """
    OMG PSEUDOCODE
    """

    def __init__(self):
        self.time = 10000 #TIME OF SIMULATION
        self.envs = [uber, hitch]


        # TODO: gen envs


    def run():
        while common.clock < self.time:
            common.clock += 1
            group = self.genGroup() if self.needGroup() else None
            for env in self.envs:
                env.step(group)
        for env in envs:
            while env.stillRunning():
                common.clock += 1
                env.step() # no group passed in

    def genGroup():
        '''
        Initialize a new group
        '''
        pass

    def needGroup():
        '''
        Some exponential arrival shit
        '''

        pass

    def getLogs():
        logs = {}
        for env in self.envs:
                logs[str(env)] = env.getLogs()
