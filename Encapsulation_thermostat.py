class Thermostat:
    def __init__(self, temperature):
        self.set_temperature(temperature)

    def set_temperature(self, temperature):
        if not 10 <= temperature <= 30:
            raise ValueError("Temperature must be between 10 and 30")
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature


thermostat = Thermostat(21)
thermostat.set_temperature(24)
print(thermostat.get_temperature())  # 24