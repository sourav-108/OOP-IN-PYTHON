class Light:
    def __init__(self, room):
        self.room = room
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False


class SmartHome:
    def __init__(self):
        self.lights = []

    def add_light(self, light):
        self.lights.append(light)

    def turn_all_on(self):
        for light in self.lights:
            light.turn_on()


home = SmartHome()
home.add_light(Light("Kitchen"))
home.add_light(Light("Bedroom"))
home.turn_all_on()

print([light.is_on for light in home.lights])  # [True, True]