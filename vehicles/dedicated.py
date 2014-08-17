from . import vehicle

class Dedicated(vehicle.Vehicle):
    def __init__(self): 
        super(Dedicated, self).__init__()

    def availableToPickUp(self):
        return self.CAPACITY if self.occupancy == 0 else 0
