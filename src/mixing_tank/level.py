from enum import Enum


class LevelState(Enum):
    FULL = 0
    ALMOST_FULL = 1
    HALF = 2
    ALMOST_EMPTY = 3
    EMPTY = 4


class LevelMeter:
    def __init__(self, name: str, tank):
        self.name = name
        self.tank = tank
        self.value = tank.level
        self.state = LevelState.EMPTY

    def update(self) -> None:
        self.value = self.tank.level

        percentage = self.value / self.tank.capacity

        if percentage >= 0.95:
            self.state = LevelState.FULL
        elif percentage >= 0.75:
            self.state = LevelState.ALMOST_FULL
        elif percentage >= 0.25:
            self.state = LevelState.HALF
        elif percentage > 0.0:
            self.state = LevelState.ALMOST_EMPTY
        else:
            self.state = LevelState.EMPTY