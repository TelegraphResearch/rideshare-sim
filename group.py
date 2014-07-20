import common
import random

class Group:
    """
    Represents a group of travelers bktween 1 and 3 people
    """

    def __init__(self):
        self.groupSize = self.genGroupSize()

        # time to drop off (a ttl while in car)
        self.ttdo = 0

        # time to pick up (a ttl while waiting for a car)
        self.ttpu = 0

        self.log = {
            'spawn' : common.clock,
            'enqueued' : None,
            'start' : None,
            'end'   : None,
            'size'  : self.groupSize
        }

    def __str__(self):
        return '<ID: %r, size: %r, ttdo: %r, ttpu %r>' % (id(self), self.groupSize, self.ttdo, self.ttpu)

    def enqueue(self, ttpu):
        self.log['driverAssigned'] = common.clock
        self.ttpu = ttpu

    def pickUp(self):
        self.log['start'] = common.clock
        self.ttdo = self.genTravelTime()

    def dropOff(self):
        self.log['end'] = common.clock
        common.log[self.logName].append(self.log)

    def step(self):
        if self.ttdo > 0:
            self.ttdo -= 1

        if self.ttpu > 0:
            self.ttpu -= 1

    def hasDroppedOff(self):
        return self.ttdo == 0

    def hasPickedUp(self):
        return self.ttpo == 0

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

    def assignLog(self, name):
        self.logName = name

