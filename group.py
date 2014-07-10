import common
import random

class Group:
    """
    Represents a group of travelers bktween 1 and 3 people
    """

    def __init__(self):
        self.groupSize = self.genGroupSize()
        self.travelTime = self.genTravelTime()
        self.ttl = self.travelTime
        self.log = {
            'spawn' : common.clock,
            'driverAssigned' : None,
            'start' : None,
            'end'   : None,
            'size'  : self.groupSize
        }

    def __str__(self):
        return '<ID: %r, size: %r, time: %r, ttl: %r>' % (id(self), self.groupSize, self.travelTime, self.ttl)

    def genGroupSize(self):
        num = random.random()
        if num >= 0.3:
            return 1
        elif num >= 0.1:
            return 2
        return 3

    def genTravelTime(self):
        mu = common.travelTimeAverage
        sigma = common.travelTimeStdDev
        num = int(random.gauss(mu, sigma))
        if (num > 1):
            return num
        return 1

    def assigned(self):
        self.log['driverAssigned'] = common.clock

    def pickUp(self):
        self.log['start'] = common.clock

    def dropOff(self):
        self.log['end'] = common.clock

    def step(self):
        self.ttl -= 1
        if self.ttl == 0:
            self.dropOff()

    def hasArrived(self):
        return self.ttl == 0
