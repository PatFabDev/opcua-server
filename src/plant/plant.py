class Plant:
    def __init__(self):
        self.machines = {}

    def add_machine(self, machine) -> None:
        self.machines[machine.name] = machine

    def remove_machine(self, name: str) -> None:
        if name not in self.machines:
            raise ValueError(f"Machine '{name}' does not exist")

        del self.machines[name]

    def print_machines(self) -> None:
        for machine in self.machines.values():
            print(machine.name)