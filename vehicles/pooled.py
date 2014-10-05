from . import vehicle

class Pooled(vehicle.Vehicle):
    def __init__(self): 
        super(Pooled, self).__init__()

    def availableToPickUp(self):
        return self.CAPACITY - self.occupancy
