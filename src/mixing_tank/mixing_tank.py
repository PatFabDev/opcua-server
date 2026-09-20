from enum import Enum

from .tank import Tank
from .level import LevelMeter, LevelState
from .temperature import TemperatureSensor, TemperatureState
from .valve import Valve, ValveState
from .agitator import Agitator, AgitatorState
from .heater import Heater, HeaterState


class MixingTankPhase(Enum):
    IDLE = 0
    FILLING_1 = 1
    FILLING_2 = 2
    HEATING = 3
    COOLING = 4
    DRAINING = 5


class MixerTank:
    def __init__(self, name: str, capacity: float):
        self.name = name
        self.phase = MixingTankPhase.IDLE

        self.tank = Tank("Tank", capacity)
        self.level_meter = LevelMeter("LevelMeter", self.tank)
        self.temperature_sensor = TemperatureSensor("TemperatureSensor", self.tank)

        self.inlet_valve_1 = Valve("InletValve1")
        self.inlet_valve_2 = Valve("InletValve2")
        self.outlet_valve = Valve("OutletValve")

        self.heater = Heater("Heater")
        self.agitator = Agitator("Agitator")

    # Mixer - Status
    def get_name(self) -> str:
        return self.name

    def get_phase(self) -> MixingTankPhase:
        return self.phase

    def get_status(self) -> dict:
        return {
            "name": self.get_name(),
            "phase": self.get_phase().name,
            "level": self.get_level(),
            "level_state": self.get_level_state().name,
            "temperature": self.get_temperature(),
            "temperature_state": self.get_temperature_state().name,
            "inlet_valve_1": self.get_inlet_valve_1_state().name,
            "inlet_valve_2": self.get_inlet_valve_2_state().name,
            "outlet_valve": self.get_outlet_valve_state().name,
            "heater": self.get_heater_state().name,
            "agitator": self.get_agitator_state().name,
        }

    # Mixer - Agitator
    def start_mixing(self) -> None:
        self.agitator.turn_on()

    def stop_mixing(self) -> None:
        self.agitator.turn_off()

    def get_agitator_state(self) -> AgitatorState:
        return self.agitator.state

    # Tank
    def fill(self, amount: float) -> None:
        self.tank.fill(amount)

    def drain(self, amount: float) -> None:
        self.tank.drain(amount)

    def get_capacity(self) -> float:
        return self.tank.capacity

    # Valves
    def open_inlet_valve_1(self) -> None:
        self.inlet_valve_1.open()

    def open_inlet_valve_2(self) -> None:
        self.inlet_valve_2.open()

    def open_outlet_valve(self) -> None:
        self.outlet_valve.open()

    def close_inlet_valve_1(self) -> None:
        self.inlet_valve_1.close()

    def close_inlet_valve_2(self) -> None:
        self.inlet_valve_2.close()

    def close_outlet_valve(self) -> None:
        self.outlet_valve.close()

    def get_inlet_valve_1_state(self) -> ValveState:
        return self.inlet_valve_1.state

    def get_inlet_valve_2_state(self) -> ValveState:
        return self.inlet_valve_2.state

    def get_outlet_valve_state(self) -> ValveState:
        return self.outlet_valve.state

    # Heater
    def turn_heater_on(self) -> None:
        self.heater.turn_on()

    def turn_heater_off(self) -> None:
        self.heater.turn_off()

    def get_heater_state(self) -> HeaterState:
        return self.heater.state

    # Sensors
    def update_sensors(self) -> None:
        self.level_meter.update()
        self.temperature_sensor.update()

    def get_level(self) -> float:
        return self.level_meter.value

    def get_level_state(self) -> LevelState:
        return self.level_meter.state

    def get_temperature(self) -> float:
        return self.temperature_sensor.value

    def get_temperature_state(self) -> TemperatureState:
        return self.temperature_sensor.state