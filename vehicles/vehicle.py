import common
import group
import random

class Vehicle(object):
    CAPACITY = 3

    def __init__(self):
        self.groups = [] # add group objects
        self.occupancy = 0 # this includes pickupQueue
        self.holdTime = 0
        self.pickUpQueue = [] # tuple of group, ttpu
        self.log = {
            'sum': {
                'groups': 0,
                'passengers': 0,
                'groupsAssigned': 0,
                'passengersAssigned': 0,
            },
            'sumSquared': {
                'groups': 0,
                'passengers': 0,
                'groupsAssigned': 0,
                'passengersAssigned': 0,
            },
            'stateCount': {
                'idle': 0,
                'drivingOccupied': 0,
                'drivingUnoccupied': 0,
                'holdingOccupied': 0,
                'holdingUnoccupied': 0,
            }
        }

    def __str__(self):
        return '<ID: %r, Number of Groups: %r, Occupancy: %r, Hold Time: %r, Queue Size: %r>' % (id(self), len(self.groups), self.occupancy, self.holdTime, len(self.pickUpQueue))

    def availableToPickUp(self):
        """
        Delegate this to subclasses
        """
        pass

        # if dedicated
        # return ocuppancy == 0

        # pooled
        # return capacity - occupancy

    def enqueueGroup(self, group):
        """
        Add group to pickUpQueue
        """

        # Tell the group that it's enqueued
        group.enqueue(self.genTimeToPickUp())

        # and store it on the vehicle
        self.pickUpQueue.append(group)

        self.occupancy += group.groupSize

    def pickUpGroup(self, group):
        """
        Move group from pickUpQueue to car
        """

        self.pickUpQueue.remove(group)
        group.pickUp()
        self.groups.append(group)
        self.genHoldTime()

    def dropOffGroup(self, group):
        self.groups.remove(group)
        self.genHoldTime()
        self.occupancy -= group.groupSize
        group.dropOff()

    def step(self):

        if self.holdTime > 0:
            self.holdTime -= 1
            return

        # Handle passengers
        for group in self.groups:
            group.step()

        for groupCopy in self.groups[:]:
            if groupCopy.hasDroppedOff():
                self.dropOffGroup(groupCopy)

        # Handle Queue
        for group in self.pickUpQueue:
            group.step()

        for groupCopy in self.pickUpQueue[:]:
            if groupCopy.hasPickedUp():
                self.pickUpGroup(groupCopy)

        if common.collectStats():
            self.statsStep()

    def genHoldTime(self):
        holdTime = random.gauss(common.vehicleHoldTimeAverage, common.vehicleHoldTimeStdDev)
        if holdTime < 1:
            holdTime = 1

        """
        Note: We don't add this. This is important if we pick up two groups
        at once - they are serviced in parallel, and we basically randomly pick
        between the two groups' hold times.
        """
        self.holdTime = int(holdTime)

    def genTimeToPickUp(self):
        pickUpTime = random.gauss(common.vehiclePickUpTimeAverage, common.vehiclePickUpTimeStdDev)
        if pickUpTime < 1:
            return 1
        return int(pickUpTime)

    def statsStep(self):
        self.log['stateCount'][self.getState()] += 1

        # number of groups in the car
        groups = len(self.groups)
        self.log['sum']['groups'] += groups
        self.log['sumSquared']['groups'] += groups^2

        #  number of passengers in the car - different than self.occupancy
        passengers = 0
        for group in self.groups:
            passengers += group.groupSize
        self.log['sum']['passengers'] += passengers
        self.log['sumSquared']['passengers'] += passengers^2

        # number of groups assigned but not yet picked up
        groupsAssigned = len(self.pickUpQueue)
        self.log['sum']['groupsAssigned'] += groupsAssigned
        self.log['sumSquared']['groupsAssigned'] += groupsAssigned^2

        # number of passengers assigned but not yet picked up
        passengersAssigned = 0
        for group in self.pickUpQueue:
            passengersAssigned += group.groupSize
        self.log['sum']['passengersAssigned'] += passengersAssigned
        self.log['sumSquared']['passengersAssigned'] += passengersAssigned^2

    def getState(self):
        if self.occupancy == 0:
            return 'idle'
        if self.holdTime == 0:
            if len(self.groups) > 0:
                return 'holdingOccupied'
            else:
                return 'holdingUnoccupied'
        else:
            if len(self.groups) > 0:
                return 'drivingOccupied'
            else:
                return 'drivingUnoccupied'
