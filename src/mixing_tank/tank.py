class Tank:
    def __init__(self, name: str, capacity: float):
        if capacity <= 0:
            raise ValueError("Tank capacity must be greater than 0")

        self.name = name
        self.capacity = capacity
        self.level = 0.0
        self.temperature = 25.0

    def fill(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Fill amount cannot be negative")

        self.level = min(self.level + amount, self.capacity)

    def drain(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Drain amount cannot be negative")

        self.level = max(self.level - amount, 0.0)

    def is_full(self) -> bool:
        return self.level >= self.capacity

    def is_empty(self) -> bool:
        return self.level <= 0.0