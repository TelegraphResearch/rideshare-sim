from . import vehicle

class Hitch(vehicle.Vehicle):
    def __init__(self): 
        super(Hitch, self).__init__()

    def availableToPickUp(self):
        return self.CAPACITY - self.occupancy
