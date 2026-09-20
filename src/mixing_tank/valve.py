from enum import Enum


class ValveState(Enum):
    CLOSED = 0
    OPEN = 1


class Valve:
    def __init__(self, name: str):
        self.name = name
        self.state = ValveState.CLOSED

    def open(self) -> None:
        self.state = ValveState.OPEN

    def close(self) -> None:
        self.state = ValveState.CLOSED

    def is_open(self) -> bool:
        return self.state == ValveState.OPEN