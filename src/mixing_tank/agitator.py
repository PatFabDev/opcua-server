from enum import Enum


class AgitatorState(Enum):
    OFF = 0
    ON = 1


class Agitator:
    def __init__(self, name: str):
        self.name = name
        self.state = AgitatorState.OFF

    def turn_on(self) -> None:
        self.state = AgitatorState.ON

    def turn_off(self) -> None:
        self.state = AgitatorState.OFF