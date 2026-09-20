from enum import Enum


class HeaterState(Enum):
    OFF = 0
    ON = 1


class Heater:
    def __init__(self, name: str):
        self.name = name
        self.state = HeaterState.OFF

    def turn_on(self) -> None:
        self.state = HeaterState.ON

    def turn_off(self) -> None:
        self.state = HeaterState.OFF