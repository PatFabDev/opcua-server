from plant.mixing_tank.mixing_tank import MixerTank, MixingTankPhase
from plant.mixing_tank.level import LevelState
from plant.mixing_tank.temperature import TemperatureState
from plant.mixing_tank.valve import ValveState
from plant.mixing_tank.heater import HeaterState
from plant.mixing_tank.agitator import AgitatorState


class MixerTankIO:
    def __init__(self, mixer_tank: MixerTank):
        self.mixer_tank = mixer_tank

    # Inputs - Sensors / States

    def get_status(self) -> dict:
        return self.mixer_tank.get_status()

    def get_level(self) -> float:
        return self.mixer_tank.get_level()

    def get_level_state(self) -> LevelState:
        return self.mixer_tank.get_level_state()

    def get_temperature(self) -> float:
        return self.mixer_tank.get_temperature()

    def get_temperature_state(self) -> TemperatureState:
        return self.mixer_tank.get_temperature_state()

    def get_phase(self) -> MixingTankPhase:
        return self.mixer_tank.get_phase()

    def get_inlet_valve_1_state(self) -> ValveState:
        return self.mixer_tank.get_inlet_valve_1_state()

    def get_inlet_valve_2_state(self) -> ValveState:
        return self.mixer_tank.get_inlet_valve_2_state()

    def get_outlet_valve_state(self) -> ValveState:
        return self.mixer_tank.get_outlet_valve_state()

    def get_heater_state(self) -> HeaterState:
        return self.mixer_tank.get_heater_state()

    def get_agitator_state(self) -> AgitatorState:
        return self.mixer_tank.get_agitator_state()

    def get_capacity(self) -> float:
        return self.mixer_tank.get_capacity()

    # Outputs - Actuators

    def open_inlet_valve_1(self) -> None:
        self.mixer_tank.open_inlet_valve_1()

    def close_inlet_valve_1(self) -> None:
        self.mixer_tank.close_inlet_valve_1()

    def open_inlet_valve_2(self) -> None:
        self.mixer_tank.open_inlet_valve_2()

    def close_inlet_valve_2(self) -> None:
        self.mixer_tank.close_inlet_valve_2()

    def open_outlet_valve(self) -> None:
        self.mixer_tank.open_outlet_valve()

    def close_outlet_valve(self) -> None:
        self.mixer_tank.close_outlet_valve()

    def turn_heater_on(self) -> None:
        self.mixer_tank.turn_heater_on()

    def turn_heater_off(self) -> None:
        self.mixer_tank.turn_heater_off()

    def start_agitator(self) -> None:
        self.mixer_tank.start_mixing()

    def stop_agitator(self) -> None:
        self.mixer_tank.stop_mixing()

    def set_phase(self, phase: MixingTankPhase) -> None:
        self.mixer_tank.phase = phase