import common
import Group
import random

class Vehicle(object):
    CAPACITY = 3

    def __init__(self):
        self.groups = [] # add group objects
        self.occupancy = 0
        self.holdTime = 0
        #TODO
        # Impending pickup queue that is a tuple of "time to pick up" (like
        # TTL) and the group that will be onboarded

    #TODO 
    def availableToPickUp(self):
        # if uber
        return ocuppancy == 0
        # hitch
        return capacity - occupancy

    def addGroup(self, group):
        self.groups.append(group)
        group.pickUp()
        self.occupancy += group.groupSize
        self.genHoldTime()

    def removeGroup(self, group):
        self.groups.remove(group)
        self.genHoldTime()
        self.occupancy -= group.groupSize

        # Store the group's data to some global for later calculation
        common.completedGroups.append(group.log)

    def step(self):
        if self.holdTime > 0:
            self.holdTime -= 1
            return

        for group in self.groups:
            group.step()

        # iterate over a copy
        for groupCopy in self.groups[:]:
            if groupCopy.hasArrived():
                self.removeGroup(groupCopy)

    def genHoldTime(self):
        holdTime = random.gauss(common.vehicleHoldTimeAverage, common.vehicleHoldTimeStdDev)
        if holdTime < 1:
            holdTime = 1
        self.holdTime = holdTime
