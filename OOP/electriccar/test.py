from electriccar import ElectricCar


class TestElectricCar:

    def testinit(self):
        car = ElectricCar(100)
        assert car.distance == 100

    def test_drive_over_max_distance(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30
        assert car.drive(50) == 0

    def test_charge(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.drive(50) == 30
        assert car.drive(50) == 0
        car.charge()
        assert car.drive(50) == 50

