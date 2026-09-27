class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = set()

    def park(self, plate):
        if len(self.cars) >= self.capacity:
            return "Full"
        if plate in self.cars:
            return "Already parked"
        self.cars.add(plate)
        return "Parked"

    def leave(self, plate):
        if plate not in self.cars:
            return "Car not found"
        self.cars.remove(plate)
        return "Left"