from enum import Enum


class TemperatureState(Enum):
    HOT = 0
    NORMAL = 1
    COLD = 2


class TemperatureSensor:
    def __init__(self, name: str, tank):
        self.name = name
        self.tank = tank
        self.value = tank.temperature
        self.state = TemperatureState.NORMAL

    def update(self) -> None:
        self.value = self.tank.temperature

        if self.value >= 60.0:
            self.state = TemperatureState.HOT
        elif self.value <= 10.0:
            self.state = TemperatureState.COLD
        else:
            self.state = TemperatureState.NORMAL