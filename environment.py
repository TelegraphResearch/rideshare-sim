import common
from group import Group
from vehicles.uber import Uber
from vehicles.hitch import Hitch
import random

class Environment(object):
    """
    An environment is the logic for assigning customers and routing vehicles
    """
    def __init__(self, serviceType):
        self.serviceType = serviceType
        self.vehicles = []
        self.queue = []
        self.genVehicles()

    def __str__(self):
        return '<ID: %r, Service Type: %s, Number in Queue: %r, Number of Vehicles: %r>' % (id(self), self.serviceType, len(self.queue), len(self.vehicles))

    def step(self, group):
        if group is not None:
            group.assignLog(self.serviceType)
            self.enqueue(group)

        for vehicle in self.vehicles:
            vehicle.step()

        self.serviceQueue()

        print(str(self) + "\n")
        print(self.serviceType + ': ' + str(len(common.logs[self.serviceType])) + "\n")

    def enqueue(self, group):
        self.queue.append(group)

    def serviceQueue(self):
        # mildly fifo
        for group in self.queue[:]: # iterate over copy
            if self.assign(group):
                self.queue.remove(group)

    def assign(self, group):
        for vehicle in self.vehicles:
            if vehicle.availableToPickUp() >= group.groupSize:
                # assign group to vehicle
                vehicle.enqueueGroup(group)

                # keep future assignments through this heuristic random
                random.shuffle(self.vehicles)

                return True

        # could not find a vehicle
        return False

    def genVehicles(self):
        for _ in range(common.vehicleQuantity[self.serviceType]):
            if self.serviceType is 'uber':
                self.vehicles.append(Uber())
            if self.serviceType is 'hitch':
                self.vehicles.append(Hitch())

    def stillRunning(self):
        if len(self.queue) > 0: 
            return True

        for vehicle in self.vehicles:
            if vehicle.availableToPickUp() != vehicle.CAPACITY:
                return True

        return False

