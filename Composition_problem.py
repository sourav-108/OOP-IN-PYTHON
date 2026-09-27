class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()

    def start(self):
        return f"{self.model}: {self.engine.start()}"


car = Car("Toyota ")
print(car.start())