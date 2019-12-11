

class ElectricCar:
    def __init__(self, distance):
        self.distance = distance
        self.counter = 0



    def drive(self, drv):
        if self.counter + drv < self.distance:
            self.counter += drv
            to_travel = drv
        else:
            to_travel = self.distance - self.counter
            self.counter = self.distance
        return to_travel


    def charge(self):
        self.counter = 0





