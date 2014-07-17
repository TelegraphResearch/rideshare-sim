from . import vehicle

class Uber(vehicle.Vehicle):
    def __init__(self): 
        super(Uber, self).__init__()

    def availableToPickUp(self):
        return self.CAPACITY if self.occupancy == 0 else 0
