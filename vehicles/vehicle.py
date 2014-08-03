import common
import group
import random
#import vehicles

class Vehicle(object):
    CAPACITY = 3

    def __init__(self):
        self.groups = [] # add group objects
        self.occupancy = 0
        self.holdTime = 0
        self.pickUpQueue = [] # tuple of group, ttpu

    def __str__(self):
        return '<ID: %r, Number of Groups: %r, Occupancy: %r, Hold Time: %r, Queue Size: %r>' % (id(self), len(self.groups), self.occupancy, self.holdTime, len(self.pickUpQueue))

    def availableToPickUp(self):
        """
        Delegate this to subclasses
        """
        pass

        # if uber
        # return ocuppancy == 0

        # hitch
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
